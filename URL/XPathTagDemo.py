from lxml import etree

f = open('XPathTagDemo.html', 'r+', encoding='utf-8')
html_str = f.read()

# 通过etree.HTML函数将我们的HTML代码解析成支持xpath的数据类型
html = etree.HTML(html_str)

# 获得title内的网页名
print(html.xpath('head/title/text()'))
# 获得span内数据
print(html.xpath('body/div/span/text()'))
