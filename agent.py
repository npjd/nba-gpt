from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
import os
load_dotenv()

db = SQLDatabase.from_uri("postgresql://nba_sql:nba_sql@localhost:5432/nba")

print(db.get_usable_table_names())

llm = OpenAI(temperature=0, verbose=True, openai_api_key=os.getenv('OPENAI_API_KEY'))


tools = SQLDatabaseToolkit(db=db, llm=llm).get_tools()

agent_executor = create_sql_agent(
    llm=llm,
    tools=tools,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent_executor.run(
    "Who has the most triple doubles?"
)
