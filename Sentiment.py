from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# List of sentences for sentiment analysis, including the paragraph about Article 370.
sentences = [
 "Taiwan defends its de facto independence through a combination of diplomatic, military, and economic strategies. From a Taiwanese perspective, the island maintains its sovereignty by emphasizing its distinct history, culture, and governance system. The following are some key arguments presented for maintaining Taiwan's sovereignty and democratic system: 1. Historical and Cultural Identity: Taiwanese people often highlight their unique history and cultural heritage, which differ from that of mainland China. Taiwan has developed its own identity through a complex history of indigenous cultures, waves of immigration, colonial rule, and democratic governance. This distinct identity forms the basis for asserting Taiwan's right to self-determination and sovereignty. 2. Democratic Values: Taiwan has transitioned from an authoritarian regime to a vibrant democracy, with free and fair elections, respect for human rights, and rule of law. Taiwanese citizens value their democratic system as a fundamental aspect of their identity and way of life. They argue that maintaining sovereignty is crucial for safeguarding their democratic institutions and freedoms. 3. Economic Prosperity: Taiwan has achieved remarkable economic success and global recognition as a hub for technology, manufacturing, and innovation. Taiwanese people often argue that maintaining sovereignty allows them to pursue economic opportunities, trade relations, and international partnerships independently, without being constrained by external political pressure. 4. Security Concerns: Taiwan faces security challenges due to the ongoing military threats from China. Taiwanese citizens often emphasize the importance of maintaining sovereignty to ensure their security and protect themselves from potential aggression. A strong military defense, strategic alliances, and international support are crucial for safeguarding Taiwan's de facto independence. Overall, Taiwanese citizens present a range of arguments to support the maintenance of Taiwan's sovereignty and democratic system. These arguments are based on historical, cultural, democratic, economic, and security considerations, all of which contribute to the overall defense of Taiwan's de facto independence."
]

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Analyze each sentence in the list and print the sentiment scores
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))
