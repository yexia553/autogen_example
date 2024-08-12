import os
from autogen.agentchat import (
    GroupChat,
    AssistantAgent,
    UserProxyAgent,
    GroupChatManager,
)
from pathlib import Path
from autogen.coding import LocalCommandLineCodeExecutor
import prompts


work_dir = Path("coding")
work_dir.mkdir(exist_ok=True)

# Create a local command line code executor.
executor = LocalCommandLineCodeExecutor(
    timeout=10,  # Timeout for each code execution in seconds.
    work_dir=work_dir,  # Use the temporary directory to store the code files.
)

llm_config = {
    "model": "gpt-4o",
    "api_key": os.environ.get("OPENAI_API_KEY"),
    "base_url": os.environ.get("OPENAI_API_BASE"),
    "api_type": "azure",
    "api_version": "2023-03-15-preview",
    "temperature": 0.9,
}


initializer = UserProxyAgent(
    name="Init",
)

# Create an agent with code executor configuration.
cea = AssistantAgent(
    "code_executor_agent",
    llm_config=False,  # Turn off LLM for this agent.
    code_execution_config={
        "executor": executor
    },  # Use the local command line code executor.
    human_input_mode="NEVER",  # Always take human input for this agent for safety.
    description="我可以执行其他Agents写好的代码，需要执行代码的时候呼叫我",
)

hp = AssistantAgent(
    name="human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
    description="我是甲方，每次其他Agent回复之后，都要呼叫我，我给出指示后才能呼叫其他Agent继续工作",
)

rb = AssistantAgent(
    name="rb",
    llm_config=llm_config,
    system_message=prompts.robotic_engineer,
    description="我是Python后端开发，在需要开发后端应用和前期项目细节设计时，请呼叫我",
)

user_proxy = UserProxyAgent(
    name="User",
    system_message=None,
    code_execution_config=False,
    human_input_mode="NEVER",
    llm_config=False,
    description="""
    永远不要呼叫我.
    """,
)


graph_dict = {}
graph_dict[user_proxy] = [hp, cea, rb]
graph_dict[hp] = [cea, rb]
graph_dict[rb] = [cea, hp]
graph_dict[cea] = [hp, rb]

agents = [user_proxy, hp, cea, rb]

group_chat = GroupChat(
    agents=agents,
    messages=[],
    max_round=10,
    allowed_or_disallowed_speaker_transitions=graph_dict,
    allow_repeat_speaker=None,
    speaker_transitions_type="allowed",
)

# create the manager
manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
    code_execution_config=False,
)

# initiate the task
user_proxy.initiate_chat(
    manager,
    message="你所在的运行环境是一个ubuntu系统，让我们尝试探索这个系统，你先问一下hp有什么想法",
    clear_history=True,
)
