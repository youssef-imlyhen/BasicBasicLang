- we create a var called lexer which = the lexer consractor that just initialize the the lexer attributes and we assign that to the parser constructor .
- the parser constructor have the following fields:
    lexer, symbols, labelsDeclared, labelsGotoed all the three = set(), curToken, peekToken all the two = none,
    and we call nextToken() twice to inicialize the current and the peek

- the nextToken() has two statements: 1 it assign the peekToken to the curToken 2. it assign the lexer.getToken() to the peekToken

- then in the main first file we call the parser.program() method that print "program" and while checkToken != NEWLINE we  skilp them with the nextToken and while checkToken is not of EOF kind we call statement() 
- statement() checks if the first token is a print if it is we print statement-pirnt and we call the nexToken() inside the if stat we check again if the checkToken is a string if it is we call the nextToken() else if it was another thing besides string we call expression
- elif it was a if sat we call the nextToken() and we call the comparision() method that print "comparison" and calls expression() method that print "expression" and it calls the term() method that print "term" and calls unary() that pirnt unary and checks if the curentToken is a plus or a minus if it was it calls primary() that print primary(curToken.toext)
and checks the curToken if it was a number we call nexToken() if it was an ident we check if currentTokent is not in symbols if that's true we call abort() with a msg that says that we are using a var that is not exists and we call the nextToken() else if the token is not a number or an idnetn we call abort("we expected a variable or a number here not") back into the term() we check if the token is a * or / we call nextToken() outside of the scope of if we call the primary() again to check if the curToeken is a unary or not  back into the expression whike  the corentToken is a + or a  - we call the nextToken() and term() methods back to the comparison() we check if the  idComparisonOperator() it returns checkToken(comparison op) if it was we call nextToken() and expression() else we call abort("expected a comparison op") and while isComparisonOperator() validate true we call nextToken() and expression() 
- if the curToken is an while we call nextToken() followed by comparison() followed by a match(TokenTypeREPEAT) method that checks if kind of curTok is not = to the cur.kind if that's evaluates true we call abort("expected" kind.name") and outside of if scope we call nextToken() back to while we call the nl()  that print(newline) and match(TokenType.newline) while curTok is newline we escape them back to while again while the curTok is not ENDWHILE we call statement() outside we call match(TOKENTYPE.ENDWHILE) 
- if it is a label we print statement-label we call nextTok() if he curTok.text is in self.labelDisDeclared we call abord(msg) else we add this label to labelIsDeclared and we call match(TokenType.IDENT)
- if GOTO we print that and we call nextTo() and we add the this label to labelGotoed and we call match(ident)
- if Let we print that and we call nextTok() we check if The curTok is not in symbols if that's true we add it to symbols outside we call match(ident) and match(eq) end expression 
- if input we print that we call nextTok() we check if the curTok is not in symbols if true we add it and we call match(ident) 
- else we call abort("Invalid statement at " + self.curToken.text + " (" + self.curToken.kind.name + ")")
and we call a newline()
