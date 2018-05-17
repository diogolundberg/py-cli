import click

from commands.load_metadata.sc_course import sc_course
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


@click.group()
def load_metadata():
    pass

load_metadata.add_command(sc_course)
load_metadata.add_command(ports)
load_metadata.add_command(countries)
load_metadata.add_command(occupations)
load_metadata.add_command(products)
load_metadata.add_command(states)
load_metadata.add_command(regions)
load_metadata.add_command(continents)
load_metadata.add_command(territories)
load_metadata.add_command(economic_blocks)
load_metadata.add_command(municipalities)
load_metadata.add_command(industries)
load_metadata.add_command(hedu_course)
load_metadata.add_command(establishments)
load_metadata.add_command(inflections)
load_metadata.add_command(metadata_command)
load_metadata.add_command(all)
