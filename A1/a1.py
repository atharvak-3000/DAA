class GFG:
    @staticmethod
    def find_first_zero(arr, size):
        index = 0
        while index < size:
            if arr[index] == 0:
                return index
            index += 1
        return -1

    @staticmethod
    def main(args):
        array = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
        length = len(array)
        first_zero_index = GFG.find_first_zero(array, length)
        if first_zero_index == -1:
            print("Count of zero is 0")
        else:
            print("Count of zero is ", end="")
            print(length - first_zero_index)

if __name__ == "__main__":
    GFG.main([])

