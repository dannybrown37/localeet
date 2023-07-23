from pathlib import Path

import pytest

from localeet.get_leetcode_problem import (
    choose_a_valid_question,
    get_question_data,
    output_code_file,
    parse_question_details,
    query_all_questions,
)
from localeet.language_maps import LANGUAGE_TO_EXTENSION


NUMBER_OF_QUESTIONS_WHEN_WRITING = 2787


def test_query_all_questions(any_int):
    """Test that query for question list works"""
    result = query_all_questions()
    assert len(result) >= NUMBER_OF_QUESTIONS_WHEN_WRITING
    assert result[-1] == {  # assuming order never changes...
        'difficulty': {'level': 1},
        'frequency': 0,
        'is_favor': False,
        'paid_only': False,
        'progress': 0,
        'stat': {
            'frontend_question_id': 1,
            'is_new_question': False,
            'question__article__has_video_solution': True,
            'question__article__live': True,
            'question__article__slug': 'two-sum',
            'question__hide': False,
            'question__title': 'Two Sum',
            'question__title_slug': 'two-sum',
            'question_id': 1,
            'total_acs': any_int,
            'total_submitted': any_int,
        },
        'status': None,
    }


def test_choose_a_valid_question():
    result = choose_a_valid_question(query_all_questions(), 1, 1)
    assert isinstance(result, str)


def test_get_question_data(
        two_sum_details_json,
        any_int,
        any_json_str,
        any_str,
    ):
    two_sum_details_json['data']['question'].update({
        'dislikes': any_int,
        'judgeType': any_str,
        'likes': any_int,
        'stats': any_json_str,
    })
    assert get_question_data('two-sum') == two_sum_details_json


def test_parse_question_details(two_sum_details_json, two_sum_essentials):
    assert parse_question_details(two_sum_details_json) == two_sum_essentials


@pytest.mark.parametrize('language', ['python', 'rust', 'golang'])
def test_output_python_file(
        two_sum_essentials,
        language,
    ):
    extension = LANGUAGE_TO_EXTENSION[language]
    with Path(f'tests/data/two_sum.{extension}').open() as f:
        expected = f.read()
    path = Path('.')
    new_file = path / f'two_sum.{extension}'
    output_path = output_code_file(path, two_sum_essentials, language)
    assert output_path == f'two_sum.{extension}'
    with new_file.open() as f:
        new_file_contents = f.read()
    try:
        assert new_file_contents == expected
    finally:
        new_file.unlink()
