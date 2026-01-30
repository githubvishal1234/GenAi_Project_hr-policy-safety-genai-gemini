BLOCKED_PATTERNS = [
    "ignore previous",
    "ignore rules",
    "salary",
    "confidential",
    "employee data",
    "admin access",
    "override",
    "pretend",
    "internal data"
]

def is_unsafe(user_input: str) -> bool:
    user_input = user_input.lower()
    return any(p in user_input for p in BLOCKED_PATTERNS)


def refusal_message() -> str:
    return (
        "I’m sorry, I can’t help with that request. "
        "I can assist with general HR policies or direct you to HR support."
    )
