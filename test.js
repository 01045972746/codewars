const tickets = require('./6kyu/vasya-clerk')
const queueTime = require('./6kyu/the-supermarket-queue')

/**
test('vasya-clerk', () => {
  expect(tickets([25, 25, 50, 50])).toBe("YES")
  expect(tickets([25, 100])).toBe("NO")
})
**/

test('the-supermarket-queue', () => {
  expect(queueTime([], 1)).toBe(0)
  expect(queueTime([1,2,3,4], 1)).toBe(10)
  expect(queueTime([2,2,3,3,4,4], 2)).toBe(9)
  expect(queueTime([1,2,3,4,5], 100)).toBe(5)
})