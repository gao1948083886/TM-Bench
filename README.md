# TM-Bench: Benchmarking Large Language Models on Low-Resource Traditional Mongolian

[![Status: Under Review](https://img.shields.io/badge/Status-Under%20Review%20@%20SIGIR%2026-orange.svg)]()
[![Data: Partial Release](https://img.shields.io/badge/Data-Partial%20Release-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]() 

> 📢 **Important Notice**: The paper corresponding to this project has been submitted to **SIGIR 2026** and is currently under review. At this stage, this repository provides a partial release of sample data to demonstrate the task formats and data structures. The complete dataset and code will be fully open-sourced upon acceptance.

## 📖 Introduction

**TM-Bench** is the first comprehensive benchmark specifically designed to evaluate the natural language understanding and generation capabilities of Large Language Models (LLMs) on **Traditional Mongolian**.

Due to the absence of a systematic evaluation framework, the performance of LLMs on Traditional Mongolian has long been constrained. To address this, TM-Bench provides an evaluation system comprising **18,357 high-quality instances** across 5 core tasks, aiming to precisely diagnose models' capability boundaries at the morphological, syntactic, semantic, and cultural knowledge levels.

## 🌟 Core Highlights

- **🛠️ Hybrid Construction Strategy**: Integrates Translation-based Adaptation, Expert-Original Authoring, and Semi-automated Synthesis to ensure scalability while maintaining data authenticity.
- **🏕️ Cultural Integration**: Breaks through the limitations of purely linguistic evaluation by deeply incorporating Mongolian history, legal common sense, nomadic life, and folklore to comprehensively assess models' cross-cultural adaptability.
- **✅ Rigorous Quality Validation**: All data underwent multiple rounds of independent auditing by a team of native expert linguists, achieving extremely high annotation consistency (Cohen's k=0.81).

## 📊 Dataset and Task Overview

This benchmark covers both Natural Language Understanding (NLU) and Natural Language Generation (NLG) dimensions. The core components of TM-Bench are as follows (the current repository contains partial sample instances):

| Task Type | Dataset | Size | Mix (%) (Translation / Expert / Semi-automated) | Domain Examples |
| :--- | :--- | :--- | :--- | :--- |
| **Topic Classification (TopicClf)** | `TM-AGNews` | 2,082 | 55% / 15% / 30% | Tech, Sports, Grassland Culture |
| **Semantic Similarity (SemSim)** | `TM-MRPC` | 2,091 | 50% / 20% / 30% | Encyclopedia, Folklore |
| **Natural Language Inference (NLI)** | `TM-MNLI`, `TM-RTE`, `TM-QNLI` | 6,229 | ~56% / 11% / 32% | Fiction, History, Policy, Geography |
| **Multiple-Choice QA (MCQA)** | `TM-HellaSwag`, `TM-MMLU`, `TM-ARC` | 5,960 | ~51% / 14% / 35% | Common Sense, Traditional Medicine, Local Textbooks |
| **Machine Translation (MT)** | `TM-CMMT` (Mongolian ↔ Chinese) | 1,995 | 56% / 14% / 30% | Dialog, Ethnic Literature |
| **Total** | **TM-Bench** | **18,357** | - | - |

> *For detailed data statistics, please refer to Table 1 in the paper.*

## 💡 Key Experimental Findings

We conducted systematic evaluations on representative open-source models, including the Llama, Qwen, and Gemma series, revealing severe challenges for current LLMs:
1. **NLU Tasks**: Model performance lags significantly behind high-resource languages, with only a few models (e.g., Gemma3-27B, Qwen3-32B) performing slightly above the random baseline.
2. **NLG Tasks**: Both automatic metrics and double-blind human evaluations indicate that current models suffer from severe "semantic collapse" when generating Traditional Mongolian, frequently producing unreadable gibberish.

## 🚀 Release Roadmap

- [x] **v0 (Current - Under Review)**: Release a partial subset of the final dataset to demonstrate task formats and data structures.
- [ ] **v1.0 (Full Release - Upon Acceptance)**: Upon acceptance of the paper, the following will be fully open-sourced:
  - 📦 The complete benchmark dataset with 18,357 instances.
  - 💻 Full evaluation code and baseline model inference scripts.
  - 📈 Detailed experimental configurations and output results for all evaluated models.

## 📝 Citation

If TM-Bench inspires or helps your research, please consider citing our work once the paper is officially published:

```bibtex
@inproceedings{gao2026tmbench,
  title={TM-Bench: Benchmarking Large Language Models on Low-Resource Traditional Mongolian},
  author={Zhenjie Gao and Feilong Bao and Aruukhan and Ruichen Hou and Jixieqi and Dabalgan Wang and Hugejile and Yuan Li},
  booktitle={Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval},
  year={2026}
}
