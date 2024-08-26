# Python program to move all zeros to the end

original_list = [5, 6, 0, 4, 6, 0, 9, 0, 8]
size = len(original_list)
modified_list = [0] * size
non_zero_index = 0
zero_count = 0

# Move non-zero elements to the new list
for i in range(size):
    if original_list[i] != 0:
        modified_list[non_zero_index] = original_list[i]
        non_zero_index += 1
    else:
        zero_count += 1

# Fill the end of the list with zeros
while zero_count > 0:
    modified_list[non_zero_index] = 0
    zero_count -= 1
    non_zero_index += 1

# Copy modified list back to the original list
for i in range(size):
    original_list[i] = modified_list[i]

# Print the modified array
for element in original_list:
    print(element, end=' ')
