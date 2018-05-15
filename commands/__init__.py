from os import listdir, getcwd, path
import re, click

command_folder = path.join(getcwd(), 'commands')

class CLI(click.MultiCommand):

    def list_commands(self, ctx):
        commands = [filename[:-3] for filename in listdir(command_folder)
                    if re.match(r'.*[^_]\.py$', filename)]

        return sorted(commands)

    def get_command(self, ctx, name):
        ns = {}
        filename = path.join(command_folder, name + '.py')
        with open(filename) as file:
            code = compile(file.read(), filename, 'exec')
            eval(code, ns, ns)
        return ns['cli']

@click.command(cls=CLI)
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))