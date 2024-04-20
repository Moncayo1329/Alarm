from playsound import playsound 
import time


def alarm(seconds):
    time_elapsed = 1
    while time_elapsed < seconds:
        time.sleep(1)  # Espera 1 segundo
        time_elapsed += 1 

        time_left = seconds - time_elapsed 
        minutes_left = time_left // 60 
        seconds_left = time_left % 60 
        print(f"{minutes_left}:{seconds_left}")

alarm(10)
