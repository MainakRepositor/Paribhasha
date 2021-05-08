"""Paribhasha : A complete NLP App"""
import streamlit as st


import pages.home
import pages.basicNLP
#import pages.captionGenerator
import pages.nertm
import pages.machineTranlation
import pages.textSummarization


PAGES = {
    "Home": pages.home,
    "Basic NLP": pages.basicNLP,
    "NER and Topic Modelling": pages.nertm,
    "Text Summarization": pages.textSummarization,
    "Machine Translation": pages.machineTranlation
    #"Caption Generator": pages.captionGenerator
}


def main():
    
    st.sidebar.title("PARIBHASHA")
    st.sidebar.text("A complete Natutal Language Processing App")
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(PAGES.keys()))

    #PAGES[page].main()


    with st.spinner(f"Loading {page} ..."):
        PAGES[page].main()

        
    
    st.sidebar.title("About App")
    
    st.sidebar.info(
        """
        This App uses State of the Art free tier API's from different paltforms
        like IBM,Google Cloud and libraries like Spacy,Genism, NLTK and Textblob etc. 
        It uses Streamlit for implemention of beatiful and easy web app.
        """
    )
    
    
    st.sidebar.title("Contact Developer")
    st.sidebar.info(
        """
        This app is develop by Mainak. You can contact me at
        [Mainak Chaudhuri](https://mainakfolio.github.io).
"""
    )


    
    
    st.sidebar.markdown("""  [Github](https://github.com/MainakRepositor)""") #change all thses three to  to iamge
    st.sidebar.markdown("""  [Linkedin](https://linkedin.com/in/mainak-chaudhuri-127898176)""")
    st.sidebar.markdown("""  [HackerRank](https://www.hackerrank.com/sultankhilji001?hr_r=1)""")



    
   


if __name__ == "__main__":
    main()
