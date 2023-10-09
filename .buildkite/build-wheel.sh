#!/bin/bash
set -eu
apt-get update -q
apt-get install -q -y \
    libboost-python-dev \
    libmapnik3.1 \
    libmapnik-dev \
    libcairo2-dev \
    python3-cairo-dev

export SKBUILD_CMAKE_VERBOSE=true
export SKBUILD_LOGGING_LEVEL=INFO
export SKBUILD_CMAKE_BUILD_TYPE=RelWithDebInfo

# not really needed here, but useful to know about
export SKBUILD_BUILD_DIR=build
export SKBUILD_CMAKE_DEFINE=CMAKE_CXX_STANDARD=14 # macOS

# needs to be a X.Y.Z.P version for CMake
COMMIT_TIME=$(git show -s --pretty=format:"%cd" --date=format:%Y%m%d%H%M%S)
perl -pi -e "s/version = \"(\d+\.\d+\.\d+).*\"/version = \"\$1.${COMMIT_TIME}\"/g" pyproject.toml

# build the wheel (to dist/)
python3 -m build -w .
