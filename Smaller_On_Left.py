/* 
Initialize an empty stack.
Traverse the array from left to right:
While the stack is not empty and the top element of the stack is greater than or equal to the current array element, pop elements from the stack.
If the stack becomes empty, there is no smaller element to the left; append -1 to the result.
Otherwise, the top element of the stack is the nearest smaller element; append it to the result.
Push the current element onto the stack for future comparisons.
Repeat for all elements in the array.
*/


def nearest_smaller_to_left(arr):
    stack = []
    result = []

    for num in arr:
        # Remove elements from stack that are >= current number
        while stack and stack[-1] >= num:
            stack.pop()

        # If stack is empty, no smaller element exists
        if not stack:
            result.append(-1)
        else:
            # The top of the stack is the nearest smaller element
            result.append(stack[-1])

        # Push the current element onto the stack
        stack.append(num)

    return result

arr = [4, 5, 2, 10, 8]
print(nearest_smaller_to_left(arr))
