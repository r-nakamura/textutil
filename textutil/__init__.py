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
    """Return the correct length of ASTR including half-width and
    full-width characters.  This function is equivalent to a function
    of Perl module, Text::VisualWidth::PP::width. """
    width = 0
    for char in astr:
        if unicodedata.east_asian_width(char) == 'W':
            width += 2
        else:
            width += 1
    return width

def vwrap(astr, width=70):
    """Wrap ASTR to multiple lines, each of which is at most WIDTH
    characters.  The main difference between vwrap and textwrap.wrap
    is how to count full-width characters."""
    lines = []
    line, w = '', 0
    for char in astr:
        w += vwidth(char); line += char
        if w >= width:
            lines.append(line)
            line, w = '', 0
    if line:
        lines.append(line)
    return lines
