import csv
import json
import pandas as pd
import numpy as np
import re
import string
from collections import Counter
import openai
from openai import OpenAI
import os
import time
import ast

"""
Before running this file run:

pip3 install --upgrade openai
pip3 install nest_asyncio
"""

# SET UP YOUR OPENAI CLIENT
def set_openai_env(api_key):
  os.environ['OPENAI_API_KEY'] = api_key # SET YOUR OWN API KEY

  api_key = os.getenv("OPENAI_API_KEY")
  if api_key is None:
      raise ValueError("Please set the OPENAI_API_KEY environment variable.")
    
  #print(api_key) # test that this env var was set
  
  client = openai.OpenAI(api_key=api_key)
  return client


def api_call(model='gpt-4-vision-preview'):
  openai.api_key = os.getenv("OPENAI_API_KEY")
  response = CLIENT.chat.completions.create(
    model=model, 
    messages=[
    {"role": "system", "content": "You are an expert at identifying objects in landscape images."},
    {"role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=1024,
  )
  response_content = response.choices[0].message.content
  return response_content

CLIENT = set_openai_env('')
print(api_call())

