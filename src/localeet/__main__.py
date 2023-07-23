"""
Entry point for CLI. Define and parse CLI arguments.
"""
from pathlib import Path

import click

from localeet.get_leetcode_problem import run
from localeet.language_maps import LANGUAGE_TO_EXTENSION


DIFFICULTY_MAP = {
    'easy': 1,
    'medium': 2,
    'hard': 3,
    '1': 1,
    '2': 2,
    '3': 3,
}

SUPPORTED_LANGUAGES = list(LANGUAGE_TO_EXTENSION.keys())


@click.command()
@click.option(
    '--max_difficulty', '--max',
    help='Max difficulty allowed',
    type=click.Choice(list(DIFFICULTY_MAP.keys())),
)
@click.option(
    '--min_difficulty', '--min',
    help='Min difficulty allowed',
    type=click.Choice(list(DIFFICULTY_MAP.keys())),
)
@click.option(
    '--output_path', '--path', '-o',
    help='Output path for code file created. Default is cwd. '
         'Will create new directories as needed',
    default='.',
)
@click.option(
    '--code_editor_open_command', '--editor', '-e',
    help='Will open the specified editor on the created file. VSCode default.',
    default='code',
)
@click.option(
    '--programming_language', '--language', '-l',
    help='The programming language you want to use for your output file',
    default='python3',

)
def main(
        max_difficulty: str,
        min_difficulty: str,
        output_path: str,
        code_editor_open_command: str,
        programming_language: str,
    ) -> None:
    """Entry point for CLI. Parse CLI arguments."""

    max_difficulty = DIFFICULTY_MAP.get(max_difficulty, 3)
    min_difficulty = DIFFICULTY_MAP.get(min_difficulty, 1)

    output_path = Path(output_path)

    language = programming_language.lower()
    if SUPPORTED_LANGUAGES.index(language) is None:
        msg = f'{programming_language} is not a supported languge'
        raise ValueError(msg)
    if language == 'python':
        language = 'python3'  # python2 is dead, long live python3
    elif language == 'go':
        language = 'golang'

    run(
        max_difficulty,
        min_difficulty,
        output_path,
        code_editor_open_command,
        language,
    )
