'''
Generic questionnaire code.
'''

QUESTION = 'question'
ANSWERS = 'answers'
CHOICE = 'choice'
ANSWER = 'answer'
CATEGORY = 'category'

GRUNGE = 'grunge'
ACADEMIA = 'academia'
STREETWEAR = 'streetwear'
SOFTGIRL = 'softgirl'

SCORES = {
    GRUNGE: 0,
    ACADEMIA: 0,
    STREETWEAR: 0,
    SOFTGIRL: 0,
}

QUESTIONNAIRE = [
    {
        QUESTION: 'How would people describe you?',
        ANSWERS: {

            'a': {
                ANSWER: 'Bubbly',
                CATEGORY: SOFTGIRL,
            },
            'b': {
                ANSWER: 'Edgy',
                CATEGORY: GRUNGE,
            },
            'c': {
                ANSWER: 'An Old Soul',
                CATEGORY: ACADEMIA,
            },
            'd': {
                ANSWER: 'Unique',
                CATEGORY: STREETWEAR,
            },

        },
    },
    {
        QUESTION: 'What song would you add to your playlist?',
        ANSWERS: {
            'a': {
                ANSWER: 'Transparent Soul by Willow Smith',
                CATEGORY: GRUNGE,
            },
            'b': {
                ANSWER: 'Honeymoon Avenue by Ariana Grande',
                CATEGORY: SOFTGIRL,
            },
            'c':{
                ANSWER: 'Graduation by Kanye West',
                CATEGORY: ACADEMIA,
            },
            'd':{
                ANSWER: 'EARFQUAKE by Tyler The Creator',
                CATEGORY: STREETWEAR,
            },
        },
    },

]


def get_questionnaire():
    return QUESTIONNAIRE


def add_to_score(category):
    SCORES[category] += 1


def eval_scores():
    max_score = 0
    max_cat = None
    for cat in SCORES:
        if SCORES[cat] > max_score:
            max_score = SCORES[cat]
            max_cat = cat
    print(f'Your style is {max_cat}')


def is_valid_choice(answers, choice):
    return choice in answers


def get_category(answers, choice):
    return answers[choice][CATEGORY]


