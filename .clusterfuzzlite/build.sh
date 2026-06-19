#!/bin/bash -eu

# Compile and bundle the Atheris harness into a self-contained executable within $OUT
compile_python_fuzzer fuzz/target_fuzzer.py
