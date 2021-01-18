using Microsoft.SqlServer.Server;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Data;

namespace IO_Mat_tlumacz.Model
{
    /*
    struct dictionaryBase
    {
        char id;        char Id => id;
        string value;   string Value => value;
        List<dictionaryBase> subnodes;
        dictionaryBase(string key, int i)
        {
            subnodes = new List<dictionaryBase>();
            id = ' ';
            value = "";
        }
        public void Insert(string key, string value)
        {
            Propagate(key, 0, value);
        }
        private void Propagate(string key, int i, string value)
        {

        }
        public dictionary Build()
        {
            dictionary output = new dictionary(' ');
            return output;
        }
        private dictionary BuildTree()
        {
            dictionary output = new dictionary(' ');
            return output;
        }
    }
    struct dictionary
    {
        dictionary[] subnodes;
        char id;            char Id => id;
        string value;       string Value => value;

        public dictionary(char id, List<dictionaryBase> subnodes)
        {
            this.id = id;
            this.value = null;
            this.subnodes = new dictionary[subnodes.Count];
            for(int i = subnodes.Count - 1; i >= 0; --i)
            {
                this.subnodes[i] = new dictionary(subnodes[i].Id)
            }
        }

        public string Read(string key)
        {
            return Propagate(key,0);
        }
        string Propagate(string key, int i)
        {
            if (i == key.Length)
                return value;
            string valueGuess;
            foreach (dictionary node in subnodes)
                if (node.Id == key[i]) return node.Propagate(key, i + 1);
            
            return null;
        }
    }
    */
    struct MathDictionary
    {

        public void Add(string key, MathObject value)
        {

        }
        public MathObject Find(string key)
        {

            return null;
        }
    }
    class MathLanguage
    {
        protected Dictionary<string, MathObject> dictionary;
        private string parsed = ""; private int parsed_length = 0;
        public string Draw(MathObject[] model)
        {
            List<MathObject> stack = new List<MathObject>();
            foreach(MathObject mo in model)
            {
                stack.Add(mo);
            }
            return stack.Last().ToString();
        }
        public virtual List<MathObject> Parse(string code)
        {
            return null;
        }
    }
    class MathObject
    {
        public virtual string Draw(List<MathObject> stack)
        {
            return "";
        }
        public virtual int Parse(string text, ref int i)
        {

            return i;
        }
        public MathObject()
        {

        }
    }
    class Text : MathObject 
    {
        private string text;
        public Text(string t)
        {
            text = t;
        }
        public override string Draw(List<MathObject> stack)
        {
            return text;
        }
    }
    abstract class Function : MathObject { };
    /*
    class Plus : MathObject
    {

    }
    class Minus : MathObject
    {

    }
    class Times : MathObject
    {

    }
    class Divide : MathObject
    {

    }
    class Open : MathObject
    {

    }
    class Close : MathObject
    {

    }
    class SquareRoot : MathObject
    {

    }
    class Fraction : MathObject
    {

    }
    class TopIndex : MathObject
    {

    }
    class BottomIndex : MathObject
    {

    }
    */
}
