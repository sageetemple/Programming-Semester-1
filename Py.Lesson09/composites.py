nums= [2,6,8,9,10,12,13,15,17,24,55,66,78,77,79]
def gFactor(number):
      for z in range(2,number,1):
            if (number%z)==0:
                return 1
            else:
                return 0


def removePrimes():
      for i in nums:
            if gFactor(i)==0:
                  nums.remove(i)
removePrimes()
print(nums)
