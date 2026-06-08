# ⚡ Ultra-Fast B2B Lead Qualifier & Parser (Groq + Llama 3.1)

A production-ready, ultra-low latency Python engine designed to intercept raw, messy, and unstructured B2B customer inquiries and instantly convert them into strictly typed JSON payloads. 

Stop wasting human hours triaging inbound emails or contact forms. This engine reads human-written text and structures it for your CRM or database in **less than 200 milliseconds** using Groq's lightning-fast inference.

---

## 💎 Unlock the PRO Version (Enterprise-Ready)

Are you looking to scale this into a fully automated enterprise pipeline? Don't reinvent the wheel. Upgrade to the **PRO Package ($49 single payment)** and get production-grade infrastructure:

* 🗄️ **Native Database Connectors:** Pre-configured backend logic for PostgreSQL, Supabase, and MongoDB.
* 🔗 **Live Webhook Architecture:** Send your qualified JSON payloads straight to **HubSpot, Pipedrive, or Salesforce** with zero delay.
* 🛡️ **Production Resilience:** Built-in token budget management, automatic rate-limit retries, and rotative API Key support.
* 🛡️ **Advanced Guardrails:** Strict schema validation to prevent LLM hallucinations from breaking your CRM.
* 📈 **Asynchronous Batch Processing:** Process thousands of historical leads simultaneously using Python's `asyncio`.

👉 [**Get Instant Access to the PRO Version ($49)**](COLE_AQUI_O_LINK_DO_LEMON_SQUEEZY)

---

## 🔥 Features & Capabilities

* **Strict Type Enforcement:** Uses Pydantic to ensure numbers stay as `float/int`, fields match exact structures, and categories match strict `ENUM` definitions.
* **Financial Intelligence:** Automatically extracts mentioned currencies and normalizes budgets directly to raw numbers in USD.
* **Urgency & Scoring Matrix:** Runs semantic analysis on the user's intent to automatically categorize priority (`HIGH`, `MEDIUM`, `LOW`) and calculate a conversion score from 1-10.

---

## 🚀 Quick Start (Free Version)

### 1. Prerequisites & Installation
Clone the repository and install the standard dependencies:
```bash
pip install pydantic groq
