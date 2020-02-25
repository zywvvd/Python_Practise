
#加载DOM minidom模块
from xml.dom.minidom import parse
#解析XML文件
contents=parse('test.xml')
root=contents.documentElement

print(root.toxml())


#获取节点名称
print(root.nodeName)
print(root.tagName)


#获取子节点
children_Nodes=root.childNodes
print(f'子节点个数：{children_Nodes.length}')

for item in children_Nodes:
    print (item.toxml())


#获取节点属性
print(root.attributes.items())
atr_root=root.attributes['type']
print(atr_root.name)
print(atr_root.value)

#获取指定名称的节点
books=root.getElementsByTagName('book')

for book in books:
    print (book.nodeName)


#判断是否包含属性值
print(books[0].hasAttribute('nnn'))
print(books[0].hasAttribute('category'))


#获取节点指定属性的属性值
print(books[0].getAttribute('category'))
print(books[1].getAttribute('category'))


#获取节点文本值
node=books[0]
author=node.getElementsByTagName('author')
print(author[0].firstChild.data)


#判断是否有子节点
print(root.hasChildNodes())
print(author[0].hasChildNodes())
print(author[0].firstChild.hasChildNodes())