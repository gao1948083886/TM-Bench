Here is the professional English translation of your `README.md`. I have optimized the formatting to ensure it meets the standards of a top-tier NLP conference repository.

---

# TM-Bench: Benchmarking Large Language Models on Low-resource Traditional Mongolian

> 
> **Note**: This repository is dedicated to our submission for **ACL 2026**. 
> 
> 

**TM-Bench** is the first comprehensive evaluation benchmark specifically designed for **Traditional Mongolian** large language models. It aims to bridge the evaluation gap for low-resource languages by covering 7 core tasks across Natural Language Understanding (NLU) and Generation (NLG), comprising a total of **22,657** high-quality instances. 

## 📝 Introduction

The scarcity of high-quality datasets has led to significant "linguistic inequality" for Traditional Mongolian in the digital era. TM-Bench is constructed using a hybrid strategy to ensure rigorous evaluation and cultural relevance: 

1. 
**Translation-based Adaptation**: Mature English benchmarks are migrated and subjected to rigorous expert proofreading. 


2. 
**Expert-Original Authoring**: Original instances are authored by Mongolian language experts based on ethnic heritage, history, and social practices. 


3. 
**Semi-automated Synthesis**: Task-specific data is synthesized from high-value native texts using a corpus-driven pipeline. 



## 📂 Detailed Statistics

The benchmark spans various domains including technology, law, folklore, and daily conversation. The detailed statistics for each sub-dataset are as follows: 

| Dataset | Task Type | Total | Source Prop. (Trans:Exp:Semi) | Domain | Avg Len |
| --- | --- | --- | --- | --- | --- |
| **NLU Tasks** |  |  |  |  |  |
| TM-AGNews | Topic Clf. | 2,100 | 0.55 : 0.15 : 0.30 | Tech, Sports, Grassland Ecology† | 36.17 |
| TM-MRPC | Sem. Sim. | 2,100 | 0.50 : 0.20 : 0.30 | Encyclopedia, Folklore Etiquette† | 47.85 |
| TM-SST2 | Sentiment | 2,200 | 0.45 : 0.20 : 0.35 | Movies, Folk Art† | 9.72 |
| TM-MNLI | NLI | 2,094 | 0.52 : 0.13 : 0.35 | Fiction, Gov. Documents, History† | 32.46 |
| TM-RTE | NLI | 2,093 | 0.60 : 0.10 : 0.30 | News, Ethnic Policy, Folklore Etiquette† | 54.09 |
| TM-QNLI | NLI | 2,075 | 0.58 : 0.12 : 0.30 | Wiki, Ethnic Geography† | 44.57 |
| TM-HellaSwag | MCQA | 2,000 | 0.48 : 0.15 : 0.37 | General Knowledge, Nomadic Life† | 134.42 |
| TM-MMLU | MCQA | 2,000 | 0.51 : 0.14 : 0.35 | Humanities, Ethnic Medicine† | 71.87 |
| TM-ARC | MCQA | 2,000 | 0.53 : 0.12 : 0.35 | Basic Science, Local Textbooks† | 45.05 |
| **NLG Tasks** |  |  |  |  |  |
| TM-CMMT | Translation | 1,995 | 0.56 : 0.14 : 0.30 | Daily Dialog, Ethnic Literature† | 25.78 |
| TM-XSum | Summ. | 2,000 | 0.47 : 0.18 : 0.35 | News, Pastoral Culture† | 90.21 |
| **Total** | --- | **22,657** | --- | --- | --- |



> 
> **†**: Domains containing expert-authored instances centered on traditional Mongolian culture and nomadic civilization. 
> 
> 

## 📂 Repository & Release Plan

This repository currently contains **representative samples** of TM-Bench for previewing data formats and task types.

> **⚠️ Important Notice**:
> To adhere to academic conventions and ensure the integrity of the double-blind peer review process, only a subset of the data is currently public. **The full dataset (22,657 instances) and evaluation scripts will be released immediately upon paper acceptance.** Thank you for your understanding.

## 🚀 Evaluation Results

Experimental results indicate that current representative LLMs face significant challenges in Traditional Mongolian: 

* 
**Limited Understanding**: The highest NLU accuracy achieved was only ~**36.81%** (Gemma3-27B), with many models performing near or below the 25% random baseline. 


* 
**Generation Collapse**: In translation and summarization tasks, models exhibit severe semantic collapse, with BLEU scores generally falling below **10**. 



## 📄 Citation

If you use this benchmark in your research, please cite our work:

```bibtex
@article{tm_bench2026,
  title={TM-Bench: Benchmarking Large Language Models on Low-resource Traditional Mongolian},
  author={Anonymous Authors},
  journal={ACL Submission},
  year={2026}
}

```

---

Would you like me to create the actual `README.md` file for you to download, or help you with the code to move your files into a new folder now?
