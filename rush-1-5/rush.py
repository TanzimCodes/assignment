import sys

def rush(x,y):

    if x < 1  or y < 1:
        print("Invalid size", file=sys.stderr)
        return

    if(x==1 and y==1):
        print('B')
        return

    if(x==1 or y==1):
        for i in range(y):  # i = row (y coordinate)
            for j in range(x):  # j = column (x coordinate)
                if (i == 0 or i == y - 1 or j == 0 or j == x - 1):
                    print('B', end="")
                else:
                    print(' ', end="")
            print()
    else:   
        for i in range(y):  # i = row (y coordinate)
            for j in range(x):  # j = column (x coordinate)
                # Check corners first
                if i == 0 and j == 0:  # top-left corner
                    print('A', end="")
                elif i == 0 and j == x - 1:  # top-right corner
                    print('C', end="")
                elif i == y - 1 and j == 0:  # bottom-left corner
                    print('C', end="")
                elif i == y - 1 and j == x - 1:  # bottom-right corner
                    print('A', end="")
                # Then check edges
                elif i == 0 or i == y - 1 or j == 0 or j == x - 1:
                    print('B', end="")
                else:
                    print(' ', end="")
            print()

       
# print('0,0')
# rush(0,0)
# print('1,1')
# rush(1,1)
# print('2,1')
# rush(2,1)
# print('1,2')
# rush(1,2)
# print('2,2')
# rush(2,2)
# print('3,3')
# rush(3,3)

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


