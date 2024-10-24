// Create a function that takes in an array of 10 numbers (0-9) and returns a string formatted as a phone number: (###) ###-####

using System;

public class Program
{
	public static String FormatNumber(int[] n)
	{
		return $"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}";
	}

	public static void Main()
	{
        Console.WriteLine(FormatNumber(new int[] {5, 5, 5, 5, 5, 5, 5, 5, 5, 5})); // (555) 555-5555
        Console.WriteLine(FormatNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0})); // (123) 456-7890
	}
}