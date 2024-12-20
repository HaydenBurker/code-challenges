// Create a function that takes in a string and returns the string without the vowels (aeiou)

using System;

public class Program
{
	public static String RemoveVowels(String str)
	{
		String noVowelStr = "";

		foreach(char c in str)
    {
			if (!"aeiou".Contains(c.ToString().ToLower()))
			{
				noVowelStr += c;	
			}
		}

		return noVowelStr;
	}

	public static void Main()
	{
	  Console.WriteLine(RemoveVowels("Hello world!")); // "Hll wrld"
		Console.WriteLine(RemoveVowels("AEioU")); // ""
		Console.WriteLine(RemoveVowels("The quick brown fox jumps over the lazy dog")); // "Th qck brwn fx jmps vr th lzy dg"
	}
}