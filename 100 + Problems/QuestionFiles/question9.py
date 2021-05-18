print("Enter something or press Enter to exit")
strs = []

while True:
   str = input("Enter a string: ")
   if str == "":
      break
   strs.append(str)

for str in strs:
   print(str.upper())
