import re
s = raw_input("Enter the password ")
if len(s)>6 and len(s)<16:
    if bool(re.search('[a-z]',s)) and bool(re.search('[A-Z]',s)) and bool(re.search('[0-9]',s)) and bool(re.search('[$#@]',s)):
        print('Valid Password')
    else:
        print('Not Valid')
    
else:
    print('Not Valid')
