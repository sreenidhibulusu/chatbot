import openai
openai.organization = 'org-aqhB2NQSHT9pNnbb9HKG7PtI'
openai.api_key = "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"
def generate_response(prompt):
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text
    return message.strip()