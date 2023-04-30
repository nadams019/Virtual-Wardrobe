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
            'c': {
                ANSWER: 'Graduation by Kanye West',
                CATEGORY: ACADEMIA,
            },
            'd': {
                ANSWER: 'EARFQUAKE by Tyler The Creator',
                CATEGORY: STREETWEAR,
            },
        },
    },
    {
        QUESTION: 'When I go to a party I prioritize being ___',
        ANSWERS: {
            'a': {
                ANSWER: 'Comfortable',
                CATEGORY: SOFTGIRL,
            },
            'b': {
                ANSWER: 'Stylish',
                CATEGORY: GRUNGE,
            },
            'c': {
                ANSWER: 'The star of the show',
                CATEGORY: ACADEMIA,
            },
            'd': {
                ANSWER: 'Warm',
                CATEGORY: STREETWEAR,
            },
        },
    },
    {
        QUESTION: 'I lean more towards ___ outfits',
        ANSWERS: {
            'a': {
                ANSWER: 'Vibrant',
                CATEGORY: SOFTGIRL,
            },
            'b': {
                ANSWER: 'Earth tone',
                CATEGORY: STREETWEAR,
            },
            'c': {
                ANSWER: 'Neutral',
                CATEGORY: ACADEMIA,
            },
            'd': {
                ANSWER: 'Black',
                CATEGORY: GRUNGE,
            },
        },
    },
    {
        QUESTION: 'A city I would love to live in is ___',
        ANSWERS: {
            'a': {
                ANSWER: 'Paris',
                CATEGORY: ACADEMIA,
            },
            'b': {
                ANSWER: 'Seattle',
                CATEGORY: GRUNGE,
            },
            'c': {
                ANSWER: 'LA',
                CATEGORY: SOFTGIRL,
            },
            'd': {
                ANSWER: 'NYC',
                CATEGORY: STREETWEAR,
            },
        },
    },
    {
        QUESTION: 'My go-to drink at a cafe is ___',
        ANSWERS: {
            'a': {
                ANSWER: 'Water',
                CATEGORY: STREETWEAR,
            },
            'b': {
                ANSWER: 'Black Coffee',
                CATEGORY: GRUNGE,
            },
            'c': {
                ANSWER: 'Chai Latte',
                CATEGORY: ACADEMIA,
            },
            'd': {
                ANSWER: 'Anything sweet!',
                CATEGORY: SOFTGIRL,
            },
        },
    },
    {
        QUESTION: 'I have always been a ___',
        ANSWERS: {
            'a': {
                ANSWER: 'Girly girl',
                CATEGORY: SOFTGIRL,
            },
            'b': {
                ANSWER: 'Tom boy',
                CATEGORY: STREETWEAR,
            },
            'c': {
                ANSWER: 'Book worm',
                CATEGORY: ACADEMIA,
            },
            'd': {
                ANSWER: 'Alte kid',
                CATEGORY: GRUNGE,
            },
        },
    },
    {
        QUESTION: 'One item I cannot live without is ___',
        ANSWERS: {
            'a': {
                ANSWER: 'Mini skirts',
                CATEGORY: SOFTGIRL,
            },
            'b': {
                ANSWER: 'Platform boots',
                CATEGORY: GRUNGE,
            },
            'c': {
                ANSWER: 'Blazer',
                CATEGORY: ACADEMIA,
            },
            'd': {
                ANSWER: 'Skateboard',
                CATEGORY: STREETWEAR,
            },
        },
    },
    {
        QUESTION: 'The walls of my room look like ___',
        ANSWERS: {
            'a': {
                ANSWER: 'lots of pastels',
                CATEGORY: SOFTGIRL,
            },
            'b': {
                ANSWER: 'my diploma',
                CATEGORY: ACADEMIA,
            },
            'c': {
                ANSWER: 'torn up posters',
                CATEGORY: GRUNGE,
            },
            'd': {
                ANSWER: 'hung up hats & skateboards',
                CATEGORY: STREETWEAR,
            },
        },
    },
    {
        QUESTION: 'When it comes to my hair __',
        ANSWERS: {
            'a': {
                ANSWER: 'Gimme all the bounce & curls!',
                CATEGORY: SOFTGIRL,
            },
            'b': {
                ANSWER: 'Slick back bun',
                CATEGORY: ACADEMIA,
            },
            'c': {
                ANSWER: 'Buzz cut',
                CATEGORY: STREETWEAR,
            },
            'd': {
                ANSWER: 'Jet black wig',
                CATEGORY: GRUNGE,
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
    # print(SCORES)
    eval_scores()


def main():
    run_questionnaire()


if __name__ == "__main__":
    main()
