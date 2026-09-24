import logging

logger=logging.getLogger(__name__)

def tokenize(text:str)->list[str]:

    logger.debug("Tokenizing text")
    tokens=text.split()
    logger.debug("Created %d tokens",len(tokens))

    return tokens