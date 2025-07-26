import datetime
def  display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date)
def calculate_future_date():
    user = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.datetime.now() - datetime.timedelta(days=user)
    print(future_date)
display_current_datetime()
calculate_future_date()