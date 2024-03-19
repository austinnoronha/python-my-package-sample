# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../sample_package/')))

from lib.helpers import generate_random_number, generate_uuid, get_answer
from sample_package import hello_world