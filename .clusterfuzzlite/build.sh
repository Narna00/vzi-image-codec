#!/bin/bash -eu

compile_python_fuzzer target_fuzzer.py

mkdir -p $OUT/target_fuzzer_corpus

if [ -d "fuzz/corpus" ]; then
    cp fuzz/corpus/* $OUT/target_fuzzer_corpus/ 2>/dev/null || true
fi
