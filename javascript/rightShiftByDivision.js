// Write a function that mimics the right shift operator and returns the result from the two given integers.

function shiftToRight(num, shift) {
  return shift === 0 ? num : shiftToRight(Math.floor(num / 2), shift - 1);
}

console.log(shiftToRight(88, 3)); // 11
console.log(shiftToRight(123, 0)); // 123
console.log(shiftToRight(8642, 1)); // 4321
console.log(shiftToRight(255, 6)); // 3
console.log(shiftToRight(256, 6)); // 4
