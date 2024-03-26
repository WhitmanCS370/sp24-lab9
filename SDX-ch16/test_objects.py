from io import StringIO
from textwrap import dedent

from io import StringIO
from objects import SaveObjects, LoadObjects

def test_save_bool():
    output = StringIO()
    saver = SaveObjects(output)
    saver.save(True)
    assert output.getvalue() == "bool:True\n"

def test_save_float():
    output = StringIO()
    saver = SaveObjects(output)
    saver.save(1.23)
    assert output.getvalue() == "float:1.23\n"

def test_save_int():
    output = StringIO()
    saver = SaveObjects(output)
    saver.save(-456)
    assert output.getvalue() == "int:-456\n"

def test_save_str():
    output = StringIO()
    saver = SaveObjects(output)
    saver.save("abc")
    #print("test_save_Str", output.getvalue())
    assert output.getvalue() == "str:1\nabc\n"

def test_save_list():
    output = StringIO()
    saver = SaveObjects(output)
    saver.save([1, 2, 3])
    assert output.getvalue() == "list:3\nint:1\nint:2\nint:3\n"

def test_save_set():
    output = StringIO()
    saver = SaveObjects(output)
    saver.save({1, 2, 3})
    assert output.getvalue() == "set:3\nint:1\nint:2\nint:3\n"

def test_save_dict():
    output = StringIO()
    saver = SaveObjects(output)
    saver.save({"key1": "value1", "key2": "value2"})
    assert output.getvalue() == "dict:2\nstr:1\nkey1\nstr:1\nvalue1\nstr:1\nkey2\nstr:1\nvalue2\n"

def test_load_bool():
    input = StringIO("bool:True\n")
    loader = LoadObjects(input)
    assert loader.load() == True

def test_load_float():
    input = StringIO("float:1.23\n")
    loader = LoadObjects(input)
    assert loader.load() == 1.23

def test_load_int():
    input = StringIO("int:-456\n")
    loader = LoadObjects(input)
    assert loader.load() == -456

def test_load_str():
    input = StringIO("str:1\nabc\n")
    loader = LoadObjects(input)
    assert loader.load() == "abc"

def test_load_list():
    input = StringIO("list:3\nint:1\nint:2\nint:3\n")
    loader = LoadObjects(input)
    assert loader.load() == [1, 2, 3]

def test_load_set():
    input = StringIO("set:3\nint:1\nint:2\nint:3\n")
    loader = LoadObjects(input)
    assert loader.load() == {1, 2, 3}

def test_load_dict():
    input = StringIO("dict:2\nstr:1\nkey1\nstr:1\nvalue1\nstr:1\nkey2\nstr:1\nvalue2\n")
    loader = LoadObjects(input)
    assert loader.load() == {"key1": "value1", "key2": "value2"}

### Test runner
import time

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
