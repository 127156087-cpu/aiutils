import logging 
import math

logger=logging.getLogger(__name__)

def cosine_similarity(
        vector_a:list[float],
        vector_b:list[float])->float:
    
    logger.debug("Calculating cosine similarity")

    if len(vector_a)!=len(vector_b):
        raise ValueError("Vectors must have the same length")

    dot_product=sum(
        a*b for a,b in zip(vector_a,vector_b)
    )

    magnitude_a=math.sqrt(sum(a*a for a in vector_a))
    magnitude_b=math.sqrt(sum(b*b for b in vector_b))

    if magnitude_a==0 or magnitude_b==0:
        return 0.0

    return dot_product/(magnitude_b * magnitude_a)