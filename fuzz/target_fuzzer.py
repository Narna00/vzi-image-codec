import atheris
import sys

with atheris.instrument_imports():
    from src.decoder import parse_vzi

def TestOneInput(data):
    try:
        parse_vzi(data)
    except Exception:
        # Catch standard Python exceptions to keep the fuzzer running.
        # Native segmentation faults from memory corruption will bypass 
        # this block and cleanly register as a target crash.
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()