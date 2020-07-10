#Write your function here
def every_three_nums(start):
  empty = []
  notempty = list(range(start, 101, 3))
  if start > 100:
    return empty
  else:
    return notempty

#Uncomment the line below when your function is done
print(every_three_nums(91))
