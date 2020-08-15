#for reduce method we required functools module
from functools import *;

def Accept_Data():
    size=int(input("Enter the no of element"))
    arr=list()
    print("enter the no of elements")
    for i in range(0,size,1):
        print("enter the ",i+1)
        no=int(input())
        arr.append(no)

    return  arr

def ChkEven(no):
    if (no%2)==0:
        return True
    else:
        return False

def Modify(no):
    return no+2

def Add(no1,no2):
    return no1+no2

def main():
    #creation of list
    Raw_Data=Accept_Data()

    #print accepted data
    print("accepted data is {}".format(Raw_Data))

    #filter data
    FilterData=list(filter(ChkEven,Raw_Data))
    print("filterd Data is {}".format(FilterData))

    #modify data
    Modified_Data=list(map(Modify,FilterData))
    print("modified or mapped data is {}".format(Modified_Data))

    #reduce data or compute the data
    ReducedData=reduce(Add,Modified_Data)
    print("the final output is after reduce method {}".format(ReducedData))





if __name__=="__main__":
    main()