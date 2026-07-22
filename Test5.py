import random

number = random.randint(1, 100)

attempts = 0

while True:
   userAnswer = int(input("Введите целое число от 1 до 100")) 
   attempts += 1
   if userAnswer > number:
     print("Число меньше")

   elif userAnswer < number:
     print("Число больше")

   else:
     print(f"Вы угадали число за {attempts} попыток")
     break