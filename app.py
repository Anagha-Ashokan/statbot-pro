from agent import analyze_data
from sandbox import check_security
import json
chat_history = []

print("StatBot Pro Started")
print("Type your question (type exit to stop)\n")


while True:
    question = input("Ask your question: ")
    if question.lower() == "exit":
        break
    if not check_security(question):
        print("⚠️ Security Alert: Malicious request blocked!")
        continue
    print("Agent Thinking...")
    print("Step 1: Understanding the question")
    print("Step 2: Analyzing dataset")
    print("Step 3: Generating result\n")
    answer = analyze_data(question)
    chat_history.append({
        "question":question,
        "answer":answer
    })
    with open("chat_history.json", "w") as f:
        json.dump(chat_history, f, indent=4)
    print("Answer",answer)
    





                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                






