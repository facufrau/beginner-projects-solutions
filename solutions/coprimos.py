def find_mcd(a, b):
    '''
    Finds the max common divisor between 2 numbers.
    '''
    mcd_values_a = set() # Uso set para mantener elementos sin repetir.
    i = 1
    while i <= a:
        if a % i == 0:
            mcd_values_a.add(i)
        i += 1

    mcd_values_b = set()
    j = 1
    while j <= b:
        if b % j == 0:
            mcd_values_b.add(j)
        j += 1

    mcd_values_a.intersection_update(mcd_values_b) #Intersección entre 2 conjuntos de divisores.
    if mcd_values_a:
        return max(mcd_values_a)

print(find_mcd(5, 7)) # Si son coprimos -> devuelve 1
print(find_mcd(11, 49)) # Si son coprimos -> devuelve 1
print(find_mcd(36, 91)) # Si son coprimos -> devuelve 1
print(find_mcd(234, 658)) # No son coprimos -> devuelve 2
print(find_mcd(14, 15)) # Si son coprimos -> devuelve 1

max_value = 25
coprimos = []

for i in range (1, max_value + 1):
    for j in range (i, max_value + 1):
        result = find_mcd(i, j)
        if result == 1:
            coprimos.append((i, j))

print(coprimos)