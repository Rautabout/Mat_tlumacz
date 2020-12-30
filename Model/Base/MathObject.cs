using Microsoft.SqlServer.Server;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Data;

namespace IO_Mat_tlumacz.Model
{
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
            return stack.Last().Draw(stack);
        }
        public MathObject[] Parse(string code)
        {
            List<MathObject> model = new List<MathObject>();
            List<MathObject> stack = new List<MathObject>();



            return model.ToArray();
        }
    }
    class MathObject
    {
        string code;
        static Dictionary<string, MathObject> syntax;
        protected short priority;
        public string Code => code;
        public short Priority => priority;
        public virtual string Draw(List<MathObject> stack) => "";
        public MathObject(string code)
        {
            this.code = code;
        }
    }
    /*
    class Text : MathObject 
    {
        private string text;
        public Text(string t)
        {
            this.text = t;
            priority = -1;
        }
        public override string Draw(List<MathObject> stack)
        {
            return text;
        }
    }
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
