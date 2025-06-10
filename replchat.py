# -*- coding: utf-8 -*-

#REPLchat.py
#import necessary libs
from openai import OpenAI
from pathlib import Path

import os

#REPL chat class does the following :
# Initialize the chat obejct with the api key.
#    Input : API key
# get_response: calls the open ai service via api client
# Input: the question from user or communications
# return: The response or error from the use in key : value format
# keepchatting : Keeps the link active for the continius communication
# When use enters exit the bit shuts down.
# Invoke the open ai service to request response for the use input
# if there are errors perculate them
#if none, send the response back.


class REPLChat:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def get_response(self, input_text):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": input_text}]
        )
        return response.choices[0].message.content # i wish there was  better way to do this.

    def keepchating(self):
        print("Welcome to REPL Chat bot. Enter your query or 'exit' to quit")

        while 1:
          user_input = input('Guest: ').strip()

          if user_input.lower() == 'exit':
            print ("thanks good night and good luck")
            break
          try:
            response = self.get_response(user_input)
            print("\n REPL Botman:", response)
          except Exception as e:
            print(f"Error: {str(e)}")

# Navigate to the input file path and validate it
# If the path exists
def load_api_key(file_path):
    try:
        path = Path(file_path).resolve()
        if not path.exists():
            raise FileNotFoundError(f"No such file. Enter the correct file path: {path}")
        if not path.is_file():
            raise ValueError(f"You did not enter the correct file path. This coudk be a directory: {path}")

        api_key = path.read_text().strip()
        if not api_key:
            raise ValueError("API key file is empty. Try entering a better one")

        return api_key

    except Exception as e:
        raise Exception(f"Failed to load API key: {e}")


def main():
    # Get API key file path from user
    try :
      print("User: welcome to REPl Chat bot. I will be using two libs for this assignment. \n")
      print(" openai and pathlib. If you dont have these installed in you Python env, please do so before using this app \n")
      file_path = input("Enter the file path to your OpenAI API key file: Dont add quotes").strip()
      api_key = load_api_key(file_path)

    except Exception as e:
        print(f"Failed to load API key: {e}")
        return

    chat = REPLChat(api_key)
    chat.keepchating()
if __name__ == "__main__":
    main()