// Create a function that takes an array of integers and returns a new array of integers that are sorted with no duplicates

using System;
using System.Collections.Generic;

public class Program
{
	public static int[] UniqueSort(int[] numbers)
	{
		HashSet<int> uniqueNumbers = new HashSet<int>(numbers);

		numbers = new int[uniqueNumbers.Count];
		uniqueNumbers.CopyTo(numbers);

		for (int i = 0; i < numbers.Length; i++)
		{
			for (int j = 0; j < numbers.Length; j++)
			{
				if (numbers[i] < numbers[j])
				{
					int temp = numbers[i];
					numbers[i] = numbers[j];
					numbers[j] = temp;
				}
			}
		}

		return numbers;
	}

	public static void PrintArray(int[] arr)
	{
		Console.Write("[");
		Console.Write(string.Join(", ", arr));
		Console.WriteLine("]");
	}

	public static void Main()
	{
		PrintArray(UniqueSort(new int[] {5, 4, 3, 2, 1})); // [1, 2, 3, 4, 5]
		PrintArray(UniqueSort(new int[] {1, 1, 1, 3, 2, 6, 6, 3, 1})); // [1, 2, 3, 6]
		PrintArray(UniqueSort(new int[0])); // []
		PrintArray(UniqueSort(new int[] {1, 2, 3})); // [1, 2, 3]
		PrintArray(UniqueSort(new int[] {4, -10, 42, 3, 4, 100, -12345})); // [-12345, -10, 3, 4, 42, 100]
	}
}