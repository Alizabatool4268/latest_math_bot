from agents import Runner
from main import math_assistant
import chainlit as cl

@cl.on_message
async def main(msg:cl.Message):
    await cl.Message(content="").send()
    #prompt
    prompt = msg.content
    #get result (LLM responce/toool response)
    result = Runner.run_sync(math_assistant,prompt)
    # send result
    await cl.Message(content=f"responce: {result.final_output}").send()