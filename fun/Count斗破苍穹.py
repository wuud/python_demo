import wordcloud
import matplotlib.pyplot as plt
import jieba

f=open(r'斗破苍穹.txt','r',encoding='utf-8')
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
background_img=plt.imread('background.jpg')
w=wordcloud.WordCloud(font_path='msyh.ttc',width=1000,height=700, mask=background_img,background_color='white')
w.generate(txt)
# img_colors = wordcloud.ImageColorGenerator(background_img)
# w.recolor(color_func=img_colors)
w.to_file('斗破苍穹.png')