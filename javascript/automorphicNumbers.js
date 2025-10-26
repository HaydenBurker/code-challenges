// Create a function that returns true if a number is authmorphic and false otherwise
// A number is automorphic if n is in the end of n^2

function isAutomorphic(num) {
  const numStr = num.toString();
  const numSquaredStr = (num * num).toString();
  return numStr === numSquaredStr.slice(numSquaredStr.length - numStr.length);
}

console.log(isAutomorphic(6)); // true
console.log(isAutomorphic(3)); // false
console.log(isAutomorphic(625)); // true
console.log(isAutomorphic(100)); // false
console.log(isAutomorphic(0)); // true
