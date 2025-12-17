"""
This is a Black History Quiz which ask the user to answer fun facts 
regarding black history. There are 7 questions total with each question
equaling 2 points for 14 points total.
"""
#Points start off as 0 with the user being able to score 14 points in total
points = 0

#For Question#1 q1 = stands for question 1 and q1_choices = stands for question 1 choices (a,b,c,d)
q1 = "Question 1: Who was the first Black United States Supreme Court Justice?\n"
q1_choices ="\n a) Clarence Thomas\n b) Thurgood Marshall\n c) Ketanji Brown Jackson\n d) Thorgood Marshall"
print(q1+q1_choices)
user_q1 = input("\nEnter a, b, c, or d: ")

"""
The if-else statements for these questions refer to the user picking out of the choices of "a,b,c,or d".
If they type in the correct letter it will award them with two points adding to their total of points. If 
the user types the wrong choice like for example in Question 1 "a" would be wrong, it results in them not 
recieving any points, which keeps their past total.
"""

if "b" == user_q1:
    points += 2
    print(f"\nYour answer is correct!You have earned two points,totaling to {points} points total.\n")
else:
    print("\n Your answer is wrong! You earned no points, totaling to {points} points.\n")

#For Question#2 q2 = stands for question 2 and q2_choices = stands for question 2 choices (a,b,c,d)
q2 = "Question 2: Who was the first black woman millionaire?\n"
q2_choices="\n a) Oprah Winfrey\n b) Sheila Johnson\n c) Madam C.J. Walker\n d) Ngina Kenyatta"
print(q2+q2_choices)
user_q2 = input("\nEnter a, b, c, or d : ")

if "c" == user_q2:
    points += 2
    print(f"\nYour answer is correct!You have earned two points,totaling to {points} points total.\n")
else:
    print(f"\n Your answer is wrong! You earned no points, keeping your {points} total points.\n")

#For Question#3 q3 = stands for question 3 and q3_choices = stands for question 3 choices (a,b,c,d)
q3 = "Question 3: What athlete broke the modern era of baseball color barrier in 1947?\n"
q3_choices = "\n a) Moses Fleetwood Walker\n b) Jackie Roberts\n c) Jackie Robison\n d) Josh Gibson"
print(q3+q3_choices)
user_q3 = input("\nEnter a, b, c, or d : ")

if "c" == user_q3:
    points += 2
    print(f"\nYour answer is correct!You have earned two points,totaling to {points} points total.\n")
else:
    print(f"\n Your answer is wrong! You earned no points, keeping your {points} total points.\n")

#For Question#4 q4 = stands for question 4 and q4_choices = stands for question 4 choices (a,b,c,d)
q4 = "Question 4: What Supreme Court case declared segregation in public schools unconstitutional?\n"
q4_choices = "\n a) Gideon v. Wainwright\n b) Miranda v. Arizona\n c) Dred Scott v. Sanford\n d) Brown v. Board of Education"
print(q4+q4_choices)
user_q4 = input("\nEnter a, b, c, or d : ")

if "d" == user_q4:
    points += 2
    print(f"\nYour answer is correct!You have earned two points,totaling to {points} points total.\n")
else:
    print(f"\n Your answer is wrong! You earned no points, keeping your {points} total points.\n")

#For Question#5 q5 = stands for question 5 and q5_choices = stands for question 5 choices (a,b,c,d)
q5 = "Question 5: Who founded the Black Panther Party in 1966?"
q5_choices = "\n a) Elaine Brown\n b) Huey P. Newton\n c) Eldridge Cleaver\n d) Bobby Hutton"
print(q5+q5_choices)
user_q5 = input("Enter a, b, c, or d : ")

if "b" == user_q5:
    points += 2
    print(f"\nYour answer is correct!You have earned two points,totaling to {points} points total.\n")
else:
    print(f"\n Your answer is wrong! You earned no points, keeping your {points} total points.\n")

#For Question#6 q6 = stands for question 6 and q6_choices = stands for question 6 choices (a,b,c,d)
q6= "Question 6: What amendment abolished slavery?"
q6_choices = "\n a) 13th\n b) 14th\n c) 15th\n d) 19th"
print(q6+q6_choices)
user_q6 = input("Enter a, b, c, or d : ")

if "a" == user_q6:
    points += 2
    print(f"\nYour answer is correct!You have earned two points,totaling to {points} points total.\n")
else:
    print(f"\n Your answer is wrong! You earned no points, keeping your {points} total points.\n")

#For Question#7 q7 = stands for question 7 and q7_choices = stands for question 7 choices (a,b,c,d)
q7= "Question 7: What state was the first to elect a black governor?"
q7_choices = "\n a) Maryland\n b) North Carolina\n c) Kentucky\n d) Virginia "
print(q7+q7_choices)
user_q7 = input("Enter a, b, c, or d : ")

if "d" == user_q7:
    points += 2
    print(f"\nYour answer is correct!You have earned two points,totaling to {points} points total.\n")
else:
    print(f"\n Your answer is wrong! You earned no points, keeping your {points} total points.\n")

"""
The Black History Quiz is now over and at the end the Quiz it
will print how many points the user attained in total out of 14. If the user points >8
then it will print how they passed. If the user points < 8
then it will print how they failed and how they should continue to study on their
Black History knowledge.
""" 
if points > 8:
    print(f"Congratulations, you passed! Scoring {points}/14.")
else:
    print(f"Unfortunately you failed, scoring {points}/14. That's okay you should continue to study up on your Black History knowledge!")

