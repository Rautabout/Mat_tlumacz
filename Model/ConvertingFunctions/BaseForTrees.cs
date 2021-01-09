using System;

public class BaseForTrees
{
		var symbols = new Dictionary<String, String[4]>() //Kolejność wartości Doc, Tex, MathML, priorytety
		{
			{ "+", ["+","+","","0"]},
			{ "-", ["-","-","","0"]},
			{ "*", ["*","\\cdot","","1"]}, 
			{ "^", ["^","^","","3"]},
			{ "_", ["_","_","","3"]},
			{ "/", ["/","\\frac","","2"]},
			{ "sqrt", ["\\sqrt","\\sqrt","","4"]},
			{ "int", ["\\int","\\int","","4"]},
			{ "alpha", ["\\alpha","\\alpha","","6"]},
			{ "beta", ["\\beta","\\beta","","6"]},
			{ "gamma", ["\\gamma","\\gamma","","6"]},
			{ "delta", ["\\delta","\\delta","","6"]},
			{ "sin", ["sin","\\sin","","4"]},
			{ "cos", ["cos","\\cos","","4"]},
			{ "tan", ["tan","\\tan","","4"]},
			{ "cot", ["cot","\\cot","","4"]},
			{ "<=", ["\\le","\\leq","","0"]},
			{ ">=", ["\\ge","\\geq","","0"]},
			{ "<", ["<","<","","0"]},
			{ ">", [">",">","","0"]},
			{ "in", ["\\in","\\in","","0"]},
			{ "notin", ["\\notelement","\\notin","","0"]},
			{ "and", ["\\vedge","\\land","","0"]},
			{ "or", ["\\vee","\\lor","","0"]},
			{ "pi", ["\\pi","\\pi","","6"]},
			{ "e", ["exp(1)","e","","6"]},
			{ "(", ["(","(","","5"]}
		};

	class Node
	{
		public string value;
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


