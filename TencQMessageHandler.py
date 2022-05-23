
from posixpath import basename
import jieba

with open("SaltyFishContainer.txt", mode="r", encoding="utf-8") as file:
    with open("1.txt", mode="w", encoding="utf-8") as out:
        with open("BannedWords.txt", mode="r", encoding="utf-8") as banned:
            bannedWorld = []
            for word in banned.readlines():
                bannedWorld.append(word.replace("\n", ""))
            index = 0
            for line in file.readlines():
                if(line == ""):
                    break
                if(line != "\n" and
                        line.startswith("202") == False and
                        line.startswith("\ufeff") == False and
                        line.startswith("http") == False and
                        line.startswith("@") == False):
                    finded = False
                    for word in bannedWorld:
                        if(line.find(word) != -1):
                            finded = True
                            break
                    if(finded == False):
                        segList = jieba.cut(line)
                        for seg in segList:
                            out.write(seg.replace("\n", " "))

