arr = ['a', 'b', 'c']
print(arr)
arr.extend(['f', 'd', 'g'])
print(arr)
arr.insert(1, 'h')
print(arr)
arr.remove('a')
print(arr)
arr.pop(0)
print(arr)
del arr[1]
print(arr)
cop = []
cop = arr[1:3]
print(cop)
cop.clear()
print(cop)
num = [1, 5, 3, 9, 8, 7, 1, 3, 5]
num.sort(reverse=True)
print(num)

tip = (1, 2, 3, 4, 5)
print(tip)
print(type(tip))
tupe = ('chen', 'hello', 'deng')
tupe = tupe[:1] + ('dear',) + tupe[1:]
print(tupe)
st = 'aaa'
print(st.capitalize())
