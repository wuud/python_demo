from lxml import etree
html_str="""
<body>
<div class="ui container">

        <table class="ui striped  table">
            <tr>
                <th>姓名</th>
                <th>性别</th>
                <th>邮箱</th>
                <th>电话</th>
            </tr>
            <tr>
                <td><a href="zhangwei">张伟</a></td>
                <td>男</td>
                <td>zhangwei@haoren.com</td>
                <td>12138-111</td>
            </tr>
            <tr>
                <td><a href="yifei">一菲</a></td>
                <td>女</td>
                <td>yifei@haoren.com</td>
                <td>12138-112</td>
            </tr>
            <tr>
                <td><a href="xiaoxian">小贤</a></td>
                <td>男</td>
                <td>xiaoxian@haoren.com</td>
                <td>12138-113</td>
            </tr>
            <tr>
                <td><a href="meijia">美嘉</a></td>
                <td>女</td>
                <td>meijia@haoren.com</td>
                <td>12138-114</td>
            </tr>
            <tr>
                <td><a href="xiaobu">小布</a></td>
                <td>男</td>
                <td>xiaobu@hundan.com</td>
                <td>12138-115</td>
            </tr>

        </table>
</div>
</body>
"""

html=etree.HTML(html_str)
#获得table的表头
print(html.xpath('.//table/tr[1]/th/text()'))
#获得所有电话
print(html.xpath('.//table/tr/td[4]/text()'))
#获得所有性别为男的姓名,使用了..来回到上一级
print(html.xpath('.//table/tr/td[text()="男"]/../td[1]/a/text()'))
#获得所有以@haoren结尾的邮箱，使用了包含关系
print(html.xpath('.//table/tr/td[contains(text(),"@haoren")]/text()'))
#获得所有以@haoren结尾的邮箱的用户姓名
print(html.xpath('.//table/tr/td[contains(text(),"@haoren")]/../td[1]/a/text()'))
# print(html.xpath(''))