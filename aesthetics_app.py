from flask import Flask
import db.users as usr
'''
question_prompts = [
    "How would people describe you?\n(a)Bubbly \n(b)Edgy \n(c)An Old Soul\n(d) Kind \n\n",
    "What song would you add to your playlist?\n(a)Transparent Soul by Willow Smith \n(b)Honeymoon Avenue by Ariana Grande \n(c)Big Poppa by The Notorious B.I.G \n(d)EARFQUAKE by Tyler The Creator\n\n",
    "When I go to a party I prioritize being ___\n(a)comfortable \n(b)stylish \n(c) the star of the show \n(d) warmth\n\n",
    "I lean more towards ___ outfits\n(a) black \n(b) vibrant \n(c)earth tone \n(d)neutral \n\n"
]
questions = [
    Question()
]
'''
while True:
    questionstobeansweredvariable = 0
    above30variable = 0
    below30varable = 0

    print(input("Welcome to personality quiz test to know if you are 30 and above, enter any key to get started"))

    question1 = input("Do you have a job? enter 1 for yes and 2 for no!: ")

    if(question1 =="1"):
        above30variable = above30variable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    elif(question1 == "2"):
        below30varable = below30varable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    question2 = input("Are you done with college? enter 1 for yes and 2 for no!: ")

    if (question2 == "1"):
        above30variable = above30variable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    elif (question2 == "2"):
        below30varable = below30varable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    question3 = input("Are you married? enter 1 for yes and 2 for no!: ")

    if (question3 == "1"):
        above30variable = above30variable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    elif (question3 == "2"):
        below30varable = below30varable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    question4 = input("Do you own a house? enter 1 for yes and 2 for no!: ")

    if (question4 == "1"):
        above30variable = above30variable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    elif (question4 == "2"):
        below30varable = below30varable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    question5 = input("Do you have kids? enter 1 for yes and 2 for no!: ")

    if (question5 == "1"):
        above30variable = above30variable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    elif (question5 == "2"):
        below30varable = below30varable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    question6 = input("Choose how old are you kids? enter 1 above 10 years and 2 for below 10 years or none!: ")

    if (question6 == "1"):
        above30variable = above30variable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    elif (question6 == "2"):
        below30varable = below30varable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    question7 = input("Have you retired? enter 1 for yes and 2 for no!: ")

    if (question7 == "1"):
        above30variable = above30variable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    elif (question7 == "2"):
        below30varable = below30varable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    question8 = input("Do you have a grand child? enter 1 for yes and 2 for no!: ")

    if (question8 == "1"):
        above30variable = above30variable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    elif (question8 == "2"):
        below30varable = below30varable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    question9 = input("Do you have real estate? enter 1 for yes and 2 for no!: ")

    if (question9 == "1"):
        above30variable = above30variable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    elif (question9 == "2"):
        below30varable = below30varable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    question10 = input("Do you have a car? enter 1 for yes and 2 for no!: ")

    if (question10 == "1"):
        above30variable = above30variable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    elif (question10 == "2"):
        below30varable = below30varable + 1
        questionstobeansweredvariable = questionstobeansweredvariable + 1

    if (questionstobeansweredvariable > 9):
        print("The result is out")
        print("You have",above30variable/ 10 * 100,"% of chance of being above 30 years old and",below30varable/ 10 * 100,"% of being below 30 years old! ")
        input("press any key to start again: ")
