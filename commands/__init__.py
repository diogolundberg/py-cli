import click

from commands.load_metadata import sc_course, load_ports, load_countries, load_occupations, load_products, load_states, load_regions, load_continents, load_territories, load_economic_blocks, load_municipalities, load_industries, load_hedu_course, load_establishments, load_inflections, load_attrs, load_metadata_command, load_all

@click.group()
def load_metadata():
    pass

load_metadata.add_command(sc_course)
load_metadata.add_command(load_ports)
load_metadata.add_command(load_countries)
load_metadata.add_command(load_occupations)
load_metadata.add_command(load_products)
load_metadata.add_command(load_states)
load_metadata.add_command(load_regions)
load_metadata.add_command(load_continents)
load_metadata.add_command(load_territories)
load_metadata.add_command(load_economic_blocks)
load_metadata.add_command(load_municipalities)
load_metadata.add_command(load_industries)
load_metadata.add_command(load_hedu_course)
load_metadata.add_command(load_establishments)
load_metadata.add_command(load_inflections)
load_metadata.add_command(load_metadata_command)
load_metadata.add_command(load_all)