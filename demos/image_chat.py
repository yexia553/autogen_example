import autogen.agentchat
from autogen.agentchat.contrib.multimodal_conversable_agent import (
    MultimodalConversableAgent,
)
import autogen
from llms import azure_gpt4o


image_agent = MultimodalConversableAgent(
    name="image_agent",
    max_consecutive_auto_reply=10,
    llm_config=azure_gpt4o,
)

user_proxy = autogen.agentchat.UserProxyAgent(
    name="user_proxy",
    system_message="a human admin",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
)

message = """
下面的图片是什么内容？
<img images/基金投资收益率.jpg>
"""

user_proxy.initiate_chat(image_agent, message=message)
