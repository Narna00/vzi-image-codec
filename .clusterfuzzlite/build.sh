#!/bin/bash -eu

# 1. Install atheris into the build image environment
pip3 install atheris

# 2. Compile the harness using the official wrapper tool
compile_python_fuzzer fuzz/target_fuzzer.py --paths=.
