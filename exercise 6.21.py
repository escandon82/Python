# Remove special symbols / punctuation from a string
sentence = "/*Jon is @developer & musician"

import re

clean_sentence=re.sub('[^A-Za-z0-9\s]+',"",sentence)

print(clean_sentence)