// Create a function that converts an integer between 1 and 3999 into a roman numeral
// Create a second function that converts a roman numeral between I and MMMCMXCIX into an integer

function intToRoman(num) {
  const letters = [
    ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    ["", "M", "MM", "MMM"],
  ];
  return num
    .toString()
    .split("")
    .reverse()
    .map((s, i) => letters[i][parseInt(s)])
    .reverse()
    .join("");
}

console.log(intToRoman(1));
console.log(intToRoman(1000));
console.log(intToRoman(3999));
console.log(intToRoman(444));
console.log(intToRoman(3765));
console.log(intToRoman(3));
console.log(intToRoman(34));
console.log(intToRoman(1888));

function romanToInt(roman) {
  const numbers = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
  return roman
    .split("")
    .reduce(
      (sum, l, i) =>
        (sum +=
          (roman[i + 1] && numbers[roman[i + 1]] > numbers[l] ? -1 : 1) *
          numbers[l]),
      0
    );
}

console.log(romanToInt("I"));
console.log(romanToInt("M"));
console.log(romanToInt("MMMCMXCIX"));
console.log(romanToInt("CDXLIV"));
console.log(romanToInt("MMMDCCLXV"));
console.log(romanToInt("III"));
console.log(romanToInt("XXXIV"));

// Create a function that checks if a roman numeral is valid

function isValidRoman(roman) {
  roman = roman.toUpperCase();
  return Array.from({ length: 3999 })
    .map((_, i) => intToRoman(i + 1))
    .some((r) => r === roman);
}

console.log(isValidRoman("Hello")); // false
console.log(isValidRoman("I")); // true
console.log(isValidRoman("i")); // true
console.log(isValidRoman("MMMCMXCIX")); // true
console.log(isValidRoman("MMMCMXCX")); // false
console.log(isValidRoman("IIX")); // false
console.log(isValidRoman("IX")); // true
console.log(isValidRoman("XIII")); // true
console.log(isValidRoman("XIIII")); // false
console.log(isValidRoman("MDCCCLXXXVIII")); // true
console.log(isValidRoman("IM")); // false
