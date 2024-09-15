import time

def main():
    time_input = int(input('Enter the time in seconds for countdown: '))
    timer(time_input)
    print('Time\'s Up.')

def timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end = '\r')
        time.sleep(1)
        seconds -= 1

main()