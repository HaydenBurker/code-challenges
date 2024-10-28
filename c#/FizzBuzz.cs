// Create a function that takes a number n and returns Fizz if n is divisible by 3, Buzz if n is divisible by 5, Fizz Buzz if n is divisible by 3 and 5, and the number itself if it is not divisible by 3 or 5

using System;

public class Program
{
	public static String FizzBuzz(int n)
	{
		return n % 3 == 0 && n % 5 == 0 ? "FizzBuzz" : n % 3 == 0 ? "Fizz" : n % 5 == 0 ? "Buzz" : n.ToString();
	}

	public static void Main()
	{
		Console.WriteLine(FizzBuzz(3)); // Fizz
		Console.WriteLine(FizzBuzz(5)); // Buzz
		Console.WriteLine(FizzBuzz(15)); // FizzBuzz
		Console.WriteLine(FizzBuzz(13)); // 13
		Console.WriteLine(FizzBuzz(9000)); // FizzBuzz
		Console.WriteLine(FizzBuzz(9001)); // 9001
	}
}