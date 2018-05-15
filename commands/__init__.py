import click

from commands.load_metadata import sc_course

@click.group()
def load_metadata():
    pass

load_metadata.add_command(sc_course)