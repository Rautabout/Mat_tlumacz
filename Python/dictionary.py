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
symbols = {"+": ["+", "+", "+", "0"],  # <mo>
           "-": ["-", "-", "-", "0"],
           "*": ["\\bullet", "\cdot", "*", "1"],
           "^": ["^", "^", "^", "3"],  # <msup>
           "_": ["_", "_", "^", "3"],  # <msub>
           "/": ["/", "\\frac", "frac", "2"],  # <mfrac>
           "sqrt": ["\sqrt", "\sqrt", "sqrt", "4"],  # <msqrt>
           "int": ["\int", "\int", "&int;", "4"],  # <mo>
           "alpha": ["\\alpha", "\\alpha", "&alpha;", "5"],
           "beta": ["\\beta", "\\beta", "&beta;", "5"],
           "gamma": ["\gamma", "\gamma", "&gamma;", "5"],
           "delta": ["\delta", "\delta", "&delta;", "5"],
           "sin": ["sin", "\sin", "sin", "4"],  # <mi>
           "cos": ["cos", "\cos", "cos", "4"],
           "tan": ["tan", "\\tan", "tan", "4"],
           "cot": ["cot", "\cot", "cot", "4"],
           "<=": ["\le", "\leq", "<=", "0"],  # <mo>
           ">=": ["\ge", "\geq", ">=", "0"],
           "<": ["<", "<", "><", "0"],
           ">": [">", ">", ">>", "0"],
           "in": ["\in", "\in", ">in", "0"],  # <mi>
           "notin": ["\\notelement", "\\notin", ">notin", "0"],
           "and": ["\\vedge", "\land", ">and", "0"],
           "or": ["\\vee", "\lor", ">or", "0"],
           "pi": ["\\pi", "\\pi", "pi", "5"],
           "e": ["exp(1)", "e", "e", "5"],

           }
teXChildsWithBrackets = ["/"]
teXChildsWithRightBracket = ["^","_"]
teXChildWithBracket=["sqrt","int"]
teXJustSymbols=["alpha","beta","gamma","delta","pi","e"]
teXFunctions=["sin","cos","tan","cot"]

mathMlStartSymbolsWithNesting = ["<msqrt>", "<msup>", "<msub>", "<mrow>", "<mfrac>"]
mathMlEndSymbolsWithNesting = ["</msqrt>", "</msup>", "</msub>", "</mrow>", "</mfrac>"]
mathMlSymbolsWithUndercoverMultiplySign = ["msqrt","mfrac", "&int;", "&alpha;", "&beta;", "&gamma;", "&delta;", "sin", "cos", "tan", "cot", "pi", "e"]
mathMlChildsWithoutBrackets = ['+', '-', '*', '<=', '>=', '<', '>','in', 'notin', 'and', 'or']
mathMlChildWithRightBracket=["^","_"]
mathMlFunctions=["sin", "cos", "tan", "cot","sqrt","int"]
mathMlJustSymbols=["alpha", "beta", "gamma", "delta", "pi", "e"]
mathMlSymbolsWithBrackets=["sqrt","int"]
mathMlSymbolsWithBracket=["/"]

mathMlStartSymbolsWithNesting = ["<msqrt>","<msup>","<msub>","<mrow>","<mfrac>"]
mathMlEndSymbolsWithNesting = ["</msqrt>","</msup>","</msub>","</mrow>","</mfrac>"]
mathMlSymbolsWithUndercoverMultiplySign= ["<msqrt>","<mi>","<mo>&int;</mo>","<mo>&alpha;</mo>","<mo>&beta;</mo>","<mo>&gamma;</mo>","<mo>&delta;</mo>"]


def findMaxPriority(dictionary):

    for value in dictionary.values():
    return maxPriority
