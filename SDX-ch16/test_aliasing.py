from io import StringIO

from aliasing import SaveAlias, LoadAlias


# [roundtrip]
def roundtrip(fixture):
    writer = StringIO()
    SaveAlias(writer).save(fixture)
    reader = StringIO(writer.getvalue())
    return LoadAlias(reader).load()


# [/roundtrip]


def test_no_aliasing():
    fixture = [True, 1, "word"]
    assert roundtrip(fixture) == fixture


def test_duplicated_string():
    fixture = ["word", "word"]
    assert roundtrip(fixture) == fixture


def test_aliased_list():
    fixture = ["word"]
    fixture.append(fixture)
    result = roundtrip(fixture)
    assert len(result) == 2
    assert result[0] == "word"
    assert isinstance(result[1], list)
    assert len(result[1]) == 2
    assert result[1][0] == "word"


### Test runner
import time


def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    for name, test in globals().items():
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


if __name__ == "__main__":
    run_tests()
