import pyperclip
from scripts.translation.openrouter_client import call_openrouter_api

def save_to_file(content, filename="answer.md"):
    with open(filename, "a") as f:
        f.write(content + "\n\n")

# Dictionary to store sessions, each with a name and prompt
sessions = {}
current_session = None

def main():
    print("Hello! I'm GitHub Copilot. Manage multiple AI chat sessions.")
    print("Commands:")
    print("- new <name>: Create a new session with given name")
    print("- list: List all sessions")
    print("- a <name>: Attach to a session")
    print("- set <prompt>: Set prompt for current session")
    print("- p: View prompt for current session")
    print("- c: Copy prompt for current session to clipboard")
    print("- ask: Send prompt to AI and get response for current session")
    print("- exit or quit: Stop the program")

    global current_session
    while True:
        session_info = f"Current Session: {current_session if current_session else 'None'}"
        user_input = input(f"{session_info} You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if user_input.startswith("new "):
            name = user_input[4:].strip()
            if name:
                if name not in sessions:
                    sessions[name] = None
                    print(f"Created session: {name}")
                else:
                    print(f"Session {name} already exists")
            else:
                print("Please provide a session name")

        elif user_input == "list":
            if sessions:
                print("Sessions:")
                for name in sessions:
                    status = "Attached" if name == current_session else ""
                    print(f"- {name} {status}")
            else:
                print("No sessions available")

        elif user_input.startswith("a "):
            name = user_input[2:].strip()
            if name in sessions:
                current_session = name
                print(f"Attached to session: {name}")
            else:
                print(f"Session {name} does not exist")

        elif user_input.startswith("set "):
            if current_session:
                prompt = user_input[4:].strip()
                sessions[current_session] = prompt
                print(f"Prompt set for session {current_session}")
            else:
                print("No session attached. Use 'a <name>' to attach to a session")

        elif user_input == "p":
            if current_session:
                if sessions[current_session] is not None:
                    print(f"Prompt for {current_session}: {sessions[current_session]}")
                else:
                    print(f"No prompt set for session {current_session}")
            else:
                print("No session attached. Use 'a <name>' to attach to a session")

        elif user_input == "c":
            if current_session:
                if sessions[current_session] is not None:
                    pyperclip.copy(sessions[current_session])
                    print(f"Copied prompt for session {current_session} to clipboard.")
                else:
                    print(f"No prompt set for session {current_session}")
            else:
                print("No session attached. Use 'a <name>' to attach to a session")

        elif user_input == "ask":
            if current_session:
                if sessions[current_session] is not None:
                    prompt = sessions[current_session]
                    print(f"Sending prompt to AI for session {current_session}...")
                    try:
                        answer = call_openrouter_api(prompt)
                        if answer:
                            interaction = f"**Session {current_session} User Input:**\n{prompt}\n\n**AI Response:**\n{answer}\n{'-'*50}"
                            save_to_file(interaction)
                            print("Received response from AI and saved to answer.md.")
                        else:
                            print("No response received from AI.")
                    except Exception as e:
                        print(f"Error calling AI API: {e}")
                else:
                    print(f"No prompt set for session {current_session}")
            else:
                print("No session attached. Use 'a <name>' to attach to a session")

        else:
            print("Unknown command. Use new, list, a, set, p, c, ask, exit")

if __name__ == "__main__":
    main()