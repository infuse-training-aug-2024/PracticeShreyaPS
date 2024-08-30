serial_number=''
average_string=''

def check_for_single_digit(average):
    number_before_decimal = average.split(".")
    if len(number_before_decimal[0]) == 1:
        average_output = "0" + average
        print(average_output)
        return average_output
    else:
        return average


def get_average(number1,number2):
    average_cal=(number1+number2)/2
    average_string=f"{average_cal:.2f}"
    print("before",average_string)
    average=check_for_single_digit(average_string)
    print("after",average)
    return average

def split_number(serial_input):
    #serial_input= input("enter serial input:")
    serial_number=serial_input[:3]
    first_number=float(serial_input[4:9])
    second_number=float(serial_input[10:])
    average_string=get_average(first_number,second_number)
    output=serial_number+'-'+average_string
    print(output)
    return output
   
    

split_number('333-00.00-10.00')