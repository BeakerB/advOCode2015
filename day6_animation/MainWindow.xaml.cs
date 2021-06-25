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

namespace day6_animation
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            for (int i = 0; i < 1000; i++)
                for (int j = 0; j < 1000; j++)
                {
                    Rectangle punkt = new Rectangle();
                    punkt.Height = 1;
                    punkt.Width = 1;
                    Canvas.SetLeft(punkt, i);
                    Canvas.SetTop(punkt, j);
                    punkt.Fill = Brushes.Black;
                    //punkt.Stroke = Brushes.White;
                    myCan.Children.Add(punkt);
                    myCan.UpdateLayout();

                }
            {

            }
        }
        
    }
}
