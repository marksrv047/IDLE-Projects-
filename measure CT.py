def create(m:str,n:list[int]):
    print('----MEASURE OF TENDENCY----')
    m=m.lower()
    if m =='mean':
        x=0
        for i in n:
            x+=i
        return x/len(n)

    elif m=='median':
        n.sort()
        l=len(n)
        if l%2== 0:
            return (n[l//2-1]+n[l//2])/2
        else:
            return n[l//2]

    elif m=='mode':
        mx= 0
        mode=n[0]
        for i in n:
            c= 0
            for j in n:
                if i==j:
                    c+= 1
            if c>mx:
                mx=c
                mode=i
        return mode

if __name__ == '__main__':
  m = input('enter measure of tendency: ')
  n = list(map(int, input('enter list of num [csv]: ').split(',')))
  print(create(m,n))
  print('-'*15)
