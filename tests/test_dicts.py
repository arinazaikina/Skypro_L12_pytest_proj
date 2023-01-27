from utils import dicts


def test_get_val(test_dict, test_key, test_default_1, test_default_2, test_value):
    assert dicts.get_val(test_dict, test_key) == test_value
    assert dicts.get_val(test_dict, test_key, test_default_1) == test_value
    assert dicts.get_val({}, test_key, test_default_1) == test_default_1
    assert dicts.get_val({}, test_key, test_default_2) == test_default_2
