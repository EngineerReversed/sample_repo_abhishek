import re

def validate(s):
    if len(s)>=6 and len(s)<=12:
        if bool(re.search('[a-z]',s)) and bool(re.search('[A-Z]',s)) and bool(re.search('[0-9]',s)) and bool(re.search('[$#@]',s)):
            print('Valid Password')
        else:
            print('Not Valid')
    
    else:
        print('Not Valid')
        
def main():
    s1 = raw_input("Enter the password ")
    obj = validate(s1)



main()
