# Disables the loathsome Synaptics touchpad
[![PyPI version](https://badge.fury.io/py/fuckpad.svg)](https://badge.fury.io/py/fuckpad)
Synaptics touchpads tend to work poorly on Linux without lots of
careful configuration. This module makes disabling and enabling
the fucking things easier. Turn to `fuckpad` when you're tired of
errant clicks and mouse movements because your palm *dared* to
enter the the touchpad's general area.

# Usage (as a command line tool)

```bash
$ fuckpad  # disable by default
Disabled touchpad
$ fuckpad disable
Disabled touchpad
$ fuckpad enable
Enabled touchpad
```

# Usage (as a Python module)

```python
>>> from fuckpad import set_touchpad
>>> set_touchpad(True)  # enabled
>>> set_touchpad(False)  # disabled
```

# Installation
Install with `pip install fuckpad`. Requires Python 2.7/3.0+.
Tested on Ubuntu with the Lenovo X1 Carbon and a much older ThinkPad.
