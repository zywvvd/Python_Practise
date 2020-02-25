from xml.dom import minidom

#1.创建DOM树对象
dom=minidom.Document()
# 2.创建根节点。每次都要用DOM对象来创建任何节点。
root_node=dom.createElement('root')
# 3.用DOM对象添加根节点
dom.appendChild(root_node)
# 用DOM对象创建元素子节点
book_node=dom.createElement('book')
# 用父节点对象添加元素子节点
root_node.appendChild(book_node)
# 设置该节点的属性
book_node.setAttribute('price','399')
name_node=dom.createElement('name')
book_node.appendChild(name_node)
# 也用DOM创建文本节点，把文本节点（文字内容）看成子节点
name_text=dom.createTextNode('C++ Primer 第1版')
# 用添加了文本的节点对象（看成文本节点的父节点）添加文本节点
name_node.appendChild(name_text)

print(dom.toxml()) #字符格式输出
print(dom.toprettyxml()) #美丽的输出


#增加要删除的节点
another_node=dom.createElement('delete')
another_node_child=dom.createElement('content')
another_node_child_text=dom.createTextNode('testing data')
another_node_child.appendChild(another_node_child_text)
another_node.appendChild(another_node_child)
root_node.appendChild(another_node)
print(dom.toprettyxml())


#删除上文增加的节点
children_Nodes=root_node.childNodes
for i in range(children_Nodes.length-1,-1,-1):
    if children_Nodes[i].tagName=='delete':
        children_Nodes.remove(children_Nodes[i]) #删除root中的文本节点

print(dom.toprettyxml())


#删除节点属性
book_node.setAttribute('price','199')
print(book_node.hasAttribute('price'))
print(book_node.getAttribute('price'))
book_node.removeAttribute('price')
print(book_node.hasAttribute('price'))


#修改节点内容
children_Nodes=root_node.childNodes
name_Append = ' (中文版)'
for item in children_Nodes:
    #print (item.toxml())
    tag_name='name'
    c_name = item.getElementsByTagName(tag_name)
    print(c_name[0].firstChild.data)
    c_name[0].firstChild.data+=name_Append
print(dom.toprettyxml())

#修改节点属性
book_node.setAttribute('price','199')
print(book_node.hasAttribute('price'))
print(book_node.getAttribute('price'))

book_node.setAttribute('price','399')
print(book_node.getAttribute('price'))

book_node.setAttribute('price2','599')
print(book_node.attributes.items())


#修改节点名称(可用、不安全)
name_node=dom.createElement('name')
name_node.nodeName='node name'
name_node.tagName='tag name'
root_node.appendChild(name_node)
print(dom.toxml())
print(name_node.nodeName)
print(name_node.localName)
#删掉刚刚增加的测试节点
children_Nodes=root_node.childNodes
children_Nodes.remove(children_Nodes[1])

#Python DOM 写入XML
with open('write_test.xml','w',encoding='UTF-8') as writer:
    dom.writexml(writer,indent='',addindent='    ',newl='\n',encoding='UTF-8')