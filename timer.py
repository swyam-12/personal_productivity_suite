import time

class Timer:
    def start_timer(self, seconds):
        try:
            seconds = int(seconds)
            while seconds:
                mins, secs = divmod(seconds, 60)
                print(f"{mins:02d}:{secs:02d}", end="\r")
                time.sleep(1)
                seconds -= 1
            print("\nTime's up!")
        except:
            print("Invalid input")