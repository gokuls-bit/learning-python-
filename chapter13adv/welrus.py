# # using walrus 
# if (n:= len([1, 2, 3, 4, 5])) > 3:
#     print(f"List is long  ({n} elements, expected<= 3)")
#    # output: List is too long (5 elements, expected<= 3)

# # types
# from typing import List, Dict, Tuple, Union
# n : int = 5
# name: str = "harvinder"

# def sum(a: int, b: int) -> int:
#     return a + b

# #sum()

# match case 
# def http_status(status: int) -> str:
#     """Return a human-readable message for a given HTTP status code."""
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown Status"
            
# if __name__ == "__main__":
#     code = int(input("Enter HTTP status code: "))
#     print(http_status(code))
#
# try : 
#     a  = int(input("Enter a number: "))
#     print(a)

# except ValueError as v:
#     print(v)

# except Exception as e :
#     print(e)
# print("thankyou")

# a = int(input("Enter a number:"))
# b = int(input("Enter a  secondnumber:"))

# if(b== 0):
#     raise ZeroDivisionError("Division by zero is not allowed")
# else: 
#  print(f"the division a/b is {a/b}")
 # try else 
# try:
#     a = int(input("Enter a number: "))
    
# except Exception as e:
#     print(e)
# else:
#     print("inside else ")

# try-finally
try:
    a = int(input("Enter a number: "))
    
except Exception as e:
    print(e)
finally:
    print("inside finally ")