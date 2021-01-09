using System;
using System.Collections.Generic;

public class BaseForTrees
{
    Dictionary<string, string[]> symbols = new Dictionary<string, string[]>() //Kolejność wartości Doc, Tex, MathML, priorytety
		{

            { "+",new string[] {"+","+","<mo>+</mo>","0" } },
			{ "-",new string[] {"-","-","<mo>-</mo>","0" } },
			{ "*",new string[] {"*","\\cdot","<mo>*</mo>","1" } }, 
			{ "^",new string[] {"^","^","<msup>","3" } },
			{ "_",new string[] {"_","_","<msub>","3" } },
			{ "/",new string[] {"/","\\frac","<mfrac>","2" } },
			{ "sqrt",new string[] {"\\sqrt","\\sqrt","<msqrt>","4" } },
			{ "int",new string[] {"\\int","\\int","<mo>&int;</mo>","4" } },
			{ "alpha",new string[] {"\\alpha","\\alpha","<mo>&alpha;</mo>","6" } },
			{ "beta",new string[] {"\\beta","\\beta","<mo>&beta;</mo>","6" } },
			{ "gamma",new string[] {"\\gamma","\\gamma","<mo>&gamma;</mo>","6" } },
			{ "delta",new string[] {"\\delta","\\delta","<mo>&delta;</mo>","6" } },
			{ "sin",new string[] {"sin","\\sin","<mi>sin</mi>","4" } },
			{ "cos",new string[] {"cos","\\cos","<mi>cos</mi>","4" } },
			{ "tan",new string[] {"tan","\\tan","<mi>tan</mi>","4" } },
			{ "cot",new string[] {"cot","\\cot","<mi>cot</mi>","4" } },
			{ "<=",new string[] {"\\le","\\leq","<mo><=</mo>","0" } },
			{ ">=",new string[] {"\\ge","\\geq","<mo>>=</mo>","0" } },
			{ "<",new string[] {"<","<","<mo><</mo>","0" } },
			{ ">",new string[] {">",">","<mo>></mo>","0" } },
			{ "in",new string[] {"\\in","\\in","<mi>in</mi>","0" } },
			{ "notin",new string[] {"\\notelement","\\notin","<mi>notin</mi>","0" } },
			{ "and",new string[] {"\\vedge","\\land","<mi>and</mi>","0" } },
			{ "or",new string[] {"\\vee","\\lor","<mi>or</mi>","0" } },
			{ "pi",new string[] {"\\pi","\\pi","<mi>pi</mi>","6" } },
			{ "e",new string[] {"exp(1)","e","<mi>e</mi>","6" } },
			{ "(",new string[] {"(","(","<mo>(</mo>","5" } }
		};


    public class Node
	{
		public string value;
		public Node left;
		public Node right;

		public Node(string value){
		
				this.value = value;
				this.left = null;
				this.right = null;
		}
	}

	public class Tree
	{
		public Node root;
		public Tree()
		{
			root = null;
		}

		bool isEmpty()
		{
			return root == null;
		}
	}


	
}


