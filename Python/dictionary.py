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

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

TexsymbolsWithUndercoverMultiplySign = ["\sqrt", "\int", "\\alpha", "\\beta", "\gamma", "\delta", "\pi", "\sin", "\cos",
                                        "\\tan", "\cot", "e"]
teXChildsWithoutBrackets = ['+', '-', '*', '<=', '>=', '<', '>','in', 'notin', 'and', 'or']
teXChildsWithBrackets = ["/"]
teXChildsWithRightBracket = ["^", "_"]
teXChildWithBracket = ["sqrt", "int"]
teXJustSymbols = ["alpha", "beta", "gamma", "delta", "pi", "e"]
teXFunctions = ["sin", "cos", "tan", "cot"]

docSymbolsWithUndercoverMultiplySign = ["\sqrt", "\int", "\\alpha", "\\beta", "\gamma", "\delta", "\pi", "\sin", "\cos","\\tan", "\cot", "exp(1)"]
docAddOrChangeBracketsAfter = ["^", "_", "/"]
docDeletSpaceBefore = ["\sqrt", "\int", "\\alpha", "\\beta", "\gamma", "\delta", "\pi", "\sin", "\cos", "\\tan", "\cot","exp(1)"]
functions = ['+', '-', '*', '<=', '>=', '<', '>', 'in', 'notin', 'and', 'or', "/", "^", "_", "sin", "cos", "tan", "cot"]

mathMlStartSymbolsWithNesting = ["<msqrt>", "<msup>", "<msub>", "<mrow>", "<mfrac>"]
mathMlEndSymbolsWithNesting = ["</msqrt>", "</msup>", "</msub>", "</mrow>", "</mfrac>"]
mathMlSymbolsWithUndercoverMultiplySign = ["msqrt","mfrac", "&int;", "&alpha;", "&beta;", "&gamma;", "&delta;", "sin", "cos", "tan", "cot", "pi", "e"]
mathMlChildsWithoutBrackets = ['+', '-', '*', '<=', '>=', '<', '>','in', 'notin', 'and', 'or']
mathMlChildWithRightBracket=["^","_"]
mathMlFunctions=["sin", "cos", "tan", "cot","sqrt","int"]
mathMlJustSymbols=["alpha", "beta", "gamma", "delta", "pi", "e"]
mathMlSymbolsWithBrackets=["sqrt","int"]
mathMlSymbolsWithBracket=["/"]



def findMaxPriority(dictionary):
    maxPriority = 0

    for value in dictionary.values():
        if int(value[3]) > maxPriority:
            maxPriority = int(value[3])

    return maxPriority
