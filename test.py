import datetime

# Ask user for log file name
log_file = input("Enter the name of the log file: ")

# Ask the user for the start and end dates
start_date_str = input("Enter start date (YYYY-MM-DD): ")
end_date_str = input("Enter end date (YYYY-MM-DD): ")

# Convert the start and end dates to datetime objects
start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d') + datetime.timedelta(days=1)

# Open the log file
with open(log_file, 'r') as f:
    # Initialize counter and log buffer
    count = 0
    buffer = []
    
    # Loop through each line in the file
    for line in f:
        # Extract the log date from the line
        log_date_str = line.split('T')[0]
        log_date = datetime.datetime.strptime(log_date_str, '%Y-%m-%d')

        # Check if the log date is within the specified range
        if start_date <= log_date < end_date:
            # Append the entire log line to the buffer
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
    
    # Check if there are any logs left in the buffer
    if buffer:
        # Print the remaining logs
        print('\n'.join(buffer))
Hello World
