# 🤖 Google x Kaggle — 5 Days of AI Agents (My Complete Implementation)

> A fully documented journey of building AI Agents across 5 days  
> Includes memory, evaluation, debugging, A2A (Agent-to-Agent), and production-ready design  
> All notes are based on what I studied during the course

---

## 🚀 Overview

This repository contains all the hands-on projects I built while completing the  
**Google x Kaggle – 5 Days of AI Agents** program.

Across these 5 days, I implemented:

* 🧠 Agents with tools, memory, and structured instructions  
* 📝 Tool-calling agents (search agents, summarizers, evaluators, etc.)  
* 🛠️ Debug-ready agents using observability and traces  
* 🤝 A complete **A2A (Agent-to-Agent) communication system**  
* ⚙️ A production-ready agent with proper architecture  
* 📚 Clean detailed notes for every concept


---

## 🎥 Demo Video

I have included a **complete video demonstration** showing:



In this demo video, I showcase:

* Autonomous Tool Chaining: The agent intelligently executes a sequence of 3 distinct tools (Fee Lookup → Exchange Rate → Calculator) to solve a complex financial query.
* Persistent State Management: The system recalls user context (Name/Location) from a SQLite database even after a complete server restart.
* Live Observability: The terminal logs reveal the agent's internal "thought process" and tool inputs in real-time, proving it isn't just guessing.
* Agent-to-Agent (A2A) Networking: Two separate terminal processes communicate via the A2A protocol, simulating a real-world Client-Server microservices architecture.
* Strict Instruction Adherence: The agent follows "Critical Rules" to bypass clarifying questions and immediately execute code for faster results.


---

## 📘 What This Repository Contains

### 🧩 **Day 1 — Single Tool Agent**

* Built my first agent using Google ADK  
* Added a custom tool and learned tool invocation  
* Implemented basic instruction tuning  
* Set up project structure and environment in VS Code  

---

### 🧩 **Day 2 — Multi-Agent Pipeline**

* Created a system where one agent uses another agent as a sub-agent  
* Integrated Google Search agent  
* Learned agent-to-agent message flow  
* Implemented structured outputs and multi-step reasoning  

---

### 🧠 **Day 3 — Memory, Context & Persistence**

* Added session state tools to store user information  
* Implemented conversation memory using `state`  
* Added **context compaction** to automatically summarize long chats  
* Enabled **database persistence** using SQLite  
* Built a complete agent that remembers the user across sessions  

---

### 🛠️ **Day 4 — Observability & Debugging**

* Enabled debugging with `--log_level DEBUG`  
* Explored full agent traces step-by-step  
* Fixed the bug in the paper-counting agent  
* Understood why incorrect tool output happens  
* Verified tool calls, search results, and LLM decisions through trace logs  

---

### 🤝 **Day 5 — A2A (Agent-to-Agent Architecture)**

* Built **two agents running on two separate terminals**  
* Vendor Agent → exposes product catalog using A2A server  
* Support Agent → communicates with Vendor Agent over localhost  
* Implemented a real multi-agent network  
* Used `RemoteA2aAgent` + Uvicorn to simulate microservices  
* Verified inter-agent communication end-to-end  

---

### 🌐 **Day 5 — Prototype to Production (PDF Notes)**

* Studied production design best practices  
* Learned about separation of concern, modular design, and agent structuring  
* Understood agent cards, tool definitions, API usage, and evaluation design  
* Created clean notes summarizing every section from the PDF  


---

## 📁 Repository Structure

```
📦 Multi-Agent-Systems-With-Google-Adk
│
├── 📂 Code Implementation
     ├── 📂 day1_agent
     ├── 📂 day2_multi_agent
     ├── 📂 day3_memory_app
     ├── 📂 day4_observability
     ├── 📂 day5_a2a
     ├──__init__.py
     ├──day3_data.db
├── 📄 README.md
└── 📜 Detailed notes
```

---

## 📄 Detailed Notes

It contains deatiled notes covering all the topics along with code implementation
To read the detailed explanation of each agent, open:

👉 [Click Here](https://docs.google.com/document/d/1vhvmeBaxnbuapaiICDWfltCvh-HPtCrouOw9cc8j1ko/edit?usp=sharing)

---

## ⭐ Final Thoughts

This 5-day project gave me a complete understanding of:

* How to design intelligent agents  
* How agents talk, think, remember, and debug  
* How to structure multi-agent systems  
* How real production agents are built

This repo serves as my personal documentation of everything I built and learned.

---
