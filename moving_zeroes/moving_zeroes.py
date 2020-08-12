'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # loop through arr
    for num in arr:
    # check if int is zero
        if num == 0:
            temp_num = num
            arr.remove(num)
             # if int is zero, save it to temp array
            arr.append(temp_num)
    # append temp array to end of original array
    return arr
    

    
print(moving_zeroes([0, 3, 1, 0, -2]))

# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [0, 3, 1, 0, -2]

#     print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")