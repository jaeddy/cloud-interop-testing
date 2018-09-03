import logging
import pytest
import yaml
import textwrap
from datetime import datetime
from wfinterop import util

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_heredoc():
    test_string = util.heredoc(
        '''
        Mock string:
        {value}
        ''', {'value': 'mock_val'}
    )

    mock_string = "Mock string:\nmock_val\n"
    assert(test_string == textwrap.dedent(mock_string))


def test_get_yaml(tmpdir):
    mock_string = """
    section:
       key: {}
    """
    mock_file = tmpdir.join('mock.yaml')
    mock_file.write(textwrap.dedent(mock_string))

    test_object = util.get_yaml(str(mock_file))
    mock_object = {'section': {'key': {}}}

    assert(test_object == mock_object)


def test_save_yaml(tmpdir):
    mock_object = {'section': {'key': {}}}

    mock_file = tmpdir.join('mock.yaml')

    util.save_yaml(str(mock_file), mock_object)

    mock_string = "section:\n  key: {}\n"

    assert(mock_file.read() == mock_string)


def test_get_json(tmpdir):
    mock_string = """
    {
       "section": {
           "key": {}
        }
    }
    """
    mock_file = tmpdir.join('mock.json')
    mock_file.write(textwrap.dedent(mock_string))

    test_object = util.get_json(str(mock_file))
    mock_object = {'section': {'key': {}}}

    assert(test_object == mock_object)


def test_save_json(tmpdir):
    mock_object = {'section': {'key': {}}}

    mock_file = tmpdir.join('mock.json')

    util.save_json(str(mock_file), mock_object)

    mock_string = """{
    "section": {
        "key": {}
    }
}"""

    assert(mock_file.read() == textwrap.dedent(mock_string))


def test_ctime2datetime():
    mock_string = 'Sun Jan 01 00:00:00 2000'

    test_datetime = util.ctime2datetime(mock_string)

    assert(test_datetime == datetime(2000, 1, 1, 0, 0))


def test_convert_timedelta():
    mock_duration = datetime(2000, 1, 1, 1, 1) - datetime(2000, 1, 1, 0, 0)

    test_string = util.convert_timedelta(mock_duration)

    assert(test_string == '1h:1m:0s')
