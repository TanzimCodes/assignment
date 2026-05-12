import sys

def rush(x,y):

    if x < 1  or y < 1:
        print("Invalid size", file=sys.stderr)
        return

    #y is row, x is col
    for i in range(y):
        for j in range(x):
            if(j==0 or j==x-1 or i==0 or i==y-1 ):
                if( (i==0 or i==y-1) and (j==0 or j==x-1)):
                    print('o', end="")
                elif (j==0 or j==x-1):
                    print('|', end="")
                else:
                    print('-', end="")
            else:
                print(' ',end="")
        print('')




    
#From assignment
# print('5,3')
# rush(5,3)
# print('5,1')
# rush(5,1)
# print('1,1')
# rush(1,1)
# print('1,5')
# rush(1,5)
# print('4,1')
# rush(4,4)


