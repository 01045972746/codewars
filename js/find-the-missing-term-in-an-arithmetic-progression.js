var findMissing = function (list) {
  var max = Math.max.apply(null, list)
  var min = Math.min.apply(null, list)
  var d = (max - min) / list.length
  return (list.length+1) * (2* min + list.length*d) / 2 - list.reduce((x, y) => x + y)
}