using System;

public class BaseForTrees
{
		var symbols = new Dictionary<String, String[3]>() //Kolejność wartości Doc, Tex, MathML
		{
			{ "+", ["+","+",""]},
			{ "-", ["-","-",""]},
			{ "*", ["*","\\cdot",""]},
			{ "^", ["^","^",""]},
			{ "_", ["_","_",""]},
			{ "/", ["/","\\frac",""]},
			{ "sqrt", ["\\sqrt","\\sqrt",""]},
			{ "int", ["\\int","\\int",""]},
			{ "alpha", ["\\alpha","\\alpha",""]},
			{ "beta", ["\\beta","\\beta",""]},
			{ "gamma", ["\\gamma","\\gamma",""]},
			{ "delta", ["\\delta","\\delta",""]},
			{ "sin", ["sin","\\sin",""]},
			{ "cos", ["cos","\\cos",""]},
			{ "tan", ["tan","\\tan",""]},
			{ "cot", ["cot","\\cot",""]},
			{ "<=", ["\\le","\\leq",""]},
			{ ">=", ["\\ge","\\geq",""]},
			{ "<", ["<","<",""]},
			{ ">", [">",">",""]},
			{ "in", ["\\in","\\in",""]},
			{ "notin", ["\\notelement","\\notin",""]},
			{ "and", ["\\vedge","\\land",""]},
			{ "or", ["\\vee","\\lor",""]},
			{ "pi", ["\\pi","\\pi",""]},
			{ "e", ["exp(1)","e",""]}
		};

	class Node
	{
		public int value;
		public Node left;
		public Node right;

		public Node(int value){
		
				this.value = velue;
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


