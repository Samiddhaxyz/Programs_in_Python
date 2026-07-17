# welcome to the python version of the number guessing game 
def number_guesser():
    counter = 1
    got_it = False          

    for i in range(6):
        user_input = int(input("Enter your guesses over here !!  "))

        if user_input > 67:
            print("Too high ! lower number please ")
        elif user_input < 67:
            print(" Too low ! Higher number please ")
        else:
            print("You got the correct number congrats ! ")
            got_it = True    
            break
        counter += 1

    if got_it:
        print("you got the correct answer after", counter, "tries")
    else:
        print("you didn't get it in time, the answer was 67")
    

number_guesser()

count = 1

for i in range(11):
   user_choice = input("Are you willing to move forward with the game ? --->  yes/no")
   if user_choice.lower() == "yes":
      number_guesser()
      count += 1
   elif user_choice.lower() == "no":
      break
   else:
       print("invalid input. Please try again")
   
 
   


print("You played the game ", count, "times")



    
