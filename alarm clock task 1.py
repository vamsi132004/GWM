from playsound import playsound
import datetime
import time

def play_alarm_sound(sound_file):
    playsound(sound_file)

def main():
    alarm_time_str = input("Enter the alarm time (format: HH:MM): ")

    try:
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
    except ValueError:
        print("Invalid time format. Use HH:MM format.")
        return

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time.strftime("%H:%M"):
            print("Time to wake up!")
            play_alarm_sound("c:\\Users\\vamsi\\Downloads\\mixkit-alarm-tone-996.wav")  
            break
        else:
            print("Current time: {}".format(current_time))
            time.sleep(60)  

if __name__ == "__main__":
    main()
