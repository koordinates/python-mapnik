#!/bin/bash
set -eu
apt-get update -q
apt-get install -q -y --no-install-recommends \
    libmapnik4.0 \
    libmapnik-dev \
    libcairo2-dev

pip install build pycairo

export PYCAIRO=true
export SYSTEM_FONTS=/usr/share/fonts

# needs to be a X.Y.Z.P version for setuptools
COMMIT_TIME=$(git show -s --pretty=format:"%cd" --date=format:%Y%m%d%H%M%S)
perl -pi -e "s/version = \"(\d+\.\d+\.\d+).*\"/version = \"\$1.${COMMIT_TIME}\"/g" pyproject.toml

# build the wheel (to dist/)
python3 -m build -w --no-isolation .
