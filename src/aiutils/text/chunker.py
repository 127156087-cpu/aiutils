import logging
logger=logging.getLogger(__name__)

def chunk_text(text:str,chunk_size:int=100)->list[str]:

    logger.debug("Chunking text with chunk size:%d",chunk_size)
    words=text.split()
    chunks=[]

    for i in range(0,len(words),chunk_size):
        chunk=" ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    logger.debug("Created %d chunks",len(chunks))

    return chunks