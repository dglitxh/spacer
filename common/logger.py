import logging 

logger = logging.getLogger("spacer")

logger.basicConfig(filename="spacer.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filemode='w')

logger.setLevel(logging.Debug)

