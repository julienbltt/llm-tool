import lmsClass

def main():
    model_ID = input(
        "Enter a model id (some fast models: google/gemma-3-4b, mistral-7b-instruct-v0.1, phi-3-mini-4k-instruct, google/gemma-3-4b, gemma-2-2b-it)\n"
    )          
    system_prompt = input(
        "Enter a system prompt (for instance: 'Answer with only one sentence.'):\n"
    )

    llm = lmsClass.LMStudioResponder(model_name=model_ID,system_prompt=system_prompt) 

    while True:
        prompt = input("Enter your message: ")
        response = llm.respond_and_speak(prompt)


if __name__ == "__main__":
    main()