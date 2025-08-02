import os
from github import fetch_github_issues
from langchain_astradb import AstraDBVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from langchain.tools.retriever import create_retriever_tool
from langchain import hub
from langchain_mistralai import ChatMistralAI
from note import save_note

def connect_to_vstore():
    embeddings=OllamaEmbeddings(model='nomic-embed-text')
    ASTRA_DB_API_ENDPOINT=os.getenv('ASTRA_DB_API_ENDPOINT')
    ASTRA_DB_APPLICATION_TOKEN=os.getenv('ASTRA_DB_APPLICATION_TOKEN')
    desired_namespace=os.getenv(" ASTRA_DB_KEY")

    if desired_namespace:
        ASTRA_DB_KEYSPACE=desired_namespace
    else:
        ASTRA_DB_KEYSPACE=None
    
    vstore=AstraDBVectorStore(
        embedding=embeddings,
        collection_name='github',
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE
    )

    return vstore

vstore=connect_to_vstore()
check_update=input('Do you want to update the issues (y/N):')

if check_update =='y' or check_update=='yes':
    owner="Abhi8149"
    repo="Simple-Math-Equation-Solver"
    issues=fetch_github_issues(owner, repo)

    try:
        vstore.delete_collection()
    except:
        pass

    vstore=connect_to_vstore()
    vstore.add_documents(issues)

    #checking if its ok until now
    # result=vstore.similarity_search('flash messages', k=3)
    # for res in result:
    #     print(f"Page has content{res.page_content} anf its metadata is {res.metadata} ")


retriever=vstore.as_retriever(search_kwargs={'k':3})
retriever_tool=create_retriever_tool(
    retriever=retriever,
    name='github_search',
    description="Search for information about github issues. For any questions about github issues, you must use this tool!"
)

tools=[retriever_tool, save_note]

prompt=hub.pull("hwchase17/openai-functions-agent")

llm=ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.1,
)

agent=create_tool_calling_agent(llm, tools, prompt)
agent_executor=AgentExecutor(agent=agent,tools=tools, verbose=True)

while (question := input("Ask a question about github issues (q to quit): ")) != "q":
    result = agent_executor.invoke({"input": question})
    print(result["output"])