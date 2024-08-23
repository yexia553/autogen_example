# from autogen.agentchat import AssistantAgent, UserProxyAgent
# import llms


# assistant = AssistantAgent("assistant", llm_config=llms.claude_35_sonnet)
# user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

# # Start the chat
# user_proxy.initiate_chat(
#     assistant,
#     message="Tell me a joke about NVDA and TESLA stock prices.",
# )

from autogen.agentchat import ConversableAgent, UserProxyAgent

local_llm_config = {
    "config_list": [
        {
            "model": "NotRequired",  # Loaded with LiteLLM command
            "api_key": "NotRequired",  # Not needed
            "base_url": "http://0.0.0.0:4000",  # Your LiteLLM URL
            "price": [0, 0],  # Put in price per 1K tokens [prompt, response] as free!
        }
    ],
    "cache_seed": None,  # Turns off caching, useful for testing different models
}

# Create the agent that uses the LLM.
assistant = ConversableAgent("agent", llm_config=local_llm_config)

# Create the agent that represents the user in the conversation.
user_proxy = UserProxyAgent("user", code_execution_config=False)

# Let the assistant start the conversation.  It will end when the user types exit.
res = assistant.initiate_chat(user_proxy, message="How can I help you today?")

print(assistant)
