import wordcloud
import matplotlib
w=wordcloud.WordCloud()
w.generate("java python java java java python java")
w.to_file("pywordcloud.png")
