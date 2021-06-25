using System;

namespace Day6_kons
{
    class Program
    {
        static void Main(string[] args)
        {
            bool[,] quadratFeld = new bool[1000, 1000];


            for (int i = 0; i < 1000; i++)
            {
                for (int j = 0; j < 1000; j++)
                {
                    quadratFeld[i, j] = false;
                }
            }
            string line;
            //int brightness = 0;

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
                        for (int i = o; i < u+1; i++)
                        {
                            for (int j = l; j < r+1; j++)
                            {
                                quadratFeld[i, j] = true;
                                //brightness++;
                            }
                        }
                    }
                    else
                    {
                        int l = Int16.Parse((befehl[2].Split(','))[0]);
                        int o = Int16.Parse((befehl[2].Split(','))[1]);
                        int r = Int16.Parse((befehl[4].Split(','))[0]);
                        int u = Int16.Parse((befehl[4].Split(','))[1]);
                        for (int i = o; i < u+1; i++)
                        {
                            for (int j = l; j < r+1; j++)
                            {
                                //if (quadratFeld[i, j] > 0)
                                //{
                                    quadratFeld[i, j] = false;
                                    //brightness--;
                                //}
                            }
                        }
                    }
                }
                else
                {
                    int l = Int16.Parse((befehl[1].Split(','))[0]);
                    int o = Int16.Parse((befehl[1].Split(','))[1]);
                    int r = Int16.Parse((befehl[3].Split(','))[0]);
                    int u = Int16.Parse((befehl[3].Split(','))[1]);
                    for (int i = o; i < u+1; i++)
                    {
                        for (int j = l; j < r+1; j++)
                        {
                            quadratFeld[i, j] = !(quadratFeld[i, j]);
                            //brightness += 2;
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
            //Console.WriteLine(brightness);
            Console.WriteLine(count);
            ConsoleKeyInfo x = Console.ReadKey();
        }
    }
}
