import requests
siti=['http://www.google.com','http://www.youtube.com','http://www.facebook.com',
      'http://www.polimi.it','http://www.amazon.com','http://www.netflix.com',]
avg=[]
for url in siti:
   print('URL:',url)
   tempi=[]
   for a in range (10):
       r=requests.get(url)
       tempi.append(r.elapsed.microseconds/1000)
   print('Tempo medio', sum(tempi)/len(tempi))
   avg.append(sum(tempi)/len(tempi))
print(siti[avg.index(min(avg))] , min(avg))
