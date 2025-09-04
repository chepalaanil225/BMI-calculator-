weight = float(input("Enter your weight in kg: ")) 
height = float(input("Enter your height in m: ")) 
bmi = weight / (height**2) 

if bmi < 18.5:
    print("You are underweight.") 
elif bmi > 18.5 and bmi <25:
    print("You have a normal weight.") 
elif bmi > 25 and bmi <30: 
    print("You are overweight.") 
else:
    print("You are obese.") 

print(f"Your BMI is {bmi:.2f}")
#Prints a formatted message. This uses an f-string (f"...") so you can embed expressions inside {}.
#{bmi:.2f} formats the bmi number to two decimal places.


