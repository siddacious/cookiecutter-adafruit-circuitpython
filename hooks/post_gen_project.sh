#!/bin/bash
echo "---- running post_gen_project.sh -----"
echo "Creating {{cookiecutter.repo_name}}"
CREATE_REPO=`which mkrepo`
echo "maybe executing "+$CREATE_REPO
if [ -n "$CREATE_REPO" ]; then
  echo "Running $CREATE_REPO {{cookiecutter.repo_name}} --YES"
  $CREATE_REPO {{cookiecutter.repo_name}} --YES
fi

git init .
git remote add adafruit {{cookiecutter.github_repo_url}}
git fetch adafruit
git merge adafruit/master
# add .files, everything else
git add .github/
	.gitignore .pre-commit-config.yaml .pylintrc .readthedocs.yml CODE_OF_CONDUCT.md LICENSE LICENSES/ README.rst README.rst.license adafruit_{{cookiecutter.library_name.lower()}}.py docs/ examples/ pyproject.toml requirements.txt setup.py


echo "DONE! Review, make changes, git add, push!"

exit 0
