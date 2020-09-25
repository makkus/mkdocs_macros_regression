#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tingex` package."""

import pytest  # noqa
import tingex


def test_assert():

    assert tingex.get_version() is not None
