#!/usr/bin/env python3
#
#
# Copyright (c) 2019, Ryo Nakamura.
# All rights reserved.
#
# $Id: textutil.py v1.1 2019/04/04 12:15:50 nakamura Exp $
#

import unicodedata

def vwidth(astr):
    width = 0
    for chr in astr:
        if unicodedata.east_asian_width(chr) == 'W':
            width += 2
        else:
            width += 1
    return width

def vwrap(astr, width=70):
    lines = []
    line, w = '', 0
    for chr in astr:
        w += vwidth(chr); line += chr
        if w >= width:
            lines.append(line)
            line, w = '', 0
    if line:
        lines.append(line)
    return lines
