class CalTool:              #=============no parenthesis
    def __init__(self, a=3, b=6):
        self.a = a
        self.b = b
        # self.sum=None
        # self.minus=None
        # self.multi=None
        # self.div=None

    def add(self):
        sum=self.a+self.b
        return sum

    def addlwj(self,x,y):
        sum=x+y+self.a+self.b
        return sum

    def minus(self):
        minus=self.a-self.b
        return minus

    def multi(self):
        multi = self.a - self.b
        return multi

    def div(self):
        div = self.a - self.b
        return div

    def lwj(self):
        print( "lwj age is {}".format(self.a),"lwj daughter is {}".format(self.b))
        # print()
