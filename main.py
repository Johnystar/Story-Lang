import click

@click.command()
@click.argument("script_file", type=click.File("rb"))
def cli(script_file):
	print(script_file.readall()) # figure out how to read the whole file at once

if __name__ == '__main__':
	cli() # yes, this is correct, no arguments need to be specified