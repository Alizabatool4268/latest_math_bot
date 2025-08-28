import os
from agents import Runner, OpenAIChatCompletionsModel, set_tracing_disabled,Agent
from openai import AsyncOpenAI
from dotenv import load_dotenv
from tools.tools import plus,subtract, multiply,divide

load_dotenv(override=True)
my_key = os.getenv("GEMINI_API_KEY")
my_base_url =os.getenv("BASE_URL")

client = AsyncOpenAI(
    api_key= my_key,
    base_url= my_base_url
)    
MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client,
)

math_assistant= Agent(
    name="Allie",
    model= MODEL,
    instructions="your name is allie. You are a helpful agent which will help users related to math. dont answer questions if they are not related to math you can answer if the user asks your name only. ",
    tools=[plus,subtract,multiply,divide]
)

set_tracing_disabled(True)
result = Runner.run_sync(
    starting_agent= math_assistant,
    input = ""
)
print(result.final_output)