using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace week4
{
    internal class a
    {
        public static void a_static()
        {
            b bclass = new b();
            Console.WriteLine("a_static");
        }
        public void a_nonstatic()
        {
            Console.WriteLine("a_nonstatic");
        }
    }
}
