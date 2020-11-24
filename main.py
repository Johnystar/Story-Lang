import click

class Interpreter():
	"""
	Base interpreter class, useless on its own
	"""

	def __init__(self):
		self.lines_processed = 0

	# PLACEHOLDER FUNCTION
	def next_section(self) -> str:
		return ''

	def cycle(self):
		self.lines_processed += 1  # keeping track of which line we're on

		processed_section = self.next_section()  # get section to process

		# pre-formatting
		processed_section = processed_section.lower()  # converting to lowercase
		if processed_section.endswith('.'): processed_section = processed_section[:-1]

		if processed_section == 'once upon a time': return


@click.command()
@click.argument("script_file", type=click.File("rb"))
def cli(script_file):
	print(script_file.readall())  # FIXME: figure out how to read the whole file at once

if __name__ == '__main__':
	cli()  # yes, this is correct, no arguments need to be specified