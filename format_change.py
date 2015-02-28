__author__ = 'jslowik'
#take input file and change formatting
#options should include single entry per line (\n break), comma-sep list, removing quotes, etc
import argparse

def argumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputFile', action='store', help='Input File')
    parser.add_argument('outputFile', action='store', help='Output File')
    parser.add_argument('-n', '--new', action='store', help='New character or pattern')
    parser.add_argument('-o', '--old', action='store', help='Old character or pattern to replace')
    parser.add_argument('-a', '--all', action='store_true', help='Replace all instances')
    parser.add_argument('-s', '--start', action='store_true', help='Replace at start of line')
    parser.add_argument('-e', '--end', action='store_true', help='Replace at end of line')
    parser.add_argument('-p', '--prepend', action='store_true', help='Prepend to line')
    parser.add_argument('-d', '--append', action='store_true', help='Append to line')

def replaceAllText(inFile,newFile,oldText,newText):
    with open(inFile,'r') as file, open(newFile, 'w') as write:
        for line in file:
            newLine = line.replace(oldText,newText)
            write.write(newLine)

if __name__ == '__main__':
    arguments = argumentParser()
    if not(arguments.inputFile or arguments.outputFile or arguments.new or arguments.old):
        print("All arguments required!")
        exit()
    else:
        None