import os
import autogen
from autogen import AssistantAgent, UserProxyAgent
from autogen import ConversableAgent


llm_config = {
    "model": "gpt-4o",
    "api_key": os.environ.get("OPENAI_API_KEY"),
    "base_url": os.environ.get("OPENAI_API_BASE"),
    "api_type": "azure",
    "api_version": "2023-03-15-preview",
    "temperature": 0.9,
}

cathy = ConversableAgent(
    "cathy",
    system_message="""
    你是一个Python开发专家，精通Python语法，善于写出高性能、易维护的Python代码，并且精通Django、Django Rest Framework、FastAPI等框架和VUE3、ElementPlus开发，请你完成我交给你的开发任务。
    你擅长选择和挑选最佳工具，并尽力避免不必要的重复和复杂性。
    请你完成我交给你的任务，在解决问题时，你会将问题分解成小的问题和改善项，并在每个步骤后建议进行小测试，以确保事情在正确的轨道上。
    如果有任何不清楚或模糊的地方，你总是会要求澄清。你会暂停讨论权衡和实现选项，如果有需要做出选择的情况。
    重要的是，你要遵循这种方法，并尽最大努力教会你的对话者如何做出有效的决策。你避免不必要的道歉，并在回顾对话时不重复早先的错误
    """,
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
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
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

result = joe.initiate_chat(
    cathy,
    message="Cathy, 我们要开发一个适用于个人的博客网站，我们一起协作吧",
    max_turns=2,
)
