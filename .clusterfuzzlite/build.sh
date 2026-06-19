#!/bin/bash -eu
# Install the package (builds the C extension)
pip install .

# Compile the fuzzer into a self-contained binary
compile_python_fuzzer fuzz/fuzzer.py
