class Calculator:
    """
    This Class Will Do Simple Ar-thematic Operations,
    Like Calculator Does in Simple ways.
    """

    def add(self, x_number: int, y_number: int) -> float:
        """
        This Function can add two numbers
        :param x_number: 2
        :param y_number: 4
        :return: 6
        """
        return x_number + y_number

    def add_multiple(self, *numbers: int or float) -> int:
        """
        This Function will take any number of int values and return
        the added value of your numbers
        :param numbers: 10, 20, 30
        :return: 60

        Note: This Function cannot take user input as an argument and add rather than
                you have to insert value manually like add(2, 4, 6) and it will return
            --> 12
        """
        total = 0
        try:
            for number in numbers:
                total += number
        except Exception as error:
            print(error)
        else:
            return total

    def subtract(self, x_number: int, y_number: int) -> float:
        """
        This is Subtracting Function That Takes,
        :param x_number: 50
        :param y_number: 40
        :return: 10
        """
        return x_number - y_number

    def multiply(self, x_number: int, y_number: int) -> float:
        """
        This Function can Multiply two numbers
        :param x_number: 4
        :param y_number: 2
        :return: 8
        """
        return x_number * y_number

    def divide(self, x_number: int, y_number: int) -> float:
        """
        This Function can divide two numbers and return float value
        :param x_number: 4
        :param y_number: 2
        :return: 2.0
        Note: You cannot divide a number with 0.
        """
        try:
            division = x_number / y_number
        except Exception as error:
            print(f"[{error}]")
        else:
            return division

    def quotient(self, x_number: int, y_number: int) -> int:
        """
        This Function can return Quotient of the division
        :param x_number: 10
        :param y_number: 4
        :return: 2.0
        """
        return x_number // y_number

    def remainder(self, x_number: int, y_number: int) -> int:
        """
        This function can return Remainder of the division
        :param x_number: 10
        :param y_number: 4
        :return: 2.0
        """
        return x_number % y_number

    def square(self, x_number: int) -> int:
        """
        This Function can return square of the number
        :param x_number: 4
        :return: 16
        """
        return x_number ** 2

    def cube(self, x_number) -> int:
        """
        This Function can return cube of the number
        :param x_number: 4
        :return: 64
        """
        return x_number ** 3
