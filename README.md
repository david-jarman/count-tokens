# Token Counter

Token Counter is a Python-based command-line tool to estimate the number of tokens in a given text using OpenAI's `tiktoken` library. It supports direct text input and piped input, making it versatile for various use cases.

---

## Features
- Tokenize text input based on OpenAI models (default: `gpt-4o`).
- Supports text input via arguments or piping.
- Configurable to use different tokenization models.

---

## Installation

### Install from Source

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd token_counter
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the tool locally:
   ```bash
   pip install .
   ```

### Install from PyPI
*(Optional: After publishing to PyPI)*
```bash
pip install token-counter
```

---

## Usage

### Run Installed Tool

Once installed, you can use the tool from anywhere:

1. Tokenize text passed as an argument:
   ```bash
   token-counter "This is a test."
   ```

2. Tokenize piped input:
   ```bash
   echo "This is a test." | token-counter
   ```

3. Specify a model (optional):
   ```bash
   token-counter "This is a test." --model gpt-4
   ```

### Run Locally Without Installation

1. Navigate to the project directory:
   ```bash
   cd token_counter
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Run the script directly:
   ```bash
   python -m token_counter "This is a test."
   ```

4. Test with piped input:
   ```bash
   echo "This is a test." | python -m token_counter
   ```

---

## Development

### Build the Project

1. Ensure you have the `build` module installed:
   ```bash
   pip install build
   ```

2. Build the project:
   ```bash
   python -m build
   ```

3. The built packages will be available in the `dist/` directory.

### Test Installation Locally

1. Install the package:
   ```bash
   pip install dist/token_counter-0.1.0-py3-none-any.whl
   ```

2. Run the tool:
   ```bash
   token-counter "Test text."
   ```

---

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and open a pull request.

---

## License

This project is licensed under the MIT License.

