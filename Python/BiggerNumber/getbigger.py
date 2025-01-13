number = [1, 33, 55, 77, 2 , 5]
ultimaposicion = 78238723478
def biggernumber(number):
  biggernumber = 0
  for  each in number :
    if (each > biggernumber):
      biggernumber = each
  return biggernumber

biggestnumber = biggernumber(number)
print("The biggest number " + str(biggestnumber))

def parinpar(number):
  numbers_par = []
  numbers_inpar = []
  for each in number: 
    if (each %2 == 0):
      numbers_par.append(each) 
    else:
      numbers_inpar.append(each) 
  return numbers_inpar, numbers_par
numbers_inpar, numbers_par = parinpar(number)

print("numeros inpares " + str(numbers_inpar) + " numeros pares " + str(numbers_par))


def lastposition(ultimaposicion):
  string_ultimaposicion = str(ultimaposicion)
