serial_number = ''
average_string = ''
import re

class SerialAverage:
    def check_for_single_digit(self, average):
        try:
            number_before_decimal = average.split(".")
            if len(number_before_decimal[0]) == 1:
                average_output = "0" + average
                return average_output
            else:
                return average
        except (TypeError) :
            print("TypeError: The input recived for checking for single digit is not a string.")
            return None

    def get_average(self, number1, number2):
        try:
            average_cal = (number1 + number2) / 2
            print(average_cal)
            average_string = f"{average_cal:.2f}"
            average = self.check_for_single_digit(average_string)
            print(average)
            return average
        except TypeError:
            print("TypeError: Non-numeric input provided for average calculation.")
            return None

    def split_number(self, serial_input):
        try:
            pattern = r"^\d{3}-\d{2}\.\d{2}-\d{2}\.\d{2}$"
            if not re.match(pattern, serial_input):
                print("Error: Invalid input format. Please provide input in the format 'XXX-YY.YY-ZZ.ZZ'.")
                return None
            else:
                serial_number = serial_input[:3]
                first_number = float(serial_input[4:9])
                second_number = float(serial_input[10:])
                average_string = self.get_average(first_number, second_number)
                if average_string is not None:
                    output = serial_number + '-' + average_string
                    print(output)
                    return output
                else:
                    print("An error occurred in calculating the average.")
                    return None
        except (ValueError, TypeError):
            print("Error: Invalid input format. Please provide input in the format 'XXX-YY.YY-ZZ.ZZ'.")
            return None

#SerialAverage().split_number('333-00.00-00.02')
SerialAverage().get_average(00.00,00.01)
