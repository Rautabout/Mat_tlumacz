symbols = { "+":["+","+","<mo>+</mo>","0" ] ,
			 "-":["-","-","<mo>-</mo>","0"],
			"*":["\\bullet","\cdot","<mo>*</mo>","1"], 
			 "^":["^","^","<msup>","3"],
			"_":["_","_","<msub>","3"],
			 "/":["/","\\frac","<mfrac>","2"],
			 "sqrt":["\sqrt","\sqrt","<msqrt>","4"],
			 "int":["\int","\int","<mo>&int;</mo>","4"],
			"alpha":["\\alpha","\\alpha","<mo>&alpha;</mo>","5"],
			"beta":["\\beta","\\beta","<mo>&beta;</mo>","5"],
			"gamma":["\gamma","\gamma","<mo>&gamma;</mo>","5"],
			"delta":["\delta","\delta","<mo>&delta;</mo>","5"],
			"sin":["sin","\sin","<mi>sin</mi>","4"],
			"cos":["cos","\cos","<mi>cos</mi>","4"],
			"tan":["tan","\\tan","<mi>tan</mi>","4"],
			"cot":["cot","\cot","<mi>cot</mi>","4"],
			"<=":["\le","\leq","<mo><=</mo>","0"],
			">=":["\ge","\geq","<mo>>=</mo>","0"],
		    "<":["<","<","<mo><</mo>","0"],
			">":[">",">","<mo>></mo>","0"],
			"in":["\in","\in","<mi>in</mi>","0"],
			"notin":["\\notelement","\\notin","<mi>notin</mi>","0"],
			"and":["\\vedge","\land","<mi>and</mi>","0"],
			"or":["\\vee","\lor","<mi>or</mi>","0"],
			"pi":["\\pi","\\pi","<mi>pi</mi>","5"],
			"e":["exp(1)","e","<mi>e</mi>","5"],

		}

numbers = ["0","1","2","3","4","5","6","7","8","9"]

TexsymbolsWithUndercoverMultiplySign = ["\sqrt","\int","\\alpha","\\beta","\gamma","\delta","\pi","\sin","\cos","\\tan","\cot","e"]
teXChildsWithoutBrackets = ['+','-','*','<=','>=','<','>','in','notin','and','or']
teXChildsWithBrackets = ["/"]
teXChildsWithRightBracket = ["^","_"]
teXChildWithBracket=["sqrt","int"]
teXJustSymbols=["alpha","beta","gamma","delta","pi","e"]
teXFunctions=["sin","cos","tan","cot"]

docAddOrChangeBracketsAfter = ["^","_","/"]
docDeletSpaceBefore = ["\sqrt","\int","\\alpha","\\beta","\gamma","\delta","\pi","\sin","\cos","\\tan","\cot","exp(1)"]
functions = ['+','-','*','<=','>=','<','>','in','notin','and','or',"/","^","_","sin","cos","tan","cot"]

def findMaxPriority(dictionary):
    maxPriority=0

    for value in dictionary.values():
        if int(value[3])>maxPriority:
            maxPriority= int(value[3])
            
    return maxPriority