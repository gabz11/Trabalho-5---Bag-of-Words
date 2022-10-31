# Gabriel Antonio Gomes de Farias
'''
ENUNCIADO 
Sua tarefa será  gerar a matriz termo documento, dos documentos recuperados da internet e 
imprimir esta matriz na tela. Para tanto: 
a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores, 
onde cada item será uma das palavras da sentença. 
b) Todos  os  vetores  devem  ser  unidos  em  um  corpus  único  formando  uma  lista  de  vetores, 
onde cada item será um lexema.  
c) Este único corpus será usado para gerar o vocabulário. 
d) O  resultado  esperado  será  uma  matriz  termo  documento  criada  a  partir  da  aplicação  da 
técnica bag of Words em todo o corpus.  
'''
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import spacy
import re

'''
OBSERVAÇÃO: A memoria da collab não processa toda a matriz devido as limitações do ambiente causada pela configuração da "--NotebookApp.iopub_data_rate_limit".
'''


nlp = spacy.load("en_core_web_sm")

# 5 sites em ingles p/processar
url1 = 'https://en.wikipedia.org/wiki/Natural_language_processing'
url2 = 'https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html'
url3 = 'https://monkeylearn.com/natural-language-processing/'
url4 = 'https://appen.com/blog/natural-language-processing/'
url5 = 'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/'

def separaTexto(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def obtemTexto(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(separaTexto, texts)
    return u" ".join(t.strip() for t in visible_texts)

corpus = []

html = urllib.request.urlopen(url1).read()
page = nlp(obtemTexto(html))
for sentence in page.sents:
    corpus.append(sentence.text)

html2 = urllib.request.urlopen(url2).read()
page = nlp(obtemTexto(html2))
for sentence in page.sents:
    corpus.append(sentence.text)

html3 = urllib.request.urlopen(url3).read()
page = nlp(obtemTexto(html3))
for sentence in page.sents:
    corpus.append(sentence.text)

html4 = urllib.request.urlopen(url4).read()
page = nlp(obtemTexto(html4))
for sentence in page.sents:
    corpus.append(sentence.text)

html5 = urllib.request.urlopen(url5).read()
page = nlp(obtemTexto(html5))
for sentence in page.sents:
    corpus.append(sentence.text)


def constroiVocabulario(corpus):
    vocabulario = set()

    for sentenca in corpus:
        for palavra in sentenca.split():
            vocabulario.add(palavra)

    return sorted(vocabulario)


def criarMatriz(corpus):
     vocabulario = constroiVocabulario(corpus)
     bagOfWords = []


     for sentenca in corpus:
         vetor = [0] * len(vocabulario)
         for palavra in sentenca.split():
             vetor[vocabulario.index(palavra)] += 1
         bagOfWords.append(vetor)

     return bagOfWords


vocabulario = constroiVocabulario(corpus)
print(vocabulario)

matriz = criarMatriz(corpus)

for linha in matriz:
    print(linha)
