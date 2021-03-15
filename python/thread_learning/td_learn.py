import threading


def main():
    print(threading.activeCount())
    print(threading.enumerate())
    print(threading.currentThread())


if __name__ == '__main__':
    main()
