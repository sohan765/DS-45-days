import nltk
nltk.download("punkt")
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
text = "As the days passed, it pushed through the soil and reached the sunlight. Birds sang in its branches, and children rested in its shade. The little seed realized that every great journey begins with a small step and a little courage."
tokens = word_tokenize(text)
print(tokens)
text1 = "that patience, hope, and determination can help us achieve our dreams, no matter how difficult the beginning may seem"
tokens1 = word_tokenize(text1)
print(tokens1)



import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text3 = "Once upon a time, a tiny seed lay quietly in the soil. It dreamed of becoming a tall, beautiful tree, but it was afraid of the dark ground around it. One day, the rain fell gently, and the warm sun shone above. The seed decided to be brave and began to grow."
words = word_tokenize(text3)
print("tokenize")
print(words)

stop_words = set(stopwords.words("english"))
print("stop words")
print(stop_words)


filtered = []
for word in words:
  if word.lower() not in stop_words:
    filtered.append(word)
print("filtered data")
print(filtered)

from nltk.stem  import PorterStemmer
stemmer = PorterStemmer()

print(stemmer.stem("Eating"))
print(stemmer.stem("eat"))
print(stemmer.stem("eaten"))
print("hello")
import nltk
nltk.download("punkt")
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
text = "my name is Sohan Patel"
tokens = word_tokenize(text)
print(tokens)
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text = "I am learning Machine Learning with shlok"
words = word_tokenize(text)
print("tokenize")
print(words)

stop_words = set(stopwords.words("english"))
print("stop words")
print(stop_words)


filtered = []
for word in words:
  if word.lower() not in stop_words:
    filtered.append(word)
print("filtered data")
print(filtered)

from nltk.stem  import PorterStemmer
stemmer = PorterStemmer()

print(stemmer.stem("playing"))
print(stemmer.stem("played"))
print(stemmer.stem("player"))