# Проверить истинность утверждения ¬(X ⋁ Y v Z) = ¬X ⋀ ¬Y ⋀ ¬Z
def Check(x, y, z):
    return not(x or y or z) == (not x and not y and not z)
for x in range(0,2):
    for y in range(0,2):
        for z in range (0,2):
            print(Check(x, y, z))