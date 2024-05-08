using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace week8
{
    internal class Onlisans : Student
    {
        public int studentId;




        public Onlisans(string educationType) : base(educationType)
        {

        }
        public Onlisans(int studentId) : base(studentId: studentId) { }
    }
}
