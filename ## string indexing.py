## string indexing 
freqDict = {"hi":45, "this":35, "the":28}
print(freqDict)
freqDict ['and'] = 28
print(freqDict.get('this'))
print(freqDict.get('from'))
print(freqDict.get('from', 'Word does not exist in the dictionary')) 
for item in freqDict.keys():
    print(item)
for item in freqDict.values():
    print(item)
for key, value in freqDict.items():
    print(key, value)
print("hi" in freqDict)
print("hello" in freqDict)