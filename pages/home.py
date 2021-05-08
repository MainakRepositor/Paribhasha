import streamlit as st
from pages.fetch import*

def main():
	front_up()
	
	st.markdown("""
			
			 This is a complete Natural Language Processing(NLP) Web Application useful for performing Language Processing tasks. The app title "Paribhasha" which means to assign a terminology to a sentiment.  
			""")
	### features

	st.header('Features')

	st.markdown("""
			#### Basic NLP Tasks:
			+ App covers the most basic NLP task of tokenisation, parts of speech tagging.
				You can paste the desired content or may directly pass the url for the text.
			#### Named Entity Recognition and Topic Modelling:
			+ Named Entites like organistion person etc are recognised and top topics from the corpus
				are found based on LDA modelling.
					
			#### Text Summarisation:
			+ It summarizes the given text into few lines. One can copy paste the article or may direclty pass the URL. It has options to use Gensim, Sumy analysers also.
			""")
 	
		 
		
