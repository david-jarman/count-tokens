import argparse
import sys
import tiktoken

def count_tokens(text, model="gpt-4o"):
    """
    Counts the number of tokens in a given text for a specified model.

    Parameters:
        text (str): The input text to tokenize.
        model (str): The OpenAI model whose tokenizer should be used (default: gpt-4o).

    Returns:
        int: The estimated number of tokens in the text.
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print(f"Model '{model}' not recognized. Falling back to default encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")

    return len(encoding.encode(text))

def main():
    parser = argparse.ArgumentParser(description="Count tokens in a text input using the OpenAI Tiktoken library.")
    parser.add_argument("text", nargs="?", type=str, help="The text to analyze for token count.")
    parser.add_argument("--model", type=str, default="gpt-4o", help="The model to use for tokenization (default: gpt-4o).")

    args = parser.parse_args()

    # Read from pipe if no text argument is provided
    if not args.text:
        if not sys.stdin.isatty():
            args.text = sys.stdin.read().strip()
        else:
            parser.print_help()
            sys.exit(1)

    token_count = count_tokens(args.text, args.model)
    print(f"The text contains approximately {token_count} tokens.")
