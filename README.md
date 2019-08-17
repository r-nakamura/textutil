# textutil Package

textutil - utility functions to deal with strings including East Asia characters

# DESCRIPTION

This manual page documents *textutil* module, a Python module
providing utility functions for dealing with strings including East
Asia characters.

This module is heavily inspired by a Perl module,
Text::VisualWidth::PP, which provides functions to treat half-width
and full-width characters.  For the details of this perl module,
please refer to
[https://metacpan.org/pod/Text::VisualWidth::PP](https://metacpan.org/pod/Text::VisualWidth::PP).

# EXAMPLE

```python
from textutil import vwidth, vwrap

import textwrap

len('あいうえお')    # 5
vwidth('あいうえお') # 10

textwrap.wrap('あいうえおかきくけこ', width=10) # ['あいうえおかきくけこ']
vwrap('あいうえおかきくけこ', width=10)         # ['あいうえお', 'かきくけこ']
```

# INSTALLATION

```
$ git clone https://github.com/r-nakamura/textutil
$ pip3 install -e textutil
```

# SEE ALSO

Text::VisualWidth::PP(3pm)

# AUTHOR

Ryo Nakamura <nakamura[atmark]zebulun.net>
