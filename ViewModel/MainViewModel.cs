using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using IO_Mat_tlumacz.ViewModel.Base;
using IO_Mat_tlumacz.Model;
using System.Windows.Controls;
using IO_Mat_tlumacz.Konsola;
using IronPython.Hosting;
using System.IO;
using Microsoft.Scripting.Hosting;

namespace IO_Mat_tlumacz.ViewModel
{
    class MainViewModel : ViewModelBase
    {
        PanelViewModel panelL;
        public PanelViewModel PanelL => panelL;
        PanelViewModel panelR;
        public PanelViewModel PanelR => panelR;
        RelayCommand translateRC;
        List<string> langNames = new List<string>();
        List<string> langCodes = new List<string>();
        private void LoadLanguages()
        {
            langNames.Add("LaTeX"); langCodes.Add("tex");
            langNames.Add("Word"); langCodes.Add("doc");
        }

        public RelayCommand Translate
        {
            get
            {
                if (translateRC == null)
                    translateRC = new RelayCommand(
                        e => { TranslateProcedure(); }, 
                        e => PanelL.SelectedLanguage!=null && PanelR.SelectedLanguage!=null
                        );
                return translateRC;
            }
        }

        public MainViewModel()
        {
            LoadLanguages();

            panelL = new PanelViewModel();
            PanelL.LanguageList = langNames.ToArray();

            panelR = new PanelViewModel();
            PanelR.LanguageList = langNames.ToArray();


            panelL.CodeText = "x=\\frac{-b\\pm\\sqrt{b^2-4ac}}{2a}";

        }

        private void TranslateProcedure()
        {
            var engine = Python.CreateEngine();

            var searchPaths = engine.GetSearchPaths();
            searchPaths.Add("..\\..\\Python");
            engine.SetSearchPaths(searchPaths);
            //var source = engine.CreateScriptSourceFromFile(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "..\\..\\Python\\__pycache__\\konwertuj.py"));
            //var source = engine.CreateScriptSourceFromFile(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Python\\konwertuj.py"));
            ScriptScope scope = engine.CreateScope();
            engine.ExecuteFile("..\\..\\Python\\konwertuj.py");
            
           
            dynamic convertFunction = scope.GetVariable("convert");

            var output = convertFunction(langCodes[panelL.SelectedLanguage], langCodes[panelR.SelectedLanguage], PanelL.CodeText);


            panelR.CodeText = output;
        }
    }
}
