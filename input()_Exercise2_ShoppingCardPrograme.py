#Excercise 2 Shopping card program

item = input ("What item you would like to buy? ;")
price = float(input("What is the price?: "))
quantity = int (input("How many items ? : "))
total = price * quantity

print (f"You have bought {quantity} X {item}/s ")
print(f"Your Total is LKR{total:.2f}")
