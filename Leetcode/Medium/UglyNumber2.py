# https://leetcode.com/problems/ugly-number-ii/description/

def solution(n):
  result = 1
  cnt = 1
  tmp = 0

  factors = [2, 3, 5]
  primeDict = {}

  while cnt != n:
    result += 1
    tmp = result

    while tmp != 1:
      if tmp % 5 != 0 and tmp % 3 != 0 and tmp % 2 != 0:
        primeDict[tmp] = True
        break

      for factor in factors:
        if tmp % factor == 0:
          mod = tmp // factor
          if primeDict.get(mod):
            break
          else:
            tmp = tmp / (mod * factor)

      print("tmp", tmp)
      if tmp == 1:
        cnt += 1
      else:
        break

  return result


class Solution:
    def nthUglyNumber(self, n: int) -> int:
      result = 1
      cnt = 1
      tmp = 0

      factors = [2, 3, 5]
      primeDict = {}

      while cnt != n:
        result += 1
        tmp = result

        while tmp != 1:
          if tmp % 5 != 0 and tmp % 3 != 0 and tmp % 2 != 0:
            primeDict[tmp] = True
            break

          for factor in factors:
            if tmp % factor == 0:
              mod = tmp // factor
              if primeDict.get(mod):
                break
              else:
                tmp = tmp / (mod * factor)

          if tmp == 1:
            cnt += 1
          else:
            break

      return result

# result = solution(10)
# result = solution(11)
result = solution(413)

# result = Solution.nthUglyNumber(413)
# result = Solution.nthUglyNumber(11)
# result = Solution.nthUglyNumber(18)
print("result", result)
