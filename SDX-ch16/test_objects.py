from io import StringIO
from textwrap import dedent
import sys

# from objects import load, save
from objects import SaveObjects, LoadObjects

def test_save_bool_single():
    with open("test_output.txt", "w") as f:
        saver = SaveObjects(f)
        saver.save(True)
    with open("test_output.txt", "r") as f:
        loader = LoadObjects(f)
        assert loader.load()

def test_save_dictionary():
    example_dictionary = {"""go to school today
                          
                          seven""": "5/2/2020", 0: ["one", "two", "three"], "thing 3": {"john", "zurain"}}
    with open("test_output.txt", "w") as f:
        saver = SaveObjects(f)
        saver.save(example_dictionary)
    with open("test_output.txt", "r") as f:
        loader = LoadObjects(f)
        assert example_dictionary == loader.load()

def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] += 1
        except Exception:
            results["error"] += 1
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")

if __name__ == '__main__':
    run_tests()
