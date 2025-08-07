// Write a function that takes in an array of box dimensions and calculates the total volume of all boxes

function totalVolume(...boxes) {
  return boxes.map(([l, w, h]) => l * w * h).reduce((acc, cur) => acc + cur, 0);
}

console.log(totalVolume([3, 4, 5])); // 60
console.log(totalVolume([1, 1, 1])); // 1
console.log(totalVolume());
