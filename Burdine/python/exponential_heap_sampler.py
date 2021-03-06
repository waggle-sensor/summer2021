import random

class ExponentialHeapSampler():
        
    def __init__(self, max_len=8, is_random=False):
        assert(max_len > 0)
        self.is_random = is_random
        self.max_len = max_len
        self.front_idx = 0
        self.items = []
        

    def __getitem__(self, index):
        return self.items[index]
    
    def __len__(self):
        return len(self.items)

    def add(self, item):
        
        # insert item
        if len(self.items) < self.max_len:
            self.items.append(item)
        else:
            self.items[self.front_idx] = item    
        self.front_idx += 1        

        # perform promotion (if necessary)
        if self.front_idx >= self.max_len:
            self._promote()
            self.front_idx = self.max_len//2

    def addget(self,item):
        
        # insert item:
        ret = None
        if len(self.items) < self.max_len:
            self.items.append(item)
        else:
            ret = self.items[self.front_idx]
            self.items[self.front_idx] = item
        self.front_idx += 1    

        # perform promotion (if necessary):
        if self.front_idx >= self.max_len:
            self._promote()
            self.front_idx = self.max_len//2
        return ret        

    def _promote(self):
        if len(self.items) == self.max_len:
             
            # perform random pair swaps (to ensure a random 
            # member of each pair is promoted):
            if self.is_random:
                for i in range(2,self.max_len,2):
                    if bool(random.getrandbits(1)):
                        self.items[i-1], self.items[i] = self.items[i], self.items[i-1]
            
            # perform promotion:
            new_items = []
            for i in range(1, self.max_len, 2):
                new_items.append(self.items[i])
            for i in range(0, self.max_len, 2):
                new_items.append(self.items[i])
            self.items = new_items
        
    def __str__(self):
        return str(self.items) + f' (front: {self.front_idx})'


def main():
    import matplotlib.pyplot as plt
    import numpy as np

    heap_times = []
    heap_deltas = []
    es = ExponentialHeapSampler(256)
    for i in range(1000000):
        last = es.addget(i)
        if last != None:
            heap_times.append(i - last)
        if (i%100) == 99:
            for j in es:
                heap_deltas.append(i-j)

    print('Mean retention time:', np.mean(heap_times))
    plt.figure()
    plt.title(f'Distribution of EHS retention times (N={es.max_len})')
    plt.hist(heap_times, density=True)
    plt.show()

    print('Mean item age:', np.mean(heap_deltas))
    plt.figure()
    plt.title(f'Distribution of age of EHS items (N={es.max_len})')
    plt.hist(heap_deltas, density=True)
    plt.show()
if __name__ == '__main__':
    main()
