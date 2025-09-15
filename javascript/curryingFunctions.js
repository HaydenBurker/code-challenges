// Create a function that takes an integer as an argument and returns a function which taken in an array as an argument and returns the array multiplied by the integer argument in the outer function

const multiply = (num) => (arr) => arr.map((e) => e * num);

console.log(multiply(5)([1, 2, 3])); // [5, 10, 15]
console.log(multiply(1)([1, 2, 3])); // [1, 2, 3]
console.log(multiply(10)([-3, 10, 42])); // [-30, 100, 420]
console.log(multiply(0)([5, 10, 15])); // [0, 0, 0]
console.log(multiply(1)([])); // []
