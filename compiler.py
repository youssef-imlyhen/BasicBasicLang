from lex import *

def main():
    input = "IF+-123 foo*THEN/"
    lexer = lex(input)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()