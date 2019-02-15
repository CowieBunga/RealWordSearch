
'''
dic = {"year": 2019, "Car": "Honda Civic"}
print(dic)
'''


'''
dic = {"vegetable": "lettuce", "fruit": "mango"}
del dic["fruit"]
'''

'''
dic = {}
dic["food"] = "hamburger"
dic["drink"] = "chocolate milk"
dic["side plate"] = "mac and cheese"
'''

'''
dic = {"apple": "macintosh", "ape": "chimpanzee", "jam": "strawberry"}
list = []
for key in dic:
    if key[0] == 'a':
        list.append(key)
for value in list:
    del dic[value]
print(dic)
'''

# DAY 2


def returnkey(values, dic):
    for key, vals in dic.items():
        if vals == values[i]:
            return key


values = ["a", "b", "c", "d"]
dic = {"first": "a", "second": "b", "third": "c", "fourth": "d"}
for i in range(0, 4):
    key = print(returnkey(values, dic))

'''
#problem number 4
dict = {}
for i in range(0, 3):
    word = input("Please input a word ")
    definition = input("now please input a definition for that word ")
    dict[word] = [definition]
print(dict)
'''


'''
#problem number 5
def listtodic(listofstr):
    dictOfWords = {i: 5 for i in listofstr}
    return dictOfWords
listofstr = ["a", "b", "c"]
print(listtodic(listofstr))
'''

