raudtee={
  "Tallinn":["Tapa"],
  "Tapa":["Tallinn", "Rakvere", "Tartu"],
  "Rakvere":["Tapa", "Narva"],
  "Narva":["Rakvere"],
  "Tartu":["Tapa", "Valga", "Petseri"],
  "Valga":["Tartu", "Petseri"],
  "Petseri":["Tartu", "Valga"]
}

algkoht="Tallinn"
uuritavad=[algkoht]
tagasitee={algkoht:algkoht}
while uuritavad:
   uuritav=uuritavad.pop(0)
   for koht in raudtee[uuritav]:
      if koht not in tagasitee:
         tagasitee[koht]=uuritav
         uuritavad.append(koht)

print(tagasitee)
sihtkoht="Valga"
teekond=[sihtkoht]
koht=sihtkoht
while koht!=algkoht:
   koht=tagasitee[koht]
   teekond.append(koht)

print("-".join(teekond))
teekond.reverse()
print("-".join(teekond), len(teekond)-1)
