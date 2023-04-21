using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Выберите метод расчета значения выражения: ");
        Console.WriteLine("1. С помощью цикла for");
        Console.WriteLine("2. С помощью цикла while");
        Console.WriteLine("3. С помощью цикла do ... while");

        int method = int.Parse(Console.ReadLine());

        Console.Write("Введите значение переменной X: ");
        double x = double.Parse(Console.ReadLine());

        Console.Write("Введите значение переменной Y: ");
        double y = double.Parse(Console.ReadLine());

        Console.Write("Введите количество слагаемых: ");
        int n = int.Parse(Console.ReadLine());

        double sum = 0;
        switch (method)
        {
            case 1:
                for (int i = 0; i < n; i++)
                {
                    double term = Math.Pow(-1, i + 1) * Math.Pow(Math.Sin(y), 3) / ((2 * i + 1) * Math.Pow(3, i));
                    term += Math.Pow(-1, i) * Math.Pow(Math.Sin(Math.Pow(x, 2)), 5) / ((2 * i + 1) * Math.Pow(5, i));
                    term -= Math.Pow(-1, i + 1) * Math.Pow(Math.Sin(Math.Pow(y, 3)), 7) / ((2 * i + 1) * Math.Pow(7, i));
                    sum += term;
                }
                break;

            case 2:
                int j = 0;
                while (j < n)
                {
                    double term = Math.Pow(-1, j + 1) * Math.Pow(Math.Sin(y), 3) / ((2 * j + 1) * Math.Pow(3, j));
                    term += Math.Pow(-1, j) * Math.Pow(Math.Sin(Math.Pow(x, 2)), 5) / ((2 * j + 1) * Math.Pow(5, j));
                    term -= Math.Pow(-1, j + 1) * Math.Pow(Math.Sin(Math.Pow(y, 3)), 7) / ((2 * j + 1) * Math.Pow(7, j));
                    sum += term;
                    j++;
                }
                break;

            case 3:
                int k = 0;
                do
                {
                    double term = Math.Pow(-1, k + 1) * Math.Pow(Math.Sin(y), 3) / ((2 * k + 1) * Math.Pow(3, k));
                    term += Math.Pow(-1, k) * Math.Pow(Math.Sin(Math.Pow(x, 2)), 5) / ((2 * k + 1) * Math.Pow(5, k));
                    term -= Math.Pow(-1, k + 1) * Math.Pow(Math.Sin(Math.Pow(y, 3)), 7) / ((2 * k + 1) * Math.Pow(7, k));
                    sum += term;
                    k++;
                } while (k < n);
                break;

            default:
                Console.WriteLine("Некорректный ввод");
                return;
        }

        Console.WriteLine($"Значение выражения при {n} слагаемых: {sum}");
        Console.ReadKey();
    }
}