nums= [2,6,8,9,10,12,13,15,17,24,55,66,78,77,79]
def gFactor(number):
      for i in range(2,number,1):
            if (number%i)==0:
                  return 1
            else:
                  return 0
def removeComposites():
      for i in nums:
            if gFactor(i)==0:
                  nums.remove(i)
removeComposites()
print(nums)
