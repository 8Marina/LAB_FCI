import requests
import matplotlib.pyplot as plt

m = 0
siti = ['http://www.google.com', 'http://www.polimi.it', 'http://www.youtube.com', 'http://www.facebook.com', 'http://www.netflix.com','http://twitter.com']

for url in siti:
    print(' URL: ', url)
    tempi = []

    for j in range(60):
        r = requests.get(url)
        tempi.append(r.elapsed.microseconds / 1000)
        
    plt.plot(tempi, label=url)
    m= max([m,max(tempi)])

plt.xlabel('Richiesta ID')
plt.ylabel('Tempo di Risposta (ms)')
plt.title('Tempo di Risposta Multipli Server http')
plt.ylim([0, 1.1 * m])
plt.legend(loc='upper right', fontsize=10)
plt.show()
