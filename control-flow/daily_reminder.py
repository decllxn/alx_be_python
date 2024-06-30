#!/usr/bin/env python3
# Author - Declan Munene
# Date - 30/6/2024
# Description - Daily reminder to remind user a single, priority task for the day based on time sensitivity

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."
        print(reminder)


# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    print("Invalid input for time sensitivity. Please enter yes or no.")

# Provide the customized reminder
print("Reminder:", reminder)
