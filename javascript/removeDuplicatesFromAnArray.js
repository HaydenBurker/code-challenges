// Create a function that takes an array of items and returns a new array in the same sequential order with all duplicate items removed

function removeDuplicates(arr) {
    return arr.reduce((arr, item) => arr.includes(item) ? arr : arr.concat(item), []);
}

console.log(removeDuplicates([1, 3, 1, 2, 2, 1])); // [1, 3, 2]
console.log(removeDuplicates(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"])); // ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
console.log(removeDuplicates([])); // []
console.log(removeDuplicates([5, 4, 3, 2, 1])); // [5, 4, 3, 2, 1]
console.log(removeDuplicates([5, 5, 5, 5, 5])); // [5]