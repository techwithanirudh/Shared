# import nltk

# def __ent__(msg, ignore_words=['how']):
#     msg = msg.title()
#     ents = []

#     for word in ignore_words:
#         msg = msg.replace(word.title(), '')

#     for sent in nltk.sent_tokenize(msg):
#         for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#             if hasattr(chunk, 'label'):
#                 ent = chunk.label(), ' '.join(c[0] for c in chunk)
#                 ent = [ent]
#                 for item in ent:
#                     ent = item[0] + ' ' + item[1]
#                 ents.append(ent)

#     return ents

# x = """Allegra (fexofenadine hydrochloride) is an antihistamine used to 
#      treat allergic symptoms of seasonal allergic rhinitis (sneezing, 
#      runny nose, itchy or watery eyes), and urticaria (hives). Allegra is 
#      available as a generic drug termed fexofenadine hydrochloride. 
#      Allegra is used in adults and children (2 years and older for 
#      allergies, 6 months and older for hives) for the control and 
#      reduction of the above symptoms. Some common side effects of Allegra
#      include GI symptoms of nausea or diarrhea, muscle or back discomfort
#      or pain, sleepiness, and menstrual cramps."""
# print(__ent__(x))

# from nltk import ne_chunk, pos_tag, word_tokenize
# from nltk.tree import Tree

# def get_continuous_chunks(text):
#     chunked = ne_chunk(pos_tag(word_tokenize(text)))
#     continuous_chunk = []
#     current_chunk = []

#     for chunk in chunked:
#             if type(chunk) == Tree:
#                 current_chunk.append(' '.join([token for token, pos in chunk.leaves()]))

#             if current_chunk:
#                 named_entity = ' '.join(current_chunk)

#                 if named_entity not in continuous_chunk:
#                     continuous_chunk.append(named_entity)
#                     current_chunk = []
#             else:
#                 continue

#     return continuous_chunk

# # my_ent = 'washington United States'
# # print(get_continuous_chunks(my_ent))

# import spacy

# nlp = spacy.load('en_core_web_sm')
# text = input()
# doc = nlp(text)
# words = []
# for ent in doc.ents:
#     words.append(str(ent))
# print(words)

# import nltk
# from nltk.corpus import state_union
# from nltk.tokenize import PunktSentenceTokenizer

# train_text = state_union.raw("2005-GWBush.txt")
# sample_text = state_union.raw("2006-GWBush.txt")

# print(sample_text, type(sample_text))
# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# tokenized = custom_sent_tokenizer.tokenize(sample_text)

# def process_content():
#     try:
#         for i in tokenized[5:]:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#             namedEnt = nltk.ne_chunk(tagged, binary=True)
#             namedEnt.draw()
#     except Exception as e:
#         print(str(e))

# process_content()
import spacy 
  
nlp = spacy.load('en_core_web_sm') 
  
data = "I like to |['GPE']| ahhahahaha |['GPE']|"
sentence = "I like to India best is the word"
index = 0
ents = []
for word in data.split(' '):
     index += 1
     try:
          word.split('|[\'')[1]
          word.split('\']|')[0]
          ents.append(index - 1)
     except:
          pass

for index in range(len(ents)):
     word = sentence.split(' ')[ents[index]]
     doc = nlp(word) 

     for ent in doc.ents: 
          ent = data.split('|[\'')[1]
          ent = ent.split('\']|')[0]
          label = ent.label_
          text = ent.text
          if label == ent:
               print(label, ':', text)