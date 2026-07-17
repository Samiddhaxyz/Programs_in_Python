# welcome to the ultimate program for tower of hanoi
# functional backends
# direct formula apprach 
def tower_of_hanoi(user_input):
     return (2**user_input - 1) 
# this is the recursive version of the same
def tower_of_hanoi_recursive(user_input):
    if user_input == 0:
         return 0 
    else:
        store = tower_of_hanoi_recursive(user_input - 1) 
        return ( store + store  + 1 ) 
    # this is the iterative version 
def tower_of_hanoi_iterative(user_input):
    total = 0
    for i in range(1, user_input + 1):
        total = total + total + 1
    return total

# main program 
user_input = int(input("Enter a number of your choice"))
print(" enter """"dir"""" for witnessing the direct approach")
print(" enter """"rec"""" for witnessing the recursive approach")
print(" enter """"ite"""" for witnessing the iterative approach")
operator = input("Enter your desired operator  ").lower()
if operator == "dir":
   print("The result of tower of hanoi through direct approach is  ", tower_of_hanoi(user_input))
elif operator == "rec":
    print("The result of the tower of hanoi through recursive approach is  ", tower_of_hanoi_recursive(user_input))
elif operator == "ite":
    print("The result of the tower of hanoi through iterative approach is  ", tower_of_hanoi_iterative(user_input))
else:
    print("invalid operation given")



