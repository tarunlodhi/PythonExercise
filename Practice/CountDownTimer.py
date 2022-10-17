import time


def count_down(t):
    while t:
        mins, sec = divmod(t, 60)
        timer = '{:02d} : {:02d}'.format(mins, sec)
        # print(timer, end='\r')
        time.sleep(1)
        t -= 1
        print(timer, end="\r", flush=True)
    print("time is up")


times = input("Enter the time in second :")
count_down(int(times))
