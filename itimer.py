# Project 7: Countdown Timer with Options
import time


def display_time(seconds):
    """Convert seconds to minutes:seconds format"""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"


while True:
    try:
        total_seconds = int(input("Enter countdown time in seconds: "))
        if total_seconds <= 0:
            print("Please enter a positive number!")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a whole number.")

while total_seconds > 0:
    print(f"\rTime remaining: {display_time(total_seconds)}", end="")

    if total_seconds <= 10 and total_seconds > 0:
        print(" ⚠️ WARNING: Last 10 seconds!", end="")

    time.sleep(1)
    total_seconds -= 1

print(f"\n\n🎉 Time's up!")
