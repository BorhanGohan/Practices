def histogram(items):
    for i in items:
        star=''
        times=i
        while(times>0):
          star+='*'
          times=times-1
        print(star)
histogram([2,3,6,5,15])
