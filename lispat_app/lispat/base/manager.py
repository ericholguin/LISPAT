import os
import sys
import spacy
import pickle
import shutil
import datetime
import pandas as pd
from lispat_app.lispat.utils.logger import Logger
from lispat_app.lispat.utils.colors import bcolors
from lispat_app.lispat.processing.model_processing import NLPModel
from lispat_app.lispat.factory.document_factory import DocumentFactory
from lispat_app.lispat.factory.argument_factory import ArgumentFactory
from lispat_app.lispat.processing.pre_processing import Preproccessing
from lispat_app.lispat.processing.visual_processing import Visualization
import en_core_web_sm

nlp = en_core_web_sm.load()

# NEEDED? ORIG.
nlp = spacy.load('en')


logger = Logger("CommandManager")


class CommandManager:
    """
    CommandManager will be used to handle multiple tasks.
    Such as spin off threads, handle command line inputs,
    and create the necessary communication between sources.
    """

    def __init__(self):
        self.docA_path = None
        self.docB_path = None
        self.docA_txt_path = None
        self.docB_txt_path = None

        self.docA_filter = None
        self.docB_filter = None

        self.doc_worker = None

        self.model = NLPModel()

    def create_path(self, docA_path, docB_path=None):
        """
        Summary: Store the absolute path(s) of the document(s)
        :param path: path user declared to processing docs
        :return: exit code
        """
        try:
            logger.getLogger().info("Command Manager - Init")

            full_path = os.path.abspath(docA_path)

            if os.path.isfile(full_path):
                logger.getLogger().info("CommandManager created with file path={}"
                                        .format(full_path))
                self.docA_path = full_path

            if docB_path is not None:
                docB_full_path = os.path.abspath(docB_path)

                if os.path.isfile(docB_full_path):
                    logger.getLogger().info("CommandManager created "
                                            "Document B path: {}"
                                            .format(docB_full_path))
                    self.docB_path = docB_full_path
            else:
                raise RuntimeError

        except RuntimeError as error:
            logger.getLogger().error("Directory does not exist")
            sys.exit(1)

    def convert(self):
        """
        Summary: Converts documents inside the path to .txt
        :return: Exit code
        """
        logger.getLogger().info("Command Manager - Convert")
        try:
            docA = DocumentFactory(self.docA_path)
            docB = DocumentFactory(self.docB_path)

            self.docA_txt_path = docA.convert_file()
            self.docB_txt_path = docB.convert_file()

        except RuntimeError as error:
            logger.getLogger().error(error)
            exit(1)

    def filter(self):
        """
        Summary: Cleans documents returns lists
        :return: Exit code
        """
        # Initialize with our docs.
        logger.getLogger().info("Command Manager - Filter")
        try:
            self.docA_filter = Preproccessing(self.docA_txt_path)
            self.docB_filter = Preproccessing(self.docB_txt_path)

            self.docA_filter.read_textfile()
            self.docB_filter.read_textfile()

            self.docA_filter.filter_nlp()
            self.docB_filter.filter_nlp()

        except RuntimeError as error:
            logger.getLogger().error(error)
            exit(1)

    def model(self):
        vis = Visualization()
        vis = Visualization(nlp)

        sentences = []
        raw_sentences = self.docB_filter.get_sentences()

        for raw_sentence in raw_sentences:
            if len(raw_sentence) > 0:
                sentences.append(self.docB_filter.get_sent_tokens(raw_sentence))

        sentences_sub = []
        raw_sentences_sub = filter_std.get_sentences()
        for raw_sentence in raw_sentences_sub:
            if len(raw_sentence) > 0:
                sentences_sub.append(filter_std.get_sent_tokens(raw_sentence))

        input_txt = filter_std.get_sent_tokens(str(args['--text']))
        file1 = os.path.basename(self.docA_path)
        points_input, points_std = self.model.semantic_properties_model(sentences_sub, user_input=input_txt)
        vis.nearest(points1=points_std, points2=points_input, file1=file1, file2="User Input")

    def get_json(self):
        """
        Summary: Makes json response
        :return: Exit code
        """
        # Initialize with our docs.
        logger.getLogger().info("Command Manager - MAKE JSON")

        docA_txt = self.docA_filter.get_raw_text()
        docB_txt = self.docB_filter.get_raw_text()

        self.docA_filter.most_frequent()
        self.docB_filter.most_frequent()

        topDocA = self.docA_filter.get_top_words()
        topDocB = self.docB_filter.get_top_words()

        data = {
            "_id": os.path.split(os.path.split(self.docA_path)[0])[1],
            "standard": docA_txt,
            "submission": docB_txt,
            "standard_file_name": os.path.splitext(self.docA_path)[0],
            "submission_file_name": os.path.splitext(self.docB_path)[0],
            "standard_keywords": topDocA,
            "submission_keywords": topDocB,
            "standard_phrases": [],
            "submission_phrases": [],
            "date": datetime.datetime.now(),
        }

        return data



    def run_analytics(self, args):
        """
        Main run function to handle learning
        :return: Exit code
        """
        # Initialize with our docs.
        logger.getLogger().info("Command Manager - Run")
        try:
            doc_worker = None
            if args['--compare']:
                doc_worker = DocumentFactory(self.docA_path)
            elif args['--train']:
                doc_worker = DocumentFactory(self.docA_path)
            else:
                raise RuntimeError("No arguments found, please try using "
                                   "--compare or --train")

            docs = doc_worker.convert_file()
            filter = Preproccessing(docs[0], docs[1])


            if args['--df']:
                nlp_array_unfiltered = self.model.build_sents(filter.nlp.sents)
                print(nlp_array_unfiltered[:5])
                csv_success = self.doc_worker.args_.csv_handler(nlp_array_unfiltered)
                if csv_success:
                    self.model.data_frame(self.doc_worker.args_.csv_path)

            if args['--sp']:
                vis = Visualization()
                sentences = []
                raw_sentences = filter.get_sentences()
                for raw_sentence in raw_sentences:
                    if len(raw_sentence) > 0:
                        sentences.append(filter.get_sent_tokens(raw_sentence))

                file = os.path.basename(self.docA_path)
                points = self.model.semantic_properties_model(sentences)
                vis.nearest(points1=points, file1=file)

            if args['--compare']:
                self.model.compare_doc_similarity(self.docA_path)
            if args['--train']:
                self.model.save_trained(filter.word_array)

        except RuntimeError as error:
            logger.getLogger().error(error)
            exit(1)

    def graph(self):
        """
        This function is to handle the comparison of two submissions using
        visuals.
        :return: N/A
        """
        logger.getLogger().info("Command Manager - Graph Function")

        try:
            args_ = ArgumentFactory()

            DocA = filter_DocA.get_raw_txt()
            DocB = filter_DocB.get_raw_txt()

            DocA_size = len(cleanDocA)
            DocB_size = len(cleanDocB)

            if(DocB_size > DocA_size):
                nlp.max_length = DocB_size + 1
            else:
                nlp.max_length = DocA_size + 1


            csv = args_.csv_with_headers(self.docB_txt_path, self.docA_txt_path,
                                         DocB, DocA)

            dataframe = pd.read_csv(csv, names=["Document Type",
                                    "Document", "Text"])

            vis = Visualization(nlp)

            html_file = vis.standard(dataframe)

        except RuntimeError as error:
            logger.getLogger().error("Error with run_sub_vs_std please "
                                     "check stack trace")
            exit(1)


    def run_sub_vs_txt(self, args):
        args_ = ArgumentFactory()
        vis = Visualization(nlp)
        doc_std = DocumentFactory(self.docA_path)
        doc_std_converted = doc_std.convert_file()
        filter_std = Preproccessing(doc_std_converted[0],
                                    doc_std_converted[1])
        std_data = filter_std.ret_doc()
        if args['--clean']:
            filter_std.filter_nlp()

        std_path = ""
        if doc_std_converted[0]:
            std_path = doc_std_converted[0]
        elif doc_std_converted[1]:
            std_path = doc_std_converted[1]

        sentences_sub = []
        raw_sentences_sub = filter_std.get_sentences()
        for raw_sentence in raw_sentences_sub:
            if len(raw_sentence) > 0:
                sentences_sub.append(filter_std.get_sent_tokens(raw_sentence))

        input_txt = filter_std.get_sent_tokens(str(args['--text']))
        file1 = os.path.basename(self.docA_path)
        points_input, points_std = self.model.semantic_properties_model(sentences_sub, user_input=input_txt)
        # vis.nearest(points1=points_std, points2=points_input, file1=file1, file2="User Input")


    def clean(self):
        """
        :param args: Arguments for which dirs to delete
        :return: Deleted dirs for file system storage
        """
        session = os.path.split(os.path.split(self.docA_path)[0])[1]

        try:
            print("Purging local storage")
            shutil.rmtree(os.path.abspath("../static/uploads/" + session))
            print("Finished")
        except RuntimeError:
            logger.getLogger().error("Error cleaning storage")
