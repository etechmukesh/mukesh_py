class Iteration:
    def __init__(self):   #Give the start value of the object
        self.num=1;
    def __iter__(self):   #Assign iteration to the object.So that the iteration can happen done one by one.
         return self;
    def __next__(self):   #When this method is called the iteration starts
        if self.num<=10
            val=self.num;
            self.num+=1;
            return val;
        else:
            raise StopIteration;
values=Iteration();
print(values.__next__());
print(values.__next__());
print(next(values));
for i in values:           #value is the argument that passes to the next function
    print(i);
# The constructor is just used to initialize the value.
# By the iter method application to the object the object becomes show its property or values by iteration.
# The next function is used to fetch the properties when the next method is called.
# When "for i in values" is executed the next method is called because the "values" object is assigned with iteration,its next value must be present and i indicates the next value of the
