# NLPJenny

**Natural Language Processing on the go...**

#### Hosted on Heroku: [NLPJenny](https://nlpjenny.herokuapp.com/)

- Website will launch very slow as in free tier heroku services the server goes into hibernation i.e. everytime a user clicks the website it lauches itself from scratch and remains active for next few minutes. Also there is a bug in integration between heroku and spacy model, while deploying, which requires to download spacy language model everytime the website launches itself.May be down by now!


#### Youtube Video: [Streamlit NLPJenny](https://youtu.be/XGpYs5mbgQ8)


![demo image](https://github.com/aryanc55/NLPJenny/blob/master/demo.png?raw=true)



## Dependencies
- Python3
- Streamlit
- Othes libraries (Everything in Pipfile and Requirement.txt)

## How to RUN:
- Run 
   > git clone https://github.com/aryanc55/NLPJenny.git
   
   > cd NLPJenny
   
   > pip install -r requirement.txt
   
   > streamlit run NLPJenny.py

## Deploy on Heroku
- Make account on heroku and install heroku-cli
   
   > sudo snap install --classic heroku
   
- RUN
   
   > cd /to_dir
   
   > heroku login
   
   > heroku create your_app_name
   
   > git push heroku master
   

## License:
MIT License
Copyright (c) 2020 Aryan Chaudhary
[MIT](LICENSE)

**Show some :heart: by leaving a :star: at this page!**  </br>
**Follow Me On [Medium](https://medium.com/@aryanc55)** </br>
**Follow Me On [Kaggle](https://www.kaggle.com/aryanc55)** </br>
 
