import json
import os
def meaning(word:str,WordLanguage:str='eng',MeaningLanguage:str='eng')->dict:
    word = word.lower().strip(' ')
    path = os.getcwd() + f'/data/{word[0]+'.json'}' # data path
    dic = open(path)
    dic = json.load(dic)
    return dic.get(word,505)