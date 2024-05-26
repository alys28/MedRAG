from src.medrag import MedRAG

question = "A lesion causing compression of the facial nerve at the stylomastoid foramen will cause ipsilateral"
options = {
    "A": "paralysis of the facial muscles.",
    "B": "paralysis of the facial muscles and loss of taste.",
    "C": "paralysis of the facial muscles, loss of taste and lacrimation.",
    "D": "paralysis of the facial muscles, loss of taste, lacrimation and decreased salivation."
}

## CoT Prompting
cot = MedRAG(llm_name="OpenAI/gpt-3.5-turbo", rag=True, retriever_name="BM25")
# answer, _, _ = cot.answer(question=question, options=options)
# print(answer)
# from openai import OpenAI
# import json
# import os
# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "..."))
# # Example prompt and completion request
# MODEL = "gpt-3.5-turbo"
# response = client.chat.completions.create(
#     model=MODEL,
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Knock knock."},
#         {"role": "assistant", "content": "Who's there?"},
#         {"role": "user", "content": "Orange."},
#     ],
#     temperature=0,
# )
# print(json.dumps(json.loads(response.model_dump_json()), indent=4))

