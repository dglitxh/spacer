import logging 

logger = logging.getLogger("spacer")

logging.basicConfig(filename="spacer.log",
                    format='%(asctime)s - %(levelname)s:  %(message)s',
                    filemode='a')

logger.setLevel(level=logging.DEBUG)

