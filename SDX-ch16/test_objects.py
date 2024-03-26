from io import StringIO
from textwrap import dedent
#from objects import *
from objects import LoadObjects as load
from objects import SaveObjects as save
#from builtin import load, save

def test_save_bool_single_Objects():
    writer = StringIO()
    saver = save(writer)
    saver.save(True)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert True == loader.load()


def test_save_dict_empty():
    writer = StringIO()
    saver = save(writer)
    saver.save({})
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert {} == loader.load()


def test_save_dict_flat():
    fixture = {"alpha": "beta", 1: 2} 
    writer = StringIO()
    saver = save(writer)
    saver.save(fixture)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert loader.load() == fixture


def test_save_float_single():
    writer = StringIO()
    saver = save(writer)
    saver.save(1.23)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert 1.23 == loader.load()


def test_save_int_single():
    writer = StringIO()
    saver = save(writer)
    saver.save(-456)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert -456 == loader.load()


# [test_save_list_flat]
def test_save_list_flat():
    fixture = [0, False]
    writer = StringIO()
    saver = save(writer)
    saver.save(fixture)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert fixture == loader.load()
# [/test_save_list_flat]


def test_save_str_single():
    fixture = dedent("""\
    a
    b
    c
    """)
    writer = StringIO()
    saver = save(writer)
    saver.save(fixture)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert fixture == loader.load()


def test_save_set_flat():
    fixture = {1, "a"}
    first = 1
    second = "a"
    writer = StringIO()
    saver = save(writer)
    saver.save(fixture)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert loader.load() == {first, second}

"""
load tests
not needed due to the saver being compared to the load outputs


def test_load_bool_single():
    writer = StringIO()
    saver = save(writer)
    saver.save(True)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert True == loader.load()


def test_load_dict_empty():
    writer = StringIO()
    saver = save(writer)
    saver.save({})
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert {} == loader.load()


def test_load_dict_flat():
    fixture = {"alpha": "beta", 1: 2} 
    writer = StringIO()
    saver = save(writer)
    saver.save(fixture)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert loader.load() == fixture


def test_load_float_single():
    writer = StringIO()
    saver = save(writer)
    saver.save(1.23)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert 1.23 == loader.load()


def test_load_int_single():
    writer = StringIO()
    saver = save(writer)
    saver.save(-456)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert -456 == loader.load()


def test_load_list_flat():
    fixture = [0, False]
    writer = StringIO()
    saver = save(writer)
    saver.save(fixture)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert fixture == loader.load()


def test_load_str_single():
    fixture = StringIO(
        dedent(
            \
    str:4
    a
    b
    c

    
        )
    )
    expected = dedent(
        \
    a
    b
    c
    
    )
    assert load(fixture) == expected


def test_load_set_flat():
    fixture = StringIO(
        dedent(
            \
    set:2
    int:1
    str:1
    a
    
        )
    )
    assert load(fixture) == {1, "a"}
"""

def test_roundtrip():
    fixture = ["a", {"b": 987.6}, {"c", True}]
    writer = StringIO()
    saver = save(writer)
    saver.save(fixture)
    reader = StringIO(writer.getvalue())
    loader = load(reader)
    assert fixture == loader.load()

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
