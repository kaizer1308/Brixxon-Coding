import os
os.system("cls")

# Accessing the List
MYLIST = ["Saudi", "UAE", "QATAR", "KUWAIT"]
print("Original List:", MYLIST)
print("Reverse List:", MYLIST[::-1])
print("length of List:", len(MYLIST))
MYLIST.append("OMAN")
print("After Appending OMAN:", MYLIST)
MYLIST.remove("QATAR")
print("After Removing QATAR:", MYLIST)
MYLIST.sort()
print("After Sorting:", MYLIST)