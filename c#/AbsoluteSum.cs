// Create a function that takes an array of integers and return the sum of the absolute values of those integers

using System;

public class Program
{
	public static int AbsoluteSum(int[] arr)
	{
		int result = 0;
		foreach (int num in arr)
		{
			result += num >= 0 ? num : -num;	
		}
		return result;
	}

	public static void Main()
	{
		Console.WriteLine(AbsoluteSum(new int[] {1, -1})); // 2
		Console.WriteLine(AbsoluteSum(new int[] {1, 2, -3, 4, -5})); // 15
		Console.WriteLine(AbsoluteSum(new int[] {})); // 0
		Console.WriteLine(AbsoluteSum(new int[] {100})); // 100
	}
}