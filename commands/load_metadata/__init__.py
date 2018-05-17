from importlib import import_module

module = import_module('commands.load_metadata.sc_course')
sc_course = module.sc_course

module = import_module('commands.load_metadata.load_metadata')

load_ports = module.load_ports
load_countries = module.load_countries
load_occupations = module.load_occupations
load_products = module.load_products
load_states = module.load_states
load_regions = module.load_regions
load_continents = module.load_continents
load_territories = module.load_territories
load_economic_blocks = module.load_economic_blocks
load_municipalities = module.load_municipalities
load_industries = module.load_industries
load_hedu_course = module.load_hedu_course
load_establishments = module.load_establishments
load_inflections = module.load_inflections
load_attrs = module.load_attrs
load_metadata_command = module.load_metadata_command
load_all = module.load_all