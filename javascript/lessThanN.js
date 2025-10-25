// Write a function that takes in 3 numbers and returns true if the first two numbers is less than the third number. Otherwise return false

function lessThanN(n1, n2, n3) {
  return n1 + n2 < n3;
}

console.log(lessThanN(1, 2, 3)); // false
console.log(lessThanN(1, 2, 4)); // true
console.log(lessThanN(-4, 2, 3)); // true
console.log(lessThanN(0, 0, -5)); // false
console.log(lessThanN(23, 45, 67)); // false
console.log(lessThanN(12, 34, 56)); // true
