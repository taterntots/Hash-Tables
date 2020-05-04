lists = [[1, 2, 3], [4, 5, 10], [7, 8, 6]]

listA = [6, 3, 4, 2, 7, 9]
newList = []

merged_list = []

for l in lists:
  merged_list += l
  merged_list.sort()

print(merged_list)


# # smallest = lists[0]
# # second = lists[1]
# # third = lists[2]

# def find_smallest(array):
#   smallest = array[0]
#   for l in array:
#     if l < smallest:
#       smallest = l
  
#   return smallest

# for l in lists:
#   newList.push(lists[l])

# print(find_smallest(lists))