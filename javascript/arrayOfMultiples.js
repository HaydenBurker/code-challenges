// Create a function that takes two numbers as arguments (num, length) and returns an array of multiples of num until the array length reaches length.

function arrayOfMultiples(num, count) {
    return Array.from({length: count}, (_, i) => num * (i + 1));
}

console.log(arrayOfMultiples(7, 5)); // [7, 14, 21, 28, 35]
console.log(arrayOfMultiples(5, 7)); // [5, 10, 15, 20, 25, 30, 35]
console.log(arrayOfMultiples(3, 0)); // []
console.log(arrayOfMultiples(3, 1)); // [3]
console.log(arrayOfMultiples(12, 15)); // [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180]