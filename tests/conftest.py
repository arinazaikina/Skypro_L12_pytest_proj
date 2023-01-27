import pytest


@pytest.fixture()
def test_dict():
    return {"vcs": "mercurial"}


@pytest.fixture()
def test_key():
    return "vcs"

@pytest.fixture()
def test_default_1():
    return "git"


@pytest.fixture()
def test_default_2():
    return "bazaar"


@pytest.fixture()
def test_value():
    return "mercurial"
