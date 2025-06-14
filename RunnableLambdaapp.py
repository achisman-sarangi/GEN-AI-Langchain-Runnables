from ast import Lambda
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda

load_dotenv()

def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables = ["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count': RunnableLambda(lambda x: len(x.split()))
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic" : "kapil sharma"})

final_result = """ {} \n word count - {} """.format(result['joke'] ,result['word_count'])

print(final_result)


