// Write a function that calculates the trace of a square matrix

function trace(matrix) {
  return matrix.reduce((trace, row, i) => trace + row[i], 0);
}

console.log(
  trace([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
  ])
); // 34 (1 + 6 + 11 + 16)

console.log(
  trace([
    [1, 4],
    [4, 1],
  ])
); // 2

console.log(
  trace([
    [9, 1, 2],
    [6, 8, 5],
    [3, 7, 4],
  ])
); // 21
