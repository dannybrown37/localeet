# localeet
A CLI tool to select and solve LeetCode and LeetCode-like problems locally


# installation

```
pip install localeet
```


# usage

This will find a random question from LeetCode's free question set.
It will create a Python file shell with the question description and
other metadata in it in your current working directory. It will finally
pop open a code editor (VSCode by default) with the new file opened in
it.

Using any of these CLI args will use the output path provided, and
create any needed directories in that path as well.

```
localeet --output_path ~/leetcode
localeet --path problems
localeet -o ~/leetcode/problems/2023-7-22
```

You can set the max or min difficulty of the problem selected using a
string or an int `{1: easy, 2: medium, 3: hard}`.

```
localeet --max_difficulty medium
localeet --max 1
localeet --min_difficulty 3
localeet --min hard
```

To specify a code editor other than VSCode, pass the CLI arg used to
open said editor using one of these args:

```
localeet -e charm
localeet --editor subl
localeet --code_editor_open_command atom
```


# contributions

## local setup

```
    git clone https://github.com/dannybrown37/localeet.git
    python -m venv .venv
    source .venv/bin/activate
    pip install -U pip
    pip install -e .[dev, test]
    pre-commit install
```

## contribution process

1. Create a new branch
2. Add features you wish to propose
3. Stage and commit your changes, ensure pre-commit checks pass
4. Push your branch
5. Open a pull request
6. Ensure Pull Request Verification CI/CD pipeline passes
7. Get approved & merged
8. Ensure Publish to PyPI pipeline passes


## feature ideas

* Support creating files for programming languages other than Python
* Add commitizen for auto version updating
* Support submitting responses to LeetCode via CLI as well
* Whatever your imagination holds
