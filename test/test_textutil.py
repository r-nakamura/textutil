#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from textutil import vwidth, vwrap 

def test_vwidth():
    assert vwidth('あいうえお') == 10
    assert vwidth('abc') == 3
    assert vwidth('abcあいうえお') == 13

def test_vwrap():
    assert vwrap('あいうえおかきくけこ', width=10) == ['あいうえお', 'かきくけこ'] 
    assert vwrap('あいうえおかき', width=10) == ['あいうえお', 'かき'] 
    assert vwrap('abcdefあいうえお', width=10) == ['abcdefあい', 'うえお'] 
