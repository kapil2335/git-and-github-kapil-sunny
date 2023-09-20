beverage = "Diet Coke"
count = 5

for num in range(count):
 print(count, "bottles of", beverage, "on the wall")
 print(count, "bottles of", "water")
 print("Take one down, pass it around")
 count = count - 1
 if(count!=0):
  print(count, "bottles of", beverage, "on the wall")
 else:
  print("No  more", "bottles of", beverage, "on the wall")
 print("")



