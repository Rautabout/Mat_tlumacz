using Microsoft.SqlServer.Server;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IO_Mat_tlumacz.Model.TreeModel
{
    abstract class MathObject
    {
        protected string OpName = null;
        protected List<MathObject> child_nodes;
        public abstract string Draw();
        public MathObject Instance()
        {
            return (MathObject)MemberwiseClone();
        }
    }

}
