import sys
import nltk
import docopt
from lispat.base.manager import CommandManager
from lispat.utils.logger import Logger
from lispat.utils.colors import bcolors
from lispat.base.constants import LISPAT_DOCOPT

DOCOPT = LISPAT_DOCOPT

logger = Logger("Main")
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def app_main(args):
    try:
        manager = CommandManager()
        if args['analytics'] and args['--path']:
            user_path = args['--path']
            manager.create_path(user_path)
            manager.run_analytics(args)

        if args['compare'] and args['--standard'] and args['--submission']:
            std_path = args['--standard']
            sub_path = args['--submission']

            manager.create_path(std_path, sub_path)

            manager.run_sub_vs_std(args)
        if args['compare'] and args['input'] and args['--standard']:
            print(args['--text'])
            std_path = args['--standard']
            print(std_path)
            manager.create_path(std_path)
            manager.run_sub_vs_txt(args)

        if args['clean']:
            manager.clean(args)

    except KeyboardInterrupt:
        logger.getLogger().error(bcolors.FAIL + "Keyboard interrupt. Exiting"
                                 + bcolors.ENDC)
        sys.exit(1)


if __name__ == '__main__':
    main()
