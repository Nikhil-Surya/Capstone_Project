## Large Language Model (LLM) Partisanship and Sycophancy Analysis Capstone

### Project Overview
- Developed and benchmarked a multi-model framework evaluating LLM behavior on political stance and sycophantic tendencies.
- Focused on identity-framed prompts influencing responses from GPT, Llama, Gemma, and others.
- Explored differences in stance alignment between smaller and larger LLMs.

### Key Contributions
- Created a novel dataset of 90 politically sensitive prompts with varying liberal, conservative, and neutral frames.
- Designed a Python-based evaluation pipeline with:
  - Manual stance classification
  - Lexical fingerprinting using TF-IDF
  - Sentiment and trend analysis
  - Cross-model stance evaluation where LLMs assessed peer model responses.
- Found smaller LLMs often align with user identity, showing sycophantic behavior.
- Larger models, e.g., GPT-4o, produce more balanced and neutral responses.
- Highlighted ethical concerns on bias, fairness, and prompt influence in LLMs.

### Technologies Used
- Python, Transformers, OpenAI API
- Scikit-learn, Pandas, Seaborn
- PyTorch with GPU acceleration

### Impact
- Recognized by faculty and peers for originality and depth.
- Sharpened skills at the intersection of cutting-edge AI research and scalable analytics.
- Provided reusable evaluation tools for fairness and bias analyses in NLP.

### Domain Diagram
<div style="text-align: center;">
  <img src="/Domain_Diagram.jpg" alt="Domain Diagram" />
</div>
