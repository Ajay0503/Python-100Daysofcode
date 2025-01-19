ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
ep1.update(ep2)
print(ep1)

ep3 = {122: 45, 123: 89, 567: 69, 670: 69}
ep3.clear()
print(ep3)

empt ={}
print(empt)

ep4 = {122: 45, 123: 89, 567: 69, 670: 69}
ep4.pop(122)
print(ep4)
ep4.popitem()
print(ep4)

del ep4[123]
print(ep4)

del ep4 #delete full ep4 list


