import requests
import json
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


class Search:
    def __init__(self):
        self.search_header = {
            "X-API-KEY": os.getenv("SERPER_API_KEY"),
            "Content-Type": "application/json",
        }
        self.llm = OpenAI(temperature=0)
        self.search_url = "https://google.serper.dev/videos"

    def invoke(self, input):
        agent_input = self.llm.invoke(self.youtube_prompt(input))
        agent_input = agent_input.replace('"', "")
        return self.youtube_search(agent_input)

    def youtube_search(self, query):
        payload = json.dumps(
            {
                "q": query,
            }
        )

        response = requests.request(
            "POST", self.search_url, headers=self.search_header, data=payload
        )

        return response.json()["videos"][0]["link"]

    def youtube_prompt(agent_output):
        return (
            "Turn the following answer into a Youtube query that we can lookup on Youtube: \n\n"
            + agent_output
            + "\n\n"
        )


# answer = "Jimmy Butler's best game against the Celtics in 2021 was on March 30, 2022. He was playing for the Heat. In that game, he scored 24 points, had 3 rebounds, and 2 assists."


# # agent_input = llm.invoke(prompt)
# # agent_input = agent_input.replace('"', "")

# print("YOUTUBE QUERY", agent_input)
