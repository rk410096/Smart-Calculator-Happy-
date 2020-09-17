import sys
sys.path.append('/mymodule/')
import my_module
from my_module.maths import *
print(response[0])
print(response[1])
while True:
    print()
    text=input("Enter some text")
    for word in text.split(" "):
        if word.upper() in operations.keys():
            try:
                l=extract_num_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("something is wrong please")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
            sorry()
