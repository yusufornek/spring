using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentClass
{
    internal class Trigonometri : Algebra
    {
        public int sayi;

        public int number = 10;

        public Trigonometri()
        {
            Console.WriteLine("Cocuk siniftan selamlar");
        }

        public void ciktila()
        {
            Console.WriteLine("Parent class number: {0}", base.number);
            Console.WriteLine("Child class number: {0}", number);
        }


    }
}
