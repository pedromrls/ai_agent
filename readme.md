# LLM Code Assistant

A powerful Python-based code assistant that leverages Large Language Models (LLMs) to analyze, debug, and enhance codebases through structured function calls and intelligent code understanding.

## Overview

This project demonstrates how to safely integrate LLMs with Python applications by providing them with controlled access to filesystem operations and code analysis capabilities. The assistant can examine your codebase, suggest improvements, identify bugs, and even propose new features while maintaining security through restricted function access.

## Features

### Core Functionality
- **File System Integration**: Safe reading, writing, and analysis of files and directories
- **Code Execution**: Controlled Python file execution within the working directory
- **Structured Tool Schema**: Clean interface between LLM reasoning and Python execution
- **Intelligent Code Analysis**: Examination of code structure, patterns, and potential issues

### Safety & Security
- Sandboxed execution environment
- Directory traversal protection
- Controlled function access scope
- Safe file operation boundaries

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/llm-code-assistant.git
cd llm-code-assistant

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/llm-code-assistant.git
cd llm-code-assistant

# Install dependencies (using uv since you have uv.lock)
uv sync

# Or if using pip
pip install -e .
```

## Configuration

```bash
# Set up your environment variables
export GEMINI_API_KEY="your-gemini-api-key-here"

# Or create a .env file
echo "GEMINI_API_KEY=your-gemini-api-key-here" > .env
```

## Usage

### Basic Setup

```python
# Since your project uses individual function modules, import what you need
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from call_function import call_function
import config

# Your main interaction would be through main.py
```

### Running the Assistant

```bash
# Run the main application
python main.py

# Test the individual functions
python -c "from functions.get_files_info import get_files_info; print(get_files_info('.'))"

# Run basic functions tests 
python tests.py
```

### Example Usage

```python
# Example of how the functions might be used
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# List files in current directory
files = get_files_info(".")
print(files)

# Read a specific file
content = get_file_content("main.py")
print(content)
```

### Example Interactions

The assistant can help with various coding tasks:

- **Bug Detection**: Identifies syntax errors, logic issues, and potential runtime problems
- **Code Review**: Suggests improvements for readability, performance, and best practices
- **Refactoring**: Proposes structural improvements and code organization
- **Feature Development**: Assists in implementing new functionality

## Configuration

```python
# config.py
CONFIG = {
    "llm_provider": "gemini",
    "model": "gemini-pro",
    "max_tokens": 4096,
    "temperature": 0.1,
    "working_directory": "./",
    "allowed_extensions": [".py", ".js", ".ts", ".java", ".cpp"],
    "max_file_size": 1024 * 1024,  # 1MB
    "safety_checks": True
}
```

## Project Structure

```
.
├── .gitignore
├── .python-version
├── calculator/                # Example project for testing
│   ├── README.md
│   ├── lorem.txt
│   ├── main.py
│   ├── pkg/
│   │   ├── calculator.py
│   │   ├── morelorem.txt
│   │   └── render.py
│   └── tests.py
├── call_function.py           # Function calling logic
├── config.py                 # Configuration settings
├── functions/                # Available LLM functions
│   ├── get_file_content.py   # Read file contents
│   ├── get_files_info.py     # List files and directories
│   ├── run_python_file.py    # Execute Python files
│   └── write_file.py         # Write/modify files
├── main.py                   # Main application entry point
├── prompts.py                # LLM prompt templates
├── pyproject.toml            # Project dependencies and metadata
├── readme.md                 # This file
├── tests.py                  # Test suite
└── uv.lock                   # Dependency lock file
```

## Future Enhancements

### Advanced Code Analysis
- **Complex Bug Detection**: Enhanced capability to identify and fix sophisticated bugs across multiple files
- **Intelligent Refactoring**: Automated refactoring of large code sections while maintaining functionality
- **Feature Development**: Complete implementation of new features from requirements to testing

### LLM Integration Improvements
- **Multiple LLM Providers**: Support for OpenAI, Anthropic, Cohere, and other major providers
- **Model Flexibility**: Integration with different Gemini models and performance optimization
- **Extended Function Library**: Broader range of tools for code manipulation, testing, and deployment

### Enhanced Capabilities
- **Multi-Codebase Support**: Ability to work across different projects and repositories
- **Advanced Security**: Enhanced sandboxing and permission management
- **Integration Tools**: Direct integration with popular IDEs and development workflows

### Experimental Features
- **Automated Testing**: Generation and execution of unit tests
- **Documentation Generation**: Automatic creation of code documentation
- **Performance Analysis**: Code profiling and optimization suggestions
- **Dependency Management**: Smart package and dependency recommendations

## Security Considerations

⚠️ **Important Security Notice**

This tool provides LLMs with controlled access to your filesystem and Python interpreter. While designed with safety in mind, always:

- Commit your changes before running the agent
- Review all suggested modifications before applying them
- Test in isolated environments when possible
- Never share this tool with untrusted parties
- Be cautious when extending filesystem permissions

## Contributing

```bash
# Fork the repository and create a feature branch
git checkout -b feature/your-feature-name

# Make your changes and test them
python -m pytest tests/

# Submit a pull request
```

Please ensure all contributions follow the existing code style and include appropriate tests.

## License

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Acknowledgments

This project serves as an educational demonstration of LLM-Python integration patterns and safe AI-assisted development practices.

---

**Disclaimer**: This is a toy implementation designed for learning purposes. For production use, consider established tools like Cursor IDE, Zed's Agentic Mode, or Claude Code, which offer more robust security and feature sets.