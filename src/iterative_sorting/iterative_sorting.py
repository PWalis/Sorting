import unittest
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # print('first loop') 
        for e in range(i+1, len(arr)):
            if arr[cur_index] > arr[e]:
                # print('less')
                arr[cur_index], arr[e] = arr[e], arr[cur_index]
            else:
                continue
    return list(arr)




l = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# m = []
# n = [1,2,3,4,5]
# print(selection_sort(l))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sorted = 0
    while sorted < len(arr)-1:
        # print(sorted, len(arr))
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = 0
            else:
                sorted+=1
                continue
    return arr

print(bubble_sort(l))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr