import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from scripts.translation.openrouter_client import call_openrouter_api

def save_to_file(content, filename="answer.md"):
    with open(filename, "a") as f:
        f.write(content + "\n\n")

# Dictionary to store sessions, each with a name and conversation history
sessions = {}
current_session = None

def main():
    print("Hello! I'm GitHub Copilot. Manage multiple AI chat sessions.")
    print("Commands:")
    print("- new <name>: Create a new session with given name")
    print("- list: List all sessions")
    print("- a <name>: Attach to a session")
    print("- ask <message>: Send message to AI for current session")
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
                    sessions[name] = []
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

        elif user_input.startswith("ask "):
            if current_session:
                message = user_input[4:].strip()
                if message:
                    # Ensure the message is not empty or just whitespace
                    if len(message.strip()) > 0:
                        sessions[current_session].append({"role": "user", "content": message})
                        print(f"Sending message to AI for session {current_session}...")
                        try:
                            conversation = sessions[current_session]
                            answer = call_openrouter_api(conversation)
                            if answer:
                                sessions[current_session].append({"role": "assistant", "content": answer})
                                interaction = f"**Session {current_session} User Input:**\n{message}\n\n**AI Response:**\n{answer}\n{'-'*50}"
                                save_to_file(interaction)
                                print("Received response from AI and saved to answer.md.")
                            else:
                                print("No response received from AI.")
                        except Exception as e:
                            print(f"Error calling AI API: {e}")
                    else:
                        print("Message is empty or contains only whitespace.")
                else:
                    print("Please provide a message to send.")
            else:
                print("No session attached. Use 'a <name>' to attach to a session")

        else:
            print("Unknown command. Use new, list, a, ask, exit")

if __name__ == "__main__":
    main()
