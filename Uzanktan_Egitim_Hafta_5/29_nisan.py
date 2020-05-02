from pprint import pprint as pp
from itertools import chain, combinations
#class ve constructor yapısı ile değerleri atıyoruz.
class Item(object): 
   def __init__(self, n, v, w): 
       self.name = n 
       self.value = v 
       self.weight = w 
   def getName(self): 
       return self.name 
   def getValue(self): 
       return self.value 
   def getWeight(self): 
       return self.weight 
   def __str__(self): 
       result = '<' + self.name + ', ' + str(self.value) + ', ' + str(self.weight) + '>' 
       return result 

def value(item): 
    return item.getValue() 

def weightInverse(item): 
    return 1.0/item.getWeight() 

def density(item): 
    return item.getValue()/item.getWeight() 

#Boyuta göre tüm olasılıkları bulan fonksiyon
def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse = True) #itemleri bizim belirlediğimiz kritere göre sıraladık.
    result = [] #çantaya koyacağımız değerler.
    totalValue, totalWeight = 0.0, 0.0  #çanta doldu mu çantamızadaki ağırlık nedir diye burda gösterdik
    
    for i in range(len(itemsCopy)): 
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i]) #Eğer total ağırlık ve alınan ağrılık topalmı maxsimum ağırlıktan küçük eşitse eşyayı çantaya ekliyoruz.
            totalWeight += itemsCopy[i].getWeight() #totalWeight i güncelliyoruz
            totalValue += itemsCopy[i].getValue() #totalValue yu güncelliyoruz.
    return (result, totalValue)

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer','gold']
    #names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [55,63,210,17,88,23,74] 
    #values = [96,32,520,78,66,31] 
    #values = [175,90,20,50,10,200]
    weights = [15,8,2,3,9,20,1]
    #weights = [20,1,2,4,9,10]
    #weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

def testGreedy(items, maxWeight, keyFunction): #degerleri yazdırıyoruz.
    taken, val = greedy(items, maxWeight, keyFunction)     
    print ('Total value of items taken = ', val)     
    for item in taken:         
        print ('   ', item)     
        
def testGreedys(maxWeight = 10):     
    items = buildItems()     
    print ('Use greedy by value to fill knapsack of size', maxWeight) # value değerini en yüksek tutarak
    testGreedy(items, maxWeight, value)     
    print ('\nUse greedy by weight to fill knapsack of size', maxWeight) # maxWeight değerini en az tutarak
    testGreedy(items, maxWeight, weightInverse)     
    print ('\nUse greedy by density to fill knapsack of size', maxWeight) # #value/maxWeight oranınagöre
    testGreedy(items, maxWeight, density)        

print("<-----------Greedys------------>")
print(testGreedys())        
print("<-----------ChooseBest------------>")

#en iyi ihtimali seçen fonksiyon    
def chooseBest(pset, maxWeight, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
            if itemsWeight <= maxWeight and itemsVal > bestVal:
                bestVal = itemsVal
                bestSet = items
    return (bestSet, bestVal)        
        
#en iyi ihtimali yazdıran fonksiyon
def testBest(maxWeight = 30):
    items = buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print("Total value of items taken is = ", val)
    for item in taken:
        print(item)       

print(testBest())
print("<------------Powerset----------->")
       
#sayıların tüm olasılılarını bulan fonksiyon
def genPowerset(iterable):
    "genPowerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3), (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

pset = set(genPowerset({1, 2, 3}))
for set_1 in pset:
   print(set_1)
pp(set(genPowerset({1, 2, 3})))
