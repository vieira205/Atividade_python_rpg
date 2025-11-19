class dado():
    def __init__(self):
        self.seed = 0

     
    def random(self,min,max):
        a = 1664525
        c = 1013904223
        m = 2**32

        seed = (a * self.seed + c) % m

        range_size = max - min + 1
        random_num = (seed % range_size) + min
        self.seed+=1
        return random_num

dado1 = dado()

