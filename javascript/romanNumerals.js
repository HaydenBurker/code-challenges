// Create a function that converts an integer between 1 and 3999 into a roman numeral
// Create a second function that converts a roman numeral between I and MMMCMXCIX into an integer

function intToRoman(num) {
    const letters = [
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "M", "MM", "MMM"]
    ];
    return num.toString().split("").reverse().map((s, i) => letters[i][parseInt(s)]).reverse().join("");
}

console.log(intToRoman(1));
console.log(intToRoman(1000));
console.log(intToRoman(3999));
console.log(intToRoman(444));
console.log(intToRoman(3765));
console.log(intToRoman(3));
console.log(intToRoman(34));

function romanToInt(roman) {
    const numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000};
    return roman.split("").reduce((sum, l, i) => sum += ((roman[i + 1] && numbers[roman[i + 1]] > numbers[l]) ? -1 : 1) * numbers[l], 0);
}

console.log(romanToInt("I"));
console.log(romanToInt("M"));
console.log(romanToInt("MMMCMXCIX"));
console.log(romanToInt("CDXLIV"));
console.log(romanToInt("MMMDCCLXV"));
console.log(romanToInt("III"));
console.log(romanToInt("XXXIV"));