// Make a function that takes an array of numbers and counts the number of occurrences where a number is greater than the previous number in the array

function increaseCounter(numbers) {
  let result = 0;

  numbers.forEach((number, i) => {
    if (i > 0 && number > numbers[i - 1]) {
      result++;
    }
  });

  return result;
}

console.log(increaseCounter([1, 3, 6, 2, 5])); // 3
console.log(increaseCounter([5, 4, 3, 2, 1])); // 0
console.log(increaseCounter([1, 2, 3, 4, 5])); // 4
console.log(increaseCounter([3, 3])); // 0
console.log(increaseCounter([])); // 0
console.log(increaseCounter([6, 4, 4, 1, 7, 5])); // 1
