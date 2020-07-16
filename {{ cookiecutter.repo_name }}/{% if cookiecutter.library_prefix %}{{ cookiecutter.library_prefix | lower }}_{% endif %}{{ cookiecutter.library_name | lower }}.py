# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.author }}{% if cookiecutter.company %} for {{ cookiecutter.company }}{% endif %}
#
# SPDX-License-Identifier: MIT
"""
`{% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | lower }}_{% endif %}{{ cookiecutter.library_name | lower }}`
================================================================================

{% if cookiecutter.library_description != "" %}
    {{- cookiecutter.library_description }}
{% else %}
.. todo:: Describe what the library does.
{% endif %}

* Author(s): {{ cookiecutter.author }}

Implementation Notes
--------------------

**Hardware:**

.. todo:: Update product link and add links to any other specific hardware product page(s), or category page(s).

* `Adafruit {{cookiecutter.library_name}} Breakout <https://www.adafruit.com/products/45XX>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Remove the Bus Device and/or the Register library dependencies based on the library's use of either.

 * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
 * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/{{ cookiecutter.github_user }}/{% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | capitalize}}_{% endif %}CircuitPython_{{ cookiecutter.library_name }}.git"

from micropython import const
from time import sleep
import adafruit_bus_device.i2c_device as i2c_device

from adafruit_register.i2c_struct import UnaryStruct, ROUnaryStruct, Struct
from adafruit_register.i2c_bit import RWBit, ROBit
from adafruit_register.i2c_bits import RWBits, ROBits

# pylint: disable=bad-whitespace
_{{ cookiecutter.library_name }}_DEFAULT_ADDRESS = 0xFF  # {{ cookiecutter.library_name.lower() }} default i2c address
_{{ cookiecutter.library_name }}_DEVICE_ID = 0xE1  # Correct content of WHO_AM_I register


#class CV:
#    """struct helper"""
#
#    @classmethod
#    def add_values(cls, value_tuples):
#        """Add CV values to the class"""
#        cls.string = {}
#        cls.lsb = {}
#
#        for value_tuple in value_tuples:
#            name, value, string, lsb = value_tuple
#            setattr(cls, name, value)
#            cls.string[value] = string
#            cls.lsb[value] = lsb
#
#    @classmethod
#    def is_valid(cls, value):
#        """Validate that a given value is a member"""
#        return value in cls.string
#
#
#class AccelRange(CV):
#    """Options for ``accelerometer_range``"""
#    pass  # pylint: disable=unnecessary-pass
#AccelRange.add_values(
#  (
#    ("FREQ_196_6HZ_3DB", 0, 196.6, None),
#    ("FREQ_151_8HZ_3DB", 1, 151.8, None),
#    ("FREQ_119_5HZ_3DB", 2, 119.5, None)
#  )
#
#)


class {{ cookiecutter.library_name }}:  # pylint:disable=too-many-instance-attributes
    """Library for the {{ cookiecutter.library_name }} Sensor


        :param ~busio.I2C i2c_bus: The I2C bus the {{ cookiecutter.library_name }} is connected to.
        :param address: The I2C slave address of the sensor

    """
    def __init__(self, i2c_bus, address):

        self.i2c_device = i2c_device.I2CDevice(i2c_bus, address)
        self._bank = 0
        if not self._device_id in [_{{ cookiecutter.library_name }}_DEVICE_ID]:
            raise RuntimeError("Failed to find an ICM20X sensor - check your wiring!")
        self.reset()
        self.initialize()

    def initialize(self):
        """Configure the sensors with the default settings. For use after calling `reset()`"""

        pass

    def reset(self):
        """Resets the internal registers and restores the default settings"""
        pass
