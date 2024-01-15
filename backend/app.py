from fastapi import FastAPI

from call_agent import call_agent

app = FastAPI()

@app.post('/add_calender')
def add_calender(message: str):
    return call_agent(message)
