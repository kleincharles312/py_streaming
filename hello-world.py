import argparse

argument_parser = argparse.ArgumentParser(description='A simple hello world program.')

argument_parser.add_argument('-n', '--name', type=str, default='World', help='Name to greet', required=True)

args = argument_parser.parse_args()

class Greeting:
    'Class documentation: Represents a simple way of saying hello'

    def __init__(self, greeter):
        if isinstance(greeter, float):
            raise TypeError("Greeters are not allowed to be floats.")
        elif isinstance(greeter, int) and greeter < 0:
            raise ValueError("No negative greeters are allowed.")
        elif not greeter and greeter != 0:
            raise ValueError("No greeter provided.")
        else:
            self.greeter = greeter

    def say_hello(self, name):
        return f"Hello, {name}. Your greeter is {self.greeter}."

greeters = ['Happy Path Joe', 1436, 0, -4, '', None, 3.14]

print(Greeting.__doc__)

for greeter in greeters:
    try:
        greeting = Greeting(greeter)
        print(greeting.say_hello(args.name))
    except (TypeError, ValueError) as e:
        print(f"Error creating Greeting with greeter '{greeter}': {e}")
