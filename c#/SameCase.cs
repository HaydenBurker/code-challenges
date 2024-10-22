// Create a function that returns true if a string contains only uppercase or lowercase characters, false otherwise

using System;

public class Program
{
	public static bool SameCase(String word)
	{
		bool upper = Char.IsUpper(word[0]);

		foreach (char c in word)
		{
			if (Char.IsUpper(c) && !upper)
			{
				return false;
			}
			else if (Char.IsLower(c) && upper)
			{
				return false;
			}
		}

		return true;
	}

	public static void Main()
	{
		Console.WriteLine(SameCase("Hello")); // false
		Console.WriteLine(SameCase("HELLO")); // true
		Console.WriteLine(SameCase("hello")); // true
		Console.WriteLine(SameCase("wORd")); // false
		Console.WriteLine(SameCase("asdf")); // true
	}
}