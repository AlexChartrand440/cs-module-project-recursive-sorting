# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB);
    merged_arr = [0] * elements;

    # Your code here
    
    indexA = 0;
    indexB = 0;
    indexM = 0;

    while len(arrA) > indexA and len(arrB) > indexB: 
        if arrA[indexA] > arrB[indexB]:
            merged_arr[indexM] = arrB[indexB];
            indexB += 1;
            indexM += 1;
        elif arrA[indexA] < arrB[indexB]:
            merged_arr[indexM] = arrA[indexA];
            indexA += 1;
            indexM += 1;

    while len(arrA) > indexA:
        merged_arr[indexM] = arrA[indexA];
        indexA += 1;
        indexM += 1;

    while len(arrB) > indexB:
        merged_arr[indexM] = arrB[indexB];
        indexB += 1;
        indexM += 1;

    return merged_arr;

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    if len(arr) < 2:
        return arr;

    index = len(arr) // 2;
    left = arr[:index];
    right = arr[index:];

    left = merge_sort(left);

    right = merge_sort(right);

    arr = merge(left, right);

    return arr;

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass;


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass;

