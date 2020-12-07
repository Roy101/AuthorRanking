from xml.dom import minidom
mytree=minidom.parse(r"E:\Thesis papers\Data\dblp.xml")
tagname=mytree.getElementsByTagName("author")
i=1
for x in tagname:
    print("Author :"+x.firstChild.data)
    i+=1
print(i)
