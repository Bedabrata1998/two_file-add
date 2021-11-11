total={}
def insert(items):
    if items in total:
        total[items]+=1
    else:
            total[items]=1
insert('Apple')
insert('Apple')
insert('Apple')
print(len(total))
