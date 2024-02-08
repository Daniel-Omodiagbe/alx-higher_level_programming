#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists"""
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by zero")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            if result != 0:
                new_list.append(result)
            else:
                new_list.append(result)
    return new_list
