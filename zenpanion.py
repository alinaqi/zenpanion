import subprocess
import openai
import getpass
import readline  # Import readline module for command history
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

openai.api_key = api_key

def parse_command(user_input):
    if user_input.startswith("/ai"):
        # Extract command and parameters
        parts = user_input.split(maxsplit=1)
        command = parts[0][4:].strip()
        parameters = parts[1].strip() if len(parts) > 1 else ""
        return command, parameters
    else:
        return user_input, ""

def execute_command(command, parameters):
    if command:
        subprocess.run(f"{command} {parameters}", shell=True)  # Execute the command
    else:
        print("Invalid command. Please try again.")

def generate_command_from_natural_language(query):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a shell. Given user's query, generate a command to execute. For example, for a query like 'list files', return ls -l. Do not add any additional content. Just return executable commands that can be passed directly to the shell."},
            {"role": "user", "content": query}
        ]
        )
    generated_command = response.choices[0].message.content.strip()
    return generated_command

def main():
    username = getpass.getuser()
    prompt = f"{username}@zpy % "

    while True:
        try:
            # Use readline to enable arrow key navigation for command history
            user_input = input(prompt)
            if user_input.strip() == "quit":
                print("Exiting Zenpanion shell.")
                break
            if user_input.startswith("/ai"):
                generated_command = generate_command_from_natural_language(user_input)
                execute_command(generated_command, "")
            else:
                try:
                    execute_command(*user_input.split(" ", 1))
                except Exception as e:
                    print(f"<error>\nTrying to fix with AI..")
                    fixed_command = generate_command_from_natural_language(f"/ai {user_input}")

                    execute_command(fixed_command, "")
        except EOFError:  # Handle EOF (Ctrl+D) to exit the shell gracefully
            print("\nExiting zenpanion shell.")
            break
        except KeyboardInterrupt:  # Handle Ctrl+C gracefully
            print("\nKeyboard interrupt detected. Please use 'quit' command to exit.")
        except Exception as e:  # Catch and display any other exceptions
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()