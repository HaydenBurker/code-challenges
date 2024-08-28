// Write a function that return the sum of all items in an array, where each item is multiplied by its index

function indexMultiplier(arr) {
    return arr.reduce((sum, num, i) => sum + num * i, 0);
}

console.log(indexMultiplier([1, 2, 3, 4, 5])); // 40
console.log(indexMultiplier([])); // 0
console.log(indexMultiplier([-10, 5, -2])); // 1