#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyta
----------------------------------

Tests for `pyta` module.
"""

import unittest

import pyta


class TestPyta(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(pyta.__version__)

    def tearDown(self):
        pass
