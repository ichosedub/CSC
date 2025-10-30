def create_messages(messages):
    send_messages = []
    for text in messages:
        send_messages.append(f"They texted {text.title()}")
        return send_messages
    
def show_messages(messages):
        for text in messages:
            print(text)

messages = ["Hey man", "How are you doing?", "Have a goodnight"]
send_messages = create_messages(messages)
show_messages(messages)

print("Previous Messages:")
show_messages(messages)

print("\nSend Messages:")
show_messages(send_messages)
