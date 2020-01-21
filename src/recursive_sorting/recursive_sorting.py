arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
arr3 = [4,3,6,7,2,1]

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    merged_arr = arrA + arrB
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # if length of list is greater than 1 
    if len(arr) > 1:
        # find the middle, split the list into 2 halves
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        # use recursion for the 2 halves
        merge_sort(left)
        merge_sort(right)

        # set variables to 0
        a = 0
        b = 0 
        c = 0

        # while 0 is less than both halves
        while a < len(left) and b < len(right):
            # if the left index is less than the right index
            if left[a] < right[b]:
                # assign left index
                arr[c] = left[a]
                # increment left
                a += 1
            else:
                # else assign right index
                arr[c] = right[b]
                # increment right
                b += 1
            # increment through list 
            c +=1

        # while a is less than length of left half, increment
        while a < len(left):
            arr[c] = left[a]
            a += 1
            c += 1

        # while b is less than length of right half, increment
        while b < len(right):
            arr[c] = right[b]
            b += 1
            c += 1

    return arr
print(merge_sort(arr3))


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
