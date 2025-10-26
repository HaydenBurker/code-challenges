// Create a function that, given an array of both integers and arrays with a single integer, sorts the array

function getNumber(val) {
  return val[0] === undefined ? val : val[0];
}

function sortArray(array) {
  return array.sort((a, b) => getNumber(a) - getNumber(b));
}

console.log([6, 1, 5]); // [1, 5, 6]
console.log([[6], [1], [5]]); // [[1], [5], [6]]
console.log(sortArray([[4], 2, 5, [3], [1]])); // [[1], 2, [3], [4], 5]
