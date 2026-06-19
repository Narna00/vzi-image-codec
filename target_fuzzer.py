import atheris
import sys

from src import decoder

@atheris.instrument_func
def TestOneInput(data):
    try:
        decoder.decode_image(data)
    except Exception:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
