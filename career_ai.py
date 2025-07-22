from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="mistral")
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

def chat_with_bot(user_input):
    # Only reply to career-related prompts
    keywords = ["career", "job", "course", "future", "skills", "interest", "study"]
    if any(k in user_input.lower() for k in keywords):
        return conversation.run(user_input)
    else:
        return "🧠 I'm trained to assist only with career-related questions."
