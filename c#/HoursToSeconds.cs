// Create a function that converts hours to seconds

using System;

public class Program
{
	public static int HoursToSeconds(int hours)
	{
		return hours * 3600;
	}

	public static void Main()
	{
		Console.WriteLine(HoursToSeconds(1)); // 3600
		Console.WriteLine(HoursToSeconds(10)); // 36000
		Console.WriteLine(HoursToSeconds(24)); // 86400
		Console.WriteLine(HoursToSeconds(0)); // 0
		Console.WriteLine(HoursToSeconds(168)); // 604800
	}
}