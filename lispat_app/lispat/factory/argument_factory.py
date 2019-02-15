import os
import sys
import csv
import docx
from io import StringIO
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from lispat.utils.logger import Logger
from lispat.utils.colors import bcolors
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter


logger = Logger("ArgumentFactory")


class ArgumentFactory:
    """
    This class handles all the file conversion.
    """

    def __init__(self, session):

        logger.getLogger().info("Argument factory init")

        self.txt = [] # DEPRECATED
        self.txt_file_path = ""

        storage = "../static/uploads/" + session
        directory_storage = os.path.abspath(storage)
        logger.getLogger().info(directory_storage)

        self.csv_dir = directory_storage + "/csv_data/"
        self.text_dir = directory_storage + "/txt_data/"
        self.visuals_dir = directory_storage + "/visuals/"

        self.csv_path = ""

        if not os.path.exists(directory_storage):
            os.makedirs(directory_storage)
        if not os.path.exists(self.text_dir):
            os.makedirs(self.text_dir)
        if not os.path.exists(self.csv_dir):
            os.makedirs(self.csv_dir)
        if not os.path.exists(self.visuals_dir):
            os.makedirs(self.visuals_dir)


    def pdfminer_handler(self, path):
        """
        Function using pdfminer to extract text from pdfs and
        store them into an array of text files
        """
        logger.getLogger().info("Running PDFMiner")

        page_nums = set()
        output = StringIO()
        la_params = LAParams()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, la_params)
        interpreter = PDFPageInterpreter(manager, converter)

        try:
            file = os.path.basename(path)
            pdf_saved = self.text_dir + file
            pdf_saved = os.path.splitext(pdf_saved)[0] + '.txt'

            if os.path.exists(pdf_saved):
                logger.getLogger().debug(bcolors.OKBLUE + "Already Exits: "
                                         + bcolors.ENDC + file)
                self.txt.append(pdf_saved) # DEPRECATED
                self.txt_file_path = pdf_saved
                return self.txt_file_path

            logger.getLogger().debug("Opening File: {}".format(file))

            try:
                with open(path, 'rb') as infile:
                    logger.getLogger().debug("Opening File Successful")

                    for page in PDFPage.get_pages(infile, page_nums):
                        interpreter.process_page(page)

                    text = output.getvalue()

                    logger.getLogger().debug("Writing " + pdf_saved)

                    text_file = self.open_file(pdf_saved)

                    text_file.write(text)

                    infile.close()
                    converter.close()
                    output.close
                    text_file.close()

                    return self.txt_file_path

            except ImportError as error:
                logger.getLogger().error(error)
                sys.exit(1)
        except RuntimeError as error:
            logger.getLogger().error(error)
            sys.exit(1)

    def docx_handler(self, path):
        """
        Function using docx library to extract text from word docs and
        store them into an array of text files
        """
        logger.getLogger().info("running docx")
        doc_text = []
        try:
            file = os.path.basename(path)
            doc_saved = self.text_dir + file
            doc_saved = os.path.splitext(doc_saved)[0] + '.txt'

            if os.path.exists(doc_saved):
                logger.getLogger().debug("Already Exits: " + file)
                self.txt.append(doc_saved)
                self.txt_file_path = doc_saved
                return self.txt_file_path

            doc = docx.Document(path)

            for para in doc.paragraphs:
                doc_text.append(para.text)

            doc_text = '\n'.join(doc_text)

            file = os.path.splitext(file)[0]
            text_file = self.open_file(doc_saved)
            text_file.write(doc_text)

            return self.txt_file_path
        except RuntimeError as error:
            logger.getLogger().error(error)
            sys.exit(1)

    def csv_handler(self, txt):
        """
        Function using tabula library to extract text from word docs and
        store them into an array of csv files


        TODO: This class needs to be more modular for different arrays
        and csv files.
        """
        logger.getLogger().info("Creating a CSV")

        try:
            csv_filename = self.csv_dir + "data-" + random.randrange(0, 100) + ".csv"
            logger.getLogger().debug("Opening File for csv: " + csv_filename)
            csv__ = open(csv_filename, 'w+')
            self.csv_path = csv_filename
            with open(csv_filename, 'a+', newline='') as outputFile:
                logger.getLogger().debug("csv file opened: " + csv_filename)

                writer = csv.writer(outputFile, dialect='excel')
                logger.getLogger().debug("csv created: " + csv_filename)
                writer.writerows(txt)

                outputFile.close()
                return True, csv_filename
        except RuntimeError as error:
            logger.getLogger().error(error)
            sys.exit(1)

    def csv_with_headers(self, docA_path, docB_path, docA_data, docB_data):

        logger.getLogger().info("Creating a CSV with headers")

        docA_path = ''.join(str(item) for sublist in docA_path
                            for item in sublist)
        docB_path = ''.join(str(item) for sublist in docB_path
                            for item in sublist)

        docA_file = os.path.basename(docA_path)
        docB_file = os.path.basename(docB_path)

        docA_name = os.path.splitext(docA_file)[0]
        docB_name = os.path.splitext(docB_file)[0]
        docA_name = "(" + docA_name[:10] + ")"
        docB_name = "(" + docB_name[:10] + ")"

        try:
            csv_filename = self.csv_dir + docB_name + "VS" + docA_name + ".csv"

            logger.getLogger().debug("Opening File for csv: " + csv_filename)

            with open(csv_filename, 'w') as outputfile:
                myFields = ['Document Type', 'Document', 'Text']
                writer = csv.DictWriter(outputfile, fieldnames=myFields)
                writer.writeheader()
                writer.writerow({'Document Type': 'standard',
                                'Document': docA_name, 'Text': docA_data})
                writer.writerow({'Document Type': 'submission',
                                'Document': docB_name, 'Text': docB_data})

                return csv_filename

        except RuntimeError as error:
            logger.getLogger().error(error)
            sys.exit(1)

    def open_file(self, path):
        """Summary: Creates/Opens text files with input file name."""
        file = os.path.basename(path)
        txt_filename = self.text_dir + file
        txt_filename = os.path.splitext(txt_filename)[0] + '.txt'

        logger.getLogger().debug("File opened for writing - {}"
                                 .format(txt_filename))
        # NO LONGER USED, RETURNING STRING NOW
        self.txt.append(txt_filename)

        self.txt_file_path = txt_filename
        return open(txt_filename, "w")

    def file_count(self, files):
        """Summary: Gets the file count from a list of files."""
        count = 0
        for file in files:
            count += 1
        return count
