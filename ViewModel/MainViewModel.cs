using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using IO_Mat_tlumacz.ViewModel.Base;
using IO_Mat_tlumacz.Model;
using System.Windows.Controls;

namespace IO_Mat_tlumacz.ViewModel
{
    class MainViewModel : ViewModelBase
    {
        PanelViewModel panelL;
        PanelViewModel panelR;
        RelayCommand translateRC;
        Dictionary<string, MathLanguage> languages = new Dictionary<string, MathLanguage>();
        private void LoadLanguages()
        {
            languages.Add("LaTeX", new Model.LaTeX.LaTeXObjects());
            languages.Add("MathML", new Model.MathML.MathMLObjects());
        }

        public PanelViewModel PanelL => panelL;
        public PanelViewModel PanelR => panelR;

        public RelayCommand Translate
        {
            get
            {
                if (translateRC == null)
                    translateRC = new RelayCommand(e => { TranslateProcedure(); }, e => true);
                return translateRC;
            }
        }

        public MainViewModel()
        {
            LoadLanguages();

            panelL = new PanelViewModel();
            PanelL.LanguageList = languages.Keys.ToArray();

            panelR = new PanelViewModel();
            PanelR.LanguageList = languages.Keys.ToArray();
        }

        private void TranslateProcedure()
        {
            panelR.CodeText = panelL.CodeText;
        }
    }
}
