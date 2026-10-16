'''Random Fun Calculator'''
while True:
    
   import random
   Lucky_number = random.randint(0,15)
   print("I have a secret number between 0 - 15")
   print("You have to guess it.")
   guess = int(input("Enter your guess: "))
   if guess == Lucky_number:
      print("Lucky!")
      num4 = int(input("Enter the number which you want to add to the secret number: "))
      def add(num1,num2):
         addition = num1 + num2
         return addition
      print(f"Result: {add(Lucky_number,num4)}")
   else:
       print("That's a Wrong number.")
       num4 = int(input("Enter the number which you want to add to the secret number: "))
       def add(num1,num2):
         addition = num1 + num2
         return addition
       print(f"Result: {add(Lucky_number,num4)}")
     
   again = str(input("Do you want to play again (y/n): "))
   if again != "y":
    break     