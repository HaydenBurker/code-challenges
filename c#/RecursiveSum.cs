// Create a function that, given a positive integer n, recursively adds the numbers from 1 to n and returns the sum

using System;

public class Program
{
	public static int RecursiveSum(int n)
	{
		return n > 1 ? n + RecursiveSum(n - 1) : 1;
	}

	public static void Main()
	{
		Console.WriteLine(RecursiveSum(5)); // 15
		Console.WriteLine(RecursiveSum(10)); // 55
		Console.WriteLine(RecursiveSum(1)); // 1
		Console.WriteLine(RecursiveSum(2)); // 3
		Console.WriteLine(RecursiveSum(9001)); // 40513501
	}
}