using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IO_Mat_tlumacz.Model.MathML
{
    class MathMLObjects : MathLanguage
    {
        /*
        public MathMLObjects()
        {
            dictionary.Add("PlusMinus", new PlusMinus());
            dictionary.Add("Fraction", new Fraction());
            dictionary.Add("TopIndex", new TopIndex());
            dictionary.Add("BottomIndex", new BottomIndex());
        }
        class Text : MathObject
        {
            string text;
            public override string Draw()
            {
                string result = "";
                foreach (char letter in text)
                    if ((letter >= 'a' && letter <= 'z')|| (letter >= 'A' && letter <= 'Z'))
                        result += $"<mi>{letter}</mi>";
                    else
                        result += $"<mo>{letter}</mo>";
                return result;
            }

        }
        class PlusMinus : MathObject
        {
            public override string Draw()
            {
                return @"<mo>&PlusMinus;</mo>";
            }
        }
        class Fraction : MathObject
        {
            public override string Draw()
            {
                return String.Format(@"<mfrac><mrow>{0}</mrow><mrow>{1}</mrow></mfrac>",child_nodes[0],child_nodes[1]);
            }

        }
        class TopIndex : MathObject
        {
            public override string Draw()
            {
                return String.Format(@"^\{{0}\}", child_nodes[0].Draw());
            }

        }
        class BottomIndex : MathObject
        {
            public override string Draw()
            {
                return String.Format(@"_\{{0}\}", child_nodes[0].Draw());
            }

        }
        */
    }
}
