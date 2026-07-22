print("Helo, this is programm for calculations your BMI")

age = int(input("Enter your age: "))

weight = float(input("Enter your weight: (Example(81.5))"))

height = float(input("Enter your height: (Example(1.23))"))

result = round(weight / height ** 2 , 1) 

print("Your BMI:", result)

