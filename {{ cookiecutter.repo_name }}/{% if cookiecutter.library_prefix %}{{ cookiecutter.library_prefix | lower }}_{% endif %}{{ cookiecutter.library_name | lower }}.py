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
