// Write a function that takes an array and adds a new element to the end that contains the original array

function cloneArray(arr) {
  return [...arr, arr];
}

console.log(cloneArray([1, 2, 3])); // [1, 2, 3, [1, 2, 3]]
console.log(cloneArray(["a", "b", "c"])); // ["a", "b", "c", ["a", "b", "c"]]
console.log(cloneArray([true, [42], "hello", null, 3.14])); // [true, [42], "hello", null, 3.14, [true, [42], "hello", null, 3.14]]
console.log(cloneArray([])); // [[]]
