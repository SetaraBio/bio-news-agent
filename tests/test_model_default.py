"""The documented default OpenAI model matches the code default."""

import re
from pathlib import Path

from config import DEFAULT_OPENAI_MODEL

_ROOT = Path(__file__).parents[1]


def test_default_openai_model_is_gpt_6_luna():
    assert DEFAULT_OPENAI_MODEL == "gpt-6-luna"


def test_env_example_names_only_the_code_default():
    text = (_ROOT / ".env.example").read_text(encoding="utf-8")
    assert set(re.findall(r"gpt-[\w.-]+", text)) == {DEFAULT_OPENAI_MODEL}


def test_development_docs_state_the_code_default():
    text = (_ROOT / "docs" / "development.md").read_text(encoding="utf-8")
    stated = re.findall(r"default API (?:fallback )?model is `([^`]+)`", text)
    assert stated == [DEFAULT_OPENAI_MODEL]
