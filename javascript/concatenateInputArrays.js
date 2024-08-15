// Create a function that concatenates n input arrays

function concatArrays(...arrays) {
    return arrays.reduce((concatArr, arr) => concatArr.concat(arr), []);
}

console.log(concatArrays([1, 2],[3],[4, 5, 6])); // [1,2,3,4,5,6]
console.log(concatArrays(['a'],['b'],['c'],['d'],['e'],['f'],['g'])); // ['a', 'b', 'c', 'd', 'e', 'f', 'g']
console.log(concatArrays([5, 5, 5, 5, 5])); // [5, 5, 5, 5, 5]