class RangeFunctions:
    arr = ['9', '5', '1', '2', '3', '4', '0', '-1']

    def element_at(self, arr, index):
        try:
            print(f"Element at index {index}: {arr[index]}")
            return arr[index]
        except IndexError:
            print(f"IndexError: Index {index} is out of range.")
            return None

    def inclusive_range(self, arr, start_pos, end_pos):
        try:
            if start_pos < 0 or end_pos >= len(arr):
                raise IndexError("Start or end position is out of range.")
            print(f"Inclusive range from {start_pos} to {end_pos}: {arr[start_pos:end_pos+1]}")
            return arr[start_pos:end_pos+1]
        except IndexError as e:
            print(f"IndexError: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
     
    def non_inclusive_range(self, arr, start_pos, end_pos):
        try:
            if start_pos < 0 or end_pos > len(arr):
                raise IndexError("Start or end position is out of range.")
            print(f"Non-inclusive range from {start_pos} to {end_pos}: {arr[start_pos:end_pos]}")
            return arr[start_pos:end_pos]
        except IndexError as e:
            print(f"IndexError: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def start_and_length(self, arr, start_pos, length):
        try:
            if start_pos < 0 or start_pos + length > len(arr):
                raise IndexError("Start position and length are out of range.")
            print(f"Start and length from {start_pos} with length {length}: {arr[start_pos:start_pos+length]}")
            return arr[start_pos:start_pos+length]
        except IndexError as e:
            print(f"IndexError: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

if __name__ == "__main__":
    obj1 = RangeFunctions()

    try:
        index = int(input("Enter index for element at: "))
        obj1.element_at(obj1.arr, index)
    except ValueError:
        print("Invalid input: Index should be an integer.")

    try:
        start_pos = int(input("Enter start position: "))
        end_pos = int(input("Enter end position: "))
        obj1.inclusive_range(obj1.arr, start_pos, end_pos)
        obj1.non_inclusive_range(obj1.arr, start_pos, end_pos)
    except ValueError:
        print("Invalid input: Start and end positions should be integers.")

    try:
        length_of_array = int(input("Enter length of array: "))
        obj1.start_and_length(obj1.arr, start_pos, length_of_array)
    except ValueError:
        print("Invalid input: Length should be an integer.")
