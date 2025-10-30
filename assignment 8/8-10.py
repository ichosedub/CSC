def create_messages(messages):
    sent_messages = []
    for text in messages:
        sent_messages.append(f"They texted {text.title()}")
        return sent_messages
    
def show_messages(messages):
        for text in messages:
            print(text)

messages = ["Hey man", "How are you doing?", "Have a goodnight"]
sent_messages = create_messages(messages)
show_messages(sent_messages)