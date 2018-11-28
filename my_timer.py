"""It's just a timer py..."""

import threading

import time

my_lock = threading.Lock()


def show_timer(name, delay, repeat):
    print("Timer " + name + " started...")

    my_lock.acquire()
    print("Timer " + name + " has the lock.")
    for i in range(repeat):
        time.sleep(delay)
        print("Timer: " + name + ", Time: " + str(time.ctime(time.time())))
    my_lock.release()
    print("Timer " + name + " released the lock.")

    print("Timer " + name + " stopped.")


def main():
    print("main() started...")

    t1 = threading.Thread(target=show_timer, args=('Timer1', 1, 5))
    t2 = threading.Thread(target=show_timer, args=('Timer2', 2, 5))
    t1.start()
    t2.start()

    print("main() completed...")


if __name__ == '__main__':
    main()