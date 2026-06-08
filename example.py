import os
import json
from pydantic import BaseModel, Field
from client import GroqFastClient

API_KEY = os.environ.get("GROQ_API_KEY", "PASTE_YOUR_GROQ_API_KEY_HERE")

class LeadPayloadSchema(BaseModel):
    client_name: str = Field(description="Extract the person's name clean.")
    company: str = Field(description="Company name. If not found, use 'Not Provided'.")
    pain_point: str = Field(description="The core technical or business problem described.")
    estimated_budget_usd: float = Field(description="Convert any mentioned budget to USD number. If none, return 0.0.")
    urgency: str = Field(description="Must be HIGH, MEDIUM, or LOW based on text context.")
    conversion_score: int = Field(description="Score from 1 to 10 on how valuable this lead is.")

try:
    client = GroqFastClient(api_key=API_KEY)
    
    raw_input = """
    Hey! I'm John from TechVanguard Solutions. Our main legacy server is crashing every single peak hour 
    and we are losing customers. We urgently need a migration setup to a cloud infrastructure this month. 
    We have around 15,000 dollars allocated for this fix if your team can deliver it fast.
    """
    
    print("⚡ [System] Processing raw lead data with Groq Ultra-Fast Engine...")
    
    system_prompt = (
        "You are a strict Data Engineer. Analyze the text and output a clean JSON payload matching the schema rules. "
        "Do not chat, do not add markdown syntax outside the required output."
    )
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Target text: {raw_input}"}
    ]
    
    response = client.create_chat_completion(
        model="llama-3.1-8b-instant", 
        messages=messages
    )
    
    result = response.choices[0].message["content"]
    print("\n📦 [CRM READY PAYLOAD - TEST VERSION]:")
    print(result)

except Exception as e:
    print(f"Error executing engine: {e}")