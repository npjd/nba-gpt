from langchain_community.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.schema import Document
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from example_query import few_shots
from langchain.agents.agent_toolkits import create_retriever_tool
import os

load_dotenv()

tool_description = """
This tool will help you understand similar examples to adapt them to the user question.
Input to this tool should be the user question.
"""

custom_suffix = """
I should first get the similar examples I know.
If the examples are similar enough to construct the query I need, I can build it.
Otherwise, I can then look at the tables in the database to see what I can query.
Then I should query the schema of the most relevant tables.
"""


class Agent:
    def __init__(self, verbose=True, open_ai_model="gpt-4") -> None:
        self.db = SQLDatabase.from_uri(os.getenv("DATABASE_URI"))
        self.llm = ChatOpenAI(model_name=open_ai_model, temperature=0)
        self.embeddings = OpenAIEmbeddings()
        few_shot_docs = [
            Document(page_content=question, metadata={"sql_query": few_shots[question]})
            for question in few_shots.keys()
        ]

        vector_db = FAISS.from_documents(few_shot_docs, self.embeddings)
        retriever = vector_db.as_retriever()

        self.retriever_tool = create_retriever_tool(
            retriever, name="sql_get_similar_examples", description=tool_description
        )
        self.custom_tool_list = [self.retriever_tool]
        
        self.agent_executor = create_sql_agent(
            llm=self.llm,
            toolkit=SQLDatabaseToolkit(db=self.db, llm=self.llm),
            verbose=verbose,
            agent_type=AgentType.OPENAI_FUNCTIONS,
            extra_tools=self.custom_tool_list,
            suffix=custom_suffix,
        )
        

    def invoke(self, input):
        return self.agent_executor.invoke(
            {"input": input}
        )
        