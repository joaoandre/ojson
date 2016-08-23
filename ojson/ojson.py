# -*- coding: UTF-8 -*-
from __future__ import print_function, unicode_literals

import collections
from functools import partial
import json


dump = json.dump
dumps = json.dumps
load = partial(json.load, object_pairs_hook=collections.OrderedDict)
loads = partial(json.loads, object_pairs_hook=collections.OrderedDict)
