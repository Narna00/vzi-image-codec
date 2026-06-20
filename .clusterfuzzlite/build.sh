#!/bin/bash -eu

# Enable AddressSanitizer for C/C++ code
export CFLAGS="-fsanitize=address -fno-omit-frame-pointer -g -O1"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-fsanitize=address"

# Build the Python extension with sanitizer
pip install .

# Compile the fuzzer harness (inherit ASAN flags)
compile_python_fuzzer fuzz/fuzzer.py
