import atheris
import sys
import os

# Allow the harness to find the 'src' directory relative to this folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import decoder

def TestOneInput(data):
    try:
        # Call your specific image decoding function
        decoder.decode_image(data)
    except Exception:
        # Catch expected exceptions cleanly so the fuzzer keeps running
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
