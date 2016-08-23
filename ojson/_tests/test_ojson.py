# -*- coding: UTF-8 -*-
from __future__ import print_function, unicode_literals

from collections import OrderedDict

import pytest

import ojson


@pytest.fixture
def json_txt():
    return '''
        {
            "foo": {
                "bravo": 2,
                "alpha": 1,
                "charlie": 3
            }
        }
    '''


@pytest.mark.parametrize('as_file', [True, False])
def test_loads(tmpdir, json_txt, as_file):
    if as_file:
        json_file = tmpdir.join('file.json')
        json_file.write_text(json_txt, 'utf8')
        result = ojson.load(json_file)
    else:
        result = ojson.loads(json_txt)

    assert isinstance(result, OrderedDict) is True
    assert isinstance(result['foo'], OrderedDict) is True
    assert list(result['foo'].keys()) == ['bravo', 'alpha', 'charlie']
