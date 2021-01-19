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
using System.Diagnostics;

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


            panelL.CodeText = "\\frac{-b\\sqrt{b^2-4ac}}{2a}";

        }

        private void TranslateProcedure()
        {
            string python = "python.exe";
            string myPythonApp = "konwertuj.py";
            ProcessStartInfo myProcessStartInfo = new ProcessStartInfo(python);

            myProcessStartInfo.UseShellExecute = false;
            myProcessStartInfo.RedirectStandardOutput = true;

            myProcessStartInfo.Arguments = myPythonApp + " " + langCodes[panelL.SelectedLanguage] + " " + langCodes[panelR.SelectedLanguage] + " " + PanelL.CodeText;

            Process myProcess = new Process();
            myProcess.StartInfo = myProcessStartInfo; 
            myProcess.Start();

            StreamReader myStreamReader = myProcess.StandardOutput;
            string myString = myStreamReader.ReadLine();

            myProcess.WaitForExit();
            myProcess.Close();

            panelR.CodeText = myString;

        }
    }
}
