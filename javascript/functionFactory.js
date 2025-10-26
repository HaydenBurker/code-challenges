// Create a function that takes a number n and returns a function which adds n to the number passed to it.

function makeAddFunction(n) {
  return function (n2) {
    return n + n2;
  };
}

const addFive = makeAddFunction(5);

console.log(addFive(10)); // 15
console.log(addFive(-5)); // 0

const addTwelve = makeAddFunction(12);

console.log(addTwelve(12)); // 24
console.log(addTwelve(30)); // 42
