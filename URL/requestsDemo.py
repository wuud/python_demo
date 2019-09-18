import requests
r = requests.get('http://www.spielzeugz.de/html5/liquid-particles-3D/')
print(r.encoding)
print(r.url)
write=open('new.html','w+',encoding='utf-8')
write.write(r.text)
