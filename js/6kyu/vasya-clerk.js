function tickets(peopleInLine) {
  var budget = {
    25: 0,
    50: 0,
    100: 0,
  }
  
  for(let item of peopleInLine) {
    if(item - 25 == 0)
      budget[25] += 1
    else if(item - 25 == 25) {
      budget[25] -= 1
      budget[50] += 1
    }
    else {
      if(budget[50] > 0) {
        budget[50] -= 1
        budget[25] -= 1
      }
      else {
        budget[25] -= 3
      }
    }

    if(budget[25] < 0 || budget[50] < 0)
      return "NO"
  }
  return "YES"
}

module.exports = tickets