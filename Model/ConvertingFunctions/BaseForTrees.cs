using System;

public class BaseForTrees
{
		var symbols = new Dictionary<String, String[3]>()
		{

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


