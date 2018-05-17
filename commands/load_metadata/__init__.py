from importlib import import_module

module = import_module('commands.load_metadata.sc_course')
sc_course = module.sc_course

from commands.load_metadata.all import ports
from commands.load_metadata.all import countries
from commands.load_metadata.all import occupations
from commands.load_metadata.all import products
from commands.load_metadata.all import states
from commands.load_metadata.all import regions
from commands.load_metadata.all import continents
from commands.load_metadata.all import territories
from commands.load_metadata.all import economic_blocks
from commands.load_metadata.all import municipalities
from commands.load_metadata.all import industries
from commands.load_metadata.all import hedu_course
from commands.load_metadata.all import establishments
from commands.load_metadata.all import inflections
from commands.load_metadata.all import attrs
from commands.load_metadata.all import metadata_command
from commands.load_metadata.all import all
