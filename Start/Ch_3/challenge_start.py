# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions
#
import string
import pprint

#CADENA A PROCESAR
test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

# YOUR CODE HERE
#total de caracteres en el string
l = len(test_str)
#numero de caracteres
nums = len([c for c in test_str if c.isnumeric()])
#contar caracteres de puntuacion
punctchars = len([c for c in test_str if c in string.punctuation])
#contar los caracteres unicos
unique = "".join({c for c in test_str if c.isalpha()})

# print the data


str_data = {
    "Length":1,
    "Digits":nums,
    "Punctuation": punctchars,
    "Unique letters":unique,
    "Unique count": len(unique)    
}
pprint.pp(str_data)
