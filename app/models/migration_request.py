from typing import List

from pydantic import BaseModel

from app.models.file_metadata import FileMetadata
from app.models.metadata import Metadata

from app.models.file_info import FileInfo

from app.models.class_metadata import ClassMetadata

from app.models.relationship import Relationship

from app.models.migration_info import MigrationInfo

from app.models.rag import Rag


class MigrationRequest(BaseModel):

    metadata: Metadata

    files: List[FileMetadata]

    # imports: List[str]

    # classes: List[ClassMetadata]

    relationships: List[Relationship]

    business_entities: List[str]

    business_flow: List[str]

    migration: MigrationInfo

    rag: Rag

    llm_provider: str = "mock"  # Default to mock LLM provider
 