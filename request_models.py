from pydantic import BaseModel, Field
from typing import Optional


class BookRequest(BaseModel):
    id: Optional[int] = Field(
        description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)  # minimum 3 characters
    author: str = Field(min_length=3)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=0, le=5)
    published_date: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "codingwithroby",
                "description": "A new description of a book.",
                "rating": 5,
                "published_date": 2012
            }
        }
    }