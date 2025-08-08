// Create a function that takes an array and checks if the last item matches all of the other items concatenated in the array

function matchLastItem(arr) {
  return arr.slice(0, -1).join("") === String(arr[arr.length - 1]);
}

console.log(matchLastItem(["Hello", " ", "world!", "Hello world!"])); // true
console.log(matchLastItem([true, "true"])); // true
console.log(matchLastItem([0, 4, 2, "42"])); // false
console.log(matchLastItem(["a", "b", "c"])); // false
console.log(matchLastItem([1, 2, 12])); // true
console.log(matchLastItem(["one item"])); // false
console.log(matchLastItem([])); // false
