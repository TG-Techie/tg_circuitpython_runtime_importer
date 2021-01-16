# SPDX-FileCopyrightText: 2017 Jonah Y-M
#
# SPDX-License-Identifier: Unlicense

import runtime_importer

# ask the user what module to import
mod = runtime_importer.importpath(input('path to import module (time time ):'))

# use the module as usual
print(mod)

# when youre done with it free it.
mod.clear_module()
