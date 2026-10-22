import pytest

def f():
    raise SystemExit(1)

def test_sample():
    with pytest.raises(SystemExit):
        f()