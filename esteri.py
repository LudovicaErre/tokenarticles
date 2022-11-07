from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#est2020
file_content = open("/Users/Ludovica/Desktop/Università/Materie unibo/DTIH/Project/esteritexts/esteri2020.txt").read()
All_punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for elements in file_content:
  if elements in All_punct:
    file_content = file_content.replace(elements, "")

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(file_content)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
print(filtered_sentence)

#est2021
file_contentwo = open("/Users/Ludovica/Desktop/Università/Materie unibo/DTIH/Project/esteritexts/esteri2021.txt").read()
All_punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for elements in file_content:
  if elements in All_punct:
    file_content = file_content.replace(elements, "")

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(file_contentwo)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
print(filtered_sentence)

#est2022
file_contenthree = open("/Users/Ludovica/Desktop/Università/Materie unibo/DTIH/Project/esteritexts/esteri2022.txt").read()
All_punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for elements in file_content:
  if elements in All_punct:
    file_content = file_content.replace(elements, "")

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(file_content)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
print(filtered_sentence)
