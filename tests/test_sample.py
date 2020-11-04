#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import logging
import os
from pathlib import Path

import kanilog
import pytest
import stdlogging
from add_parent_path import add_parent_path

with add_parent_path():
    import periodical_requests_recorder


def setup_module(module):
    pass


def teardown_module(module):
    pass


def setup_function(function):
    pass


def teardown_function(function):
    pass


def test_func():
    rec = periodical_requests_recorder.RequestsRecorder()
    rec.load_yaml(Path(__file__).parents[1] / "example.yaml")
    rec.start()


if __name__ == "__main__":
    kanilog.setup_logger(logfile='/tmp/%s.log' % (os.path.basename(__file__)), level=logging.INFO)
    stdlogging.enable()

    pytest.main([__file__, '-k test_', '-s'])
