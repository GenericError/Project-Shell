""" Prints the list of arguments given by terminal """
# NOTE: This script is for testing purposes only

import sys
sys.argv.pop(0) # Removes the script name
print(sys.argv)
raw_sys_argv = input("Input sys.argv equivalent > ")
for i in raw_sys_argv.split(' '):
    print(i)

print("Now fixing the list.....")

ESCAPE_TEXT = "$ESCAPE$"
raw_sys_argv = raw_sys_argv.replace("\\"+" ", ESCAPE_TEXT)
fixed_list = raw_sys_argv.split(" ")
incrementer = 0
while incrementer < len(fixed_list):
    fixed_list[incrementer] = str(fixed_list[incrementer]).replace(ESCAPE_TEXT, " ")
    incrementer += 1
if fixed_list[0] == "python":
    fixed_list.pop(0)
elif fixed_list[0] == "python3":
    fixed_list.pop(0)
fixed_list.pop(0) # Remove the script name
print(fixed_list)

# OLD CODE THAT DIDN'T WORK
# fixed_list = raw_sys_argv.split(' ')
# current_location = 0
#
# while current_location <= len(fixed_list):
#     try:
#         if fixed_list[current_location].endswith('\\ '):
#             fixed_list[current_location] = fixed_list[current_location].strip('\\')
#             fixed_list[current_location] += [current_location+1]
#             current_location += 1
#         else:
#             current_location += 1
#     except:
#         break
# print(fixed_list)

if fixed_list == sys.argv:
    print("Success!")
