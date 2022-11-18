import pytest
import db.aesthetics as q


def test_valid_response():
    with pytest.raises(TypeError):
        q.add_answer("-", {})


def test_add_missing_field():
    with pytest.raises(ValueError):
        q.add_field('a new response', {'foo': 'bar'})


def test_add_question():
    details = {}
    for field in q.REQUIRED_FLDS:
        details[field] = 2
    q.add_question(q.TEST_RESPONSE, details)
    assert q.question_exists(q.TEST_RESPONSE)
