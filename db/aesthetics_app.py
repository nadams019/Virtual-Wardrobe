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
        Streetwear += 1
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

    elif question2 == "d":
        Streetwear += 1
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
        Streetwear += 1
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
        Streetwear += 1
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
        Streetwear += 1
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
        Streetwear += 1
        questionstobeansweredvariable += 1

    question7 = input("I have always been a___\n"
                      "(a) Girly girl \n"
                      "(b) Tom boy \n"
                      "(c)Book worm \n(d)Alte kid \n\n")

    if (question7 == "a"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    elif (question7 == "b"):
        Grunge += 1
        questionstobeansweredvariable += 1

    elif (question7 == "c"):
        Academia += 1
        questionstobeansweredvariable += 1

    elif (question7 == "d"):
        Streetwear += 1
        questionstobeansweredvariable += 1

    question8 = input("One item I can't live without is\n"
                      "(a) mini skirts \n"
                      "(b) platform boots \n"
                      "(c)blazer \n(d)skateboard \n\n")

    if (question8 == "a"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    elif (question8 == "b"):
        Grunge += 1
        questionstobeansweredvariable += 1

    elif (question8 == "c"):
        Academia += 1
        questionstobeansweredvariable += 1

    elif (question8 == "d"):
        Streetwear += 1
        questionstobeansweredvariable += 1

    question9 = input("My walls of my room look like\n"
                      "(a) lots of pastel  \n"
                      "(b) torn up posters \n"
                      "(c)my diploma \n"
                      "(d)hung up hats & skateboards\n\n")

    if (question9 == "a"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    elif (question9 == "b"):
        Grunge += 1
        questionstobeansweredvariable += 1

    elif (question9 == "c"):
        Academia += 1
        questionstobeansweredvariable += 1

    elif (question9 == "d"):
        Streetwear += 1
        questionstobeansweredvariable += 1

    question10 = input("When it comes to hair__\n"
                      "(a) Gimme all the bounce & curls \n"
                      "(b) Jet black wig \n"
                      "(c) Slick back bun\n"
                      "(d) helmet hair\n\n")

    if (question10 == "a"):
        Softgirl += 1
        questionstobeansweredvariable += 1

    elif (question10 == "b"):
        Grunge += 1
        questionstobeansweredvariable += 1

    elif (question10 == "c"):
        Academia += 1
        questionstobeansweredvariable += 1

    elif (question10 == "d"):
        Streetwear += 1
        questionstobeansweredvariable += 1

    if (questionstobeansweredvariable > 9):
        print("The result is out")
