from main import Interpreter

class LiveInterpreter(Interpreter):
	def next_section(self):
		return input('>>> ')

if __name__ == '__main__':
	interpreter_instance = LiveInterpreter()

	while True:
		interpreter_instance.cycle()