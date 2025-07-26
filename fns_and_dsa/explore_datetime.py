# File: explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print("Current date and time:", formatted_date)
    
    return current_date  # Return it for use in next function

def calculate_future_date(current_date):
    try:
        # Ask the user for number of days to add
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        
        # Calculate future date
        future_date = current_date + timedelta(days=number_of_days)
        
        # Print the result in "YYYY-MM-DD" format
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    
    except ValueError:
        print("❌ Please enter a valid integer.")

# Main code
if __name__ == "__main__":
    now = display_current_datetime()
    calculate_future_date(now)
