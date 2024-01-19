from calendar_event import CalendarEvent
from llm_prompts import system_prompt
from openai_client import openai_client

def parse_event_details(message: str):
    result: list[CalendarEvent] = []

    # Functionを登録
    tools = [
        {'type': 'function','function': parse_event_details_definition},
    ]
    # 会話履歴を登録
    messages = [
        system_prompt,
        {'role':'user', 'content': message},
    ]

    while True:
        response = openai_client.chat.completions.create(
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

                calendar_event = CalendarEvent.model_validate_json(tool_call.function.arguments)
                result.append(calendar_event)

                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": "OK",
                    }
                )
        else:
            return result

# この関数の動作について：
# descriptionにはカレンダーに登録する関数との記述があります。
# しかし実際の動作としては、予定をパースするのみで登録はしません。
# 登録する関数とした方がプロンプト短くなるのでこの記述になっています。
parse_event_details_definition = {
    "name": "parse_event_details",
    "description": "予定やタスクをカレンダーに登録する関数です。", # 嘘です
    "parameters": CalendarEvent.model_json_schema()
}
