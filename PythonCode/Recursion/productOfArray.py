
# Write a function called productOfArray which takes in an array of 
# numbers and returns the product of them all.

# productOfArray([1,2,3]) // 6
# productOfArray([1,2,3,10]) // 60

def productOfArray(arr):
    if(len(arr) == 0 ): return 1
    return arr[0] * productOfArray(arr[1:])

val = productOfArray([1,2,3])
print(val)

