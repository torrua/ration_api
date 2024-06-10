from typing import Any

from pydantic import BaseModel, field_validator, ConfigDict
from sqlalchemy.orm import Query


class OrmBase(BaseModel):
    # Common properties across orm models
    # id: int = Field(..., alias='id')
    model_config = ConfigDict(from_attributes=True)

    # Pre-processing validator that evaluates lazy relationships before any other validation
    # NOTE: This validator is applied before any other validation, thanks to the `pre=True` flag.
    #       It checks if the input is an instance of Query and if so,
    #       converts it to a list of results.
    #       This approach ensures that all lazy relationships
    #       are evaluated before any other validation occurs.

    @field_validator("*")
    def evaluate_lazy_columns(cls, v: Any) -> Any:  # pylint: disable=E0213
        if isinstance(v, Query):
            return v.all()
        return v
