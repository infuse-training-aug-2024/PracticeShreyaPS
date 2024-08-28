serial_number=''
average_string=''

def get_average(number1,number2):
    average_cal=(number1+number2)/2
    average=f"{average_cal:.2f}"
    average_string=str(average)
    return average_string

def split_number(serial_input):
   # serial_input= input("enter serial input:")
    serial_number=serial_input[:3]
    first_number=float(serial_input[4:9])
    second_number=float(serial_input[10:])
    average_string=get_average(first_number,second_number)
    output=serial_number+'-'+average_string
    print(output)
    return output
   
    

