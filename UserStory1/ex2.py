arr=['9','5','1','2','3','4','0','-1']

class RangeFunctions:
    

    def element_at(self,arr,index):
        print(arr[index])
        return arr[index]

    def inclusive_range(self,arr,start_pos,end_pos):
        print( arr[start_pos:end_pos+1])
        return arr[start_pos:end_pos+1]
     
    def non_inclusive_range(self,arr,start_pos,end_pos):
        print( arr[start_pos:end_pos])
        return arr[start_pos:end_pos]

    def start_and_length(self,arr,start_pos,len):
        print( arr[start_pos:start_pos+len])
        return arr[start_pos:start_pos+len]

obj1=RangeFunctions()
index=int(input("enter index for element at"))
obj1.element_at(arr, index)
start_pos=int(input("enter start position :"))
end_pos=int(input("enter end position :"))
obj1.inclusive_range(arr,start_pos,end_pos)
obj1.non_inclusive_range(arr,start_pos,end_pos)
length_of_array=int(input("enter length of array"))
obj1.start_and_length(arr,start_pos,length_of_array)