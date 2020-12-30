﻿using System;
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

        }
        public string[] LanguageList
        {
            get { return (string[])GetValue(LanguageListDP); }
            set { SetValue(LanguageListDP, value); }
        }
        public static DependencyProperty LanguageListDP = DependencyProperty.Register
            ("LanguageList", typeof(string[]), typeof(CodeView), new PropertyMetadata());
        public string SelectedLanguage
        {
            get { return (string)GetValue(SelectedLanguageDP); }
            set { SetValue(SelectedLanguageDP, value); }
        }
        public static DependencyProperty SelectedLanguageDP = DependencyProperty.Register
            ("SelectedLanguage", typeof(string), typeof(CodeView), new PropertyMetadata());
        public string CodeText
        {
            get { return (string)GetValue(CodeTextDP); }
            set { SetValue(CodeTextDP, value); }
        }
        public static DependencyProperty CodeTextDP = DependencyProperty.Register
            ("CodeText", typeof(string[]), typeof(CodeView), new PropertyMetadata());

    }
}