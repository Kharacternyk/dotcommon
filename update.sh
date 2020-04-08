#!/bin/bash

DATE=$(date +"%R %D")

./crawler.py && \
git reset && \
git stage README.rst && \
git commit -m "Update $DATE." && \
git push
