from importlib import import_module

module = import_module('commands.load_metadata.sc_course')
sc_course = module.sc_course
