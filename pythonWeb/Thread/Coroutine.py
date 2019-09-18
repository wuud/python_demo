def consumer():
    r=''
    while True:
        n=yield r
        print("Consumer consuming  {}...".format(n))
        r='200 0K'
def produce(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('Producer producing  {}...'.format(n))
        r=c.send(n)
        print('Comsumer return {}'.format(r))
    c.close()
c=consumer()
produce(c)
