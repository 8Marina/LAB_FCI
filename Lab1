#TEMPO DI RISPOSTA GOOGLE
import requests
import matplotlib.pyplot as plt

tempi=[]

for j in range(10):
  r=requests.get('http://www.google.com')
  tempi.append(r.elapsed.microseconds/1000)
  print('Tempo di risposta',r.elapsed.microseconds/1000,'ms')
  
print ('Tempo di risposta minimo',min(tempi))
print ('Tempo di risposta massimo',max(tempi))
print ('Tempo di risposta medio',sum(tempi)/len(tempi))

plt.figure()
plt.plot(tempi)
plt.xlabel('ID richiesta')
plt.ylabel('Tempo di risposta(ms)')
plt.title('Tempo di Risposta Google')
plt.ylim([0.8*min(tempi),1.1*max(tempi)])
plt.show()
