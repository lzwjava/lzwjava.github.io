---
title: Validate LLM JSON Responses Safely
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
---

When you’re using an LLM API to build agents, you’ll often want to **check that the model’s JSON response is valid and structured as expected**. Python’s built-in `json` module is the simplest tool for this.

Here’s a step-by-step guide:

---

### 1. Basic validation with `json.loads`

```python
import json

response_text = '{ "name": "Alice", "age": 30 }'  # from LLM API

try:
    data = json.loads(response_text)
    print("Valid JSON:", data)
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)
```

* If `json.loads` succeeds → the response is syntactically valid JSON.
* If it raises `JSONDecodeError` → the response is malformed (extra commas, missing quotes, etc.).

---

### 2. Enforcing schema (structure and types)

`json.loads` only checks **syntax**, not whether fields are present or of the right type.
For deeper validation, use a schema validator like `jsonschema`:

```python
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name", "age"]
}

try:
    data = json.loads(response_text)
    validate(instance=data, schema=schema)
    print("Valid JSON and matches schema")
except (json.JSONDecodeError, ValidationError) as e:
    print("Validation failed:", e)
```

---

### 3. Making agents robust with LLM APIs

When calling LLM APIs (e.g., OpenAI, Anthropic, DeepSeek, etc.), models sometimes return text with extra explanations, not pure JSON. To handle this:

* **Trim JSON with regex**: Extract the first valid `{...}` block before `json.loads`.
* **Retry strategy**: If parsing fails, send a follow-up prompt like *“Return only valid JSON conforming to this schema”*.
* **Use `response_format="json"` (if API supports it)**: Some APIs can enforce structured JSON output.

---

### 4. Putting it together for agents

```python
def safe_parse_json(llm_output: str, schema=None):
    import re
    import json
    from jsonschema import validate, ValidationError

    # Extract JSON block (naive but useful)
    match = re.search(r'\{.*\}', llm_output, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in output")
    
    try:
        data = json.loads(match.group())
        if schema:
            validate(instance=data, schema=schema)
        return data
    except Exception as e:
        raise ValueError(f"Invalid JSON: {e}")
```

Now your agent can safely parse and validate any LLM JSON output.

---

👉 Do you want me to show you a **full example** where an agent calls an LLM API, gets JSON back, and runs validation (with retry if invalid)?