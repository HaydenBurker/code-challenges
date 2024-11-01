// Create a function that takes in a string and returns a string that only contains the letters from the string that was passed in

using System;

public class Program
{
	public static String LettersOnly(String s)
	{
		String lettersOnlyString = "";
		foreach (char c in s)
		{
			if (Char.IsLetter(c))
			{
				lettersOnlyString += c;	
			}
		}
		return lettersOnlyString;
	}

	public static void Main()
	{
		Console.WriteLine(LettersOnly("He110")); // He
		Console.WriteLine(LettersOnly("H5#a#l16l%o[}.w\\|e/?~1`e3n")); // Halloween
		Console.WriteLine(LettersOnly("LettersOnly")); // LettersOnly
	}
}