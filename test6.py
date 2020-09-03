from array import*;
a=array('i',[]);
n=int(input("Enter the lengthy of the array"));
for i in range(n):
    c=int(input("Enter the number"));
    a.append(c);
y=array(a.typecode,(i for i in a));
print("The elements of the array are=");
for i in range(n):
    print(a[i]);
for i in y:
    print(i);
for i in range(5):
    print("Mukesh");
for i in range(len(y)):
    print(y[i]);

