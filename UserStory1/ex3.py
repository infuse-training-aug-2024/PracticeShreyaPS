
# class  SkipSports:

#     def skip_sports(skip_integer):
#         sports_input=input("enter list of sports")
#         sports_array=sports_input.split(",")
#         index_array=[]
#         p=len(sports_array)
#         for i in range (p):
#             index_array.append(i+1)
#         #skip_integer=2
#         integers_to_include=[]
#         for i in range(skip_integer+1,p+1):
#             integers_to_include.append(i)

#         myDict = { k:v for (k,v) in zip(index_array, sports_array)} 
#         print(myDict)
#         subset_dict = {k: myDict[k] for k in integers_to_include}
#         print(subset_dict)
#         return(subset_dict)

# SkipSports()


























# class SkipSports:
#     new_sports_array=[]
#     def skip_sports(self,sports_array,skip_integer):
#         try:
#             len_of_array=len(sports_array)
#             for i in range(skip_integer,len_of_array):
#                 index=str(i)
#                 new_sports_array.append(index+":"+sports_array[i])


#             return new_sports_array

        
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")


# sports_array=input("enter list of sports").split(",")
# skip_integer=int(input("enter skip integer"))
# SkipSports().skip_sports(sports_array,skip_integer)




class SkipSports:
    def __init__(self):
        self.new_sports_array = []

    def skip_sports(self, sports_array, skip_integer):
        try:
            if not isinstance(skip_integer, int) or skip_integer < 0:
                raise ValueError("skip_integer must be a non-negative integer.")
            len_of_array = len(sports_array)
            if skip_integer >= len_of_array:
                raise ValueError("skip_integer is greater than or equal to the length of the sports array.")

            self.new_sports_array = []
            for i in range(skip_integer, len_of_array):
                index = str(i)
                self.new_sports_array.append(index + ":" + sports_array[i])

            return self.new_sports_array

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None


sports_list = ['Football', 'Basketball', 'Tennis', 'Baseball', 'Hockey']
skip_integer = 2

skip_sports_instance = SkipSports()
result = skip_sports_instance.skip_sports(sports_list, skip_integer)
print(result) 
