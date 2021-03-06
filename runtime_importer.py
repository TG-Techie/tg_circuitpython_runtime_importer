# The MIT License (MIT)
#
# Copyright (c) 2021 Jonah Yolles-Murphy (TG-Techie)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import gc

# get the type of Module for __init__ checks in ModuleWrapper
_ModuleType = type(gc)

def importpath(path):
    global ModuleWrapper
    return ModuleWrapper.frompath(path)

class ModuleWrapper:
    """ A wrapper that holds a single instance of a module.

    ModuleWrappers ar used to control acess to modules that have been
    imported and that will need to be "exported". By wrapping the modules in
    ModuleWrappers their attributes can be accessed in a ctrolled manner. This
    allows the modules to be garbage collected.
    """

    def __init__(self, module):
        global _ModuleType, isinstance
        assert isinstance(module, _ModuleType), f"ModuleWrappers must wrap Modules, got {self}"
        self._wrapped_module_ = module
        self._wrapped_module_name_ = module.__name__

    def isfull(self):
        return bool(self._wrapped_module_ is not None)

    def clear_module(self):
        global gc, sys
        mod = self._wrapped_module_
        self._wrapped_module_ = None
        del mod
        gc.collect()

    def __getattr__(self, name):
        mod = self._wrapped_module_
        if mod is None:
            raise RuntimeError(f"{self} is empty")
        attr = getattr(mod, name, self)
        # using b/c a module's attribute could potentiall be `None` but a module
        # shoudl never container its wrapper (as is wraps it...)
        if attr is self: # than the mod does not have that attr
            raise AttributeError(f"{self._wrapped_module_name_} has no attribute {rerp(name)}")
        else: # the attribute should be returned
            return attr

    def __repr__(self):
        return f"<ModuleWrapper '{self._wrapped_module_name_}'>"

    @classmethod
    def frompath(cls, path):
        global __import__, ImportError, sys

        # keep a copy of what modules wer imported before this one so references
        # to the new modules can be removed from sys.modules
        sys_modules = sys.modules
        previously_imported = set(sys_modules.keys())

        # try to import it
        # if the module import fails or succeeds, sys.modules needs to be
        try:
            module = __import__(path)
            was_import_error = False
        except ImportError:
            was_import_error = True

        # clean sys.modules from sub-imported modules (even with failed imports)
        modules_to_clean = set(sys.modules.keys()) - previously_imported
        for mod in modules_to_clean:
            sys_modules.pop(mod)
        else:
            gc.collect()

        if was_import_error:
            raise ImportError(f"unable to import {repr(path)} into a ModuleWrapper")
        else:
            return cls(module)
