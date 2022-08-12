class help:

    def work(self):
        self.x=3
        self.y=4
        self.z=self.x+self.y
        print(self.z)


    def time(self):
        # self.x=5
        x =help().work()
        return x

help().work()
help().time()