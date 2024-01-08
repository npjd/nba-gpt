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

db = SQLDatabase.from_uri("postgresql://nba_sql:nba_sql@localhost:5432/nba")

llm = ChatOpenAI(model_name="gpt-4", temperature=0)
embeddings = OpenAIEmbeddings()

few_shot_docs = [
    Document(page_content=question, metadata={"sql_query": few_shots[question]})
    for question in few_shots.keys()
]
vector_db = FAISS.from_documents(few_shot_docs, embeddings)
retriever = vector_db.as_retriever()


tool_description = """
This tool will help you understand similar examples to adapt them to the user question.
Input to this tool should be the user question.
"""

retriever_tool = create_retriever_tool(
    retriever, name="sql_get_similar_examples", description=tool_description
)
custom_tool_list = [retriever_tool]


custom_suffix = """
I should first get the similar examples I know.
If the examples are similar enough to construct the query I need, I can build it.
Otherwise, I can then look at the tables in the database to see what I can query.
Then I should query the schema of the most relevant tables.
"""


agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    extra_tools=custom_tool_list,
    suffix=custom_suffix,
)

agent_executor.invoke(
    {"input": "What is Lebrons worst game in the NBA?", "chat_history": []}
)
