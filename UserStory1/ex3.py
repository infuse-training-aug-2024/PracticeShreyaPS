

def skip_sports(skip_integer):
    sports_input=input("enter list of sports")
    sports_array=sports_input.split(",")
    index_array=[]
    p=len(sports_array)
    for i in range (p):
        index_array.append(i+1)
    #skip_integer=2
    integers_to_include=[]
    for i in range(skip_integer+1,p+1):
        integers_to_include.append(i)

    myDict = { k:v for (k,v) in zip(index_array, sports_array)} 
    print(myDict)
    subset_dict = {k: myDict[k] for k in integers_to_include}
    print(subset_dict)
    return(subset_dict)

skip_sports(2)




