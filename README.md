# DiscordGPT
Use data from Discord in a GPT model and talk to a simulation of you and your friends. Details and tutorial [on my website](http://www.harysdalvi.com/discord).

Before running this project, you should use the [Discord Chat Explorer](https://github.com/Tyrrrz/DiscordChatExporter) to generate your own `channel.csv` file from one of your Discord servers. It's recommended to run `preprocess.py` locally, put the resulting file on your Google Drive, and then use it with `discordgpt.ipynb` on Google Colab.

## Acknowledgements
I would like to thank the Brown Machine Intelligence Community, whose GPT workshop and code at Brown University were instrumental for me to train the model here. I would also like to thank the [Discord Chat Explorer](https://github.com/Tyrrrz/DiscordChatExporter) and [Hugging Face](https://huggingface.co) for Discord data collection and GPT-2 model templates.