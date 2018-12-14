'''This function returns the result of the math operation(using mathjs API)'''
from urllib.parse import quote
import requests


def calculate(expr):
    return requests.get('http://api.mathjs.org/v4/?expr=' +
                        quote(expr, safe='')).text

