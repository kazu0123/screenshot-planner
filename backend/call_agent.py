import os
import json

from openai import OpenAI
from dotenv import load_dotenv

from add_event_to_google_calendar import add_event_to_google_calendar, add_event_to_google_calendar_definition
from llm_prompts import system_prompt

load_dotenv(verbose=True)

client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY')
)

agent_functions = {
    "add_event_to_google_calendar": {
        "callable": add_event_to_google_calendar,
        "definition": add_event_to_google_calendar_definition,
    },
}

tools = []
for agent_function in agent_functions:
    tools.append({'type': 'function','function': agent_functions[agent_function]["definition"]})

def call_agent(message: str):
    messages = [
        system_prompt,
        {'role':'user', 'content': message},
    ]
    while True:
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=messages,
            tools=tools,
            tool_choice='auto',
        )
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls
        messages.append(response_message)

        if tool_calls is not None:
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                matched = agent_functions[function_name]

                if len(matched) <= 0:
                    raise 'function_call.nameにマッチする関数がありません。'
                if 1 < len(matched):
                    raise 'function_call.nameに関数が複数マッチしました。'
                
                function_to_call = matched['callable']
                function_response = function_to_call(**function_args)

                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    }
                )
        else:
            return response_message.content
