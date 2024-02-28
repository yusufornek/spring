namespace CalculateFruitPrice
{
    internal class Program
    {
        
        static void Main(string[] args)
        {
            Console.WriteLine("Give me the price of Apple please! : ");
            double apple = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Now, give me the price of Lemon my dear producer! : ");
            double lemon = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Finally, I just want to price of Cherry! <3 : ");
            double cherry = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("I was just  kidding, that was not final, give me a price of watermelon! : ");
            double watermelon = Convert.ToInt32(Console.ReadLine());
            calculate(apple, lemon, cherry, watermelon);
        }
        public static void calculate(double apple, double lemon, double cherry, double watermelon)
        {
            double result = ((apple + apple * 0.05) + (lemon + lemon * 0.07) + (cherry + cherry * 0.08) + (watermelon + watermelon * 0.10));
            Console.WriteLine(result);
        }


        


    }
}
