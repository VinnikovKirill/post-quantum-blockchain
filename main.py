import sys

from src.Command import getCommand

if __name__ == '__main__':
    commandName = sys.argv[1] if len(sys.argv) > 1 else '--help'
    command = getCommand(commandName)
    command.execute()