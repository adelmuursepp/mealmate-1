raudtee={
  "Tallinn":["Tapa"],
  "Tapa":["Tallinn", "Rakvere", "Tartu"],
  "Rakvere":["Tapa", "Narva"],
  "Narva":["Rakvere"],
  "Tartu":["Tapa", "Petseri", "Valga"],
  "Petseri":["Valga", "Tartu"],
  "Valga":["Tartu", "Petseri"]
}

kuvatud=[]

def kuva(linn, sygavus):
  print(sygavus*" "+linn)
  kuvatud.append(linn)
  for koht in raudtee[linn]:
    if koht not in kuvatud:kuva(koht, sygavus+1)

kuva("Tartu", 0)
