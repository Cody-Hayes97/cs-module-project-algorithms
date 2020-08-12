'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
#    set the current index and create new array
   curr_i = 0
   result = []
#    make a loop that ends when the current index is equal to the length of the arr
   while curr_i < len(arr):
    #    set a new pointer for the index of the inside while loop
       inside = 0
    #    set the base that each index will be multiplied by 
       new_res = 1
    #    make a loop for the inside index so that it ends when the inside pointer is equal to the length of the arr
       while inside < len(arr):
        #    if the two pointers are equal, move index to point to the number after
           if inside == curr_i:
               inside += 1
           else:
            #    set the base num to be itself multiplied by the index of the array based on the inside pointer
               new_res = new_res * arr[inside]
            #    incrememnt the inside pointer
               inside += 1
        # append the multiplication of each inside index to the new array
       result.append(new_res)
    #    incrememnt the current pointer and the nested while loop starts again
       curr_i += 1
   return result
    




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
