// Write a function that takes in a temperature in farenheit and converts it to celcius and kelvin

function temperatureConversion(f) {
  const c = (5 * (f - 32)) / 9;
  const k = c + 273.15;
  if (k < 0) return "too cold";
  return [parseFloat(c.toFixed(2)), parseFloat(k.toFixed(2))];
}

console.log(temperatureConversion(98.6)); // [37, 310.15]
console.log(temperatureConversion(32)); // [0, 273.15]
console.log(temperatureConversion(-459)); // [-272.78, 0.37]
console.log(temperatureConversion(-460)); // too cold
console.log(temperatureConversion(212)); // [100, 373.15]
console.log(temperatureConversion(1000)); // [537.78, 810.93]
console.log(temperatureConversion(0)); // [-17.78, 255.37]
