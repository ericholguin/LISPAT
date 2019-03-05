import os
import random
import datetime
import webbrowser
import scattertext as st
from scattertext import word_similarity_explorer
from lispat_app.lispat.utils.logger import Logger


logger = Logger("Visuals")


class Visualization:

    def __init__(self, nlp):

        self.nlp = nlp

        vis_dir = os.path.abspath("lispat_app/static")

        if not os.path.isdir(vis_dir):
            os.mkdir(vis_dir)

        self.std_file = os.path.abspath(vis_dir + "/Graph" + ".html")
        self.term_file = os.path.abspath(vis_dir + "/Similarity-Visual" + ".html")


    def standard(self, dataframe):
        corpus = st.CorpusFromPandas(dataframe, category_col='Document Type',
                                     text_col='Text', nlp=self.nlp).build()

        html = st.produce_scattertext_explorer(corpus, category='1st Document',
                                               category_name='1st Document',
                                               not_category_name='2nd Document',
                                               width_in_pixels=1000)

        logger.getLogger().info("Opening Standard Visual")
        open(self.std_file, 'wb').write(html.encode('utf-8'))


    def word_similarity_graph(self, dataframe, word):
        corpus = st.CorpusFromPandas(dataframe, category_col='Document Type',
                                     text_col='Text', nlp=self.nlp).build()

        html = word_similarity_explorer(corpus,
                                        category='1st Document',
                                         category_name='1st Document',
                                         not_category_name='2nd Document',
                                         target_term=word,
                                         minimum_term_frequency=5,
                                         pmi_threshold_coefficient=4,
                                         width_in_pixels=1000,
                                         alpha=0.01,
                                         max_p_val=0.05,
                                         save_svg_button=True)
        logger.getLogger().info("Opening Word Similarity Visual")
        open(self.term_file, 'wb').write(html.encode('utf-8'))

