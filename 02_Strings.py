"""
01: Strings and Bytes
02: Template Strings
"""

from string import Template

def template_strings():
    # Usual string formatting with format()
    str1 = "This Repository {0} Is Created and Maintained by {1}".format("Python Returns", "Prasun Chakraborty")

    print(str1)
    
    # create a template with placeholders
    templ = Template("This Repository ${title} Is Created and Maintained by ${author}")
    
    # use the substitute method with keyword arguments
    str2 = templ.substitute(title="Python Returns", author="Prasun Chakraborty")
    print(str2)
    
    # use the substitute method with a dictionary
    data = { 
        "author": "Prasun Chakraborty",
        "title": "Python Returns"
    }
    str3 = templ.substitute(data)    
    print(str3)


def strings_and_bytes():
    """strings and bytes are not directly interchangeable
    strings contain unicode, bytes are raw 8-bit values"""

    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    s = "This is a string"
    print(s)
    
    # Try combining them. This will cause an error:
    # print(s+b)
    
    # Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    s2 = b.decode('utf-8')
    print(s+s2)
    
    b2 = s.encode('utf-8')
    print(b+b2)
    
    # encode the string as UTF-32
    b3 = s.encode('utf-32')
    print(b3)
    
if __name__ == "__main__":
    strings_and_bytes()
    template_strings()
