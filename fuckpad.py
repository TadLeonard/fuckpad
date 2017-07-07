"""
Synaptics touchpads tend to work poorly on Linux without lots of
careful configuration. This module makes disabling and enabling
the fucking things easier.

Sample usage:

    >>> from fuckpad import set_touchpad
    >>> set_touchpad(True)  # enabled
    >>> set_touchpad(False)  # disabled
"""


from __future__ import print_function

import re
import sys

from subprocess import Popen, PIPE
from functools import partial


def run_subprocess(cmd):
    cmd = cmd.encode("ascii")
    args = cmd.split()
    return Popen(args, stdout=PIPE, stderr=PIPE)


TOUCHPAD_NAME = "Synaptics TouchPad"
ID_PATTERN = re.compile("id=\d{1,3}")
EN_PATTERN = re.compile("Device Enabled \(\d{1,3}\)")


def set_touchpad(enable=False):
    """Find and disable/enable the wretched touchpad"""
    # find the touchpad address
    touchpad_id = get_touchpad_device()

    # find the touchpad enable offset
    touchpad_en = get_touchpad_enable(touchpad_id)

    # write a '0' or '1' to the touchpad enable
    set_touchpad_enable(touchpad_id, touchpad_en, enable)


def get_touchpad_device():
    """Get the stupid Synaptics touchpad device ID"""
    list_dev = run_subprocess("xinput list")
    out = run_cmd(list_dev)
    for line in out.decode("UTF-8").splitlines():
        if TOUCHPAD_NAME in line:
            try:
                touchpad_id = ID_PATTERN.search(line).group()
                return touchpad_id[3:]
            except (IndexError, ValueError):
                pass  # keep looking
    raise XinputError("Couldn't find Synaptics touchpad device")


def get_touchpad_enable(touchpad_id):
    """Find the absurd enable address is for the touchpad"""
    cmd = "xinput list-props {}".format(touchpad_id)
    list_props = run_subprocess(cmd)
    out = run_cmd(list_props).decode("UTF-8")
    enable = EN_PATTERN.search(out)
    enable_group = enable.group() if enable else ""
    enable_address = re.search("\d{1,3}", enable_group)
    if not enable_address:
        raise XinputError("Couldn't find touchpad enable address")
    return enable_address.group()


def set_touchpad_enable(device, enable, value):
    """Set `device` ID's `enable` address to bool `value`.
    This either writes a '0' or a '1' to device -> enable."""
    enable_value = "1" if value else "0"
    set_prop = run_subprocess("xinput set-prop {} {} {}".format(
                              device, enable, enable_value))
    out = run_cmd(set_prop)
    if out:
        # this xinput command only produces output if there's an error
        raise XinputError("Couldn't set touchpad enable byte: {}".format(out))


def run_cmd(cmd):
    """A way of using `suprocess.run_subprocess` that's compatible with ancient
    versions of Python. This bails out if the subprocess writes to stderr."""
    out, err = cmd.communicate()
    if err:
        raise XinputError("Command {} failed with '{}'".format(cmd, err))
    return out


class XinputError(ValueError):
    pass
