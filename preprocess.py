import pandas as pd
import numpy as np

df = pd.read_csv('channel.csv', sep=',', header=None).to_numpy()
df = df[1:] # ignore the first line with the field names AuthorID,Author,Date,Content,Attachments,Reactions
authors = df[:,1].astype('str') # author is field index 1
messages = df[:,3].astype('str') # content is field index 3

codenames = {
  "Alice#2027": "A",
  "Bob#1091": "B",
  "Charlie#7181": "C"
} # change this based on the users in your channel. exclude bots that you don't want to be included in the GPT output.

dialogue = "\""
for i in range(messages.shape[0]):
  try:
    # in this line, we will:
    # 1) use the "code name" for this user (use a unique initial like A, B, C)
    # 2) replace newlines with spaces, and double quotes with single quotes, so that the resulting CSV format is valid
    dialogue += codenames[users[i]]+": "+messages[i].replace('\n',' ').replace("\"", "'")+" "
    # the result will look like B: hi, nice to meet u
    if i % 64 == 63: # after every 64 messages,
      dialogue += "\",\n\"" # end this line of the CSV and start a new conversation block
  except KeyError: continue # ignore users that are not in the `codenames` dict
dialogue += "\"," # complete the last line of the CSV

# write the result to disk
file = open('discord.csv', 'w+')
file.write("Conversation,\n") # include a basic CSV header. we only need one field for this task.
file.write(dialogue)
file.close()
