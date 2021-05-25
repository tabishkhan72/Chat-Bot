Trained with Gunthercox dataset on word level using GloVe encoding
Trained with Gunthercox dataset on word level using One-hot encoding
Trained with Gunthercox dataset on character level
Trained with Cornell dataset on word level using GloVe encoding
Trained with Cornell dataset on word level using One-hot encoding
Trained with Cornell dataset on character level
Code:
Code for the chatbot is divided in 2 parts:
Machine Learning part (using keras)
Web deployment part (using Flask)
Machine Learning part ( chatbot_train):
First subdirectory in this folder is data which have both the datasets.
Second subdirectory is models, which have saved ml models for chatbot trained on both the dataset. The chatbot is built based on seq2seq models, and can infer based on either character-level or word-level. The seq2seq model is implemented using LSTM encoder-decoder on Keras. During runtime, these models are used to reply.
And the last subdirectory is very_large_data which would have gloVe file(if your system doesn’t have gloVe file then it will be downloaded automatically when running the chatbot).


