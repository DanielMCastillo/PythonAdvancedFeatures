# Example file for Advanced Python: Language Features by Joe Marini
# demonstrate template string functions


# Usual string formatting with f-strings
from pipes import Template


str1 = "Advanced Python: Language Features"
str2 = "Joe Marini"
outputstr = f"You're watching {str1} by {str2}"
print(outputstr)

# TODO: create a template with placeholders
templ = Template("Your'e wathcing ${title} by ${author}")
# TODO: use the substitute method with keyword arguments
str3 = templ.substitute(title="Advanced Python: Language Features",
                        author = "Daniel Castillo")
print(str3)
# TODO: use the substitute method with a dictionary
data = {
    "author": "Daniel Castillo",
    "title": "Advanced Python: Language Features",
    
}

str4 = templ.substitute(data)
print(str4)