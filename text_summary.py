# import spacy
# from spacy.lang.en.stop_words import STOP_WORDS 
# from heapq import nlargest
# from string import punctuation
# import pickle


# text="""
# In 1938, during Japanese-ruled Korea, Lee Byung-chul (1910–1987) of a large landowning family in the Uiryeong county moved to nearby Daegu and founded Mitsuboshi Trading Company (株式会社三星商会 (Kabushiki gaisha Mitsuboshi Shōkai)), or Samsung Sanghoe (주식회사 삼성상회). Samsung started out as a small trading company with forty employees located in Su-dong (now Ingyo-dong).[16] It dealt in dried fish,[16] locally-grown groceries and noodles.[17] The company prospered and Lee moved its head office to Seoul in 1947. When the Korean War broke out, he was forced to leave Seoul. He started a sugar refinery in Busan named Cheil Jedang. In 1954, Lee founded Cheil Mojik, a textiles company, and built the first plant in Chimsan-dong, Daegu. It was the largest woollen mill in the country at the time of construction.[18]
# Samsung diversified into many different areas. Lee sought to establish Samsung as a leader in a wide range of industries. Samsung moved into lines of business such as insurance, securities, and retail.
# """
# def summarize(rawdocs):
#     stopwords=list(STOP_WORDS)
#     # print(stopwords)
#     nlp=spacy.load("en_core_web_sm")
#     doc=nlp(rawdocs)
#     # print(doc)
#     # tokens=[token.text for token in doc]
#     # print(tokens)
#     word_freq={}

#     for word in doc:
#         if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
#             if word.text not in word_freq.keys():
#                 word_freq[word.text]=1

#             else:
#                 word_freq[word.text]+=1

#     # print(word_freq)

#     max_freq=max(word_freq.values())
#     # print(max_freq)


#     for word in word_freq.keys():
#         word_freq[word]=word_freq[word]/max_freq

#     # print(word_freq)

#     sent_tokens=[sent for sent in doc.sents]
#     # print(sent_tokens)

#     sent_scores={}
#     for sent in sent_tokens:
#         for word in sent:
#             if word.text in word_freq.keys():
#                 if sent not in sent_scores.keys():
#                     sent_scores[sent]=word_freq[word.text]
#                 else:
#                     sent_scores[sent]+=word_freq[word.text]

#     select_len=int(len(sent_tokens)*0.3)
#     # print(select_len)

#     summary=nlargest(select_len,sent_scores,key=sent_scores.get)
#     # print(summary)

#     final_summary=[word.text for word in summary]
#     summary=" ".join(final_summary)
#     # print(summary)


#     # print("length of original text ",len(text.split(" ")))
#     # print("length of summary text ",len(summary.split(" ")))

#     # return summary,doc,len(rawdocs.split(" ")),len(summary.split(" "))
#     return summary

# # with open("summarizer.pkl", "wb") as file:
# #     pickle.dump(summarize, file)
# pickle.dump(summarize,open('model.pkl','wb'))



import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
from string import punctuation
import pickle

class TextSummarizer:
    def __init__(self):
        # Load the spaCy model when the class is initialized
        self.nlp = spacy.load("en_core_web_sm")
        self.stopwords = list(STOP_WORDS)

    def summarize(self, rawdocs):
        # Process the document
        doc = self.nlp(rawdocs)
        word_freq = {}

        # Calculate word frequencies, ignoring stopwords and punctuation
        for word in doc:
            if word.text.lower() not in self.stopwords and word.text.lower() not in punctuation:
                if word.text not in word_freq:
                    word_freq[word.text] = 1
                else:
                    word_freq[word.text] += 1

        # Normalize word frequencies
        max_freq = max(word_freq.values())
        for word in word_freq.keys():
            word_freq[word] = word_freq[word] / max_freq

        # Calculate sentence scores
        sent_tokens = [sent for sent in doc.sents]
        sent_scores = {}
        for sent in sent_tokens:
            for word in sent:
                if word.text in word_freq.keys():
                    if sent not in sent_scores:
                        sent_scores[sent] = word_freq[word.text]
                    else:
                        sent_scores[sent] += word_freq[word.text]

        # Select the top sentences based on the score
        select_len = int(len(sent_tokens) * 0.3)
        summary = nlargest(select_len, sent_scores, key=sent_scores.get)

        # Combine the top sentences into the final summary
        final_summary = [word.text for word in summary]
        summary = " ".join(final_summary)

        return summary

# Save the instance to a pickle file (optional)
summarizer = TextSummarizer()
pickle.dump(summarizer, open('model.pkl', 'wb'))

