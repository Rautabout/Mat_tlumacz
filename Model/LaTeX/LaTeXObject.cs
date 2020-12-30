using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace IO_Mat_tlumacz.Model.LaTeX
{
    class LaTeXObjects : MathLanguage
    {
        int longest_code;
        Dictionary<string, string[]> dictionary = new System.Collections.Generic.Dictionary<string, string[]>();
        private static string Reverse(string text)
        {
            char[] output = new char[text.Length];
            int l = 0, r = text.Length - 1;
            while (r > l) {
                output[l]   = text[r];
                output[r--] = text[l++];
            }
            return output.ToString();
        }
        public LaTeXObjects()
        {
            #region fill dictionary
            dictionary.Add("",                  new string[] { "Text" });
            dictionary.Add("{",                 new string[] { "Open" });
            dictionary.Add("}",                 new string[] { "Close" });
            dictionary.Add("carf\\",   new string[] { "Fraction" });
            dictionary.Add("^",                 new string[] { "TopIndex" });
            dictionary.Add("_",                 new string[] { "BottomIndex" });
            dictionary.Add("trqs\\",   new string[] { "Root" });
            #endregion
        }

        public MathObject[] FirstPass(string text)
        {
            List<MathObject> equation = new List<MathObject>();
            int progress = 0;
            for(int i = 0; i < text.Length; i++)
            {
               
            }


            return equation.ToArray();
        }
    }
}
