# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense


import runtime_importer

# ask the user what module to import
mod = runtime_importer.importpath(input('path to import module (time time ):'))

print(mod)

# use the module as usual

mod.clear_module()
