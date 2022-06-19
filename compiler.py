from lex import *
from emitter import *
from parser import *
import sys

def main():
    print("Teeny Tiny Compiler")

    # if len(sys.argv) != 2:
    #     sys.exit("Error: Compiler needs source file as argument.")
    with open("test_print.b", 'r') as inputFile:
        input = inputFile.read()

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(input)
    emitter = Emitter("print.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    print("Compiling completed.")

main()
