n=int(input("entrez le nombre des notes:"))
s=0
for i in range(n):
    note=float(input(f"entrez la note {i+1}:"))
    s=s+note
moy=s/n
print(f"la moyenne des {n} nombres est : {moy}")
