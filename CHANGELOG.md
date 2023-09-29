## 0.2.1 (2023-09-30)

### Fix

- remove unneeded blocks from cz config

## 0.2.0 (2023-09-30)

### Feat

- add cz in CI and remove CI test regarding version change
- add pip install confirmation in CI + --version CLI arg
- optionally overwrite default CLI args using environment variables
- add support for generating code in any leetcode programming language
- add support for generating code in any leetcode programming language
- add support for generating code in any leetcode programming language
- pop open code editor on new file; take cli arg to specify code editor other that default vscode
- add test to ensure version number has been updated as related to pypi version number
- add publishing to pypi on merge to main

### Fix

- various fixes to metadata, CI, output files, etc.
- fix version comparison in pypi.yaml
- wrap question line length at 79 characters
- remove invisible characters; wrap <code> blocks in
- fix docs example; fix test case in output file; add pip install post twine deploy
- skip version test except in CI/pre-commit + ruff on tests now + other code cleanup
- update docs with pypi installation and contributions section
- ran ruff on tests/; all rules don't necessarily apply so won't add to CI
- configuration for twine should work now
- tweak pypi deployment yml file