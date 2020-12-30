using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IO_Mat_tlumacz.Model.TreeModel
{
    class MathLanguage
    {
        protected Dictionary<string, MathObject> dictionary;
        public MathObject GetOperationByName(string name)
        {
            return dictionary[name].Instance();
        }
    }
}
