// Create a function that calculates the factorial of a non-negative integer

using System;
					
public class Program
{
	public static int Factorial(int num)
	{
		return num == 0 ? 1 : num * Factorial(num - 1);
	}
	
	public static void Main()
	{
		Console.WriteLine(Factorial(3)); // 6
		Console.WriteLine(Factorial(0)); // 1
		Console.WriteLine(Factorial(1)); // 1
		Console.WriteLine(Factorial(5)); // 120
		Console.WriteLine(Factorial(10)); // 3628800
	}
}