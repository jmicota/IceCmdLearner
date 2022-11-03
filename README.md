# IceCmdLearner

This project has been created as final project fro Natural Language Processing course at Reykjavík University in October 2022.

It provides simple cmd interface for users to learn Icelandic. User chooses input language:
- English input gets translated and each word of Icelandic output is further analysed.
- Icelandic input sentence is corrected, token level mistakes are annotaed in English.

Translator source can be chosen from two options:
- OpenAI
- Helsinki-NLP

Using OpenAI is recommended, as output of Helsinki-NLP translations often fails to translate single tokens or produces sentence structure that cannot be parsed by Greynir.

Translation can be easily extended for multiple languages as both OpenAI and Helsinki-NLP are available in hundreds of languages. However correction and lemmatization modules have to be written manually for ech language.

The goal of this project is to provide user with quick and easy to read feedback. Combined with **common sense** and **tolerance** for errors of currently available quality of tools it is possible to extract knowledge useful in simple day to day language learning!

Modules:
- **correction.py**         
  uses Greynir to correct icelandic sentence and tokens in icelandic sentence
- **lemmatization.py**      
  uses Greynir and nltk to analyse input icelandic sentence (split to tokens and extract lemmas)
- **translator_helsinki.py**         
  uses pretrained Helsinki-NLP models to translate sentences
- **translator_openai.py**         
  uses pretrained OpenAI models to translate sentences
- **ice_cmd_learner.py**    
  combines all modules into user pipeline

Authors:
- Jónína Jófríður Jóhannesdóttir
- Justyna Micota
- Lára Margrét Hólmfríðardóttir

