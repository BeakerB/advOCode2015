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

namespace day6_p1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            bool[,] quadratFeld = new bool[1000, 1000];


            for (int i = 0; i < 1000; i++)
            {
                for (int j = 0; j < 1000; j++)
                {
                    quadratFeld[i, j] = false;
                }
            }
            string line;

            // Read the file line by line.  
            System.IO.StreamReader file =
                new System.IO.StreamReader(@"c:\Users\Andre\Documents\___py\advOCode2015\day6_p1\day6.txt");
            while ((line = file.ReadLine()) != null)
            {
                String[] befehl = line.Split();
                if (befehl.Length == 5)
                {
                    if (befehl[1] == "on")
                    {
                        int l = Int16.Parse((befehl[2].Split(','))[0]);
                        int o = Int16.Parse((befehl[2].Split(','))[1]);
                        int r = Int16.Parse((befehl[4].Split(','))[0]);
                        int u = Int16.Parse((befehl[4].Split(','))[1]);
                        for (int i = o; i < u; i++)
                        {
                            for (int j = l; j < r; j++)
                            {
                                quadratFeld[i, j] = true;
                            }
                        }
                    } else
                    {
                        int l = Int16.Parse((befehl[2].Split(','))[0]);
                        int o = Int16.Parse((befehl[2].Split(','))[1]);
                        int r = Int16.Parse((befehl[4].Split(','))[0]);
                        int u = Int16.Parse((befehl[4].Split(','))[1]);
                        for (int i = o; i < u; i++)
                        {
                            for (int j = l; j < r; j++)
                            {
                                quadratFeld[i, j] = false;
                            }
                        }
                    }
                }else
                {
                    int l = Int16.Parse((befehl[2].Split(','))[0]);
                    int o = Int16.Parse((befehl[2].Split(','))[1]);
                    int r = Int16.Parse((befehl[4].Split(','))[0]);
                    int u = Int16.Parse((befehl[4].Split(','))[1]);
                    for (int i = o; i < u; i++)
                    {
                        for (int j = l; j < r; j++)
                        {
                            quadratFeld[i, j] = !(quadratFeld[i, j]);
                        }
                    }
                }
            }

            file.Close();
            int count = 0;
            for (int i = 0; i < 1000; i++)
            {
                for (int j = 0; j < 1000; j++)
                {
                    if (quadratFeld[i, j])
                    {
                        count++;
                    }
                }
            }
            ergebnis.Text = count.ToString();
        }

    }
}
