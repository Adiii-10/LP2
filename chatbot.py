def chatbot():
    responses = {
        "hello": "Hi! How can I help you?",
        "hi": "Hello! What do you need?",
        "order": "Track your order using order ID.",
        "refund": "Refund takes 5-7 days.",
        "delivery": "Delivery takes 3-5 days.",
        "payment": "We accept UPI, cards, net banking."
    }

    print("🤖 Chatbot started (type 'exit' to quit)\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("🤖 Bye!")
            break

        found = False
        for key in responses:
            if key in user:
                print("🤖", responses[key])
                found = True
                break

        if not found:
            print("🤖 Sorry, I didn’t understand.")

chatbot()
