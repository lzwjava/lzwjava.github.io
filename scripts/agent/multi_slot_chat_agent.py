import pyperclip
import os

def save_to_file(content, filename="answer.md"):
    with open(filename, "a") as f:
        f.write(content + "\n\n")

prompts = [None] * 5

def main():
    print("Hello! I'm GitHub Copilot. Manage up to 5 concurrent interactions.")
    print("Commands:")
    print("- setN: <prompt> to set prompt for slot N (1-5), e.g., set1: Hello world")
    print("- pN to view prompt for slot N")
    print("- cN to copy prompt for slot N to clipboard")
    print("- iN to retrieve the copied answer from clipboard for slot N and save")
    print("- exit or quit to stop")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if user_input.startswith("set"):
            try:
                parts = user_input[3:].split(":", 1)
                if len(parts) == 2:
                    num_str, text = parts
                    num = int(num_str.strip()) - 1
                    if 0 <= num < 5:
                        prompts[num] = text.strip()
                        print(f"Prompt set for slot {num+1}")
                    else:
                        print("Slot must be 1-5")
                else:
                    print("Invalid format. Use setN: prompt")
            except ValueError:
                print("Invalid set command")

        elif user_input.startswith("p"):
            try:
                num = int(user_input[1:]) - 1
                if 0 <= num < 5:
                    if prompts[num] is not None:
                        print(f"Prompt for {num+1}: {prompts[num]}")
                    else:
                        print(f"No prompt set for slot {num+1}")
                else:
                    print("Slot must be 1-5")
            except ValueError:
                print("Invalid p command")

        elif user_input.startswith("c"):
            try:
                num = int(user_input[1:]) - 1
                if 0 <= num < 5:
                    if prompts[num] is not None:
                        pyperclip.copy(prompts[num])
                        print(f"Copied prompt for slot {num+1} to clipboard. Paste into chatbot, copy answer when ready.")
                    else:
                        print(f"No prompt set for slot {num+1}")
                else:
                    print("Slot must be 1-5")
            except ValueError:
                print("Invalid c command")

        elif user_input.startswith("i"):
            try:
                num = int(user_input[1:]) - 1
                if 0 <= num < 5:
                    if prompts[num] is not None:
                        answer = pyperclip.paste()
                        if answer:
                            print(f"Retrieved answer for slot {num+1} from clipboard.")
                            interaction = f"**Slot {num+1} User Input:**\n{prompts[num]}\n\n**Chatbot Answer:**\n{answer}\n{'-'*50}"
                            save_to_file(interaction)
                            print("Saved to answer.md. You can reuse or set a new prompt for this slot.")
                        else:
                            print("Clipboard is empty")
                    else:
                        print(f"No prompt set for slot {num+1}")
                else:
                    print("Slot must be 1-5")
            except ValueError:
                print("Invalid i command")

        else:
            print("Unknown command. Use setN:, pN, cN, iN, exit")

if __name__ == "__main__":
    main()