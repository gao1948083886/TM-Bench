# TM-Bench: Benchmarking Large Language Models on Low-Resource Traditional Mongolian

[![Status: Accepted](https://img.shields.io/badge/Status-Accepted%20@%20SIGIR%202026-brightgreen.svg)]()
[![Data: Full Release](https://img.shields.io/badge/Data-Full%20Release-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]() 

> 📢 **Important Notice**: Our paper has been **accepted by SIGIR 2026**. This repository now provides the full TM-Bench release, including the complete benchmark data, evaluation code, and baseline result files.

## 📖 Introduction

**TM-Bench** is the first comprehensive benchmark specifically designed to evaluate the natural language understanding and generation capabilities of Large Language Models (LLMs) on **Traditional Mongolian**.

Due to the absence of a systematic evaluation framework, the performance of LLMs on Traditional Mongolian has long been constrained. To address this, TM-Bench provides an evaluation system comprising **18,357 high-quality instances** across 5 core tasks, aiming to precisely diagnose models' capability boundaries at the morphological, syntactic, semantic, and cultural knowledge levels.

## 🌟 Core Highlights

- **🛠️ Hybrid Construction Strategy**: Integrates Translation-based Adaptation, Expert-Original Authoring, and Semi-automated Synthesis to ensure scalability while maintaining data authenticity.
- **🏕️ Cultural Integration**: Breaks through the limitations of purely linguistic evaluation by deeply incorporating Mongolian history, legal common sense, nomadic life, and folklore to comprehensively assess models' cross-cultural adaptability.
- **✅ Rigorous Quality Validation**: All data underwent multiple rounds of independent auditing by a team of native expert linguists, achieving extremely high annotation consistency (Cohen's k=0.81).

## 📊 Dataset and Task Overview

This benchmark covers both Natural Language Understanding (NLU) and Natural Language Generation (NLG) dimensions. The dataset statistics are listed below (aligned with Table 1 in the paper):

| Dataset | Task | Size | Mix (%) (Translation / Expert / Semi-automated) | Domain |
| :--- | :--- | :--- | :--- | :--- |
| **NLU** |  |  |  |  |
| `TM-AGNews` | TopicClf | 2,082 | 55 / 15 / 30 | Tech, Sport, Grassland<sup>†</sup> |
| `TM-MRPC` | SemSim | 2,091 | 50 / 20 / 30 | Encyclopedia, Folklore<sup>†</sup> |
| `TM-MNLI` | NLI | 2,084 | 52 / 13 / 35 | Fiction, Gov., History<sup>†</sup> |
| `TM-RTE` | NLI | 2,083 | 60 / 10 / 30 | News, Policy, Folklore<sup>†</sup> |
| `TM-QNLI` | NLI | 2,062 | 58 / 12 / 30 | Wiki, Ethnic Geography<sup>†</sup> |
| `TM-HellaSwag` | MCQA | 1,976 | 48 / 15 / 37 | Knowledge, Nomadic Life<sup>†</sup> |
| `TM-MMLU` | MCQA | 1,987 | 51 / 14 / 35 | Science, Ethnic Medicine<sup>†</sup> |
| `TM-ARC` | MCQA | 1,997 | 53 / 12 / 35 | Science, Local Textbooks<sup>†</sup> |
| **NLG** |  |  |  |  |
| `TM-CMMT` | Trans. | 1,995 | 56 / 14 / 30 | Dialog, Ethnic Literature<sup>†</sup> |
| **Total** |  | **18,357** |  |  |

> **†** denotes culturally specific domains.

## 💡 Key Experimental Findings

We conducted systematic evaluations on representative open-source models, including the Llama, Qwen, and Gemma series, revealing severe challenges for current LLMs:
1. **NLU Tasks**: Model performance lags significantly behind high-resource languages, with only a few models (e.g., Gemma3-27B, Qwen3-32B) performing slightly above the random baseline.
2. **NLG Tasks**: Both automatic metrics and double-blind human evaluations indicate that current models suffer from severe "semantic collapse" when generating Traditional Mongolian, frequently producing unreadable gibberish.

## 📝 Citation

If TM-Bench inspires or helps your research, please cite our paper:

```bibtex
@inproceedings{gao2026tmbench,
  title={TM-Bench: Benchmarking Large Language Models on Low-Resource Traditional Mongolian},
  author={Zhenjie Gao and Feilong Bao and Aruukhan and Ruichen Hou and Jixieqi and Dabalgan Wang and Hugejile and Yuan Li},
  booktitle={Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval},
  year={2026}
}
```
