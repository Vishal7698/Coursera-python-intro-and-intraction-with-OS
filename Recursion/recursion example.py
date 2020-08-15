def gun(no):
    print(no)
    no=no-1
    if no>0:
        gun(no)
    print(":"+str(no))

gun(5)