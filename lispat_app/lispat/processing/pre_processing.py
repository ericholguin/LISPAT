import re
import sys
import nltk
import spacy
from collections import Counter
from lispat_app.lispat.utils.logger import Logger
from lispat_app.lispat.utils.colors import bcolors
from lispat_app.lispat.factory.filtered_factory import FilteredFactory


logger = Logger("Noise Filter")


class Preproccessing:

    def __init__(self, txt_file):

        """
        Summary: Initialize class and its variables for the preprocessing.
        :param txt: All data coming from the text document
        """
        self.txt_file = txt_file
        self.txt_data = ""

        self.top_words = None
        self.clean_txt_data = None
        self.clean_txt_array = None

        self.nlp = spacy.load('en')
        self.nlp_filtered = spacy.load('en')

        self.filter = FilteredFactory()

        logger.getLogger().info("Noise filter initialized")

    def read_textfile(self):
        filename = ''.join(self.txt_file)
        with open(filename, 'rt', newline='') as text:
            self.txt_data = text.read()


    #def filter_nlp(self, lc=None, p=None, n=None, sw=None, int=None, lw=None, lem=None, stm=None):
    def filter_nlp(self):
        """
        :return: Filtered nlp data spacy object.
        """

        try:
            logger.getLogger().debug("Running pre-processing on file: "
                                         + ''.join(self.txt_file))

            tokens = self.filter.tokenize(self.txt_data)
            stripped = self.filter.translate(tokens)
            words = self.filter.punctuation(stripped)
            words = self.filter.stop_words(words)
            words = self.filter.remove_names(words)
            words = self.filter.integers(words)
            words = self.filter.long_words(words)
            words = self.filter.lemmatize(words)
            words = self.filter.stemmer(words)

            logger.getLogger().info("Finished cleaning!")

            # Turn filtered words back to a spacy doc for better data handling.
            txt = " ".join(words)
            txt_len = len(txt)
            self.nlp_filtered.max_length = txt_len + 1
            nlp_filtered = self.nlp_filtered(txt)

            # Set the class variables
            self.clean_txt_array = words
            self.clean_txt_data = txt
            self.nlp_filtered = nlp_filtered

        except RuntimeError as error:
            logger.getLogger().error("Noise filter", error)

    def most_frequent(self):

        """
        :return: a word count on most commonly used words in the data set
        """
        logger.getLogger().info("Getting a word count on filtered words")
        try:
            if len(self.clean_txt_array) == 0:
                raise ValueError("No words to reduce", self.clean_txt_array)

            words = Counter(self.clean_txt_array)
            top_words = [word for word, word_count in words.most_common(20)]
            self.top_words = top_words

        except ValueError as error:
            logger.getLogger().error(bcolors.FAIL + "Error, please check"
                                     " stack trace" + bcolors.ENDC)
            sys.exit(1)

    def get_raw_text(self):
        return self.txt_data

    def get_clean_txt_list(self):
        return self.clean_txt_array

    def get_clean_txt_data(self):
        return self.clean_txt_data

    def get_top_words(self):
        return self.top_words

    def get_sentences(self):
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        raw_sentences = tokenizer.tokenize(self.txt_data)
        return raw_sentences

    def get_sent_tokens(self, raw):
        clean = re.sub("[^a-zA-Z]", " ", raw).lower()
        words = clean.split()
        return words
