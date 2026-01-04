import sys

from Commands import getCommand

if __name__ == '__main__':
    command_name = sys.argv[1] if len(sys.argv) > 1 else '--help'
    command = getCommand(command_name)
    command.execute()
