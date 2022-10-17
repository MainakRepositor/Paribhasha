import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import punkt
from gensim import corpora
from gensim import models 
import gensim
import pyLDAvis.gensim
import re
import streamlit as st
import pandas as pd
from pages.fetch import *
from textblob import TextBlob
import sys
from matplotlib import pyplot as plt

import spacy
from spacy import displacy
import en_core_web_sm
from spacy import load

def entity_analyzer(my_text):
	nlp = en_core_web_sm.load()

	docx = nlp(my_text)
	tokens = [token.text for token in docx]
	entities = [(entity.text, entity.label_)for entity in docx.ents]
	allData = ['"Token":{},\n"Entities":{}'.format(tokens, entities)]
	return allData

#Function for named entity recognition
def ner(my_text):
    nlp = en_core_web_sm.load()

    doc = nlp(my_text)
    html = displacy.render([doc], style="ent", page=False)
    #st.write(html, unsafe_allow_html=True)
    st.markdown(html, unsafe_allow_html=True)
    st.markdown(" <br> </br>", unsafe_allow_html= True)

    #displacy.serve(doc, style="ent")


def process_text(text):
	
   
    text = re.sub('[^A-Za-z]', ' ', text.lower())
    tokenized_text = word_tokenize(text)
    clean_text = [
        word for word in tokenized_text
        if word not in stopwords.words('english')
    ]
    #gensim.parsing.stem_text(word)
    
    #word list only
    return clean_text




def topic_mod(my_text , num_topics=10,num_words=5):
    
    nlp = en_core_web_sm.load()

    doc = nlp(my_text)
    
    
    text_data = [sent.string.strip() for sent in doc.sents] 
    #st.write(text_data)
    
    texts = [process_text(text) for text in text_data]
    #st.write(texts)
    dictionary = corpora.Dictionary(texts)
    
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    model = models.ldamodel.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10,random_state =2)
    topics = model.print_topics(num_words=num_words)
    for topic in topics:
        st.write(topic)
    
    
    #lda_display = pyLDAvis.gensim.prepare(model, corpus, dictionary, sort_topics=True)
    # st.pyplot(pyLDAvis.display(lda_display))
    #pyLDAvis.display(lda_display)
    #plt.show()

    

    




def main():
	# Title
	front_up()
	st.title('Named Entity Recognition and Topic Modelling ')

	if st.checkbox('Show Named Entities', key='ner'):
		st.subheader('Plot NER')
		boool, text = selection(key='ner')

		if st.button("Analyze", key='ner'):
			if boool == 0:
				message = text
				ner(message)
				#st.json(nlp_result)

			else:
				try:
					message = get_text(text)
					ner(message)
					#st.json(nlp_result)
				except BaseException as e:
					st.warning(e)

	if st.checkbox('Show top Topics of the Text', key='topics'):
		st.subheader('Top topics of your text')

		boool, text = selection(key='topics')
		num_topics=st.number_input('Number of Topics',key='topic',step=1,min_value=1,format = '%d')
		num_words=st.number_input('Number of Words per Topic' , key='words', format='%d', min_value=1,step=1)
		if st.button("Analyze", key='topcs'):
			if boool == 0:
				message = text
				#function here
				topic_mod(message,num_topics,num_words)
			else:
				try:
					message = get_text(text)
					#function here
					topic_mod(message,num_topics,num_words)
				except BaseException as e:
					st.warning(e)

	
