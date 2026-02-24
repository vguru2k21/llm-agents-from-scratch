"""Base LLM."""

from abc import ABC, abstractmethod
from typing import Any, Sequence, TypeAlias, TypeVar
from pydantic import BaseModel

from llm_agents_from_scratch.data_structures import (
  ChatMessage,
  CompleteResult,
  TooCallResult,
)
