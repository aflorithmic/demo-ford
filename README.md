# 1. What is it for

This is a custom demo template to create a voice over video with the voice, sound template, and text of your choice. 

For example: 

```voice = "voice of your choice"```
```speed = 110 - choose the voice speed```
```soundTemplate = "sound design of your choice"```

# 2. How it works

First we create an audio file with the chosen text, voice, mastering presets and sound template.
Then we overlay the created audio onto video. 

# 3. How to run - instructions:

Then open your code editor and install the following packages: 
1. ```pip3 -r requirements.txt```
2. Get your API_KEY from [API.audio console](https://console.api.audio/)
3. Add .env file to your project root directory and add your API_KEY=****************************
4. Make sure that you added all the values to the variables (voice, speed, soundTemplate) (For more voices and sound templates visit our [Voice & Sound library](https://library.api.audio/voices)
5. To render your python script: Open your terminal at your project and type in: python3 main.py
6. Your files will be saved in your project directory

