from langchain import OpenAI, LLMChain, PromptTemplate

# 1. Initialize the LLM
llm = OpenAI(temperature=0.7)

# 2. Create a prompt template
template = PromptTemplate(
    input_variables=["product"],
    template="Write a short marketing blurb for the product: {product}."
)

# 3. Build the chain
chain = LLMChain(llm=llm, prompt=template)

# 4. Run it
result = chain.run({"product": "wireless noise-cancelling headphones"})
print(result)
