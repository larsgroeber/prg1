"""
Exercise 10.1 and 10.2.
"""

class BinarySearch:
    """
    Implements methods for a binary search algorithm.
    """

    def __init__(self):
        self.numbers = []
        self.to_search = None

    def input(self):
        """
        Captures user input and sets properties 'numbers' and 'to_search'.
        """
        min_numbers = 20
        numbers = input(
            f"Please enter at least {min_numbers} integers space-separated.\n>>> ")
        number_split: [str] = numbers.split(" ")
        if len(number_split) < 20:
            print(f"Please enter at least {min_numbers} integers.")
            return self.input()
        if any(map(lambda n: not n.isdigit(), number_split)):
            print("Please enter only integers.")
            return self.input()
        self.numbers = sorted(map(int, number_split))

        to_search = input(f"Please enter the number to search.\n>>> ")
        if not to_search.isdigit():
            print(f"Please enter an integer.")
            return self.input()
        self.to_search = int(to_search)

    def search(self):
        """
        Does an iteratively binary search and returns the result.
        """
        search_list = self.numbers
        while len(search_list) > 1:
            middle_index = int(len(search_list) / 2)
            middle_element = search_list[middle_index]
            if middle_element == self.to_search:
                print(middle_element, '==', self.to_search)
                return True
            if middle_element > self.to_search:
                print(middle_element, '>', self.to_search)
                search_list = search_list[:middle_index]
            if middle_element < self.to_search:
                print(middle_element, '<', self.to_search)
                search_list = search_list[middle_index:]

        print(search_list, '==', [self.to_search])
        return search_list == [self.to_search]

    def search_recursive(self, search_list):
        """
        Does a binary search recursively and returns the result.
        Transformation steps:
         - add a 'search_list' parameter to pass the list to be searched to the
           next function call
         - remove the 'while' loop and replace it with an if statement
           'len(search_list) <= 1' at the start to end the recursion here
         - add the recursive call to the end of the function
        """
        if len(search_list) <= 1:
            print(search_list, '==', [self.to_search])
            return search_list == [self.to_search]
        middle_index = int(len(search_list) / 2)
        middle_element = search_list[middle_index]
        if middle_element == self.to_search:
            print(middle_element, '==', self.to_search)
            return True
        if middle_element > self.to_search:
            print(middle_element, '>', self.to_search)
            search_list = search_list[:middle_index]
        if middle_element < self.to_search:
            print(middle_element, '<', self.to_search)
            search_list = search_list[middle_index:]
        
        return self.search_recursive(search_list)

if __name__ == "__main__":
    b = BinarySearch()
    b.input()
    print()
    print("Iterative binary search:")
    print("Result:", b.search())
    print()
    print("Recursive binary search:")
    print("Result:", b.search_recursive(b.numbers))
