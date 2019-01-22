with open('book.json','r', encoding='cp949') as tag:
    text = tag.read()
    text.encode('utf-8-sig')

with open('book.json','w', encoding='utf-8-sig') as tag:
    tag.write(text)
   
