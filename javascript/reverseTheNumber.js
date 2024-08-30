// Create a function that takes an integer and reverses it

function reverseNumber(num) {
    let firstDigit = 0;
    let lastDigit = Math.floor(Math.log10(num));

    while (firstDigit < lastDigit) {
        let num1 = Math.pow(10, firstDigit++);
        let num2 = Math.pow(10, lastDigit--);

        let diff = Math.floor(num % (num1 * 10) / num1) - Math.floor(num % (num2 * 10) / num2);
        num = num - diff * num1 + diff * num2;
    }

    return num;
}

console.log(reverseNumber(123)); // 321
console.log(reverseNumber(0)); // 0
console.log(reverseNumber(8)); // 8
console.log(reverseNumber(95)); // 59
console.log(reverseNumber(2024)); // 4202
console.log(reverseNumber(3000)); // 3 (0003)
console.log(reverseNumber(9876543210)); // 123456789
console.log(reverseNumber(123456789)); // 987654321