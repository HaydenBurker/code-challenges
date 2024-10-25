// Create a function that takes in a string and an integer n and returns a string with each character repeated n times

using System;

public class Program
{
	public static String RepeatNTimes(String word, int n)
	{
		String repeatedWord = "";
		foreach (char letter in word)
		{
			for	(int i = 0; i < n; i++)
			{
				repeatedWord += letter;	
			}
		}
		return repeatedWord;
	}

	public static void Main()
	{
		Console.WriteLine(RepeatNTimes("Hello", 3)); // HHHeeellllllooo
		Console.WriteLine(RepeatNTimes("world!", 2)); // wwoorrlldd!!
		Console.WriteLine(RepeatNTimes("I", 5)); // IIIII
		Console.WriteLine(RepeatNTimes("same", 1)); // same
	}
}