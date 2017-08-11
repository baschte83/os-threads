import threading


def increment():
    global i
    for n in range(1000):
        i += 1
        print(str(threading.currentThread().getName()) + ": " + str(i) + "\n")


def decrement():
    global i
    for n in range(1000):
        i -= 1
        print(str(threading.currentThread().getName()) + ": " + str(i) + "\n")


def main():
    threadList = []
    for n in range(10):
        if n < 5:
            thrd = threading.Thread(target=increment)
        else:
            thrd = threading.Thread(target=decrement)
        thrd.start()
        threadList.append(thrd)
    print(threadList)

    for thr in threadList:
        thr.join()
        print("{0} joined\n".format(str(thr.getName())))


i = 0
main()
print("Value of global variable is: %d" % i)
