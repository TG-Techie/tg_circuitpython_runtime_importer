Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-circuitpython-runtime_importer/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/runtime_importer/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/TG-Techie/Circuitpython_CircuitPython_runtime_importer/workflows/Build%20CI/badge.svg
    :target: https://github.com/TG-Techie/Circuitpython_CircuitPython_runtime_importer/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A tool for importing modules at runtime so they can be de-imported later.


Dependencies
=============
This driver depends on:

* Python3.5+ or `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

.. todo:: Remove the above note if PyPI version is/will be available at time of release.
   If the library is not planned for PyPI, remove the entire 'Installing from PyPI' section.

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-runtime_importer/>`_. To install for current user:

.. code-block:: shell

    pip3 install runtime-importer

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install runtime-importer

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install runtime-importer

Usage Example
=============

.. code-block:: javascript
  :linenos:

  code . . .
  import runtime_importer

  # imports the module and retunrs it in a wrapper
  mod = runtime_importer.importpath('/path/to/your/mod')

  # you can then proceed to use it as normal
  mod.some_funtion()
  attr = mod.some_module_global_or_class

  # "de-import" and free the module's memory
  mod.clear_module()

  # the module is no longer usable,
  mod.some_funtion() # raises AttributeError

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/TG-Techie/Circuitpython_CircuitPython_runtime_importer/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
