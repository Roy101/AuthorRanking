from xml.etree import ElementTree
#xml_iter = ElementTree.iterparse("F:\Thesis Work\example2\\test.xml" , events=('start','end'))
#for event, elem in xml_iter:
    #if event=='start':
        #print('<%s>' %elem.tag, end='')
        #text = elem.text.strip()
        #if text!='':
            #print(text, end='')
    #elif event == 'end':
            #print ('</%s>' %elem.tag)
mytree = ElementTree.parse(r"C:\Users\Asus\Desktop\\test.xml")
myroot=mytree.getroot()
#print(myroot.tag)
#for x in myroot[1]:
    #print(x.text)
i=0
listofAuthor=list()
dic=dict()
for x in myroot.findall("phdthesis"):
    author=x.find('author').text
    listofAuthor.append(author)
    title=x.find('title').text
    year=x.find('year').text
    print("Author :",author,"  Title :",title,"  Year :",year)
    i+=1
#print(listofAuthor)
#for names in listofAuthor:
    #dic[names]=dic.get(names,0)+1
#print(dic)
print(i)
#comment
