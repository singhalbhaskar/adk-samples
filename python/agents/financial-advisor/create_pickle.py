import cloudpickle
from financial_advisor.agent import root_agent
from vertexai.preview.reasoning_engines import AdkApp

adk_app = AdkApp(
    agent=root_agent,
    enable_tracing=True,
)

with open("cloudpickle.pkl", "wb") as f:
    cloudpickle.dump(app, f)
