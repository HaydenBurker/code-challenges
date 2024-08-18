// Create a function that takes an object and returns the keys and values as separate arrays.
// Return the keys sorted alphabetically, and their corresponding values in the same order.

function keysAndValues(obj) {
    return [Object.keys(obj).sort(), Object.values(obj).sort()];
}

console.log(keysAndValues({a:1, b:2, c:3})); // [["a", "b", "c"], [1, 2, 3]]
console.log(keysAndValues(["hello", "world"])); // [["0", "1"], ["hello", "world"]]