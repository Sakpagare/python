# removing all whitespace in a string

import re

string = "C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces,"",string)
print(result)
