using System;
using System.Collections.Generic;

public class BaseForTrees
{
		var symbols = new Dictionary<String, String[4]>() //Kolejność wartości Doc, Tex, MathML, priorytety
		{
			{ "+", ["+","+","<mo>+</mo>","0"]},
			{ "-", ["-","-","<mo>-</mo>","0"]},
			{ "*", ["*","\\cdot","<mo>*</mo>","1"]}, 
			{ "^", ["^","^","<msup>","3"]},
			{ "_", ["_","_","<msub>","3"]},
			{ "/", ["/","\\frac","<mfrac>","2"]},
			{ "sqrt", ["\\sqrt","\\sqrt","<msqrt>","4"]},
			{ "int", ["\\int","\\int","<mo>&int;</mo>","4"]},
			{ "alpha", ["\\alpha","\\alpha","<mo>&alpha;</mo>","6"]},
			{ "beta", ["\\beta","\\beta","<mo>&beta;</mo>","6"]},
			{ "gamma", ["\\gamma","\\gamma","<mo>&gamma;</mo>","6"]},
			{ "delta", ["\\delta","\\delta","<mo>&delta;</mo>","6"]},
			{ "sin", ["sin","\\sin","<mi>sin</mi>","4"]},
			{ "cos", ["cos","\\cos","<mi>cos</mi>","4"]},
			{ "tan", ["tan","\\tan","<mi>tan</mi>","4"]},
			{ "cot", ["cot","\\cot","<mi>cot</mi>","4"]},
			{ "<=", ["\\le","\\leq","<mo><=</mo>","0"]},
			{ ">=", ["\\ge","\\geq","<mo>>=</mo>","0"]},
			{ "<", ["<","<","<mo><</mo>","0"]},
			{ ">", [">",">","<mo>></mo>","0"]},
			{ "in", ["\\in","\\in","<mi>in</mi>","0"]},
			{ "notin", ["\\notelement","\\notin","<mi>notin</mi>","0"]},
			{ "and", ["\\vedge","\\land","<mi>and</mi>","0"]},
			{ "or", ["\\vee","\\lor","<mi>or</mi>","0"]},
			{ "pi", ["\\pi","\\pi","<mi>pi</mi>","6"]},
			{ "e", ["exp(1)","e","<mi>e</mi>","6"]},
			{ "(", ["(","(","<mo>(</mo>","5"]}
		};


    class Node
	{
		public int value;
		public Node left;
		public Node right;

		public Node(int value){
		
				this.value = value;
				this.left = null;
				this.right = null;
		}
	}

	class Tree
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


