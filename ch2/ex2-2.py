import random
fruitsList= ['Banana', 'Apple', 'Grape', 'Pineapple', 'Orange']
print(fruitsList)
random.shuffle(fruitsList)
print('打亂順序後: {}'.format(fruitsList))
fruitsList.reverse()
print('反轉後: {}'.format(fruitsList))
fruitsList.sort()
print('由小至大排序後: {}'.format(fruitsList))
fruitsList.sort(reverse=True)
print('由大至小排序後: {}'.format(fruitsList))
sortedFruitsList = sorted(fruitsList) # 回傳排序後的串列
print('排序後: {}'.format(sortedFruitsList))
fruitsList3 = random.sample(fruitsList, 3) # 隨機取出3個元素
print('隨機取出3個元素: {}'.format(fruitsList3))
