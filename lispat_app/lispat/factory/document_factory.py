"""
DocumentFactory.

This script recieves user defined path containing the file to be converted into text files.
"""

import os
import sys
from pathlib import Path
from joblib import Parallel, delayed
from lispat_app.lispat.utils.logger import Logger
from lispat_app.lispat.utils.colors import bcolors
import lispat_app.lispat.factory.argument_factory as arg_fac
from lispat_app.lispat.factory.argument_factory import ArgumentFactory



logger = Logger("DocumentFactory")


class DocumentFactory:
    """
    Handles file conversion, using the user defined path.

    This class uses the passed in file path and checks if the file is either a pdf
    or docx file and applies the proper function to convert to text.

    """

    def __init__(self, path):
        logger.getLogger().info("DocumentFactory Created")

        self.isPdf = False
        self.isDoc = False
        self.path = path

        self.args_ = ArgumentFactory()

        try:
            file = Path(path)
            if file.is_file():
                if file.suffix == ".doc":
                    logger.getLogger().debug(bcolors.OKGREEN + "File Found: "
                                             + bcolors.ENDC + " {}"
                                             .format(os.path.basename(path)))
                    self.isDoc = True

                if file.suffix == ".docx":
                    logger.getLogger().debug(bcolors.OKGREEN + "File Found: "
                                             + bcolors.ENDC + " {}"
                                             .format(os.path.basename(path)))
                    self.isDoc = True

                if file.suffix == '.pdf':
                    logger.getLogger().debug(bcolors.OKGREEN + "File Found: "
                                             + bcolors.ENDC + " {}"
                                             .format(os.path.basename(path)))
                    self.isPdf = True

        except FileNotFoundError as error:
            logger.getLogger().error("No required file types Found - Exiting")
            sys.exit(1)

    def convert_file(self):
        """
        Handles the file conversion.

        Iterate through pdfs and docx files calls ArgumentFactory Class
        functions to extract text.
        """
        try:


            if self.isDoc:
                doc_data_txt = (
                    Parallel
                    (n_jobs=4, backend="multiprocessing", verbose=10)
                    (delayed
                     (self.args_.docx_handler)
                     (self.path)
                        for  i in range(1)))

                return doc_data_txt

            elif self.isPdf:
                pdf_data_txt = (
                    Parallel
                    (n_jobs=4, backend="multiprocessing", verbose=10)
                    (delayed
                     (self.args_.pdfminer_handler)
                     (self.path)
                        for i in range(1)))

                return pdf_data_txt

        except RuntimeError as error:
            logger.getLogger().error(error)
            exit(1)
