'''
question_prompts = [
    "How would people describe you?\n(a)Bubbly \n(b)Edgy \n
    (c)An Old Soul\n(d) Kind \n\n",
    "What song would you add to your playlist?\n
    (a)Transparent Soul by Willow Smith \n(b)Honeymoon Avenue by Ariana Grande
    \n(
    c)Big Poppa by The Notorious B.I.G \n
    (d)EARFQUAKE by Tyler The Creator\n\n",
    "When I go to a party I prioritize being ___\n
    (a)comfortable \n(b)stylish \n
    (c) the star of the show \n(d) warmth\n\n",
    "I lean more towards ___ outfits\n(a) black \n
    (b) vibrant \n(c)earth tone \n
    (d)neutral \n\n"
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

    print(input("Still trying to figure out your personal style? "
                "Take the style aesthetics quiz to see what "
                "aesthetic is more YOU"))

    question1 = input("How would people describe you?\n(a)Bubbly \n"
                      "(b)Edgy \n"
                      "(c)An Old Soul\n"
                      "(d) Kind \n\n")
#
    if (question1 == "a"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    elif (question1 == "b"):
        Grunge += 1
        questionstobeansweredvariable += 1

    elif (question1 == "c"):
        Academia += 1
        questionstobeansweredvariable += 1

    elif (question1 == "d"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    question2 = input("What song would you add to your playlist?\n"
                      "(a)Transparent Soul by Willow Smith \n"
                      "(b)Honeymoon Avenue by Ariana Grande \n"
                      "(c)Big Poppa by The Notorious B.I.G \n"
                      "(d)EARFQUAKE by Tyler The Creator\n\n")

    if (question2 == "a"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    elif (question2 == "b"):
        Grunge += 1
        questionstobeansweredvariable += 1

    elif (question2 == "c"):
        Academia += 1
        questionstobeansweredvariable += 1

    elif (question2 == "d"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    question3 = input("When I go to a party I prioritize being ___\n"
                      "(a)comfortable "
                      "\n(b)stylish \n"
                      "(c) the star of the show \n"
                      "(d) warmth\n\n")

    if (question3 == "a"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    elif (question3 == "b"):
        Grunge += 1
        questionstobeansweredvariable += 1

    elif (question3 == "c"):
        Academia += 1
        questionstobeansweredvariable += 1

    elif (question3 == "d"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    question4 = input("I lean more towards ___ outfits\n(a) black \n"
                      "(b) vibrant \n(c)earth tone \n(d)neutral \n\n")

    if (question4 == "a"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    elif (question4 == "b"):
        Grunge += 1
        questionstobeansweredvariable += 1

    elif (question4 == "c"):
        Academia += 1
        questionstobeansweredvariable += 1

    elif (question4 == "d"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    question5 = input("A city I'd love to live in would be ____\n"
                      "(a) Paris \n"
                      "(b) NYC \n(c)LA \n(d)Dubai \n\n")

    if (question5 == "a"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    elif (question5 == "b"):
        Grunge += 1
        questionstobeansweredvariable += 1

    elif (question5 == "c"):
        Academia += 1
        questionstobeansweredvariable += 1

    elif (question5 == "d"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    question6 = input("My go-to drink at a cafe is___\n"
                      "(a) Water \n"
                      "(b) Black Coffee \n"
                      "(c)Chai Latte \n(d)Anything sweet! \n\n")

    if (question6 == "a"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    elif (question6 == "b"):
        Grunge += 1
        questionstobeansweredvariable += 1

    elif (question6 == "c"):
        Academia += 1
        questionstobeansweredvariable += 1

    elif (question6 == "d"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    if (questionstobeansweredvariable > 9):
        print("The result is out")
