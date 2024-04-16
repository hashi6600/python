# Write your code her 
freqDict = {"hi":45, "this": 35,"the":28}
freqDict.update({"the": 40})
#freqDict({"the": 40})
print(freqDict)
copyfreqDict = freqDict.copy()
print(copyfreqDict)
print(copyfreqDict.popitem())
newfreqDict = copyfreqDict.setdefault("data", "21")
print(newfreqDict)
count = freqDict.pop("this")
print(count)
freqDict.clear()
print(freqDict)
keys = {'d', 'i', 'c', 't'}
value = [1]
newDict = dict.fromkeys(keys, value)
print(newDict)