################# NOT USED ###### DEPRECATED ###################################
#        self.empath_file = vis_dir + "/Empath-Visual-" + ".html"
#        self.gitc_file = vis_dir + "/GITC-Visual-" + ".html"
#        self.chr_file = vis_dir + "/Characteristic-Visual-" + ".html"
#    def empath(self, dataframe):
#        feat_builder = st.FeatsFromOnlyEmpath()
#        empath_corpus = st.CorpusFromParsedDocuments(dataframe,
#                                                     category_col=
#                                                     feats_from_spacy_doc=
#                                                     feat_builder,
#                                                     parsed_col='Text').build()
#
#        html = st.produce_scattertext_explorer(empath_corpus,
#                                               category='submission',
#                                               category_name='Submission',
#                                               not_category_name='Standard',
#                                               width_in_pixels=1000,
#                                               use_non_text_features=True,
#                                               use_full_doc=True,
#                                               topic_model_term_lists=
#                                               feat_builder.
#                                               get_top_model_term_lists())
#
#        logger.getLogger().info("Opening Empath Visual")
#        open(self.empath_file, 'wb').write(html.encode('utf-8'))
#
#    def gitc(self, dataframe):
#        general_inquirer_feature_builder = st.FeatsFromGeneralInquirer()
#
#        corpus = st.CorpusFromPandas(dataframe, category_col='Document Type',
#                                     text_col='Text',
#                                     nlp=st.whitespace_nlp_with_sentences,
#                                     feats_from_spacy_doc=
#                                     general_inquirer_feature_builder).build()
#
#        html = st.produce_frequency_explorer(corpus, category='submission',
#                                             category_name='Submission',
#                                             not_category_name='Standard',
#                                             use_non_text_features=True,
#                                             use_full_doc=True,
#                                             term_scorer=st.LogOddsRatioUninformativeDirichletPrior(),
#                                             grey_threshold=1.96,
#                                             width_in_pixels=1000,
#                                             topic_model_term_lists=general_inquirer_feature_builder.get_top_model_term_lists())
#
#        logger.getLogger().info("Opening GITC-Visual")
#        open(self.gitc_file, 'wb').write(html.encode('utf-8'))
#
#    def chrctrstc(self, dataframe):
#        corpus = (st.CorpusFromPandas(dataframe, category_col='Document Type',
#                                      text_col='Text',
#                                      nlp=st.whitespace_nlp_with_sentences)
#            .build().get_unigram_corpus().compact(
#            st.ClassPercentageCompactor(term_count=5, term_ranker=
#            st.OncePerDocFrequencyRanker)))
#
#        html = st.produce_characteristic_explorer(corpus, category='submission',
#                                                  category_name='Submission',
#                                                  not_category_name='Standard', )
#
#        logger.getLogger().info("Opening Characteristic Visual")
#        open(self.chr_file, 'wb').write(html.encode('utf-8'))
#
    #### DEPRECATED ###
    # def nearest(self, points1=None, points2=None, file1=None, file2=None):
    #     try:
    #         if file1 is None:
    #                 raise Exception("File now found")
    #         if points1 is not None and points2 is None:
    #                 fig, ax = plt.subplots(figsize=(15, 10))
    #
    #                 p = ax.scatter(points1['x'], points1['y'], s=15, color='b', marker='o',
    #                                alpha=.3)
    #                 labels = []
    #
    #                 for i in range(points1.shape[0]):
    #                     label = points1.ix[[i], :].T
    #                     label.columns = ['Row {0}'.format(0)]
    #                     labels.append(str(label.to_html()))
    #
    #                 # Setting axis label
    #                 ax.set_xlabel('X')
    #                 ax.set_ylabel('Y')
    #                 ax.set_title('{} Nearest Neighbor'.format(file1), size=60)
    #
    #                 # for i, point in points1.iterrows():
    #                 #     x = float(point.x + 0.050)
    #                 #     y = float(point.y + 0.050)
    #                 #     w = str(point.word)
    #                 #
    #                 #     ax.text(x, y, w, fontsize=11)
    #                 # Plugins for tooltip
    #                 tooltip = plugins.PointHTMLTooltip(p,
    #                                                    labels, voffset=10,
    #                                                    hoffset=10, css=css)
    #
    #                 plugins.connect(fig, tooltip)
    #                 mpld3.show()
    #
    #         if points1 is not None and points2 is not None:
    #             fig, ax = plt.subplots(figsize=(15, 10))
    #
    #             p1 = ax.scatter(points1['x'], points1['y'], s=15, color='b', marker='o',
    #                             alpha=.3, label=file1)
    #             p2 = ax.scatter(points2['x'], points2['y'], s=15, color='r', marker='o',
    #                             alpha=.3, label=file2)
    #
    #             labels = []
    #             for i in range(points1.shape[0]):
    #                 label = points1.ix[[i], :].T
    #                 label.columns = ['Row {0}'.format(0)]
    #                 labels.append(str(label.to_html()))
    #
    #             labels2 = []
    #             for i in range(points2.shape[0]):
    #                 label = points2.ix[[i], :].T
    #                 label.columns = ['Row {0}'.format(0)]
    #                 labels2.append(str(label.to_html()))
    #
    #             ax.set_xlabel('X')
    #             ax.set_ylabel('Y')
    #             ax.set_title('{} vs {} - Nearest Neighbor'.format(file1, file2), size=15)
    #
    #             legend_labels = [file1, file2]
    #             plot_collection = [p1, p2]
    #             legend = plugins.InteractiveLegendPlugin(plot_collection, legend_labels)
    #             tooltip = plugins.PointHTMLTooltip(p1,
    #                                                labels, voffset=10,
    #                                                hoffset=10, css=css)
    #
    #             tooltip2 = plugins.PointHTMLTooltip(p2,
    #                                                    labels2, voffset=10,
    #                                                    hoffset=10, css=css)
    #
    #             plugins.connect(fig, legend)
    #             plugins.connect(fig, tooltip)
    #             plugins.connect(fig, tooltip2)
    #             mpld3.show()
    #
    #     except Exception as e:
    #         logger.getLogger().error(e)
    #         return
    #
    #     # print(doc2vec.most_similar("security"))
    #     pass
