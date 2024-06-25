from pydantic import Field
from utils.constants import UPPERCASE_START_REGEX

NameField = Field(min_length=1, max_length=100, pattern=UPPERCASE_START_REGEX)
NameDefaultField = Field(max_length=100, default=None, pattern=UPPERCASE_START_REGEX)
YearField = Field(ge=0, le=2100)
