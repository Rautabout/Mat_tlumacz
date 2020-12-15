using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using IO_Mat_tlumacz.ViewModel.Base;

namespace IO_Mat_tlumacz.ViewModel
{
    class PanelViewModel : ViewModelBase
    {
        public PanelViewModel()
        {

        }
        private string[] _languagelist;
        public string[] LanguageList { 
            get { return _languagelist; } 
            set {_languagelist = value; onPropertyChanged(nameof(LanguageList)); 
            } }
        public string SelectedLanguage { get; set; }
        private string _codetext;
        public string CodeText { 
            get { return _codetext; } 
            set { 
                _codetext = value; 
                onPropertyChanged(nameof(CodeText)); 
            } 
        }
    }
}
