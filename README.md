# log-analyzer



### **This module contains functions to filter and search through log files.**

**Functions:**

* **get_log_file_name()**: Prompts the user to enter the name of the log file and returns it.* 

* **get_filter_type()**: Prompts the user to enter the filter type (start_end_date, hour, or day) and returns it.

* **get_search_keyword()**: Prompts the user to enter a search keyword and returns it.

* **get_filter_values(filter_type)**: Prompts the user to enter filter values based on the filter type and returns them.

* **calculate_filter_delta(filter_type, filter_value)**: Calculates and returns a timedelta object based on the filter type and value.

* **convert_dates_to_datetime_objects(start_date_str, end_date_str)**: Converts start and end date strings to datetime objects and returns them.

* **calculate_filter_cutoff_time(filter_type, filter_delta)**: Calculates and returns a cutoff datetime based on the filter type and delta.

* **process_log_file(log_file, search_keyword, filter_type, start_date_str, end_date_str, filter_value)**: Filters and searches a log file based on the input parameters and displays the results.

* **main()**: Runs the functions to get user input and process the log file.

Examples:

```

get_log_file_name()
Prompts the user to enter a log file name and returns it

get_filter_type()
Prompts the user to enter a filter type (start_end_date, hour, or day) and returns it

get_search_keyword()
Prompts the user to enter a search keyword and returns it

get_filter_values("start_end_date")
Prompts the user to enter start and end dates and returns them

calculate_filter_delta("hour", 5)
Returns a timedelta object representing 5 hour

convert_dates_to_datetime_objects("2020-01-01", "2020-01-03")
Returns datetime objects for January 1, 2020 and January 3, 2020

calculate_filter_cutoff_time("hour", timedelta(hours=5))
Returns a datetime object representing 5 hours before the current time

process_log_file("log.txt", "error", "hour", None, None, 5)
Filters and searches "log.txt" for the keyword "error" within the past 5 hours and displays the results

```Hello there
