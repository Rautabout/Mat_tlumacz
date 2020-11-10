using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace IO_Mat_tlumacz
{
    /// <summary>
    /// Logika interakcji dla klasy CodeView.xaml
    /// </summary>
    public partial class CodeView : UserControl
    {
        public CodeView()
        {
            InitializeComponent();

            debugList = new List<string>(  new string[] { "LaTeX", "MathML", "DocX" }  );
            LanguagePick.ItemsSource = DebugList;
        }

        private List<string> debugList;
        public List<string> DebugList => debugList;
    }
}
