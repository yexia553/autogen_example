from autogen.agentchat import AssistantAgent, UserProxyAgent
import llms


assistant = AssistantAgent("assistant", llm_config=llms.doubao_pro_32k)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Tell me a joke about NVDA and TESLA stock prices.",
)
