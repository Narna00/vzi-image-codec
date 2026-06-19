Markdown
# vzi-image-codec

A lightweight, high-performance Python decoder engine designed for the Vectorized Zone Image (VZI) format. This library utilizes native heap memory management via `ctypes` to achieve low-overhead, fast decompression and parsing of binary image data streams.

## Features

* **Zero-Copy Performance:** Uses native heap allocation via `ctypes` buffers to minimize serialization overhead.
* **Hybrid Stream Processing:** Supports structured RLE (Run-Length Encoding) chunks and raw literal blocks.
* **Minimal Dependencies:** Built strictly using the Python standard library, making it highly portable and suitable for embedded environments.

---

## Installation

To set up the development environment locally, clone the repository and ensure you have Python 3.8+ installed:

```bash
git clone [https://github.com/Narna00/vzi-image-codec.git](https://github.com/Narna00/vzi-image-codec.git)
cd vzi-image-codec
Usage
You can process raw VZI bitstreams passing standard Python bytes objects directly into the core decoder module.

Python
from src.decoder import parse_vzi

# Read a compressed VZI file
with open("sample.vzi", "rb") as f:
    binary_data = f.read()

# Execute the decoding pipeline
success = parse_vzi(binary_data)

if success:
    print("Image stream decoded successfully into native memory block.")
else:
    print("Failed to decode stream: Invalid header or corrupted payload.")
Testing & Quality Assurance
This repository includes continuous robustness validation via differential testing and fuzzing harnesses.

Local Fuzzing Integration
The project is structured to seamlessly integrate with ClusterFuzzLite and uses Atheris for coverage-guided mutation fuzzing. To execute the harness locally:

Install the fuzzing engine:

Bash
   pip install atheris
Execute the fuzz target from the repository root:

Bash
   python3 fuzz/target_fuzzer.py
