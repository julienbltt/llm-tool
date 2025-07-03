from llm import LMStudioResponder
from tts import talk_stream

def main():
    model_ID = input("Enter a model id:\n")
    system_prompt = input("Enter a system prompt:\n")

    llm = LMStudioResponder(model_name=model_ID, system_prompt=system_prompt)

    while True:
        prompt = input("Enter your message: ")
        stream = llm.respond(prompt)
        response = talk_stream(stream)
        print(">>", response)

if __name__ == "__main__":
    main()
