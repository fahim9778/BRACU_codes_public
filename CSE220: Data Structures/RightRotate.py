"""Right Rotate an array by two position"""
def rightRotate(arr, d, n):
    for i in range(d):
        rightRotatebyOne(arr, n)
def rightRotatebyOne(arr, n):
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp
def printArray(arr,size):
    for i in range(size):
        print ("% d"% arr[i], end =" ")
arr = [1, 2, 3, 4, 5, 6, 7]
rightRotate(arr, 2, 7)
printArray(arr, 7)