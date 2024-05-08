using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentClass
{
    class Onlisans : Student
    {
        public Onlisans(string educationType) : base(educationType)
        {
        }

        public Onlisans(int studentId) : base(studentId)
        {
        }
    }
}
