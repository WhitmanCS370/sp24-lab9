from io import StringIO
from textwrap import dedent

from objects import LoadObjects, SaveObjects

def test_save_bool_single():
    fixture = StringIO()
    output = SaveObjects(fixture)
    output.save(True)
    assert output.writer.getvalue() == "bool:True\n"


def test_save_dict_empty():
    fixture = StringIO()
    output = SaveObjects(fixture)
    output.save({})
    assert output.writer.getvalue() == "dict:0\n"


def test_save_dict_flat():
    fixture = StringIO()
    output = SaveObjects(fixture)
    output.save({"alpha": "beta", 1: 2})

    expected = dedent("""\
    dict:2
    str:1
    alpha
    str:1
    beta
    int:1
    int:2
    """)
    assert output.writer.getvalue() == expected


def test_save_float_single():
    fixture = StringIO()
    output = SaveObjects(fixture)
    output.save(1.23)
    assert output.writer.getvalue() == "float:1.23\n"


def test_save_int_single():
    fixture = StringIO()
    output = SaveObjects(fixture)
    output.save(-456)
    assert output.writer.getvalue() == "int:-456\n"


# [test_save_list_flat]
def test_save_list_flat():
    fixture = [0, False]
    expected = dedent("""\
    list:2
    int:0
    bool:False
    """)
    output = StringIO()
    SaveObjects.save(fixture)
    assert output.getvalue() == expected
# [/test_save_list_flat]


def test_save_str_single():
    fixture = dedent("""\
    a
    b
    c
    """)
    expected = dedent("""\
    str:4
    a
    b
    c

    """)
    

def test_save_set_flat():
    fixture = {1, "a"}
    first = dedent("""\
    set:2
    int:1
    str:1
    a
    """
    )
    second = dedent("""\
    set:2
    str:1
    a
    int:1
    """
    )
    output = StringIO()
    SaveObjects.save(fixture)
    actual = output.getvalue()
    assert actual in {first, second}


def test_load_bool_single():
    fix = StringIO("bool:True\n")
    fixture = LoadObjects(fix)
    assert fixture.load() == True


def test_load_dict_empty():
    fix = StringIO("dict:0\n")
    fixture = LoadObjects(fix)
    assert fixture.load() == {}


def test_load_dict_flat():
    fix = StringIO(
        dedent("""\
        dict:2
        str:1
        alpha
        str:1
        beta
        int:1
        int:2
        """)
    )
    fixture = LoadObjects(fix)
    assert fixture.load() == {"alpha": "beta", 1: 2}


def test_load_float_single():
    fix = StringIO("float:1.23\n")
    fixture = LoadObjects(fix)
    assert fixture.load() == 1.23


def test_load_int_single():
    fix = StringIO("int:-456\n")
    fixture = LoadObjects(fix)
    assert fixture.load() == -456


def test_load_list_flat():
    fix = StringIO(
        dedent(
            """\
    list:2
    int:0
    bool:False
    """
        )
    )
    fixture = LoadObjects(fix)
    assert fixture.load() == [0, False]


def test_load_str_single():
    fix = StringIO(
        dedent(
            """\
    str:4
    a
    b
    c

    """
        )
    )
    expected = dedent(
        """\
    a
    b
    c
    """
    )
    fixture = LoadObjects(fix)
    assert fixture.load() == expected


def test_load_set_flat():
    fix = StringIO(
        dedent(
            """\
    set:2
    int:1
    str:1
    a
    """
        )
    )
    fixture = LoadObjects(fix)
    assert fixture.load() == {1, "a"}


def test_roundtrip():
    fix = ["a", {"b": 987.6}, {"c", True}]
    output = StringIO()
    SaveObjects.save(output, fixture)
    archive = output.getvalue()
    fixture = LoadObjects(fix)
    result = fixture.load(StringIO(archive))
    assert result == fixture

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
