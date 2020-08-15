import os
import multiprocessing

def fun(number):
    print("pid of parent process of fun",os.getppid())
    print("pid of fun",os.getpid())
    for i in range(number):
        print(i)

def gun(number):
    print("pid of parent process of gun" , os.getppid())
    print("pid of gun", os.getpid())
    for i in range(number):
        print(i*10)

if __name__ == "__main__" :
    print("pid of parent process of main" , os.getppid())
    print("pid of main",os.getpid())
    number =12

    p1=multiprocessing.Process(target=fun,args=(number,))
    p2=multiprocessing.Process(target=gun,args=(number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()