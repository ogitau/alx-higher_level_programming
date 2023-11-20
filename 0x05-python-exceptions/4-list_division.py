#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division = []

    for i in range(0, list_length):
        try:
            division.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            division.append(0)
        except ZeroDivisionError:
            print("division by zero")
            division.append(0)
        except IndexError:
            print("out of range")
            division.append(0)
        finally:
            pass
    return division
