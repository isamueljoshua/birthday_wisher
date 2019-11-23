import sys

try:
    arg_ls = [arg for arg in sys.argv]
    to_name = " ".join(arg_ls[1:])

except Exception as e:
    to_name = 'TO YOU'
    
print("\n")
print("\t\t****************************************************")
print("\t\t\t !!! HAPPY BIRTHDAY " + to_name + " !!!")
print("\t\t****************************************************")
