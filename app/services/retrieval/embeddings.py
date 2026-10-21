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
    try:
        embedding_model = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-2-preview",
            google_api_key=settings.GEMINI_API_KEY
        )

        embedding_model.embed_query("probe")
        logfire.info("Gemini embeddings ready (gemini-embedding-2-preview, 3072-dim).")
        return embedding_model
    except Exception as e:
        logfire.warning(f"Gemini probe failed: {e}. Will use sentence-transformers fallback.")
        return None

def _load_fallback():
    from sentence_transformers import SentenceTransformer
    logfire.info("Loading sentence-transformers fallback (all-mpnet-base-v2, 768-dim).")
    return SentenceTransformer("all-mpnet-base-v2")

def _init():
    pass

def get_embedding_dim() -> int:
    """
        Return the vector dimension for the active model. Call after _init()
    """
    pass

def _embed_documents(texts: list[str]) -> list[list[float]]:
    """
        Embed a list of texts using the active model. Call after _init()
    """
    pass

def _embed_batch(batch : list[str]) -> list[list[float]]:
    pass

def embed_query(query : str) -> list[float]:
    pass

def embed_texts(texts: list[str]) -> list[list[str]]:
    _init()
