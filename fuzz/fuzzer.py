import atheris
import sys
import myparser

def TestOneInput(data):
    try:
        myparser.parse(data)
    except Exception:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
