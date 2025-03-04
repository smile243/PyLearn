from langchain_core.prompts import ChatPromptTemplate
import base as b
# 模板化输入输出
model = b.init()

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})

response = model.invoke(prompt)
print(response.content)