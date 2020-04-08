#!/bin/bash
set -eu

[[ $# == 0 ]] && exit

for preset in "$@"; do
    ./src/$preset.py > ./data/$preset
done

cat README-TEMPLATE.rst data/* > README.rst

git reset && \
git stage README.rst && \
git commit -m "Update $DATE." && \
git push
