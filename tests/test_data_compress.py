import pytest
from data_compress.data_compress import *


@pytest.mark.parametrize('exception, arg', [(FileNotFoundError, ' '),
                                            (ValueError, 'tests_files/empty')])
def test_exceptions(exception, arg):
    with pytest.raises(exception):
        get_folder_files(arg)


def test_get_files():
    files = ['tests_files/files\\data.py',
             'tests_files/files\\2\\data.json']
    assert get_folder_files('tests_files/files') == files
