// Create a function that takes in a string and returns the string in reversed order

using System;

public class Program
{
	public static String Reverse(String str)
	{
		String reversedStr = "";
		for (int i = str.Length - 1; i >= 0; i--)
		{
			reversedStr += str[i];
		}
		return reversedStr;
	}

	public static void Main()
	{
		Console.WriteLine(Reverse("Hello world!")); // !dlrow olleH
		Console.WriteLine(Reverse("The quick brown fox jumps over the lazy dog.")); // .god yzal eht revo spmuj xof nworb kciuq ehT
		Console.WriteLine(Reverse("I")); // I
		Console.WriteLine(Reverse("racecar")); // racecar
	}
}