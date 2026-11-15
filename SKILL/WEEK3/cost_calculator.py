
# Example rates per 1 million tokens.
# These are sample rates. Verify actual pricing before using them.

PRICING = {
    "gemini-2.5-flash": {
        "input": 0.50,
        "output": 2.00
    }
}


def calculate_cost(provider, model, input_tokens, output_tokens):

    # Ollama runs locally and has no hosted API token charge.
    if provider in ("Ollama", "OllamaProvider"):
        return 0.0

    rates = PRICING.get(model)

    if rates is None:
        return None

    input_cost = (
        input_tokens * rates["input"]
    ) / 1_000_000

    output_cost = (
        output_tokens * rates["output"]
    ) / 1_000_000

    return round(input_cost + output_cost, 10)
