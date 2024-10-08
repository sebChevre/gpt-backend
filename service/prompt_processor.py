import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from store.vectorstore_provider import get_vectorstore_for_index

ES_INDEX = os.environ.get('ES_VECTOR_STORE_INDEX')

_llm = None
_vectorstore = None


def get_llm():
    global _llm

    if _llm is None:
        _llm = ChatOpenAI(model="gpt-4o-mini")

    return _llm


def ask(question):
    global _vectorstore

    if _vectorstore is None:
        _vectorstore = get_vectorstore_for_index(ES_INDEX)

    retriever = _vectorstore.as_retriever()

    prompt_template = PromptTemplate(
        input_variables=['context', 'question'],
        template="Vous êtes un assistant pour des tâches de questions-réponses. Utilisez les éléments de contexte récupérés ci-dessous pour répondre à la question. Si vous ne connaissez pas la réponse, dites simplement que vous ne la connaissez pas. Utilisez un maximum de trois phrases et gardez la réponse concise.\nQuestion : {question} \nContexte : {context} \nRéponse :",
        messages=[HumanMessagePromptTemplate(
            prompt=PromptTemplate(input_variables=['context', 'question'], input_types={}, partial_variables={},
                                  template="Vous êtes un assistant pour des tâches de questions-réponses. Utilisez les éléments de contexte récupérés ci-dessous pour répondre à la question. Si vous ne connaissez pas la réponse, dites simplement que vous ne la connaissez pas. Utilisez un maximum de trois phrases et gardez la réponse concise.\nQuestion : {question} \nContexte : {context} \nRéponse :"),
            additional_kwargs={})]
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt_template
            | get_llm()
            | StrOutputParser()
    )

    response = rag_chain.invoke(question)

    return response
