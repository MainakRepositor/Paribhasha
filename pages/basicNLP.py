import streamlit as st
import pandas as pd 
from pages.fetch import *

from textblob import TextBlob
import sys
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import spacy

import en_core_web_sm
from spacy import load



# Function to Analyse Tokens and Lemma
@st.cache
def text_analyzer(my_text):
	nlp = en_core_web_sm.load()

	docx = nlp(my_text)
	
	allData = [('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_))for token in docx ]
	return allData

# FUnction for pos tagging
@st.cache
def pos_tagging(my_text):
	data ={}
	nlp = en_core_web_sm.load()

	doc = nlp(my_text)
	
	c_tokens = [token.text for token in doc]
	c_pos = [token.pos_ for token in doc]

	new_df = pd.DataFrame(zip(c_tokens,c_pos),
	                      columns=['Tokens', 'POS'])

	return new_df

#Function for sentiment analysis

def sent_analysis(my_text):
	testimonial = TextBlob(my_text)
	return testimonial.sentiment.polarity, testimonial.sentiment.subjectivity

#Function for world cloud

def word_cloud(my_text):
	wordcloud = WordCloud(width=1200, height=600,background_color='white',random_state=42, stopwords=set(STOPWORDS)).generate(my_text)
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	st.pyplot()



def main():
	# Title
	front_up()
	st.title('Basic NLP ')

	if st.checkbox('Show Tokens and Lemma', key ='token'):
		st.subheader('Tokenize your text')
		boool, text = selection(key='token')

		if st.button("Analyze", key='token'):
			if boool == 0:
				message = text
				nlp_result = text_analyzer(message)
				st.json(nlp_result) 
			else:
				try:
					message = get_text(text)
					nlp_result = text_analyzer(message)
					st.json(nlp_result)
				except BaseException as e:
					st.warning(e)

			



	if st.checkbox('Show Parts of Speech', key='pos'):
		st.subheader('POS tagging on your text')

		boool,text = selection(key= 'pos')
		

		if st.button("Analyze", key='pos'):
			if boool == 0:
				message = text
				nlp_result = pos_tagging(message)
				st.dataframe(nlp_result)
				#function here
			else:
				try:
					message = get_text(text)
					nlp_result = pos_tagging(message)
					st.dataframe(nlp_result)
					#function here
				except BaseException as e:
					st.warning(e)
					

	if st.checkbox('Show Sentiment of the sentence ', key='sent'):
		st.subheader('Subjectivity and Polarity on the text')

		boool, text = selection(key='sent')

		if st.button("Analyze", key='sent'):
			if boool == 0:
				message = text
				polarity, subjectivity = sent_analysis(message)
				st.info("Polarity: {} , Subjectivity: {} ".format(polarity, subjectivity))
				
				#function here
			else:
				try:
					message = get_text(text)
					polarity, subjectivity = sent_analysis(message)
					st.info("Polarity: {} , Subjectivity: {} ".f(polarity,subjectivity) )
					#function here
				except BaseException as e:
					st.warning(e)


	if st.checkbox('Show Word Cloud', key='cloud'):
		st.subheader('Plot WordCloud on the text')

		boool, text = selection(key='cloud')

		if st.button("Analyze", key='cloud'):
			if boool == 0:
					message = text
					
					#function here
					word_cloud(message)
			else:
					try:
						message = get_text(text)
						
						#function here
						word_cloud(message)
					except BaseException as e:
						st.warning(e)



