name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail


# Write your code here
no={}

for e in name:
    if e=='(' or e==')':
        if e in no:
            no[e]=no[e]+1
        else:
            no[e]=1
ans=no['(']-no[')']
print(ans)