import logging

logger=logging.getLogger(__name__)

def clean_text(text:str)->str:

    logger.debug("cleaning text")
    cleaned_text=" ".join(text.split())

    return cleaned_text
