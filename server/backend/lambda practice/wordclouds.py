import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to read text from a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Directory containing your text files
text_dir = './data/hbo/text'

# Read text from each file and combine
combined_text = ''
for filename in os.listdir(text_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(text_dir, filename)
        combined_text += read_file(file_path) + ' '

# Generate a word cloud image
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)

# Display the generated image
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
