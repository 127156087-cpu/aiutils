import logging

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class Document(BaseModel):
    content: str
    metadata: dict[str, str] = Field(default_factory=dict)

    def __init__(self, **data) -> None:
        super().__init__(**data)

        logger.debug("Document created")