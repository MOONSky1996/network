# coding = utf-8
import csv
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
#input = open('d:/DataProgress/new_carDataset_mentionCar_clean_8.csv', 'r')
input = open('d:/DataProgress/compare_2.csv', 'r')
G = nx.DiGraph()
list = []
reader = csv.reader(input)
for row in csv.reader(input):
    G.add_edge(row[0], row[1])
 #   list.append((row[0]))
input.close()
#nsize=[1600,800,800,600,400,200,100]
#print(G.size())
#nx.draw_networkx(G)
#nx.draw_spring(G,with_labels = True)
#nx.draw_circular(G,with_labels = True)
#D:\anaconda\Lib\site-packages\matplotlib\mpl-data\fonts\ttf 字体路径
#######
nx.draw(G,  with_labels=True, node_size=2800, bold = True)
nx.draw(G,  with_labels=True, node_size=2800, bold = True)
plt.savefig('d:/plot123_8.png', dpi=300)
plt.show()