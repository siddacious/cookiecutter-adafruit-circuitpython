#!/bin/bash
echo "Creating {{cookiecutter.repo_name}}"
CREATE_REPO=`which mkrepo`
if $CREATE_REPO != ''; then
  echo "Running $CREATE_REPO {{cookiecutter.repo_name}} --YES"
  $CREATE_REPO {{cookiecutter.repo_name}} --YES
fi

git init .
git remote add adafruit {{cookiecutter.github_repo_url}}
git fetch adafruit
git merge adafruit/master
# add .files, everything else


echo "DONE! Review, make changes, git add, push!"

exit 0
