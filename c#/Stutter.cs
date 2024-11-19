// Create a function that takes in a word and returns a stuttered version of that word. The first two letters are repeated followed by an ellipsis (...) and at the end of a word an exclamation point is added

using System;

public class Program
{
	public static String Stutter(String word)
	{
		String stutterPhraise = $"{word[0]}{word[1]}";
		return $"{stutterPhraise}... {stutterPhraise}... {word}";
	}

	public static void Main()
	{
		Console.WriteLine(Stutter("amazing")); // am... am... amazing!
		Console.WriteLine(Stutter("beautiful")); // be... be... beautiful!
		Console.WriteLine(Stutter("thats all folks")); // th... th... thats all folks!
	}
}