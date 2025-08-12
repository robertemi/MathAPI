x = 100
y = -30
z = 0

print(f'Integer x: {x} <-> ID Integer x {id(x)}')
x = float(x)
print(f'Float x: {x} <-> ID Float x {id(x)}')
x = bool(x)
print(f'Bool x: {x} <-> ID Bool x {id(x)}')

print('##########################################')

print(f'Integer y: {y} <-> ID Integer y {id(y)}')
y = float(y)
print(f'Float y: {y} <-> ID Float y {id(y)}')
y = bool(y)
print(f'Bool y: {y} <-> ID Bool y {id(y)}')

print('##########################################')

print(f'Integer z: {z} <-> ID Integer z {id(z)}')
z = float(z)
print(f'Float z: {z} <-> ID Float z {id(z)}')
z = bool(z)
print(f'Bool z: {z} <-> ID Bool z {id(z)}')

