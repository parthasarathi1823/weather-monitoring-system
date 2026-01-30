import logging

def setup_logger():
    logging.basicConfig(filename="activities.log",
                    level=logging.INFO,
                    format="%(levelname)s:%(asctime)s:%(message)s")