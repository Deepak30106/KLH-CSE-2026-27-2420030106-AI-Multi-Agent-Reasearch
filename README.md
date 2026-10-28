# AI Multi-Agent Research Assistant

## Overview

The AI Multi-Agent Research Assistant is a Python-based research system that uses multiple specialized agents to research a user's question, analyze information, validate evidence, rank sources, synthesize a final answer, and generate a PDF research report.

The system uses Ollama with Llama 3.1 8B for local language-model processing and Tavily for web research.

---

## Main Features

- Research question planning
- Automatic research-task generation
- Search-query generation
- Web research using Tavily
- Research analysis
- Source-quality filtering
- Hybrid keyword and vector retrieval
- Research validation
- Evidence-based answer synthesis
- PDF report generation
- Command-line interface

---

## Research Pipeline

The system follows this workflow:

```text
User Research Question
        |
        v
Planner Agent
        |
        v
Research Tasks
        |
        v
Search Query Generation
        |
        v
Research Agent
        |
        v
Web Sources
        |
        v
Research Analysis
        |
        v
Validation Agent
        |
        v
Source Quality Filter
        |
        v
Hybrid RAG
        |
        v
Final Synthesis
        |
        v
PDF Report