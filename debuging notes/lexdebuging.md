# the lexer algorithm

- first thing in the caller file we import all things from lex.

- we initialize lex with the input as an argument: the constructor adds a NL to the end of the input
then it defines a property called curChar that equal '' then another one called curPos that equals -1 then it calls the method 
- nextChar that update the curChar if the curPos + 1 is less than the length of the input if it is then the curChar is '\0'.
- then in the same file, we create a variable named token and we assign to it the return value of the lexer.getToken() which calls the skipWhitespacd() and the skipComment methods and assign the token to equal none. then it checks what is that char 

- if it is an operator +-/* we token = Token(self.curChar, TokenType.(plus|minus ...)
if the curChar equals = we use the peek() to see what is the nextChar if it was another = we call the Token Constructor and give it == and TokenType.EQEQ else if the next char is something else we know then that it is an = EQ....................
we do the same thing for the '>= <= !=' operators

- if the curChar is '\"' we skip that to the next char and we define the startPos and while the curChar doesn't = to '\"' we check if it = some illegal char like \t we call abort witch is a method of the same class that takes a msg argument and call sys.exit("Lexing error. " + message)

else if it is safe we define the tokText var that = the string from the startPos : curPos
then we call the Token constructor 

- if the curChar is an isdigit():
    we define the startPos with the curPos then while is peek() we call nextChar 
    if the peek() = '.'
    then we call nextChar()
        if peek is not a digit then we call abort and we tell it that there is an illegal char in the number
        while peek() is a digit we call nextChar()
    we get the subString with the curPos + 1 to get the last digit and we call the Token Contractor

- if it was an isalpha() 
we assign a var called startPos with the curPos and while the peek() method doesn't return the end of the line and returns an isalnum() we call the nextChar() method and create that tokText = self.source[startPos : self.curPos + 1] # Get the substring. and then we assign the return value of token.checkIfKeyword(tokenText) that loops on TokenType enum and checks if the kind.name == tokenText and kind.value is in between 100 and 200 if that's true we return kind else it returns none.
back to the getToken method, we see if the keyword var is node if that's true then we assign the token to the contractor of the Class Toekn that takes two args tokText and TokenType.IDENT and fill the two propreties of the class text and kind with them(args) else if the keyword is not none then it is a keyword we give the contractor tokTex and the keyword
and at the end of the getChat() we call nextChar() and we return the token var.
- and while the token.kind is not TokenType.EOF we print the token and we assign the lex.getToken() to the token var.
# TokenType is our enum for all the types of tokens.
class TokenType(enum.Enum):
	EOF = -1
	NEWLINE = 0
	NUMBER = 1
	IDENT = 2
	STRING = 3
	# Keywords.
	LABEL = 101
	GOTO = 102
	PRINT = 103
	INPUT = 104
	LET = 105
	IF = 106
	THEN = 107
	ENDIF = 108
	WHILE = 109
	REPEAT = 110
	ENDWHILE = 111
	# Operators.
	EQ = 201  
	PLUS = 202
	MINUS = 203
	ASTERISK = 204
	SLASH = 205
	EQEQ = 206
	NOTEQ = 207
	LT = 208
	LTEQ = 209
	GT = 210
	GTEQ = 211