function zeroes (base, number) {
  var factors = {}, i = 1;
  while(++i <= base) 
    while(base%i == 0) {
      base /= i; 
      factors[i] = (factors[i]||0) + 1;
    }

  return Math.min(...Object.keys(factors).map(factor => {
    var count = 0, i = 1;
    while((i *= factor) <= number) count += Math.floor(number/i);
    return count/factors[factor];
  }));
}
