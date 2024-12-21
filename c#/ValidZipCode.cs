// Create a function that takes in a string and returns the string without the vowels (aeiou)

using System;

public class Program
{
	public static bool ValidZipCode(String zip)
	{
		if (zip.Length != 5)
		{
			return false;
		}

		foreach(char digit in zip)
		{
			if (!Char.IsDigit(digit))
			{
				return false;
			}
		}

		return true;
	}

	public static void Main()
	{
		Console.WriteLine(ValidZipCode("12345")); // True
		Console.WriteLine(ValidZipCode("12e45")); // False
		Console.WriteLine(ValidZipCode("6 7890")); // False
		Console.WriteLine(ValidZipCode("59718")); // True
		Console.WriteLine(ValidZipCode("424242")); // False
	}
}