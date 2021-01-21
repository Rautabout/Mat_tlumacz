symbols = {"+": ["+", "+", "[+]", "0","<mo>+</mo>"],  # <mo>
           "-": ["-", "-", "[-]", "0","<mo>-</mo>"],
           "*": ["\\bullet", "\cdot", "[*]", "1","<mo>*</mo>"],
           "^": ["^", "^", "[^]", "3","<msup>"],  # <msup>
           "_": ["_", "_", "[_]", "3","<msub>"],  # <msub>
           "/": ["/", "\\frac", "[mfrac]", "2","<mfrac>"],  # <mfrac>
           "sqrt": ["\sqrt", "\sqrt", "[msqrt]", "4","<msqrt>"],  # <msqrt>
           "int": ["\int", "\int", "[&int;]", "4","<mo>&int;</mo>"],  # <mo>
           "alpha": ["\\alpha", "\\alpha", "[&alpha;]", "5","<mo>&alpha;</mo>"],
           "beta": ["\\beta", "\\beta", "[&beta;]", "5","<mo>&beta;</mo>"],
           "gamma": ["\gamma", "\gamma", "[&gamma;]", "5","<mo>&gamma;</mo>"],
           "delta": ["\delta", "\delta", "[&delta;]", "5","<mo>&delta;</mo>"],
           "sin": ["sin", "\sin", "[sin]", "4","<mi>sin</mi>"],  # <mi>
           "cos": ["cos", "\cos", "[cos]", "4","<mi>cos</mi>"],
           "tan": ["tan", "\\tan", "[tan]", "4","<mi>tan</mi>"],
           "cot": ["cot", "\cot", "[cot]", "4","<mi>cot</mi>"],
           "<=": ["\le", "\leq", "[<=]", "0","<mo><=</mo>"],  # <mo>
           ">=": ["\ge", "\geq", "[>=]", "0","<mo>>=</mo>"],
           "<": ["<", "<", "[<]", "0","<mo><</mo>"],
           "=": ["=", "=", "[=]", "0", "<mo>=</mo>"],
           ">": [">", ">", "[>]", "0","<mo>></mo>"],
           "in": ["\in", "\in", "[in]", "0","<mi>in</mi>"],  # <mi>
           "notin": ["\\notelement", "\\notin", "[notin]", "0","<mi>notin</mi>"],
           "and": ["\\vedge", "\land", "[and]", "0","<mi>and</mi>"],
           "or": ["\\vee", "\lor", "[or]", "0","<mi>or</mi>"],
           "pi": ["\\pi", "\\pi", "[pi]", "5","<mi>pi</mi>"],
           "e": ["exp(1)", "e", "[e]", "5","<mi>e</mi>"],

           }

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

TexsymbolsWithUndercoverMultiplySign = ["\sqrt", "\int", "\\alpha", "\\beta", "\gamma", "\delta", "\pi", "\sin", "\cos",
                                        "\\tan", "\cot", "e"]
teXChildsWithoutBrackets = ['+', '-', '*', '<=', '>=', '<', '=','>','in', 'notin', 'and', 'or']
teXChildsWithBrackets = ["/"]
teXChildsWithRightBracket = ["^", "_"]
teXChildWithBracket = ["sqrt", "int"]
teXJustSymbols = ["alpha", "beta", "gamma", "delta", "pi", "e"]
teXFunctions = ["sin", "cos", "tan", "cot"]

docSymbolsWithUndercoverMultiplySign = ["\sqrt", "\int", "\\alpha", "\\beta", "\gamma", "\delta", "\pi", "\sin", "\cos","\\tan", "\cot", "exp(1)"]
docAddOrChangeBracketsAfter = ["^", "_", "/"]
docDeletSpaceBefore = ["\sqrt", "\int", "\\alpha", "\\beta", "\gamma", "\delta", "\pi", "\sin", "\cos", "\\tan", "\cot","exp(1)"]
functions = ['+', '-', '*', '<=', '>=', '<', '=','>', 'in', 'notin', 'and', 'or', "/", "^", "_", "sin", "cos", "tan", "cot"]

mathMlStartSymbolsWithNesting = ["<msqrt>", "<msup>", "<msub>", "<mrow>", "<mfrac>"]
mathMlEndSymbolsWithNesting = ["</msqrt>", "</msup>", "</msub>", "</mrow>", "</mfrac>"]
mathMlSymbolsWithUndercoverMultiplySign = ["msqrt","mfrac", "&int;", "&alpha;", "&beta;", "&gamma;", "&delta;", "sin", "cos", "tan", "cot", "pi", "e"]
mathMlChildsWithoutBrackets = ['+', '-', '*', '<=', '>=', '<', '>','in', 'notin', 'and', 'or']
mathMlChildWithRightBracket=["^","_"]
mathMlFunctions=["sin", "cos", "tan", "cot"]
mathMlJustSymbols=["alpha", "beta", "gamma", "delta", "pi", "e"]
mathMlSymbolsWithBrackets=["sqrt","int"]
mathMlSymbolsWithBracket=["/"]



def findMaxPriority(dictionary):
    maxPriority = 0

    for value in dictionary.values():
        if int(value[3]) > maxPriority:
            maxPriority = int(value[3])

    return maxPriority
