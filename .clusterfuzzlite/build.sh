#!/bin/bash -eu

# 1. Install atheris into the build image environment
pip3 install atheris

# 2. Compile the harness using the official wrapper tool
# We pass --paths=. so PyInstaller can find your 'src' directory from the root
compile_python_fuzzer fuzz/target_fuzzer.py --paths=.
