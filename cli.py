import argparse
import datetime


def filter_logs(log_file, filter_type, search_keyword, start_date_str, end_date_str, filter_value):
    """
    Filter log entries by keyword and date/time range.
    """
    # Calculate the filter time delta
    if filter_type == "hour":
        filter_delta = datetime.timedelta(hours=filter_value)
    elif filter_type == "day":
        filter_delta = datetime.timedelta(days=filter_value)

    # Convert the start and end dates to datetime objects
    if start_date_str and end_date_str:
        start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d') + datetime.timedelta(days=1)

    # Calculate the filter cutoff time
    if filter_type != "start_end_date":
        filter_cutoff_time = datetime.datetime.utcnow() - filter_delta

    # Initialize the result list
    result = []

    # Open the log file
    with open(log_file, 'r') as f:
        # Initialize counter and log buffer
        count = 0
        buffer = []

        # Loop through each line in the file
        for line in f:
            # Check if the line contains the search keyword
            if search_keyword in line:
                # Extract the log date and time from the line
                log_datetime_str = line[0:23]
                log_datetime = datetime.datetime.strptime(log_datetime_str, '%Y-%m-%dT%H:%M:%S.%f')

                # Initialize add_to_buffer
                add_to_buffer = False

                # Check if the log time is within the specified range
                if filter_type == "start_end_date":
                    if start_date <= log_datetime < end_date:
                        add_to_buffer = True
                elif filter_type == "hour" or filter_type == "day":
                    if log_datetime >= filter_cutoff_time:
                        add_to_buffer = True

                # Append the entire log line to the buffer
                if add_to_buffer:
                    buffer.append(line)

                    # Increment the counter
                    count += 1

                    # Check if the counter is a multiple of 20
                    if count % 20 == 0:
                        # Append the buffer to the result
                        result.append('\n'.join(buffer))

                        # Clear the buffer
                        buffer = []

                        # Reset the counter
                        count = 0

                    # Reset the add_to_buffer flag
                    add_to_buffer = False

        # Check if there are any logs left in the buffer
        if buffer:
            # Append the remaining logs to the result
            #result.append('\n'.join(buffer))
            print('\n'.join(buffer))

    # Return the filtered logs
    #return result


def main():
    parser = argparse.ArgumentParser(description="Filter log entries by keyword and date/time range.")
    parser.add_argument("log_file", help="The name of the log file.")
    parser.add_argument("filter_type", choices=["start_end_date", "hour", "day"], help="The type of filter to apply.")
    parser.add_argument("search_keyword", help="The keyword to search for in the log entries.")
    parser.add_argument("--start-date", dest="start_date", help="The start date (YYYY-MM-DD) for the filter.")
    parser.add_argument("--end-date", dest="end_date", help="The end date (YYYY-MM-DD) for the filter.")
    parser.add_argument("--filter-value", type=int, help="The filter value (in hours or days) for the filter.")

    args = parser.parse_args()

    # Call the filter_logs function with the command line arguments
    filter_logs(args.log_file, args.filter_type, args.search_keyword, args.start_date, args.end_date, args.filter_value)

    if __name__ == '__main__':
        main()
Hello World
