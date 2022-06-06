

def flatten_array(numbers):
    num= []
    for items in numbers:
        for i in items:
            num.append(i)
    return sorted(num)
print(flatten_array([[2,12, 1],[5,8,18],[4,15,9]]))
print(flatten_array([[2,12, 1],[5,8,18],[4,15,9]]))

'''
class TestArray:
    def __init__(self):
        self.arr = []

    def flatten_and_sort(self, newArray):
        for item in newArray:
            for i in item:
                self.arr.append(i)
        return sorted(self.arr)

testOOP = TestArray()
testResult = testOOP.flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]])
print(testResult)
'''
'''
How does this solution ensure data immutability?  The input provided produced similar output and the input cannot be modified or changed. 
Is this solution a pure function? Why or why not? The solution is pure function because it has no side effect.
Is this solution a higher order function? Why or why not? no, it is not. A higher order function required another function as an argument and return a function. This solution doesnt take another function.
Would it have been easier to solve this problem using a different programming style? No, It's possible to solve it with another programming style but functional programming is much easier and produce written less code.
Why in particular is functional programming a helpful paradigm when solving this problem? Its mathematical function style provide quick solution to problems. The assembly line will always produce similar output.
'''

class Prodracer:
    def __init__(self, max_speed, codition, price):
        self.max_speed = max_speed
        self.price = price
        self.condition = codition

    def repair(self):
        self.condition = "repaired"
        
class AnakinsPod(Prodracer):
    def __init__(self, max_speed, codition, price):
        super().__init__(max_speed, codition, price)

    def boost(self):
        self.max_speed *= 2 

class SebulbasPod(Prodracer):
    def __init__(self, max_speed, codition, price):
        super().__init__(max_speed, codition, price)

    def flame_jet(self,):
        self.condition = "trashed"


pod= Prodracer(100, "repaired", 20)
pod.repair()
print(pod.condition)

new_pod = AnakinsPod(2, "repaired", 20)
new_pod.boost()
print(new_pod.max_speed)

third_pod= SebulbasPod(2, "repaired", 20)
third_pod.flame_jet()
print(third_pod.condition)
'''
Once an Object Oriented solution has been implemented, answer the following questions:
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
Encapsulation: Having our data living in the insatances of the class is encapsulation
Abstraction: Classes with method are using abstraction
Inheritance: AnakinsPod, SebulbasPod inherit the properties of the parent Prodracer
Polymorphism: We didnt make use of polymorphism in our solution
Would it have been easier to implement a solution to this problem using a different coding style? Why or why not? no, object oriented programming is easier in solving this type of problem due to its four pillars
How in particular did Object Oriented Programming assist in the solving of this problem? Giving the fact that the children can inherit from the parent class and the data pass down to the children can be updated assist in solving this problem.
'''