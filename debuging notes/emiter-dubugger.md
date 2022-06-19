## inside emiter
we have 3 vars fullpath header and code 
we have four funcs emit(it takes a code arg and adds it to the code) emitLine(it's like emit but we add \n to the code before adding it to the oldcode) headerLine it's obuose writeFile() it adds code to header and write it into a file 

## inside parser
__init__ after the initializing the lexer we do the same for the emiter
the first lines of the program we include with self.emitter.headerLine(include studio) and the main func. after the while parsing statement we return 0 and we close the main fun.
inside the print when we check if the second token is a string we emitLine printf(curTok.text); if the tok is an expression we emit "printf(\"%" + ".2f\\n\", (float)("
and after expression() we close ));

if the tok is an if after escaping the if we emit if( before parsing the statement we emitline ){ and after that we emitLine}

if tok was a while we escape the while and basicly we do the same as the if

if label we emitLine curTok.text + :

if goto before last line we emitLIne goto + tok + ;

if let after we add the symborl in the header using headerLine folat + tok and we add the eq = ex and after that we ;

if input we add the var using the same thing as before and we emitLine if(0 == scanf(\"%" + "f\", &" + self.curToken.text + ")) { emitLine(self.curToken.text + " = 0;") emit("scanf(\"%") emitLine("*s\");") emitLine("}")

comparison after knowing iscomop we emit tok and while iscomop we emit tok

expression while tok is plus or minus we emit tok 

term if tok is * / we emit tok 

primary if tok is number we emit tok else if tok is an ident and it's declared we emit tok 