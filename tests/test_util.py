import sys
sys.path.insert(1, '..')

from pifx import util

def test_auth_header_generator():
    generated_header = util.generate_auth_header("abc123")
    auth_key = generated_header["Authorization"]

    assert auth_key == "Bearer abc123"

def test_arg_tup_to_dict():
    argument_tuples = [
        ('test1', None),
        ('test2', "abc123"),
        ('test3', "abc321"),
        ('test4', None)
    ]
    generated_dict = util.arg_tup_to_dict(argument_tuples)

    assert generated_dict.get('test1') == None
    assert generated_dict.get('test4') == None
    assert generated_dict.get('test2') == "abc123"
    assert generated_dict.get('test3') == "abc321"

def test_encode_url_path():
    url_path = "/12345/testing/words123"
    expected_path = "/12345/testing/words123"
    actual_path = url_encode_path(url_path)
    assert actual_path == expected_path
    
    url_path = "/label:Living Room Lights/"
    expected_path = "/label:Living%20Room%20Lights/"
    actual_path = url_encode_path(url_path)
    assert actual_path == expected_path
    
