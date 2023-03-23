import datetime

def get_log_file_name():
    return input("Enter the name of the log file: ")

def get_filter_type():
    return input("Enter the filter type (start_end_date/hour/day): ")

def get_search_keyword():
    return input("Enter the keyword to search: ")

def get_filter_values(filter_type):
    if filter_type == "start_end_date":
        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        end_date_str = input("Enter end date (YYYY-MM-DD): ")
        return start_date_str, end_date_str, None
    elif filter_type == "hour" or filter_type == "day":
        filter_value = int(input(f"Enter the filter value ({filter_type}s): "))
        return None, None, filter_value
    else:
        return None, None, None

def calculate_filter_delta(filter_type, filter_value):
    if filter_type == "hour":
        return datetime.timedelta(hours=filter_value)
    elif filter_type == "day":
        return datetime.timedelta(days=filter_value)
    else:
        return None

def convert_dates_to_datetime_objects(start_date_str, end_date_str):
    if start_date_str and end_date_str:
        start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d') + datetime.timedelta(days=1)
        return start_date, end_date
    else:
        return None, None

def calculate_filter_cutoff_time(filter_type, filter_delta):
    if filter_type != "start_end_date":
        return datetime.datetime.utcnow() - filter_delta
    else:
        return None

def process_log_file(log_file, search_keyword, filter_type, start_date_str, end_date_str, filter_value):
    filter_delta = calculate_filter_delta(filter_type, filter_value)
    start_date, end_date = convert_dates_to_datetime_objects(start_date_str, end_date_str)
    filter_cutoff_time = calculate_filter_cutoff_time(filter_type, filter_delta)

    with open(log_file, 'r') as f:
        count = 0
        buffer = []
        for line in f:
            if search_keyword in line:
                log_datetime_str = line[0:23]
                log_datetime = datetime.datetime.strptime(log_datetime_str, '%Y-%m-%dT%H:%M:%S.%f')
                add_to_buffer = False
                if filter_type == "start_end_date":
                    if start_date <= log_datetime < end_date:
                        add_to_buffer = True
                elif filter_type == "hour" or filter_type == "day":
                    if log_datetime >= filter_cutoff_time:
                        add_to_buffer = True
                if add_to_buffer:
                    buffer.append(line.strip())
                    count += 1
                    if count % 20 == 0:
                        print('\n'.join(buffer))
                        buffer = []
                        input("Press any key to show the next 20 logs...")
                        add_to_buffer = False
        if buffer:
            print('\n'.join(buffer))

def main():
    log_file = get_log_file_name()
    filter_type = get_filter_type()
    search_keyword = get_search_keyword()
    start_date_str, end_date_str, filter_value = get_filter_values(filter_type)
    process_log_file(log_file, search_keyword, filter_type, start_date_str, end_date_str, filter_value)

if __name__ == '__main__':
    main()
