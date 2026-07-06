import random
goal=(random.randint(1,100))
tries=0
while True:
    a=int(input("Guess the number between 1-100: "))
    if goal==a:
        print("congrats!! you have guessed the number")
        break
    elif goal>a:
        print("try a higher no.")
    elif goal<a:
        print("try a lower no.")
    tries=tries+1

print("you have guessed the number in ",tries)