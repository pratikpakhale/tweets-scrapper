import google.generativeai as genai
import os
import json
import re
import time

def extract_json(input_string):
    if isinstance(input_string, dict):
        return input_string

    try:
        return json.loads(input_string)
    except json.JSONDecodeError:
        json_matches = re.findall(r'{(?:[^{}\\]|\\.)*}', input_string)
        if json_matches:
            try:
                return json.loads(json_matches[0])
            except json.JSONDecodeError:
                return None
        else:
            return None

genai.configure(api_key="**********************************")

model = genai.GenerativeModel('gemini-1.0-pro')

prompt = """SYSTEM : You are an agent used for sentiment/emotion analysis on IPL tweet texts.
You are provided with a tweet text and you are supposed to respond with it's sentiment intensity (-5 being completely negative, 5 being completely positive and 0 being neutral ), emotion state (available emotions are - happiness, sadness, anger, fear, surprise, love). Consider the language, use of emoijis and other factors as well for the analysis.

The tweet may mention IPL players as well, now record the tweets impression regarding the player with same sentiment and emotion format just like the tweet. A tweet may have multiple player mentions. So consider it as an array of analysis.

IT is highly possible that the tweet is not IPL related and could be SPAM, in that case respond with sentiment value of 0 and emotion value of "spam", the players array must be empty.

STRICTLY RESPOND IN JSON FORMAT ONLY

{{
  tweet: {{
    sentiment: "intensity from -5 to 5",
    emotion: "one from happiness, sadness, anger, fear, surprise, love, spam"
  }},
  players: [
    {{
      sentiment: "",
      emotion: "",.
      player_name: "the actual player name from IPL referred to",
    }}
  ]
}}

USER TWEET CONTENT: {tweet} 
"""

if not os.path.exists('results'):
    os.makedirs('results')

with open('data/DATA.json', 'r') as file:
    data = json.load(file)

try:
    with open('results/analysed.json', 'r') as analysed_file:
        analysed_data = json.load(analysed_file)
except FileNotFoundError:
    analysed_data = {}

def generate_and_save_content(key, element):
    if key not in analysed_data:
        response = model.generate_content(prompt.format(tweet=element['text']))
        print(extract_json(response.text))
        analysed_data[key] = extract_json(response.text)
        analysed_data[key]['text'] = element['text']

        with open('results/analysed.json', 'w') as outfile:
            json.dump(analysed_data, outfile, indent=4)
        return True
    else: return False
for key, element in data.items():
    print("trying", key)
    success = False
    retries = 5
    while not success:
        try:
            res = generate_and_save_content(key, element)
            success = True
            if res: time.sleep(0.5)
        except Exception as e:
            print(f"Error processing {key}: {e}")
            print("Retrying...")
            if "candidate.safety_ratings" in str(e):
                success = True
            time.sleep(1)
            retries = retries - 1
            if retries <= 0: success = True




