import os
from typing import Optional
from openai import OpenAI

def create_llm_client(api_key: Optional[str] = None, base_url: Optional[str] = None) -> OpenAI:
    """
    Create a unified OpenAI client that works with OpenAI, Ollama, Qwen, etc.
    
    Args:
        api_key: API key (optional). If None, tries RAG_LLM_API_KEY env var.
        base_url: Base URL (optional). If None, tries RAG_LLM_BASE_URL env var.
    
    Returns:
        OpenAI client configured for the target provider.
    """
    # Use provided values or fall back to environment variables
    final_api_key = api_key or os.getenv("RAG_LLM_API_KEY")
    final_base_url = base_url or os.getenv("RAG_LLM_BASE_URL")
    
    # Defaults for Ollama if detected via provider env var
    # Note: If called from RAGClient, these values are likely already resolved in APIConfig
    # This fallback is mainly for standalone scripts or direct usage
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    
    if provider == "ollama":
        if not final_base_url:
            final_base_url = "http://localhost:11434/v1"
        if not final_api_key:
            final_api_key = "ollama"
            
    # OpenAI client handles None base_url by using default (https://api.openai.com/v1)
    return OpenAI(
        api_key=final_api_key,
        base_url=final_base_url
    )
