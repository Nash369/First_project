import art



print(art.logo)
print("Welcome to Pizza deliveries!, please make your order")
  
size = input("Do you want small , medium or large? ").lower()

if size == "small":
  print("That will be $15")
elif size == "medium":
  print("That will be $20")
elif size == "large":
      print("That will be $25")
else:
  print("Sorry but that isn't on our menu")

add_pepperoni = input("Do you want extra pepperoni? ").lower()

if size == "small" and add_pepperoni == "yes":
  print("That will be an extra $2")
elif size == "medium" or "large" and add_pepperoni == "yes":
  print("That will be an extra $3")
elif size == "small" or "medium" or "large" and add_pepperoni == "no":
  print("Okay, how about cheese")
else:
  ("Sorry but that isn't on our menu")

cheese = input("Do you want extra cheese? ").lower()

if size == "small" and add_pepperoni == "yes" and cheese == "yes":
  print("Great! That will be another extra $1. Your total bill now is $18.")
elif size == "small" and add_pepperoni == "no" and cheese == "yes":
  print("Great! That will be an extra $1. Your total bill now is $16.")
elif size == "small" and add_pepperoni == "yes" and cheese == "no":
  print("Okay. Your total bill now is $17.")
elif size == "small" and add_pepperoni == "no" and cheese == "no":
  print("Okay. Your total bill is $15.")
elif size == "medium" and add_pepperoni == "yes" and cheese == "yes":
  print("Great! That will be another extra $1. Your total bill now is $24.")
elif size == "medium" and add_pepperoni == "no" and cheese == "yes":
  print("Great! That will be an extra $1. Your total bill now is $21.")
elif size == "medium" and add_pepperoni == "yes" and cheese == "no":
  print("Okay. Your total bill now is $23.")
elif size == "medium" and add_pepperoni == "no" and cheese == "no":
  print("Okay. Your total bill is $20.")
elif size == "large" and add_pepperoni == "yes" and cheese == "yes":
  print("Great! That will be another extra $1. Your total bill now is $29.")
elif size == "large" and add_pepperoni == "no" and cheese == "yes":
  print("Great! That will be an extra $1. Your total bill now is $26.")
elif size == "large" and add_pepperoni == "yes" and cheese == "no":
  print("Okay. Your total bill now is $28.")
elif size == "large" and add_pepperoni == "no" and cheese == "no":
  print("Okay. Your total bill is $25.")
else:
  print("Sorry but that isn't on our menu")
 
 
