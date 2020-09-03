from functools import reduce;
a=[10,20,30,40];
b=list(map(lambda n:n*n,a));
print(b);
def update(k):
  if k%2==0:
      return k;
def mapping(k,l):
    return k+l;
c=list(filter(update,b));
print(c);
d=reduce(mapping,c);
print(d);
v=reduce(lambda n,m:n+m,c);
print(v);
if(d==v):
    print("Thats Fine and great");