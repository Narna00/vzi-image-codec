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
