import requests

siti = ['http://www.google.com',  'http://www.youtube.com', 'http://www.facebook.com']

for url in siti:
    print(' URL: ', url)
    tempi = []

    for j in range(10):
        r = requests.get(url)
        tempi.append(r.elapsed.microseconds / 1000)

    print('Minimo tempo di risposta: ', min(tempi))
    print('Massimo tempo di risposta: ', max(tempi))
    print('Tempo di risposta medio: ', sum(tempi) / len(tempi))
    m = max([m, max(times)])
    plt.plot(times, label=url)
