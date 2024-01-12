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
        yt_query = self.llm.invoke(self.youtube_prompt(input))
        yt_query = yt_query.replace('"', "")
        return self.youtube_search(yt_query)

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

    def youtube_prompt(self, agent_output):
        return (
            "Turn the following answer into a Youtube query that we can lookup on Youtube: \n\n"
            + agent_output
            + "\n\n"
        )