def run_questionnaire():
    print(input("Still trying to figure out your personal style? "
                "Take the style aesthetics quiz to see what "
                "aesthetic is more YOU"))
    for question in QUESTIONNAIRE:
        print(question[QUESTION])
        choice = None
        while True:
            answers = question[ANSWERS]
            for opt in answers:
                print(f'{opt}: {answers[opt][ANSWER]}')
            choice = input('Type the letter for your choice: ')
            if is_valid_choice(answers, choice):
                cat = get_category(answers, choice)
                add_to_score(cat)
                break
            else:
                print(f'Invalid choice: {choice}')
    print(SCORES)
    eval_scores()

    # question1 = input("How would people describe you?\n(a)Bubbly \n"
    #                   "(b)Edgy \n"
    #                   "(c)An Old Soul\n"
    #                   "(d)Unique \n\n")
    # #
    # if (question1 == "a"):
    #     softgirl += 1
    #     questionstobeansweredvariable += 1

    # elif (question1 == "b"):
    #     grunge += 1
    #     questionstobeansweredvariable += 1

    # elif (question1 == "c"):
    #     academia += 1
    #     questionstobeansweredvariable += 1

    # elif (question1 == "d"):
    #     streetwear += 1
    #     questionstobeansweredvariable += 1

    # question2 = input("What song would you add to your playlist?\n"
    #                   "(a)Transparent Soul by Willow Smith \n"
    #                   "(b)Honeymoon Avenue by Ariana Grande \n"
    #                   "(c)Graduation by Kanye West \n"
    #                   "(d)EARFQUAKE by Tyler The Creator\n\n")

    # if (question2 == "a"):
    #     grunge += 1
    #     questionstobeansweredvariable += 1

    # elif (question2 == "b"):
    #     softgirl += 1
    #     questionstobeansweredvariable += 1

    # elif (question2 == "c"):
    #     academia += 1
    #     questionstobeansweredvariable += 1

    # elif question2 == "d":
    #     streetwear += 1
    #     questionstobeansweredvariable += 1

    # question3 = input("When I go to a party I prioritize being ___\n"
    #                   "(a)comfortable "
    #                   "\n(b)stylish \n"
    #                   "(c) the star of the show \n"
    #                   "(d) warm\n\n")

    # if (question3 == "a"):
    #     softgirl += 1
    #     questionstobeansweredvariable += 1

    # elif (question3 == "b"):
    #     grunge += 1
    #     questionstobeansweredvariable += 1

    # elif (question3 == "c"):
    #     academia += 1
    #     questionstobeansweredvariable += 1

    # elif (question3 == "d"):
    #     streetwear += 1
    #     questionstobeansweredvariable += 1

    # question4 = input("I lean more towards ___ outfits\n(a) black \n"
    #                   "(b) vibrant \n(c)earth tone \n(d)neutral \n\n")

    # if (question4 == "a"):
    #     grunge += 1
    #     questionstobeansweredvariable += 1

    # elif (question4 == "b"):
    #     softgirl += 1
    #     questionstobeansweredvariable += 1

    # elif (question4 == "c"):
    #     academia += 1
    #     questionstobeansweredvariable += 1

    # elif (question4 == "d"):
    #     streetwear += 1
    #     questionstobeansweredvariable += 1

    # question5 = input("A city I'd love to live in would be ____\n"
    #                   "(a) Paris \n"
    #                   "(b) Seattle \n(c)LA \n(d)NYC \n\n")

    # if (question5 == "a"):
    #     academia += 1
    #     questionstobeansweredvariable += 1

    # elif (question5 == "b"):
    #     grunge += 1
    #     questionstobeansweredvariable += 1

    # elif (question5 == "c"):
    #     softgirl += 1
    #     questionstobeansweredvariable += 1

    # elif (question5 == "d"):
    #     streetwear += 1
    #     questionstobeansweredvariable += 1

    # question6 = input("My go-to drink at a cafe is___\n"
    #                   "(a) Water \n"
    #                   "(b) Black Coffee \n"
    #                   "(c)Chai Latte \n(d)Anything sweet! \n\n")

    # if (question6 == "a"):
    #     softgirl += 1
    #     questionstobeansweredvariable += 1

    # elif (question6 == "b"):
    #     grunge += 1
    #     questionstobeansweredvariable += 1

    # elif (question6 == "c"):
    #     academia += 1
    #     questionstobeansweredvariable += 1

    # elif (question6 == "d"):
    #     streetwear += 1
    #     questionstobeansweredvariable += 1

    # question7 = input("I have always been a___\n"
    #                   "(a) Girly girl \n"
    #                   "(b) Tom boy \n"
    #                   "(c)Book worm \n(d)Alte kid \n\n")

    # if (question7 == "a"):
    #     softgirl += 1
    #     questionstobeansweredvariable += 1

    # elif (question7 == "b"):
    #     grunge += 1
    #     questionstobeansweredvariable += 1

    # elif (question7 == "c"):
    #     academia += 1
    #     questionstobeansweredvariable += 1

    # elif (question7 == "d"):
    #     streetwear += 1
    #     questionstobeansweredvariable += 1

    # question8 = input("One item I can't live without is\n"
    #                   "(a) mini skirts \n"
    #                   "(b) platform boots \n"
    #                   "(c)blazer \n(d)skateboard \n\n")

    # if (question8 == "a"):
    #     softgirl += 1
    #     questionstobeansweredvariable += 1

    # elif (question8 == "b"):
    #     grunge += 1
    #     questionstobeansweredvariable += 1

    # elif (question8 == "c"):
    #     academia += 1
    #     questionstobeansweredvariable += 1

    # elif (question8 == "d"):
    #     streetwear += 1
    #     questionstobeansweredvariable += 1

    # question9 = input("My walls of my room look like\n "
    #                   "(a) lots of pastel  \n, "
    #                   "(b) torn up posters \n,"
    #                   "(c)my diploma \n,"
    #                   "(d)hung up hats & skateboards\n\n")

    # if (question9 == "a"):
    #     softgirl += 1
    #     questionstobeansweredvariable += 1

    # elif (question9 == "b"):
    #     grunge += 1
    #     questionstobeansweredvariable += 1

    # elif (question9 == "c"):
    #     academia += 1
    #     questionstobeansweredvariable += 1

    # elif (question9 == "d"):
    #     streetwear += 1
    #     questionstobeansweredvariable += 1

    # question10 = input("When it comes to hair__\n"
    #                    "(a) Gimme all the bounce & curls \n"
    #                    "(b) Jet black wig \n"
    #                    "(c) Slick back bun\n"
    #                    "(d) helmet hair\n\n")

    # if (question10 == "a"):
    #     softgirl += 1
    #     questionstobeansweredvariable += 1

    # elif (question10 == "b"):
    #     grunge += 1
    #     questionstobeansweredvariable += 1

    # elif (question10 == "c"):
    #     academia += 1
    #     questionstobeansweredvariable += 1

    # elif (question10 == "d"):
    #     streetwear += 1
    #     questionstobeansweredvariable += 1

    # question11 = input("I call my significant other___\n"
    #                    "(a) honey  \n"
    #                    "(b) boo\n"
    #                    "(c) scholar \n"
    #                    "d) pookie\n\n")

    # if (question11 == "a"):
    #     softgirl += 1
    #     questionstobeansweredvariable += 1

    # elif (question11 == "b"):
    #     grunge += 1
    #     questionstobeansweredvariable += 1

    # elif (question11 == "c"):
    #     academia += 1
    #     questionstobeansweredvariable += 1

    # elif (question11 == "d"):
    #     streetwear += 1
    #     questionstobeansweredvariable += 1


def main():
    run_questionnaire()


if __name__ == "__main__":
    main()
