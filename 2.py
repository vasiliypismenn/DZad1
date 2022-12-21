# 1.	Напишите программу для 
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
print('x y z  проверка истинности')
for x in range (2):
      for y in range (2):
            for z in range (2):
               a = ((not(x or y or z)) == (not (x) and(y) and(z)))
               print(x,y,z,"  ", a)
