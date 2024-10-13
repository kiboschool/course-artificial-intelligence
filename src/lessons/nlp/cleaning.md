# Cleaning
Before we can start building NLP models or executing NLP tasks, we need to clean the text. This is important because it ensures that the text is consistent and that the model can learn from it effectively. 

The list of cleaning approaches is long and depends on the specific task and the data. Some typical cleaning approaches include removing punctuation, converting text to lowercase, removing stop words, removing special characters, and many more. Most of these cleaning approaches can be implemented using regular expressions and basic Python's string methods. However, some cleaning tasks may require more complex methods. 

Let's explore some common cleaning approaches further.

## Removing Stop Words
To remove stop words, we need to first download the list of stop words from the NLTK library. Then, we can remove the stop words from the text using a list comprehension.

```python
import nltk
from nltk.corpus import stopwords

# Removing stop words
stop_words = set(stopwords.words('english'))
text = "the quick brown fox jumps over the lazy dog"

text = ' '.join([word for word in text.split() if word not in stop_words])

print(text) # quick brown fox jumps lazy dog
```

## Lemmatization
A lemma is the base form of a word. For instance, the lemma of "rocks" is "rock". Lemmatization is the process of reducing words to their base or root form. This is important because it ensures that the model treats words with different forms consistently. Lemmatization involves determining the base or dictionary form of a word based on its context. It uses language dictionaries and morphological analysis to accurately reduce words to their base form.


To lemmatize the text, we can use the WordNetLemmatizer from the NLTK library.

```python
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')

text = "rocks and cats"

lemmatizer = WordNetLemmatizer() 
text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
print(text) # rock and cat
```

## Stemming
Stemming performs a similar function to lemmatization. It follows a rule-based approach reduces words to 1their base or root form by removing suffixes, such as "ing" or "ed".

```python
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')

text = "running in a stunning day"

stemmer = PorterStemmer()
text = ' '.join([stemmer.stem(word) for word in text.split()])

print(text) # run in stun day
```

Note that the NLTK's WordNetLemmatizer is designed to lemmatize words based on their part-of-speech (POS) tag. By default, if no POS tag is specified, it assumes the word is a noun. However, to lemmatize verbs accurately, you need to explicitly provide the POS tag.

```python
lemmatizer.lemmatize("runnin") # running 
```


```python
lemmatizer.lemmatize("running", pos = 'v') # run
```


## Exercise
Use any paragraph of text and clean it using the following steps:
- Remove punctuation marks.
- Convert all text to lowercase.
- Remove numbers.
- Remove stopwords (common words that often do not carry significant meaning like "the", "is", "and", etc.).