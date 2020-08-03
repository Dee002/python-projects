def odd_indices(lst):
  new_lst = []
  for i in list(range(len(lst))):
    if i % 2 != 0:
      new_lst.append(lst[i])
  return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))
