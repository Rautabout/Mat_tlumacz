using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IO_Mat_tlumacz.Model.TreeModel.LaTeX
{
    class LaTeXObject: MathLanguage
    {
        public LaTeXObject()
        {
            dictionary.Add("Text",  new Text());
            dictionary.Add("PlusMinus", new PlusMinus());
            dictionary.Add("Fraction",  new Fraction());
            dictionary.Add("TopIndex", new TopIndex());
            dictionary.Add("BottomIndex", new BottomIndex());
        }
        class Text : MathObject
        {
            string text;
            public override string Draw()
            {
                return text;
            }

        }
        class PlusMinus : MathObject
        {
            public override string Draw()
            {
                return @"\\pm";
            }
        }
        class Fraction : MathObject
        {
            public override string Draw()
            {
                return String.Format(@"\\frac\{{0}\}\{{1}\}",child_nodes[0].Draw(),child_nodes[1].Draw());
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
    }
}
