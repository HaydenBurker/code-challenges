// Create a function that checks if an array of strings is sorted in alphabetical order

using System;

public class Program
{
	public static bool AreStringsSorted(String[] strings)
	{
		for (int i = 1; i < strings.Length; i++)
		{
			if (String.Compare(strings[i - 1], strings[i]) > 0) return false;
		}

		return true;
	}

	public static void Main()
	{
		Console.WriteLine(AreStringsSorted(new String[]{"a", "b", "c"})); // True
		Console.WriteLine(AreStringsSorted(new String[]{"c", "a", "b"})); // False
		Console.WriteLine(AreStringsSorted(new String[]{"hello", "world"})); // True
		Console.WriteLine(AreStringsSorted(new String[]{"1", "5", "12"})); // False
		Console.WriteLine(AreStringsSorted(new String[0])); // True
		Console.WriteLine(AreStringsSorted(new String[]{"a"})); // True
		Console.WriteLine(AreStringsSorted(new String[]{"he", "hello", "hey"})); // True
	}
}