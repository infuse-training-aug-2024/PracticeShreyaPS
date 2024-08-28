arr=['9','5','1','2','3','4','0','-1']

class range_functions:
    def __init__(self,index1, index2, index3):
        self.index1=index1
        self.index2=index2
        self.index3=index3

    def element_at(self,arr):
        print(arr[self.index1])
        return arr[self.index1]

    def inclusive_range(self,arr):
        print( arr[self.index2:self.index3])
        return arr[self.index2:self.index3]
     
    def non_inclusive_range(self,arr):
        print( arr[self.index2:self.index3])
        return arr[self.index2:self.index3]

    def start_and_length(self,arr):
        print( arr[self.index2:self.index2+self.index1])
        return arr[self.index2:self.index2+self.index1]

obj1=range_functions(3,4,6)
obj1.element_at(arr)
obj1.inclusive_range(arr)
obj1.non_inclusive_range(arr)
obj1.start_and_length(arr)