"""Change the array nums such that the first k elements of nums contain the elements which are equal to val.
      Approach - Two Pointer (In-place Overwrite).
    - A reader that scans every element in the array.
    - A writer that only moves forward when it finds a valid element to place."""

def removeElements(nums, val):
    k = 0    # Write pointer
    for i in range(len(nums)): # read pointer
        if nums[i] != val:     # found a valid element 
            nums[k] = nums[i]  # overwrite at write position 
            k += 1             # advance write pointer             
    return k                   # Count of valid elements (without val)

def test_case():
    tst_input1 = list(map(int,input("Number list: ").split(',')))
    tst_input2 = int(input("The Element: "))

    k = removeElements(tst_input1, tst_input2)

    print("New length: ", k)
    print("Updated list:", tst_input1[:k])

test_case()

    
