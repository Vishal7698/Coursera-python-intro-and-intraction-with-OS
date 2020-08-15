import threading

def fun(number):
    print("fun thread id",threading.get_ident())
    print("tid", threading.current_thread())

    for i in range(number):
        print(i*12873543)


def gun(number):
    print("gun thread id", threading.get_ident())
    print("tid",threading.current_thread())

    for i in range(number):
        print(i * 12873543)

if __name__ == "__main__":
    print("inside main")

    t1=threading.Thread(fun(6))
    t2=threading.Thread(gun(16))

    t1.start()
    t2.start()

    t1.join()
    t2.join()