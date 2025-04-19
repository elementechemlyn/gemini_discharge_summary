import os
import time
import google.genai as genai

api_key=os.environ["GEMINI_API_KEY"]
model_version=os.environ.get("GEMINI_MODEL","gemini-2.5-flash-preview-04-17")
num_outputs=os.environ.get("NUM_OUTPUTS",10)

client = genai.Client(api_key=api_key)


prompt = """You are a software developer in the NHS. You need to generate a synthetic discharge summary in html format. 
You will use example medications from NHS DM+D and example diagnosis and treatments from SNOMED CT. 
You will generate fake details for the patient, the clinicians, the hospital and the GP practice involved ensuring they don't match real life values. 
You will ensure that the patient problems, symptoms and diagnosis are realistic for the Sex and Age of the patient
and that the treatments and medications are realistic for the problems, symptoms, and diagnosis. 
Ground your responses but don't include links or references to SNOMED CT or DM+D in the final output. 
Deliberately include occasional spelling mistakes and typos to reflect natural human input. 
Include only the discharge summary in your output. The header for the document should be 'Discharge Summary for [patient name]'. 
"""

# Fiddle with the model settings
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 65536,
  "response_mime_type": "text/plain",
}


for i in range(0,num_outputs):
    print(f"Making document {i+1} of {num_outputs}")
    response = client.models.generate_content(
        model=model_version,
        config=generation_config,
        contents=prompt
    )

    response_json = response.model_dump_json(
        exclude_none=True, indent=4)

    with open(f"outputs/zeroshot/output{i}.html","w") as f:
        f.write(response.text.replace("```html\n","").replace("```",""))

    print(response_json)
