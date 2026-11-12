from langchain_openai import ChatOpenAI

def main():
    # LangSmith tracing is enabled through environment variables,
    # so there is NO tracing code here.
    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0 )

    prompts = [
        "What is artificial intelligence? Explain in 2 sentences.",
        "What are the three main benefits of cloud computing?",
        "Write a short motivational message for a student learning Python."
    ]

    for i, prompt in enumerate(prompts, start=1):
        response = model.invoke(prompt)

        print(f"\n--- Prompt {i} ---")
        print(f"Question: {prompt}")
        print(f"Answer: {response.content}")


if __name__ == "__main__":
    main()