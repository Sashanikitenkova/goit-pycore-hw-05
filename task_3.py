import argparse
from datetime import datetime


# Define all available logging levels
LOG_LEVELS = ("INFO", "DEBUG", "ERROR", "WARNING")


def parse_log_line(line: str) -> dict:
    # Split the log line into its components
    parts = line.strip().split(maxsplit=3)

    # Check if the log line has all required components
    if len(parts) != 4:
        raise ValueError("Invalid log line format")

    date, time, level, message = parts

    # Validate the date and time format
    datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")

    # Validate the logging level
    if level not in LOG_LEVELS:
        raise ValueError(f"Unknown logging level: {level}")

    # Return the parsed log information as a dictionary
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }


def load_logs(file_path: str) -> list:
    # Create an empty list to store log records
    logs = []

    # Open the log file and read it line by line
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):

            # Skip empty lines
            if not line.strip():
                continue

            try:
                # Parse the current log line
                logs.append(parse_log_line(line))
            except ValueError as error:
                # Include the line number in the error message
                raise ValueError(
                    f"Error in line {line_number}: {error}"
                ) from error

    # Return the list of parsed log records
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    # Filter log records using the specified logging level
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    # Create a dictionary with zero counts for all logging levels
    counts = {level: 0 for level in LOG_LEVELS}

    # Count the number of records for each logging level
    for log in logs:
        counts[log["level"]] += 1

    # Return the statistics dictionary
    return counts


def display_log_counts(counts: dict):
    # Print the logging statistics as a table
    print(f"{'Рівень логування':<18} | {'Кількість'}")
    print("-" * 30)

    for level, count in counts.items():
        print(f"{level:<18} | {count}")


def display_logs_by_level(logs: list, level: str):
    # Print all log records for the selected level
    print(f"\nДеталі логів для рівня '{level}':")

    for log in logs:
        print(
            f"{log['date']} {log['time']} - {log['message']}"
        )


def main():
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(
        description="Analyze a log file and display statistics."
    )

    # Add the required log file path argument
    parser.add_argument("file_path", help="Path to the log file")

    # Add an optional logging level argument
    parser.add_argument(
        "level",
        nargs="?",
        choices=[level.lower() for level in LOG_LEVELS],
        help="Optional logging level to filter"
    )

    # Read command-line arguments
    args = parser.parse_args()

    try:
        # Load and parse the log file
        logs = load_logs(args.file_path)

        # Calculate the number of records for each level
        counts = count_logs_by_level(logs)

        # Display the logging statistics
        display_log_counts(counts)

        # Display filtered records if a level was provided
        if args.level:
            filtered_logs = filter_logs_by_level(logs, args.level)
            display_logs_by_level(filtered_logs, args.level.upper())

    except FileNotFoundError:
        # Handle the case when the file does not exist
        print(f"Error: File '{args.file_path}' was not found.")

    except (OSError, UnicodeDecodeError) as error:
        # Handle file reading errors
        print(f"Error while reading the file: {error}")

    except ValueError as error:
        # Handle invalid log entries
        print(f"Error: {error}")


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()
