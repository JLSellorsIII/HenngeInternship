
#Input is of format
# N where N is an integer between 1 and 100 specifying the number of cases
# a case consists of
# X integer specifying number of integers in next line
# Yn, X integers between 1 and 100
# function prints sums of the squares of the Yn of each case
# Function is designed with precondition of correct formatting

#Takes input, prints sums of squares, then exits
def main():
    n = int(input())
    recursivePrint(0, recursiveProcessCase(n, list()))
    exit(1)

#recursively prints items from the list vals
def recursivePrint(i, vals):
    if (i <= len(vals)-1):
        print(vals[i])
        recursivePrint((i+1), vals)

#recursively processes cases, appending them to accumulator list
def recursiveProcessCase(n,vals):
    if(n > 0):
        vals.append(processCase())
        recursiveProcessCase((n-1), vals)
    return vals

#takes input and preforms calculations for each case, returning sum of
def processCase():
    x = int(input())
    val = sum(map(lambda n: n**2, (map (lambda y: int(y), input().split(" ", x)))))
    return val

if __name__ == '__main__':
    main()



