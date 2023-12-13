class MathDojo:
    def __init__(self):
        self.result = 0
 
    def add(self, num, *nums):
        if (len(nums) != 0):
            for i in nums:
                self.result = self.result + i
        self.result = self.result + num
        return self.result
    
    def subtract(self, num, *nums):
        self.result = self.result - num
        for i in nums:
            self.result = self.result - i
        return self.result
    
md = MathDojo().add(5)
bm = MathDojo().add(15,20)
am = MathDojo().add(3,9,4,21)
print(md)
print(bm)
print(am)

gm = MathDojo().subtract(15,5)
dm = MathDojo().subtract(35,17)
qm = MathDojo().subtract(167,22)
print("1.-",gm)
print("2.-",dm)
print("3.-",qm)