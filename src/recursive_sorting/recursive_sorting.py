# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # compare value and merge so that it is sorted
    # Compare first item in list, smaller item gets appended to merged_arr
    # appended item gets taken off arr and merge happens again
    while True:
        if len(arrA) > 0 and len(arrB) > 0:
            a, b = arrA[0], arrB[0]
            if a < b:
                merged_arr.append(arrA.pop(0))
            else:
                merged_arr.append(arrB.pop(0))

        elif len(arrA) > 0 and len(arrB) == 0:
            merged_arr.append(arrA.pop(0))

        elif len(arrA) == 0 and len(arrB) > 0:
            merged_arr.append(arrB.pop(0))
        else:
            break

    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    mid_point = len(arr)//2
    if len(arr) <= 1:
        return arr
    else:
        # split at mid point
        arrA = arr[:mid_point]
        arrB = arr[mid_point:]
        return merge(merge_sort(arrA), merge_sort(arrB))

print(merge_sort([2,1,5,6,3]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
