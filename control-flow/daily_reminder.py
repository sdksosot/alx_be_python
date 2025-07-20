!/usr/bin/python3
"""
Personal Daily Reminder Script
This script prompts the user for a single task, its priority, and time sensitivity,
then provides a customized reminder message.
"""

def main():
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity
    print()  # Add a blank line for better output formatting
    print("Reminder:", end=' ')

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"'{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"'{task}' is a high priority task. You should focus on this soon.")
        case "medium":
            if time_bound == "yes":
                print(f"'{task}' is a medium priority task that should be completed today.")
            else:
                print(f"'{task}' is a medium priority task. Try to complete it this week.")
        case "low":
            if time_bound == "yes":
                print(f"Note: '{task}' is a low priority but time-bound task. Complete it when possible.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level entered. Please use high, medium, or low.")

if __name__ == "__main__":
    while True:
        main()
        # Ask if user wants to add another task
        another = input("\nWould you like to add another task? (yes/no): ").lower()
        if another != 'yes':
            print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
            print("\n🚀 Click here to tweet! 🚀")
            break
