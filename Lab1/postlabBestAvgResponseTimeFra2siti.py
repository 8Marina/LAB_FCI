#scrivere uno script che stampi il nome della pagina col miglior tempo di risposta MEDIO fra 2 siti
#siti:google e youtube
#numero richieste=10
import requests
tempi1=[]

for a in range (10):
    r=requests.get('http://www.google.com')
    tempi1.append(r.elapsed.microseconds/1000)
avg1= sum(tempi1)/len(tempi1)
print ('Tempo medio Google:',avg1)

tempi2=[]

for b in range(10):
    r=requests.get('http://www.youtube.com')
    tempi2.append(r.elapsed.microseconds/1000)
avg2=sum(tempi2)/len(tempi2)
print('Tempo medio YouTube:',avg2)

#come troverei io il minore dei 2 medi :
#print('Tempo migliore:'min(avg1,avg2))

#come lo ha fatto il prof
if avg<avg2:
   print('Google ha il tempo migliore')    
else:
  print('Youtube ha il tempo migliore')
