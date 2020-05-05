# ------------------------------------------------
# -----------------Understanding------------------
# ------------------------------------------------



# ------------------------------------------------
# --------------------Planning--------------------
# ------------------------------------------------

# define it as a list
# define a smallest list, make it empty
# iterate through the list
  # sort the list so each inner array has the smallest number at index 0
  # append the index zero to a new list

# ------------------------------------------------
# ------------------Execution---------------------
# ------------------------------------------------

list =  [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

def smallest_sum (array):
  smallest_list = []

  for i in array:
    i.sort()
    print(array)
    smallest_list.append(i[0])
    print(smallest_list)
  
  return sum(smallest_list)

print(smallest_sum(list))