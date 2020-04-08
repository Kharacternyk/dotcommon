#!/bin/bash
set -eu

[[ $# != 1 ]] && exit

./src/$1.py > ./data/$1

cat README-TEMPLATE.rst data/* > README.rst

cd data

git reset && \
git stage ../README.rst "$1" && \
git commit -m "Update $1." && \
git push
