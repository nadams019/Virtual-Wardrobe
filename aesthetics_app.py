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
    Grunge = 0
    Academia = 0
    Streetwear = 0
    Softgirl = 0

    print(input("Still trying to figure out your personal style? Take the style aesthetics quiz to see what aesthetic is more YOU"))

    question1 = input("How would people describe you?\n(a)Bubbly \n(b)Edgy \n(c)An Old Soul\n(d) Kind \n\n)

    if(question1 =="a"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    elif(question1 == "b"):
        Grunge += 1
        questionstobeansweredvariable += 1

    elif (question1 == "c"):
        Academia += 1
        questionstobeansweredvariable += 1

    elif (question1 == "d"):
        Softgirl += 1
        questionstobeansweredvariable += 1



    if (questionstobeansweredvariable > 9):
        print("The result is out")
        input("press any key to start again: ")