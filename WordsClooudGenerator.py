from wordcloud import WordCloud

with open("1.txt", mode="r", encoding="UTF-8") as file:
    c = WordCloud(font_path="./SIMYOU.TTF", width=1920, height=1080)
    seg = file.read()
    c.generate(seg)
    c.to_file("1.png")
