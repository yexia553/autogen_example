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

host = AssistantAgent(
    name="host",
    llm_config=llms.azure_gpt4o,
    system_message="你是本次辩论赛的主持人，负责开场白。",
    description="我是主持人，负责开场陈词。在应该有主持人出场的时候呼叫我",
)

b1 = AssistantAgent(
    name="正方一辩",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是正方一辩手，只负责开场陈词。且必须以“尊敬的主持人，评委老师，各位观众，大家好！我是正方一辩”开头。辩论的内容要搞笑一些。你坚决认为：伴侣的钱，就是我的钱。
    """,
    description="我是正方一辩手，只负责开场陈词。在应该由正方一辩出场的时候呼叫我",
)

b2 = AssistantAgent(
    name="正方二辩",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是正方二辩手，只负责攻辩环节。且必须以“尊敬的主持人，评委老师，各位观众，大家好！我是正方二辩”开头。辩论的内容要搞笑一些。你坚决认为：伴侣的钱，就是我的钱。
    """,
    description="我是正方二辩手，只负责攻辩环节。在应该由正方二辩出场的时候呼叫我",
)

b3 = AssistantAgent(
    name="正方三辩",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是正方三辩手，只负责攻辩环节。且必须以“尊敬的主持人，评委老师，各位观众，大家好！我是正方三辩”开头。辩论的内容要搞笑一些。你坚决认为：伴侣的钱，就是我的钱。
    """,
    description="我是正方三辩手，只负责攻辩环节。在应该由正方三辩出场的时候呼叫我",
)

b4 = AssistantAgent(
    name="正方四辩",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是正方四辩手，只负责总结陈词。且必须以“尊敬的主持人，评委老师，各位观众，大家好！我是正方四辩”开头。辩论的内容要搞笑一些。你坚决认为：伴侣的钱，就是我的钱。
    """,
    description="我是正方四辩手，只负责总结陈词。在应该由正方四辩出场的时候呼叫我",
)

w1 = AssistantAgent(
    name="反方一辩",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是反方一辩手，只负责开场陈词。且必须以“尊敬的主持人，评委老师，各位观众，大家好！我是反方一辩”开头。辩论的内容要搞笑一些。你坚决认为：伴侣的钱，不是我的钱。
    """,
    description="我是反方一辩手，只负责开场陈词。在应该由反方一辩出场的时候呼叫我",
)

w2 = AssistantAgent(
    name="反方二辩",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是反方二辩手，只负责攻辩环节。且必须以“尊敬的主持人，评委老师，各位观众，大家好！我是反方二辩”开头。辩论的内容要搞笑一些。你坚决认为：伴侣的钱，不是我的钱。
    """,
    description="我是反方二辩手，只负责攻辩环节。在应该由反方二辩出场的时候呼叫我",
)

w3 = AssistantAgent(
    name="反方三辩",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是反方三辩手，只负责攻辩环节。且必须以“尊敬的主持人，评委老师，各位观众，大家好！我是反方三辩”开头。辩论的内容要搞笑一些。你坚决认为：伴侣的钱，不是我的钱。
    """,
    description="我是反方三辩手，只负责攻辩环节。在应该由反方三辩出场的时候呼叫我",
)

w4 = AssistantAgent(
    name="反方四辩",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是反方四辩手，只负责总结陈词。且必须以“尊敬的主持人，评委老师，各位观众，大家好！我是反方四辩”开头。辩论的内容要搞笑一些。你坚决认为：伴侣的钱，不是我的钱。
    """,
    description="我是反方四辩手，只负责总结陈词。在应该由反方四辩出场的时候呼叫我",
)

judge = AssistantAgent(
    name="裁判",
    llm_config=llms.azure_gpt4o,
    system_message="""
    你是裁判，你必须以公正客观的态度评判辩论赛的表现，并给出详细的评语和最终的胜负结果。
    """,
    description="我是裁判。在应该由裁判出场的时候呼叫我",
)

user_proxy = UserProxyAgent(
    name="User",
    system_message="""我们要进行一场辩论赛，辩论题目为: 伴侣的钱是不是我的钱？
            """,
    code_execution_config=False,
    human_input_mode="NEVER",
    llm_config=False,
    description="""
    永远不要呼叫我.
    """,
)


graph_dict = {}
graph_dict[user_proxy] = [host]
graph_dict[host] = [b1]
graph_dict[b1] = [w1]
graph_dict[w1] = [b2]
graph_dict[b2] = [w2]
graph_dict[w2] = [b3]
graph_dict[b3] = [w3]
graph_dict[b4] = [w4]
graph_dict[w4] = [judge]

agents = [user_proxy, b1, w1, b2, w2, b3, w3, b4, w4, judge, host]

# create the groupchat
group_chat = GroupChat(
    agents=agents,
    messages=[],
    max_round=15,
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
    message="""我们要进行一场辩论赛，辩论题目为: 伴侣的钱是不是我的钱？""",
    clear_history=True,
)
