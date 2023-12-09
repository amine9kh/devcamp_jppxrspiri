from openai import OpenAI
import openai
import json
import time
client = OpenAI(api_key='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')


# def gpt_process(string_value):
#     completion = client.chat.completions.create(model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a knowledgeable assistant specialized in e-commerce and social media marketing. Provide detailed and creative strategies."},
#         {"role": "user", "content": string_value}
#     ])

#     return str(completion.choices[0].message.content)

# print(gpt_process("I want to sell my product on Facebook and Instagram. What should I do?"))

with open("Data46.jsonl", "r") as f:
    training_data=json.load(f)
    # Initialize a new model with the base model you want to fine-tune 
    model="gpt-3.5-turbo-1106"
    fine_tuned_model= OpenAI.Model.create(
    model=model,
    fine_tune=True,
    training_data=training_data
    )
    # Wait for the model to finish fine-tuning 
    while fine_tuned_model.status()["data"]["ready"] is False:
        time.sleep(30)
        fine_tuned_model=OpenAI.Model.retrieve(fine_tuned_model.id)
        print("Fine-tuning complete")