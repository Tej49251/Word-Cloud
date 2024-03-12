import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


text = "protein calcium minerals magnsium Healthy life happy life strong  import library help world bird water"

cloud = WordCloud(background_color="white").generate(text)

plt.imshow(cloud)
plt.axis('off')
plt.show()