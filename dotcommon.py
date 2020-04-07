#!/usr/bin/env -S python -i

import sys

sys.ps1 = ".c'mon> "
sys.ps2 = ".c'mon~ "

from github import Github

import dotcommon.crawler as crawler
import dotcommon.presets as presets
