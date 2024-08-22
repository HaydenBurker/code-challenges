// Create a function that squares every digit in a number.

function squareDigits(n) {
    return parseInt(n.toString().split("").map(s => parseInt(s)).map(n => n*n).map(n => n.toString()).join(""));
}

console.log(squareDigits(5)); // 25
console.log(squareDigits(9132)); // 81194
console.log(squareDigits(1234567890)); // 1491625364964810
console.log(squareDigits(9876543210)); // 8164493625169410