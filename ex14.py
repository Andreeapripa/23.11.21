A=str(input('primul sir:'))
B=str(input('al doilea sir:'))
A=set(A)
B=set(B)
print('A) caractere ce se intilnesc cel putin in unul dintre siruri:', A.union(B))
print('B) caractere care apar in ambele siruri:', A.intersection(B))
print('C) caractere care apar in primul sir si nu apar in sirul al doilea:', A.difference(B))