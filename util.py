import sys
from typing import Iterator


def get_in_path() -> str:
	"""
	Get input file path passed as command line parameter.
	"""
	args = sys.argv
	try:
		in_path = args[1]
		return in_path

	except IndexError:
		print("Specify an input file!")


def read_lines(in_path: str) -> Iterator[str]:
	"""
	Generator to return lines of lines read from input file.
	"""
	with open(in_path) as in_file:
		for line in in_file:
			line = line.strip()
			yield line

def get_input_list() -> list:

	in_path = get_in_path()
	input_list = []

	for line in read_lines(in_path):
		input_list.append(int(line))

	return input_list
