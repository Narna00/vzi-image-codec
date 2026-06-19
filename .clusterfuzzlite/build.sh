#!/bin/bash -eu

# Compile the python harness located at the root directory
# We include --paths=. so the compiler can map your 'src' folder perfectly
compile_python_fuzzer target_fuzzer.py --paths=.

# Create the required destination folder for your seed corpus
mkdir -p $OUT/target_fuzzer_corpus

# Copy your corpus seeds into the destination if they exist
if [ -d "fuzz/corpus" ]; then
    cp fuzz/corpus/* $OUT/target_fuzzer_corpus/ 2>/dev/null || true
fi
