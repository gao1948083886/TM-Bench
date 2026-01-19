# TM-Bench: Benchmarking Large Language Models on Low-resource Traditional Mongolian

> **Note**: This repository is dedicated to our submission for **ACL 2026**.

**TM-Bench** 是首个针对大语言模型**传统蒙古文**能力的综合性评估基准。它旨在弥补低资源语言在系统性评估框架上的缺失，涵盖了自然语言理解 (NLU) 和自然语言生成 (NLG) 的核心任务，包含共计 **22,657** 个高质量实例 。

## 📝 项目简介

由于高质量数据集的匮乏，传统蒙古文在数字时代面临着严重的“语言不平等”现象 。TM-Bench 通过以下三种混合策略构建，确保了评估的严谨性与文化相关性：

1. **翻译自适应**：迁移成熟的英文基准并进行严格专家校对 。

2. **专家原创**：由蒙古语专家基于民族文化、历史及社会实践原创，增强本地化相关性 。

3. **半自动综合**：利用语料驱动的流水线从原生文本中提取并生成任务数据，实现大规模扩展 。


---

## 📂 数据集统计 (Detailed Statistics)

本基准涵盖了 7 大类任务，跨越科技、法律、民俗及日常对话等多个领域。以下是 TM-Bench 各子数据集的详细统计信息 ：

| Dataset | Task Type | Total | Source Prop. (Trans:Exp:Semi) | Domain |
| --- | --- | --- | --- | --- |
| **NLU Tasks** |  |  |  |  |
| TM-AGNews | Topic Clf. | 2,100 | 0.55 : 0.15 : 0.30 | Tech, Sports, Grassland Ecology† |
| TM-MRPC | Sem. Sim. | 2,100 | 0.50 : 0.20 : 0.30 | Encyclopedia, Folklore Etiquette† |
| TM-SST2 | Sentiment | 2,200 | 0.45 : 0.20 : 0.35 | Movies, Folk Art† |
| TM-MNLI | NLI | 2,094 | 0.52 : 0.13 : 0.35 | Fiction, Gov. Documents, History† |
| TM-RTE | NLI | 2,093 | 0.60 : 0.10 : 0.30 | News, Ethnic Policy, Folklore Etiquette† |
| TM-QNLI | NLI | 2,075 | 0.58 : 0.12 : 0.30 | Wiki, Ethnic Geography† |
| TM-HellaSwag | MCQA | 2,000 | 0.48 : 0.15 : 0.37 | General Knowledge, Nomadic Life† |
| TM-MMLU | MCQA | 2,000 | 0.51 : 0.14 : 0.35 | Humanities, Ethnic Medicine† |
| TM-ARC | MCQA | 2,000 | 0.53 : 0.12 : 0.35 | Basic Science, Local Textbooks† |
| **NLG Tasks** |  |  |  |  |
| TM-CMMT | Translation | 1,995 | 0.56 : 0.14 : 0.30 | Daily Dialog, Ethnic Literature† |
| TM-XSum | Summ. | 2,000 | 0.47 : 0.18 : 0.35 | News, Pastoral Culture† |
| **Total** | --- | **22,657** | --- | --- |

> 
> **†**：标注该符号的领域包含由专家撰写的、以传统蒙古文化和游牧文明为核心的实例 。
> 
> 

---

## 📂 仓库说明与开放计划

当前仓库包含 TM-Bench 的**部分公开样本**，旨在供研究人员预览数据格式。

> **⚠️ 重要提示**：
> 为遵守学术惯例并确保同行评审的公正性，本仓库目前仅公开代表性数据子集。**完整的数据集及配套评测代码将在论文被录用后立即全面开放。** 感谢您的关注。

## 🚀 评测结果简述

实验结果表明，目前的通用大模型在处理传统蒙古文时面临巨大挑战 ：

* **理解能力受限**：NLU 任务最高准确率仅约 **36.81%** (Gemma3-27B)，许多模型表现甚至低于 25% 的随机基准 。

* **生成能力崩溃**：在翻译与摘要任务中，模型普遍存在语义崩溃现象，BLEU 分数通常低于 **10** 。



这些发现证明了针对蒙古文进行专门形态建模和语料扩展的紧迫性 。

---





















非常抱歉，在之前的转换中忽略了表格中的特殊标记和“平均长度（Avg Len）”这一列。

根据您提供的 LaTeX 源码和 PDF 中的统计数据 ，我已经重新调整了 README 中的表格，补齐了所有的标记（†）和数据。

以下是为您修正后的完整 `README.md` 内容：

---

# TM-Bench: Benchmarking Large Language Models on Low-resource Traditional Mongolian

> **Note**: This repository is dedicated to our submission for **ACL 2026**.

**TM-Bench** 是首个针对**传统蒙古文 (Traditional Mongolian)** 大规模语言模型能力的综合性评估基准 。它旨在弥补低资源语言在系统性评估框架上的缺失，涵盖了自然语言理解 (NLU) 和自然语言生成 (NLG) 的核心任务，包含共计 **22,657** 个高质量实例 。

## 📝 项目简介

由于高质量数据集的匮乏，传统蒙古文在数字时代面临着严重的“语言不平等”现象 。TM-Bench 通过以下三种混合策略构建，确保了评估的严谨性与文化相关性 ：

1. 
**翻译自适应 (Translation-based Adaptation)**：迁移成熟的英文基准并进行严格专家校对 。


2. 
**专家原创 (Expert-Original Authoring)**：由蒙古语专家基于民族文化、历史及社会实践原创 。


3. 
**半自动综合 (Semi-automated Synthesis)**：利用语料驱动的流水线从原生文本中提取并生成任务数据 。



## 📂 数据集统计 (Detailed Statistics)

本基准涵盖了 7 大类任务，跨越科技、法律、民俗及日常对话等多个领域 。以下是 TM-Bench 各子数据集的详细统计信息 ：



## 📂 仓库说明与开放计划

当前仓库包含 TM-Bench 的**部分公开样本**，旨在供研究人员预览数据格式。

> **⚠️ 重要提示**：
> 为遵守学术惯例并确保同行评审的公正性，本仓库目前仅公开代表性数据子集。**完整的数据集（22,657 个实例）及配套评测代码将在论文被录用 (Accepted) 后立即全面开放。** 感谢您的理解。

## 🚀 评测结果简述

实验结果表明，目前的通用大模型在处理传统蒙古文时表现普遍欠佳 ：

* 
**理解能力受限**：NLU 任务最高准确率仅约 **36.81%** (Gemma3-27B) 。


* 
**生成能力崩溃**：在翻译与摘要任务中，模型普遍存在语义崩溃现象，BLEU 分数通常低于 **10** 。



## 📄 引用 (Citation)

如果您在研究中使用了本项目，请引用我们的工作：

```bibtex
@article{tm_bench2026,
  title={TM-Bench: Benchmarking Large Language Models on Low-resource Traditional Mongolian},
  author={Anonymous Authors},
  journal={ACL Submission},
  year={2026}
}

```
