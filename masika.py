Thislist=(["jereh","mark","silver","marcus"])
print(Thislist[1:2])

Thislist=["jereh","mark","marcus"]
Thislist[1]="isaac"
print(Thislist)

Thislist=["mark","marcus","jereh"]
Thislist.append("silver")
print(Thislist)

Thislist=["mark","isaac","jereh","silver"]
Thislist.remove("mark")
print(Thislist)

Thislist=["mark","jere","silver"]
for x in Thislist:
  print(x)

students=["mark","isaac","marcus","jereh"]
newlist=[]
for x in students:
  if "a" in x:
   newlist.append(x)
print(newlist)
Thislist=["mark","isaac","jere","silver"]
Thislist.sort()
print(Thislist)

Thislist=["marc","jere","isaac","silver"]
Thislist.copy()
print(Thislist)

List1=["jere","dan","isaac"]
List2=[1,2,3]
List1.extend(List2)
print(List1)





















