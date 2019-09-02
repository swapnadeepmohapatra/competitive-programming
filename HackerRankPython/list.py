# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer a at position i .
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

n = input()
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd != "print":
        cmd += "(" + ",".join(args) + ")"
        eval("l."+cmd)
    else:
        print(l)


# if command=="insert":
#     L.insert(i,e)
# elif command=="remove":
#     L.remove(e)
# elif command=="append":
#      L.append(e)
# elif command=="sort":
#      L.sort()
# elif command=="pop":
#      L.pop()
# elif command=="reverse":
#      L.reverse()
# elif command=="print":
#      print(L)
