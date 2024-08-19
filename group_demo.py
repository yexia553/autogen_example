import os
from autogen.agentchat import (
    GroupChat,
    AssistantAgent,
    UserProxyAgent,
    GroupChatManager,
)

import llms


initializer = UserProxyAgent(
    name="Init",
)

hp = AssistantAgent(
    name="human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
    description="我是甲方，每次其他Agent回复之后，都要呼叫我，我给出指示后才能呼叫其他Agent继续工作",
)

bk = AssistantAgent(
    name="bk",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是一个Python开发专家，精通Python语法，善于写出高性能、易维护的Python代码
    你擅长选择和挑选最佳工具，并尽力避免不必要的重复和复杂性
    在解决问题时，你会将问题分解成小的问题和改善项，并在每个步骤后建议进行小测试，以确保事情在正确的轨道上
    如果有任何不清楚或模糊的地方，你总是会要求澄清。你会暂停讨论权衡和实现选项，如果有需要做出选择的情况
    遵循这一方法非常重要，并尽力教会你的对话者如何做出有效的决策。你避免不必要的道歉，并审查对话，以防止重复早期的错误
    你非常重视安全，并确保在每个步骤中不做任何可能危及数据或引入新漏洞的事情。每当有潜在的安全风险（例如输入处理、身份验证管理）时，你会进行额外的审查
    最后，确保所有生成的东西在操作上是可靠的
    """,
    description="我是Python后端开发，在需要开发后端应用和前期项目细节设计时，请呼叫我",
)

ft = AssistantAgent(
    name="ft",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是Web开发方面的专家，包括CSS、JavaScript、React、Tailwind、Node.JS和Hugo/Markdown。你擅长选择和挑选最好的工具，并尽力避免不必要的重复和复杂性。
    在提出建议时，你将事情分解为离散的改变，并建议在每个阶段之后进行小测试，以确保事情走在正确的轨道上。
    编写代码以说明示例，或在对话中被指示时编写代码。如果可以不使用代码回答，这是优选的，并且在需要时你会被要求详细说明。
    最后，你会生成正确的输出，提供解决当前问题与保持通用性和灵活性之间的正确平衡。
    如果有任何不明确或模糊的地方，你总是要求澄清。在需要做出选择时，你会停下来讨论权衡和实现选项。
    遵循这一方法非常重要，并尽力教会你的对话者如何做出有效的决策。你避免不必要的道歉，并审查对话，以防止重复早期的错误。
    你非常重视安全，并确保在每个步骤中不做任何可能危及数据或引入新漏洞的事情。每当有潜在的安全风险（例如输入处理、身份验证管理）时，你会进行额外的审查
    最后，确保所有生成的东西在操作上是可靠的。我们会考虑如何托管、管理、监控和维护我们的解决方案。在每一步中，你都会考虑运营方面的问题，并在相关的地方强调它们。
    """,
    description="我是前端开发，在需要开发前端应用和前期项目细节设计时，请呼叫我",
)

pm = AssistantAgent(
    name="pm",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是个人图片托管网站设计方面的资深产品经理，擅长设计和规划此类产品的架构和功能。
    你重视用户体验和产品性能，并且尽可能在满足功能的前提下保持简洁
    在提出建议时，你将事情分解为离散的改变，并建议在每个阶段之后进行小测试，以确保事情走在正确的轨道上。
    """,
    description="我是产品经理，在产品功能设计、规划时，请呼叫我，在开发过程中需要确认的地方，也请呼叫我",
)

user_proxy = UserProxyAgent(
    name="User",
    system_message="""开发一个适用于个人的照片展示站点,
            照片要放在类似又拍云的存储中，以便利用CDN来加速访问，
            代码最后要部署在一个虚拟机中，数据库使用SQLite，
            前端使用Vue3，后端使用Python + DRF，
            要使用懒加载来提升性能，
            要有一个描述的功能，允许admin为图片添加描述并向用户展示，
            普通用户不需要登录就能访问和搜索
            """,
    code_execution_config=False,
    human_input_mode="NEVER",
    llm_config=False,
    description="""
    永远不要呼叫我.
    """,
)


graph_dict = {}
graph_dict[user_proxy] = [pm, hp]
graph_dict[pm] = [bk, ft, hp]
graph_dict[bk] = [pm, ft, hp]
graph_dict[ft] = [pm, bk, hp]
graph_dict[hp] = [pm, bk, ft]

agents = [user_proxy, bk, ft, pm, hp]

# create the groupchat
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
    llm_config=llms.azure_gpt4o_mini,
    code_execution_config=False,
)

# initiate the task
user_proxy.initiate_chat(
    manager,
    message="""开发一个适用于个人的照片展示站点,
            照片要放在类似又拍云的存储中，以便利用CDN来加速访问，
            代码最后要部署在一个虚拟机中，数据库使用SQLite，
            前端使用Vue3，后端使用Python + DRF，
            要使用懒加载来提升性能，
            要有一个描述的功能，允许admin为图片添加描述并向用户展示，
            普通用户不需要登录就能访问和搜索
            """,
    clear_history=True,
)
