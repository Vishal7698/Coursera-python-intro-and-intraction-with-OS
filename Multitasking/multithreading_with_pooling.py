import multiprocessing
import os


def square(n):
    print("worker process id for {}  {}".format(n , os.getpid()))

    return (n * n)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 323, 332]

    # create pool object
    p = multiprocessing.Pool()

    # map the list to target function
    result = p.map(square, arr)
    print(result)
