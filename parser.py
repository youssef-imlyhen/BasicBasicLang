import sys
from lex import *


class Parser:
    def __init__(self, lexer, emitter):
        self.lexer = lexer
        self.emitter = emitter

        self.symbols = set()    
        self.labelsDeclared = set() 
        self.labelsGotoed = set() 

        self.curTok = None
        self.peekToken = None
        self.nextTok()
        self.nextTok()    

    
    def checkToken(self, kind):
        return kind == self.curTok.kind

    
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name + ", got " + self.curTok.kind.name)
        self.nextTok()

    
    def nextTok(self):
        self.curTok = self.peekToken
        self.peekToken = self.lexer.getToken()
        

    
    def isComparisonOperator(self):
        return self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ) or self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ)

    def abort(self, message):
        sys.exit("Error! " + message)


    

    
    def program(self):
        self.emitter.headerLine("#include <stdio.h>")
        self.emitter.headerLine("int main(void){")
        
        
        while self.checkToken(TokenType.NEWLINE):
            self.nextTok()

        
        while not self.checkToken(TokenType.EOF):
            self.statement()

        
        self.emitter.emitLine("return 0;")
        self.emitter.emitLine("}")

        
        for label in self.labelsGotoed:
            if label not in self.labelsDeclared:
                self.abort("Attempting to GOTO to undeclared label: " + label)


    
    def statement(self):
        

        
        if self.checkToken(TokenType.PRINT):
            self.nextTok()

            if self.checkToken(TokenType.STRING):
                
                self.emitter.emitLine("printf(\"" + self.curTok.text + "\\n\");")
                self.nextTok()

            else:
                
                self.emitter.emit("printf(\"%" + ".2f\\n\", (float)(")
                self.expression()
                self.emitter.emitLine("));")

        
        elif self.checkToken(TokenType.IF):
            self.nextTok()
            self.emitter.emit("if(")
            self.comparison()

            self.match(TokenType.THEN)
            self.nl()
            self.emitter.emitLine("){")

            
            while not self.checkToken(TokenType.ENDIF):
                self.statement()

            self.match(TokenType.ENDIF)
            self.emitter.emitLine("}")

        
        elif self.checkToken(TokenType.WHILE):
            self.nextTok()
            self.emitter.emit("while(")
            self.comparison()

            self.match(TokenType.REPEAT)
            self.nl()
            self.emitter.emitLine("){")

            
            while not self.checkToken(TokenType.ENDWHILE):
                self.statement()

            self.match(TokenType.ENDWHILE)
            self.emitter.emitLine("}")

        
        elif self.checkToken(TokenType.LABEL):
            self.nextTok()

            
            if self.curTok.text in self.labelsDeclared:
                self.abort("Label already exists: " + self.curTok.text)
            self.labelsDeclared.add(self.curTok.text)

            self.emitter.emitLine(self.curTok.text + ":")
            self.match(TokenType.IDENT)

        
        elif self.checkToken(TokenType.GOTO):
            self.nextTok()
            self.labelsGotoed.add(self.curTok.text)
            self.emitter.emitLine("goto " + self.curTok.text + ";")
            self.match(TokenType.IDENT)

        
        elif self.checkToken(TokenType.LET):
            self.nextTok()

            
            if self.curTok.text not in self.symbols:
                self.symbols.add(self.curTok.text)
                self.emitter.headerLine("float " + self.curTok.text + ";")

            self.emitter.emit(self.curTok.text + " = ")
            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)
            
            self.expression()
            self.emitter.emitLine(";")

        
        elif self.checkToken(TokenType.INPUT):
            self.nextTok()

            
            if self.curTok.text not in self.symbols:
                self.symbols.add(self.curTok.text)
                self.emitter.headerLine("float " + self.curTok.text + ";")

            
            self.emitter.emitLine("if(0 == scanf(\"%" + "f\", &" + self.curTok.text + ")) {")
            self.emitter.emitLine(self.curTok.text + " = 0;")
            self.emitter.emit("scanf(\"%")
            self.emitter.emitLine("*s\");")
            self.emitter.emitLine("}")
            self.match(TokenType.IDENT)

        
        else:
            self.abort("Invalid statement at " + self.curTok.text + " (" + self.curTok.kind.name + ")")

        
        self.nl()


    
    def comparison(self):
        self.expression()
        
        if self.isComparisonOperator():
            self.emitter.emit(self.curTok.text)
            self.nextTok()
            self.expression()
        
        while self.isComparisonOperator():
            self.emitter.emit(self.curTok.text)
            self.nextTok()
            self.expression()


    
    def expression(self):
        self.term()
        
        while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.emitter.emit(self.curTok.text)
            self.nextTok()
            self.term()


    
    def term(self):
        self.unary()
        
        while self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.SLASH):
            self.emitter.emit(self.curTok.text)
            self.nextTok()
            self.unary()


    
    def unary(self):
        
        if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.emitter.emit(self.curTok.text)
            self.nextTok()        
        self.primary()


    
    def primary(self):
        if self.checkToken(TokenType.NUMBER): 
            self.emitter.emit(self.curTok.text)
            self.nextTok()
        elif self.checkToken(TokenType.IDENT):
            
            if self.curTok.text not in self.symbols:
                self.abort("Referencing variable before assignment: " + self.curTok.text)

            self.emitter.emit(self.curTok.text)
            self.nextTok()
        else:
            
            self.abort("Unexpected token at " + self.curTok.text)

    
    def nl(self):
        
        self.match(TokenType.NEWLINE)
        
        while self.checkToken(TokenType.NEWLINE):
            self.nextTok()