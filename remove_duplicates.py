# Remove duplicates in a sorted list

def remove_duplicates(nums): 
    """Removes duplicates from a sorted list in-place
        using the two-pointer technique.
    Args: nums (list): A sorted list of integers
    
    Returns: int: Count of unique elements (k)"""

    # 'Write' is a pointer (index) that tracks
    # Where the next unique value should be placed.
    # It starts at 0 because the first element
    write = 0

    # 'i' is the read/scanner pointer.
    # It starts at 1 because we compare each element
    # against the last written unique value (write).
    # No point comparing index 0 with itself.
    for i in range(1, len(nums)):

        # Compare the current scanned value nums[i]
        # Against the last unique value placed at nums[write]
        # If they are different, we found a new unique element.
        if nums[i] != nums[write]:

            # Move the write pointer one step forward.
            # To make room for the new unique value.
            write += 1

            # Copy the new unique value from the scanner
            # Position (i) into the write position.
            # This is the in-place overwrite.
            nums[write] = nums[i]

    # write is a zero-based index, so the total
    # count of unique elements is write + 1.
    return write + 1



nums = [11, 11, 22, 33, 33, 55, 55, 66]

length= remove_duplicates(nums)

print(length)
print(nums[:length])

