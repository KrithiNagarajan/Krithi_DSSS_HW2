import random


def numbers(min, max):
    
    return random.randint(min, max) #gives any random number between the range 


def operations():
    return random.choice(['+', '-', '*']) 


def quiz(num1, num2, operator):
    p = f"{num1} {operator} {num2}" 
    if operator == '+': 
      ans = num1 + num2
    elif operator == '-': 
      ans = num1 - num2
    else: 
      ans = num1 * num2
    return p, ans #gives the problem as well as the solution

def math_quiz():
    score = 0 #score earned by the user
    total = 5 #total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(total):
        num1 = numbers(1, 10) 
        num2 = numbers(1, 50)
        operator = operations()

        PROBLEM, ANSWER = quiz(num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")
        try:
          useranswer = input("Your answer: ")
          useranswer = int(useranswer)
        except ValueError:
          print("Invalid input")
          continue 


        if useranswer == ANSWER: #if the answer given by the user matches with the original answer,it is printed correct
            print("Correct! You earned a point.")
            score = score+1 #score is increased
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
            

    print(f"\nGame over! Your score is: {score}/{total}")

if __name__ == "__main__":
    math_quiz()