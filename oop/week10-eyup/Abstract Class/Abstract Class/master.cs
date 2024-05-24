using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Abstract_Class
{
    internal class Master : Ogrenci
    {

     
        public override void study(string _ogrenciTipi)
        {

            Console.WriteLine($" {_ogrenciTipi} Ogrencisi 2 kere calisir.");

        }
      
    }
}
