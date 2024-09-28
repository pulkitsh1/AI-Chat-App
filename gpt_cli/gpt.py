from dotenv import load_dotenv, set_key, dotenv_values
import os
import openai
import typer


SYSTEM_MESSAGE = """
Provide short, concise answers to the user's questions.
"""
env_path = ".env"
load_dotenv(env_path)

app = typer.Typer()

@app.command()
def run(args: str = typer.Argument(..., help="Question to ask ChatGPT")):
    print(f"Q: {args}")
    chat_history = []
    ask_gpt(args, chat_history, SYSTEM_MESSAGE)

    user_input = input(">_: ")
    while user_input != "":
        ask_gpt(user_input, chat_history, SYSTEM_MESSAGE)
        user_input = input(">_: ")
    print("Ending Session")


@app.command()
def help():
    help_str = """
    Usage: gpt [Command] [Args]...
    
    Commands:
        run : run command is used for getting any type of imformation from ChatGPT.
        addkey : addkey command is used for adding Open AI key to env file to connect it to ChatGPT.
        help : help command is to get to know about different types of commands in this CLI tool.
        
    Args:
        run [args] : args receives a question which we want to ask ChatGPT.
        addkey [args] : args receives a key of OpenAI.
        help : help doesn't receive any args.
        """
    print(help_str)


@app.command()
def addkey(value: str = typer.Argument(..., help="OpenAI key to add to the .env file")):
    if not os.path.exists(env_path):
        raise FileNotFoundError(f"{env_path} not found")
    
    env_values = dotenv_values(env_path)

    env_values["GPT_KEY"] = value

    with open(env_path, 'w') as file:
        for k, v in env_values.items():
            file.write(f"{k}={v}\n")
    print("Key Successfully Added!")

def ask_gpt(prompt: str, chat_history: list, system_message: str):
    openai.api_key = os.getenv("GPT_KEY")

    if not openai.api_key:
        print("GPT_KEY not found in the environment. Please set it using the 'addkey' command.")
        return

    user_prompt = {"role": "user", "content": prompt}
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            *chat_history,
            user_prompt,
        ],
    )

    content = response["choices"][0]["message"]["content"]
    chat_history.append(user_prompt)
    chat_history.append({"role": "assistant", "content": content})

    # Print the text in a green color.
    print("\033[92m" + content + "\033[0m")
    return content


def main():
    app()

if __name__ == "__main__":
    main()