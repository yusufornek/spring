using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace week6
{
    internal class arithmetic
    {
        public static int kare(int a)
        {

            return a * a;
        }

        public static double kare(double a)
        {
            return a * a;
        }
        public static int varsayilandegermethodu(int a = 7)
        {
            return a * a;
        }
        public static int reflimethod(ref int a)
        {
            return a * a;
        }
        public static int outlumethod(out int a)
        {
            a = 0; //Out parametresi içeride mutlaka tekrar tanımlanmalıdır.
            return a * a;
        }


    }
}
