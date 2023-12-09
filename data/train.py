from openai import OpenAI
client = OpenAI(api_key="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")

client.files.create(
  file=open("data-tune.jsonl", "rb"),
  purpose="fine-tune"
)


client.fine_tuning.jobs.create(
  training_file="file-KnBKrC2kG1o1E7XnPXB9dTtc", 
  model="gpt-3.5-turbo-1106"
)

client.fine_tuning.jobs.list(limit=10)

# Retrieve the state of a fine-tune
client.fine_tuning.jobs.retrieve("ftjob-WGs2J1qg2VqGPnrwQhLjMdOn")

