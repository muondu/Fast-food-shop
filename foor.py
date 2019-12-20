fastfood = {
    "Chips" : 50,
    "Chicken" : 80,
   "Sausage" : 10
}
print(fastfood)
input1 = input("How many times do you want to print it:  ")
integer = int(input1)
constructor = list()

for c in range(integer):
    input2 = fruits[input("Enter what food you want:  ")]
    print("The price of the food is " + str(input2))
    
    
    constructor.append(input2)
    
    total = sum(constructor)
    
    
    print("Your total is " + str(total))