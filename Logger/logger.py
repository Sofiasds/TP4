import logging

class logger:
    
    def __init__(self):
        logging.basicConfig(filename='loggings.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

    def logs(message):
        logging.info(message.content)