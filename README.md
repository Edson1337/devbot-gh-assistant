# DevBot GitHub Assistant

A GitHub operations assistant that uses an LLM agent with Model Context Protocol (MCP) tool servers.

## Description

This project is a GitHub operations assistant that utilizes a Large Language Model (LLM) agent integrated with Model Context Protocol (MCP) tool servers to automate and facilitate various GitHub-related tasks.

## Prerequisites

- **Python 3.8+** (Python 3.11 or higher recommended)
- **UV Package Manager** - Install from: [UV Getting Started - Installation](https://docs.astral.sh/uv/getting-started/installation/)

To check your Python version:
```bash
python --version
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Edson1337/devbot-gh-assistant.git
   cd devbot-gh-assistant
   ```

2. **Install dependencies using UV:**
   ```bash
   uv sync
   ```

3. **Activate the virtual environment:**
   ```bash
   uv shell
   ```

## Usage

```bash
# Run the assistant
uv run python main.py
```

## Configuration

Configure the necessary environment variables:

```bash
# Example configuration
export GITHUB_TOKEN="your_token_here"
export OPENAI_API_KEY="your_api_key_here"
```

## Features

- 🤖 LLM agent for GitHub operations
- 🔧 Model Context Protocol (MCP) tool servers integration
- 📋 Automation of repetitive tasks
- ⚡ Fast and efficient processing
- 🔗 Complete GitHub API integration

## Demo Repository

Check out a practical demonstration of this assistant's capabilities in the [MCP Test Repository](https://github.com/Edson1337/mcp-test), where the following operations were successfully automated:

- ✅ **Repository Creation** - Created a new repository from scratch
- ✅ **Branch Management** - Created and managed feature branches
- ✅ **File Operations** - Uploaded and managed files through the assistant
- ✅ **Pull Request Workflow** - Opened and merged pull requests automatically
- ✅ **Issue Management** - Created and closed issues programmatically

This demo showcases the real-world capabilities of the DevBot GitHub Assistant in automating common GitHub workflows.

## Architecture

This assistant leverages Model Context Protocol (MCP) servers to provide specialized tools and capabilities, enabling seamless interaction with GitHub's ecosystem through standardized interfaces.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.