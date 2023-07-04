import datetime

# Ask user for log file name
log_file = input("Enter the name of the log file: ")

# Ask user for the filter type
filter_type = input("Enter the filter type (start_end_date/hour/day): ")

# Ask user for the keyword to search
search_keyword = input("Enter the keyword to search: ")

# Initialize variables for filter values
start_date_str = ''
end_date_str = ''
filter_value = 0

# Determine the filter values based on filter type
if filter_type == "start_end_date":
    # Ask the user for the start and end dates
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")
elif filter_type == "hour":
    # Ask the user for the filter value
    filter_value = int(input("Enter the filter value (hours): "))
elif filter_type == "day":
    # Ask the user for the filter value
    filter_value = int(input("Enter the filter value (days): "))

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
                buffer.append(line.strip())

                # Increment the counter
                count += 1

                # Check if the counter is a multiple of 20
                if count % 20 == 0:
                    # Print the buffer
                    print('\n'.join(buffer))

                    # Clear the buffer
                    buffer = []

                    # Ask the user to continue
                    input("Press any key to show the next 20 logs...")

                # Reset the add_to_buffer flag
                add_to_buffer = False
    
    # Check if there are any logs left in the buffer
    if buffer:
        # Print the remaining logs
        print('\n'.join(buffer))
Hello World
