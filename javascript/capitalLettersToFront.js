// Create a function that moves all capital letters to the front of a word.

function capToFront(letters) {
  let capitalLetters = "";
  let otherLetters = "";

  letters
    .split("")
    .forEach((l) =>
      /[A-Z]/.test(l) ? (capitalLetters += l) : (otherLetters += l)
    );
  return capitalLetters + otherLetters;
}

console.log(capToFront("Hello World!")); // "HWello orld!"
console.log(capToFront("raceCAR")); // "CARrace"
console.log(capToFront("aBcDeFg")); // "BDFaceg"
