import os
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv


load_dotenv()

client = OpenAI(api_key=os.environ.get("API_KEY"))
model ="gpt-3.5-turbo-16k"

#chatBot = client.beta.assistants.create(
#    name = "Chat Bot",
    #instruction="You will help students learn about the AI Club",
#      model=model
#)

#assistant_id= chatBot.id
#print(assistant_id)

# Thread
# thread = client.beta.threads.create (
 #    messages=[
  #       {
   #          "role":"user",
    #         "content":"How I start managing my time"
  #       }
 #    ]
# ) 


#thread_id = thread.id
#print(thread_id)
assistant_id = os.environ.get("ASST_ID")
thread_id = os.environ.get("THREAD_ID")


# ==== Create a Message =====
message = "What is a AI club"
#message = client.beta.messages.create(
message = client.beta.threads.messages.create(
    thread_id = thread_id,
    role="user",
    content=message
)

#=== Run our Assistant
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as a student"
)
message = client.beta.threads.messages.list(thread_id = thread_id)
last_message = message.data[0]
response = last_message.content[0].text.value
print(response)



# === Run ===
        #wait_for_run_completion(client=client, thread_id=thread_id,
         #                        run_id=run.id)
# run_steps = client.beta.threads.runs.steps.list(
#     thread_id=thread_id, run_id=run.id
# )
# print(f"Steps----> {run_steps.data[0]}")