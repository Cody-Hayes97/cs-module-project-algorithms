'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # create a new array to add the max values to
    result = []
    # while our variable on the left of the less than is not equal to 0
    # length is subtracted by k - 1 so that the window array finishes at the end og the original array
    # k - 1 is the length of the window basically
    while 0 < len(nums) - (k - 1):
        # start the window array from the first index to whichever index K represents
        window = nums[0:k]
        # in the scope of that array, find the max value and append it to the result array
        result.append(max(window))
        # remove the first item in the original array, so that when we loop through again,
        # the window starts at the index after it started last
        nums.pop(0)
    return result

 



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
