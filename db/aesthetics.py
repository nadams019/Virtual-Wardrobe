"""
This module encapsulates details about the aesthetics quiz.
"""

TEST_RESPONSE = 'Test result'
QUESTION = 'question'
ANSWER = 'answer'
STYLE = 'style'

REQUIRED_FLDS = [QUESTION, ANSWER]
questions = {TEST_RESPONSE: {QUESTION: 'FOO', ANSWER: 'BAR'},
             'question2': {QUESTION: 'q2', ANSWER: 'a2'},
             'question3': {QUESTION: 'q3', ANSWER: 'a3'}, }

QUESTION_KEY = 'question'
QUESTIONS_COLLECT = 'questions'


def question_exists(question):
    return question in questions


def add_answer(question, answer):
    return


def add_field(question, answer):
    return


def add_question(question, answer):
    if not isinstance(question, str):
        raise TypeError(f'Wrong type for question: {type(question)=}')
    if not isinstance(answer, dict):
        raise TypeError(f'Wrong type for answers: {type(answer)=}')
    for field in REQUIRED_FLDS:
        if field not in answer:
            raise ValueError(f'Required {field=} missing from answers.')
    questions[question] = answer
