import time

def countdown_timer(duration):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes, seconds = divmod(remaining_time, 60)
        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

    print("Countdown complete!")

# Example usage: Countdown for 5 minutes (300 seconds)
countdown_timer(300)
