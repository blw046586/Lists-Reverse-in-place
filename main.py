import sys

# Read all input as a list of strings
data = list(map(int, sys.stdin.read().split()))

# First value is the number of items
num_inputs = data[0]

# The rest are the list elements
list_nums = data[1:]

# Reverse list in place (swapping front/back)
for i in range(num_inputs // 2):
    temp = list_nums[i]
    list_nums[i] = list_nums[num_inputs - 1 - i]
    list_nums[num_inputs - 1 - i] = temp

# Output the reversed list
for i in range(num_inputs):
    print(list_nums[i], end=" ")

print("")
