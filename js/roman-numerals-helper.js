const symbol = {
  'I': 1,
  'IV': 4,
  'V': 5,
  'IX': 9,
  'X': 10,
  'XL': 40,
  'L': 50,
  'XC': 90,
  'C': 100,
  'CD': 400,
  'D': 500,
  'CM': 900,
  'M': 1000
}

class RomanNumerals {

  static toRoman(num) {
    var arr = []
    Object.keys(symbol).reverse().forEach(k => {
      while(true) {
        num -= symbol[k]
        if(num < 0) {
          num += symbol[k]
          break
        }
        arr.push(k)
      }
    })
    return arr.join('')
  }

  static fromRoman(str) {
    var strarr = str.split(''),
        idx = strarr.length,
        result = 0
    while(idx--) {
      if( symbol[strarr[idx]] < symbol[strarr[idx+1]] )
        result -= symbol[strarr[idx]]
      else
        result += symbol[strarr[idx]]
    }
    return result
    
    
  }

}

RomanNumerals.toRoman(1000); //M
RomanNumerals.toRoman(1990); //MCMXC
RomanNumerals.toRoman(2008); //MMVIII
RomanNumerals.fromRoman("M"); // 1000
RomanNumerals.fromRoman("MCMXC"); // 1990