#For Loop

board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
   print(game)
for sport in sport_games:
  print(sport)


#Using Range in Loops
promise = "I will not chew gum in class"
for i in range(6):
  print(promise)

#while loop
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  
print(students_in_poetry)




#Nested Loops

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for element in location:
    scoops_sold += element
    print(scoops_sold)
  print(location)



#List Comprehensions
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = (height for height in heights if height > 161)

print(can_ride_coaster)


#More List Comprehensions
celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp*(9/5) + 32 for temp in celsius]

print(fahrenheit)





























