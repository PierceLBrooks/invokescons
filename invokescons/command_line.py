import sys
import SCons.Script
import subprocess

def main():
    arguments = sys.argv
    command = []
    if (len(arguments) > 1):
        command.append(sys.executable)
        command.append("-c")
        command.append("\"import SCons.Script; SCons.Script.main()\"")
        command += arguments[1:]
        result = subprocess.check_output(command)
        print(result.decode())
    else:
        SCons.Script.main()
    return 0
