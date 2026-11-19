def burrows_wheeler(stringa):
    if not stringa:
        return""

rotazioni =[]

for i in range(len(stringa)):
    rotazione=stringa[i:]+stringa[:i]
    rotazioni.append(rotazione)

    rotazione.sort()

     risultato=""
for rotazione in rotazioni:
        risultato +=rotazione[-1]

        return risultato
