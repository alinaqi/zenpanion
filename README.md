# Zenpanion Shell

Zenpanion is an AI-powered shell that enhances your command-line experience by translating natural language into shell commands using OpenAI's GPT models.

I made it early 2024 just as an experiment. I was curious if I could use LLMs to make a shell that is easier to use.

## Features

- Natural language command processing
- AI-powered command correction
- Command history navigation
- Graceful error handling
- Environment-based configuration

## Prerequisites

- Python 3.x
- OpenAI API key
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/alinaqi/zenpanion.git
cd zenpanion
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy the `.env.example` file to `.env`
   - Add your OpenAI API key to the `.env` file:
```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Zenpanion shell:
```bash
python zenpanion.py
```

2. Use natural language commands with the `/ai` prefix:
```bash
username@zpy % /ai list all files in current directory
username@zpy % /ai create a new directory called test
username@zpy % /ai show system information
```

3. Use regular shell commands without the `/ai` prefix:
```bash
username@zpy % ls -l
username@zpy % pwd
username@zpy % mkdir test
```

4. Exit the shell:
```bash
username@zpy % quit
```

## Error Handling

- If a regular command fails, Zenpanion will attempt to fix it using AI
- Ctrl+C is handled gracefully
- Ctrl+D (EOF) exits the shell cleanly

## Development

The project structure is organized as follows:
```
zenpanion/
├── README.md
├── requirements.txt
├── .env
├── .gitignore
└── zenpanion.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Security Notes

- Never commit your `.env` file
- Regularly rotate your API keys
- Review AI-generated commands before execution

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT API
- Python community for excellent libraries 