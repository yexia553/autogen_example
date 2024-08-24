import os


azure_gpt4o = {
    "model": "gpt-4o",
    "api_key": os.environ.get("OPENAI_API_KEY"),
    "base_url": os.environ.get("OPENAI_API_BASE"),
    "api_type": "azure",
    "api_version": "2024-02-15-preview",
    "temperature": 0.9,
}

azure_gpt4o_mini = {
    "model": "gpt-4o-mini",
    "api_key": os.environ.get("OPENAI_API_KEY"),
    "base_url": os.environ.get("OPENAI_API_BASE"),
    "api_type": "azure",
    "api_version": "2024-02-15-preview",
    "temperature": 0.8,
}

kimi_8k = {
    "model": "moonshot-v1-8k",
    "api_key": os.environ.get("KIMI_API_KEY"),
    "base_url": os.environ.get("KIMI_API_BASE"),
    "temperature": 0.8,
}

kimi_32k = {
    "model": "moonshot-v1-32k",
    "api_key": os.environ.get("KIMI_API_KEY"),
    "base_url": os.environ.get("KIMI_API_BASE"),
    "temperature": 0.8,
}

kimi_128k = {
    "model": "moonshot-v1-128k",
    "api_key": os.environ.get("KIMI_API_KEY"),
    "base_url": os.environ.get("KIMI_API_BASE"),
    "temperature": 0.8,
}


UNIAPI_CONFIG_LIST = [
    {
        "model": "moonshot-v1-8k",
        "api_key": os.environ.get("KIMI_API_KEY"),
        "base_url": os.environ.get("KIMI_API_BASE"),
        "temperature": 0.8,
    },
]
