from agent import analyze_data

while True:
    question = input("Ask your question: ")
    answer = analyze_data(question)
    print(answer)




