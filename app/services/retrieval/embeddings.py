import time
import logfire
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import settings

BATCH_SIZE = 50
_GEMINI_DIM = 3072
_FALLBACK_DIM = 768

_active_model = None
_model_type : str | None = None

def _probe_gemini():
    """
    Try one embed call to verify Gemini is reachable. Return model or None.
    """

def load_fallback():
    pass

def init():
    pass

def get_embedding_dim() -> int:
    """
        Return the vector dimension for the active model. Call after _init()
    """
    pass

def embed_documents(texts: list[str]) -> list[list[float]]:
    """
        Embed a list of texts using the active model. Call after _init()
    """
    pass

def _embed_batch(batch : list[str]) -> list[list[float]]:
    pass

def embed_query(query : str) -> list[float]:
    pass


