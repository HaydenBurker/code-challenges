// Create a function that takes a list of integers and returns the amount of integers which are of equal value.

function equalValues(nums) {
  const count = {};
  for (const num of nums) {
    count[[num]] = count[[num]] ? count[[num]] + 1 : 1;
  }
  return Object.values(count)
    .filter((num) => num > 1)
    .reduce((sum, num) => sum + num, 0);
}

console.log(equalValues([1, 2, 2])); // 2
console.log(equalValues([5, 1, 2])); // 0
console.log(equalValues([12, 12, 12])); // 3
console.log(equalValues([])); // 0
console.log(equalValues([42])); // 0
console.log(equalValues([5, 5, 8, 8])); // 4
console.log(equalValues([5, 8, 8, 8])); // 3
console.log(equalValues([8, 8, 8, 8])); // 4
console.log(equalValues([1, 2, 3, 4, 5, 5, 2, 6, 4, 5])); // 7
