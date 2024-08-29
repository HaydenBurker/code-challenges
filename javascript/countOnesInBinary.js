// Write a function that counts the amount of ones in the binary representation of an integer.

function countOnes(num) {
    let ones = 0;
    while (num > 0) {
        ones += num % 2;
        num = Math.floor(num / 2);
    }
    return ones;
}

console.log(countOnes(12)); // 2 (1100)
console.log(countOnes(0)); // 0
console.log(countOnes(1)); // 1
console.log(countOnes(999)); // 8
console.log(countOnes(63)); // 6
console.log(countOnes(64)); // 1