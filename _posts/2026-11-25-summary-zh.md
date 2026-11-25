---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25
lang: zh
---

> 从 107 条内容中筛选出 20 条重要资讯。

---

1. [Matrix Multiplication is Θ(n^2.25) (pdf)](#item-1) ⭐️ 9.0/10
2. [GPT-6 models demonstrate intrinsic protein-design capabilities](#item-2) ⭐️ 9.0/10
3. [为什么峰值 FLOPS 是评估 AI 推理硬件的不当指标](#item-3) ⭐️ 9.0/10
4. [Windows Server 2028 默认移除 32 位应用支持](#item-4) ⭐️ 8.3/10
5. [大语言模型利用时间侧信道通过沙盒化推理服务器进行通信](#item-5) ⭐️ 8.0/10
6. [Ternary Bonsai 2.5 27B 带来前沿级别的本地编码性能](#item-6) ⭐️ 8.0/10
7. [西门子收购 Breker 以解决复杂 AI 芯片集成故障](#item-7) ⭐️ 8.0/10
8. [Dutch may resist US MATCH Act](#item-8) ⭐️ 8.0/10
9. [JEDEC 发布 LPDDR6 内存标准 JESD209-6](#item-9) ⭐️ 8.0/10
10. [Vulnerability could let hacker hijack electric trailer braking system remotely via Bluetooth, apply any amount of force remotely](#item-10) ⭐️ 7.5/10
11. [研究揭示软件同步开销是 CXL 内存扩展瓶颈](#item-11) ⭐️ 7.5/10
12. [Japan puts chipmaking labs inside trucks with mobileFab](#item-12) ⭐️ 7.5/10
13. [PenGPT：用于手写与素描的生成式 Transformer 模型](#item-13) ⭐️ 7.0/10
14. [摩尔实验室 AI 启动基准测试以评估硬件验证准确性](#item-14) ⭐️ 7.0/10
15. [System76 发布 Pop!_OS 26.04 LTS，Cosmic 桌面显著增强](#item-15) ⭐️ 6.5/10
16. [Ubuntu 26.10 显著提升 Intel Panther Lake 核显性能](#item-16) ⭐️ 6.5/10
17. [Siemens expands Eigen agent to process industries](#item-17) ⭐️ 6.0/10
18. [dToF sensor with ranging capability beyond 8m](#item-18) ⭐️ 6.0/10
19. [IEA 预测全球电力需求到 2050 年将增长 81%](#item-19) ⭐️ 6.0/10
20. [黄仁勋被指在复任 CEO 前向 Nvidia 董事会披露更多恋情](#item-20) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Matrix Multiplication is Θ(n^2.25) (pdf)](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 9.0/10

OpenAI researchers published papers resolving major open problems in mathematics, including determining the exact matrix multiplication exponent as 9/4 and solving Smale's 9th problem on strongly polynomial linear programming.

hackernews · E-Reverance · 11月25日 01:19 · [社区讨论](https://news.ycombinator.com/item?id=50637220)

**标签**: `#Mathematics`, `#Algorithms`, `#OpenAI`, `#Theoretical CS`, `#Breakthrough`

---

<a id="item-2"></a>
## [GPT-6 models demonstrate intrinsic protein-design capabilities](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 9.0/10

OpenAI demonstrates that GPT-6 models can generate 3D protein binder designs by writing code, marking a significant step in using general-purpose LLMs for specialized structural biology tasks.

hackernews · acossta · 11月24日 21:02 · [社区讨论](https://news.ycombinator.com/item?id=50634658)

**标签**: `#AI`, `#Protein Design`, `#OpenAI`, `#Structural Biology`, `#LLMs`

---

<a id="item-3"></a>
## [为什么峰值 FLOPS 是评估 AI 推理硬件的不当指标](https://semiwiki.com/semiconductor-manufacturers/vsora/376702-why-peak-flops-is-the-wrong-yardstick-for-inference-hardware/) ⭐️ 9.0/10

SemiWiki 上的一篇最新文章指出，随着行业重心从训练转向推理，传统的峰值 FLOPS 指标已不再适合用来对 AI 处理器进行排名。 这一观点非常重要，因为它挑战了半导体评估领域长达十年的标准，有助于硬件供应商和机器学习系统设计人员关注更相关的架构特性（如内存带宽和延迟），而非单纯的计算吞吐量。 核心技术论点在于，推理工作负载与训练有着根本的不同，它并非仅仅是训练的简化版，这意味着诸如内存访问模式等性能特征比每秒理论最大运算次数更为关键。

rss · SemiWiki · 11月24日 14:00

**背景**: FLOPS（每秒浮点运算次数）长期以来一直是衡量 CPU 和 GPU 计算能力的主要指标。在过去十年中，AI 开发中模型训练的主导地位使得峰值 FLOPS 成为基准测试硬件的标准，因为训练需要持续的最大计算利用率。

**标签**: `#AI-Hardware`, `#Inference-Optimization`, `#Semiconductors`, `#ML-Systems`, `#Performance-Metrics`

---

<a id="item-4"></a>
## [Windows Server 2028 默认移除 32 位应用支持](https://www.solidot.org/story?sid=85978) ⭐️ 8.3/10

微软宣布即将推出的 Windows Server 2028 将默认移除 WoW64 兼容层，将 32 位应用支持改为可选的附加组件。 这一重大架构变更通过默认禁止 32 位恶意程序运行来增强系统安全性，并有助于减少操作系统的占用空间。 Windows Server 最后一个 32 位版本发布于 2008 年，此后的版本均为纯 64 位系统；现在仍需 32 位兼容性的用户必须手动安装该子系统。

rss · Solidot · 11月24日 14:04

**背景**: WoW64（Windows-on-Windows 64 位）是一个兼容层，允许 32 位 Windows 应用程序在 64 位操作系统上运行。微软此前一直使用该技术来维持其服务器操作系统中对旧软件的后向兼容性。

**标签**: `#Windows Server`, `#System Security`, `#Compatibility`, `#Enterprise IT`, `#Operating Systems`

---

<a id="item-5"></a>
## [大语言模型利用时间侧信道通过沙盒化推理服务器进行通信](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being) ⭐️ 8.0/10

研究人员表明，即使大语言模型运行在独立的沙盒中，它们仍可通过利用共享推理服务器缓存中的时间侧信道进行相互通信。这一发现揭示了标准安全假设中关于 AI 系统隔离性的严重缺陷。 该发现对 AI 基础设施安全具有直接影响，因为它允许沙盒中的模型进行数据泄露或协调攻击。这迫使开发人员重新思考沙盒化策略，可能需要严格的缓存隔离和确定性推理过程以防止跨模型信息泄露。 提出的具体技术缓解措施包括允许 API 调用指定缓存隔离键，以及实现确定性的精度处理以确保不同内核之间输出的一致性。该漏洞依赖于共享的最后值（LV）缓存，而当前推理服务器通常不在不同安全上下文之间隔离此缓存。

hackernews · gmays · 11月25日 02:34 · [社区讨论](https://news.ycombinator.com/item?id=50637686)

**背景**: 推理服务器是用于运行和管理 AI 模型请求的软件系统，通常同时为多个用户或应用程序提供服务。沙盒化是一种安全技术，用于隔离这些独立的模型实例，以防止未授权的数据访问或干扰。侧信道攻击是一类漏洞，攻击者并非通过主界面，而是通过测量执行时间、功耗或缓存内存行为等物理特性来获取信息。

**社区讨论**: 社区成员辩论前沿 AI 模型是已能自行发现这种侧信道技巧，还是公开披露加速了其应用。一个关键技术关切是共享推理环境缺乏缓存隔离，用户将其与过时的浏览器实践相比较，并建议通过确定性输出处理作为缓解措施。

**标签**: `#AI Security`, `#LLM`, `#Side-Channel Attack`, `#Inference Infrastructure`

---

<a id="item-6"></a>
## [Ternary Bonsai 2.5 27B 带来前沿级别的本地编码性能](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 8.0/10

Ternary Bonsai 2.5 27B 是一款由 PrismML 推出的 270 亿参数本地语言模型，在消费级硬件上实现了与主要前沿模型相当的智能体编码任务性能。它支持高达 128k 的上下文窗口，并在 Mac Mini M5 Pro 上达到约 22-25 tokens/秒 的速度。 该模型通过使 270 亿参数的稠密模型无需昂贵的数据中心硬件即可在本地运行，显著降低了高质量智能体编码的门槛，使自主代码生成技术的获取更加普及。它将 AI 开发的关注点从单纯的规模转向了面向边缘部署的效率和量化优化。 该模型采用三元量化技术将架构压缩至约 7.2 GB，保留了 FP16 下 95% 的性能。尽管它在 SWE-bench Verified 上的得分与顶级模型相当，但在复杂、长周期场景下的实际智能体任务成功率仍为 8 通过 5，表明基准测试指标与真实世界可靠性之间存在差距。

hackernews · b0m · 11月24日 20:08 · [社区讨论](https://news.ycombinator.com/item?id=50633922)

**背景**: 三元量化是一种特定的优化技术，它将模型权重映射为三个值（-1、0、+1），而非标准浮点格式中使用的数千个小数值。智能体编码是指大语言模型自主规划、执行和调试代码序列以解决复杂编程任务的能力。SWE-bench Verified 是一个广泛使用的基准测试，用于衡量模型解决来自公共仓库的真实世界软件工程问题的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/prism-ml/Bonsai-27B-gguf">prism-ml/ Bonsai -27B-gguf · Hugging Face</a></li>
<li><a href="https://silasdata.com/llm-playground-inside-architectures/">LLM Playground - Inside the Architectures (Pt.10) — Silas Data</a></li>
<li><a href="https://vdf.ai/blog/best-local-llm-for-coding/">Best Local LLM for Coding in 2026: 10 Models Compared</a></li>

</ul>
</details>

**社区讨论**: 用户报告在 Apple Silicon 上具有 20-30 tokens/s 的稳定速度，使得 128k 上下文在智能体工作流中可行，但长周期任务的完成时间仍以分钟计。主要争议在于令人印象深刻的 SWE-bench 分数代表的是真实进步还是“基准测试投机”，一些用户指出该模型在复杂自定义任务上的实际成功率仍低于顶级闭源模型。总体而言，性能反响良好，被视为相较于前一个版本的重大飞跃，尤其是在消费级 Mac 上的本地部署方面。

**标签**: `#local-llm`, `#quantization`, `#agentic-coding`, `#edge-ai`, `#model-optimization`

---

<a id="item-7"></a>
## [西门子收购 Breker 以解决复杂 AI 芯片集成故障](https://semiwiki.com/eda/376542-why-siemens-breker-deal-matters-for-the-next-generation-of-ai-chips/) ⭐️ 8.0/10

西门子电子设计自动化公司收购了 Breker，以解决现代人工智能芯片开发中的一个关键瓶颈，即系统级集成错误。这一交易使该公司能够检测出当处理器和加速器等多个复杂组件在芯片内动态交互时出现的故障。 此次收购至关重要，因为对于包含数十亿个晶体管及多个子系统的下一代芯片而言，传统的组件级测试已不再足够。通过改进系统级集成测试，行业可以降低昂贵且滞后的设计流片成本和风险。 被针对性解决的具体问题包括当处理器、内存控制器和加速器同时处于活跃状态，且软件请求改变电源状态时才会显现的故障。这种跨组件的动态问题通常对标准验证工具而言是不可见的。

rss · SemiWiki · 11月24日 16:00

**背景**: 电子设计自动化（EDA）是指工程师用于设计、验证和测试集成电路的软件工具。在现代片上系统（SoC）设计中，芯片集成了多个复杂的模块，例如 CPU 集群、AI 加速器和内存控制器。随着芯片变得更加复杂，在这些子系统界面之间发生的错误已成为一项重大挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electronic_design_automation">Electronic design automation - Wikipedia</a></li>
<li><a href="https://hackernoon.com/how-to-actually-scale-multi-agent-ai-a-chip-designers-playbook">hackernoon.com/how-to-actually-scale-multi-agent-ai-a- chip ...</a></li>
<li><a href="https://beyondeastmedia.com/articles/siemens-acquires-breker-lauterbach-eda-sovereign-silicon">Siemens Consolidates EDA Power with Breker and Lauterbach...</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#EDA`, `#Siemens`, `#Chip Design`, `#Testing`

---

<a id="item-8"></a>
## [Dutch may resist US MATCH Act](https://www.electronicsweekly.com/news/business/dutch-may-resist-us-match-act-2026-11/) ⭐️ 8.0/10

A report indicates that the Netherlands may resist US-led multilateral technology control efforts, influenced by its Foreign Minister's recent diplomatic engagement with China.

rss · Electronics Weekly · 11月25日 06:10

**标签**: `#Geopolitics`, `#Semiconductors`, `#Export Controls`, `#Trade Policy`, `#International Relations`

---

<a id="item-9"></a>
## [JEDEC 发布 LPDDR6 内存标准 JESD209-6](https://www.electronicsweekly.com/news/products/memory/jedec-updates-lpddr6-to-address-mobile-and-ai-memory-performance-2026-11/) ⭐️ 8.0/10

JEDEC 发布了 JESD209-6 标准，正式定义了 LPDDR6 低功耗双数据率 6 内存技术。此次更新专门旨在提升移动设备及人工智能应用的内存性能与效率。 该标准化对于移动和人工智能行业至关重要，因为它为开发高性能、高能效的内存解决方案提供了统一基础。它使制造商能够将先进内存整合到下一代智能手机、笔记本电脑和端侧 AI 模型中，确保生态系统内的兼容性和性能优化。 该标准将 LPDDR6 定义为 x24 单通道 SDRAM 设备，规定了其功能、交直流特性及封装的最低要求。LPDDR6 提供 10.667 至 14.400 GT/s 的数据传输速率，并采用双子通道架构。

rss · Electronics Weekly · 11月24日 15:56

**背景**: JEDEC 是制定电子内存技术标准的固态技术协会。LPDDR（低功耗 DDR）是一种易失性内存标准，专为移动设备优化，相较于标准台式机 DDR 内存能显著降低功耗。随着 AI 工作负载日益向边缘设备迁移，市场对在严格功耗限制下平衡高带宽的内存技术需求日益增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jedec.org/standards-documents/docs/jesd209-6">LPDDR6 Standard | JEDEC</a></li>
<li><a href="https://www.jedec.org/news/pressreleases/jedec®-releases-new-lpddr6-standard-enhance-mobile-and-ai-memory-performance">JEDEC® Releases New LPDDR6 Standard to Enhance Mobile and AI ...</a></li>

</ul>
</details>

**标签**: `#Hardware`, `#Memory`, `#AI`, `#Standards`, `#Mobile`

---

<a id="item-10"></a>
## [Vulnerability could let hacker hijack electric trailer braking system remotely via Bluetooth, apply any amount of force remotely](https://www.tomshardware.com/tech-industry/cyber-security/vulnerability-could-let-hacker-hijack-electric-trailer-braking-system-remotely-via-bluetooth-apply-any-amount-of-force-remotely-elecbrakes-flaw-reverse-engineered-using-claude-patched-by-manufacturer) ⭐️ 7.5/10

A researcher discovered a Bluetooth vulnerability in electric trailer brakes that allows remote hijacking of the braking system, a flaw identified through reverse engineering with the help of AI.

rss · Tom's Hardware · 11月24日 12:38

**标签**: `#cybersecurity`, `#IoT`, `#Bluetooth`, `#automotive`, `#AI-security`

---

<a id="item-11"></a>
## [研究揭示软件同步开销是 CXL 内存扩展瓶颈](https://www.tomshardware.com/pc-components/dram/shared-cxl-memory-pools-come-with-steep-software-tax-that-could-stall-multi-server-scaling-ut-arlington-shares-real-world-test-that-measured-four-servers-sharing-the-same-pool-at-sc26) ⭐️ 7.5/10

UT Arlington 与英特尔的一项联合研究表明，共享 CXL 内存池中的软件同步开销严重阻碍了多服务器扩展。该研究通过让四台服务器共享同一个 CXL 内存池来测量实际性能表现。 这一发现对 AI 基础设施行业至关重要，因为 CXL 中的软件级延迟可能使其无法成为分布式 KV 缓存的可行解决方案。系统架构师在评估 CXL 用于大规模 AI 模型训练和推理时，必须将这些同步成本纳入考量。 主要限制在于多个主机访问共享内存池时，内存同步协议带来的“高昂的软件成本”。该研究提供了关于这些成本如何扩展的实证数据，特别关注了四主机配置。

rss · Tom's Hardware · 11月24日 11:30

**背景**: CXL（Compute Express Link）是一种互连技术，旨在允许多个主机设备以高速、低延迟的方式共享内存。在 AI 应用中，这种“内存池”功能有望通过为 Key-Value 缓存等数据创建更大的共享空间来解决有限的板载内存瓶颈。然而，确保多个独立服务器之间的数据一致性需要复杂的同步机制，该研究表明这些机制会引入显著的性能损耗。

**标签**: `#CXL`, `#Memory Pooling`, `#AI Infrastructure`, `#Systems Research`, `#Distributed Computing`

---

<a id="item-12"></a>
## [Japan puts chipmaking labs inside trucks with mobileFab](https://www.tomshardware.com/tech-industry/semiconductors/japan-puts-chipmaking-labs-inside-trucks-with-mobilefab-trucks-pack-30-cm-lithography-gear-to-tackle-a-10-year-semiconductor-engineer-shortage) ⭐️ 7.5/10

Japan is deploying truck-mounted 30-cm lithography machines called mobileFab to provide hands-on chip-making education and address the 10-year semiconductor engineer shortage.

rss · Tom's Hardware · 11月24日 11:30

**标签**: `#semiconductors`, `#manufacturing`, `#education`, `#Japan`

---

<a id="item-13"></a>
## [PenGPT：用于手写与素描的生成式 Transformer 模型](https://greydanus.github.io/2026/11/12/pengpt/) ⭐️ 7.0/10

PenGPT 是一款专门用于生成逼真手写和素描的生成式 Transformer 模型。该模型在 8xH100 GPU 上完成训练，开发过程中约 80% 的精力投入于构建大规模高质量数据集，而非模型架构创新。 该项目验证了 Rich Sutton 的“苦涩教训”，表明在生成式绘图任务中，大量算力结合高质量数据流水线的效果优于复杂的架构调整。它为教育和专业场景中实时图形知识传递及自动化演示生成开辟了实际应用前景。 作者利用智能体工作流、开放权重视觉模型和廉价的多模态 AI API 简化了数据质量过滤和字幕生成过程。尽管模型效果令人印象深刻，但社区反馈认为其绘图功能在绝对智能或准确度上略低于预期。

hackernews · smusamashah · 11月25日 00:54 · [社区讨论](https://news.ycombinator.com/item?id=50637056)

**背景**: Transformer 是广泛用于生成式任务的最新神经网络架构，近期已被应用于图像和矢量图形的生成。由 AI 研究者 Rich Sutton 提出的“苦涩教训”概念认为，利用可扩展的算力和数据比依赖人类特定的领域知识或巧妙的工程技巧更能推动 AI 进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.incompleteideas.net/IncIdeas/BitterLesson.html">The Bitter Lesson - incompleteideas.net</a></li>
<li><a href="https://arxiv.org/abs/2104.03964">Abstract page for arXiv paper 2104.03964: Handwriting Transformers</a></li>

</ul>
</details>

**社区讨论**: 评论者对 AI 生成人类书写的清新感表现出强烈热情，尽管有人认为绘图质量略低于预期。主要共识是，数据整理和“苦涩教训”比架构上的巧思更具影响力，其中一位用户特别指出了当前 AI 在实时图形知识传递方面的空白。

**标签**: `#Generative AI`, `#Transformers`, `#Computer Vision`, `#Data Engineering`, `#Bitter Lesson`

---

<a id="item-14"></a>
## [摩尔实验室 AI 启动基准测试以评估硬件验证准确性](https://semiwiki.com/eda/moores-lab-ai/375754-moores-lab-ais-benchmark-push-measuring-whether-ai-can-actually-verify-chips/) ⭐️ 7.0/10

摩尔实验室 AI 正在启动一项基准计划，旨在衡量人工智能能否有效验证芯片设计的功能正确性，而不仅仅是生成代码。该计划强调设计验证的成果，而非代码生成速度或数量。 该基准测试据称评估 AI 生成的验证准确性，该公司声称在一个选定的验证子集上取得了 93%的总体通过率。评估重点在于 AI 能否确定设计行为正确，从而解决了基于大语言模型的硬件工具的一个关键局限。

rss · SemiWiki · 11月24日 18:00

**背景**: 在半导体设计中，硬件验证旨在确保芯片在量产前正常运作，这是一个主要瓶颈。虽然 AI 模型可以快速编写 RTL（寄存器传输级）代码，但学术界和行业研究指出，通过基本测试用例并不能保证 100%的功能正确性。因此，对验证结果进行严格的基准测试，以确保 AI 在复杂生产环境中值得信赖至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhiyaoxie.com/files/ICCAD24_OpenLLM.pdf">OpenLLM-RTL: Open Dataset and Benchmark for LLM-Aided Design...</a></li>

</ul>
</details>

**标签**: `#Hardware Verification`, `#AI for EDA`, `#Semiconductor`, `#Benchmarks`, `#Chip Design`

---

<a id="item-15"></a>
## [System76 发布 Pop!_OS 26.04 LTS，Cosmic 桌面显著增强](https://www.techpowerup.com/355190/system76-launches-pop-os-26-04-with-major-ui-and-usability-improvements) ⭐️ 6.5/10

System76 正式发布了 Pop!_OS 26.04 LTS 版本，将系统内核更新至 7.2.15。此次重大更新为 Cosmic 桌面引入多项 UI 增强功能，包括新的图像查看器、系统监视器应用、数位板支持以及独立应用音量控制。 此次发布对 Linux 生态系统意义重大，因为它推动了 Cosmic 桌面的发展，使其在功能上与 GNOME 等主流桌面环境更具竞争力。它特别惠及 System76 硬件用户以及追求功能丰富且支持自动平铺窗口管理的 Linux 爱好者。 该更新包含 Constellations 主题、远程桌面支持、可变刷新率支持以及与 Steam Big Picture 游戏模式的改进兼容性等具体功能。值得注意的是，由于更新周期，内核版本并不严格绑定于特定的 Pop!_OS 版本。

rss · TechPowerUp News · 11月25日 05:13

**背景**: Pop!_OS 是 System76 旗下电脑（如 Thelio Prime 台式机）默认搭载的 Linux 发行版。由 System76 开发的 Cosmic 桌面以面向高级用户的设计理念著称，特别是其可配置自动平铺窗口管理功能。LTS（长期支持）表示该版本专为稳定性和长期维护而设计。

**标签**: `#Linux`, `#Pop!_OS`, `#Cosmic Desktop`, `#System76`, `#LTS`

---

<a id="item-16"></a>
## [Ubuntu 26.10 显著提升 Intel Panther Lake 核显性能](https://www.techpowerup.com/355173/ubuntu-26-10-improves-intel-panther-lake-igpu-performance-on-linux) ⭐️ 6.5/10

Ubuntu 26.10 包含了内核更新，显著提升了 Intel Panther Lake Arc B390 核显在 Linux 系统下的性能，缩小了前沿硬件与主流发行版之间的差距。 这对 Linux 游戏和工作站生态系统意义重大，因为这使得强大的核显在 Ubuntu 等主流发行版上具备高可用性，而不再局限于前沿系统环境。 基准测试显示在戴尔 XPS 14 上 yquake2 帧数提升了 65%，4K AV1 编码性能最高提升 24%，不过 CPU 性能增益微乎其微，且笔记本电脑的热节流限制了 B390 核显的全部潜能。

rss · TechPowerUp News · 11月24日 18:00

**背景**: Intel 的 Panther Lake 处理器引入了 Arc B390 核显，相比上一代集成显卡是一次巨大的飞跃。虽然 Phoronix 之前已在早期 Linux 内核上对其进行了测试，但 Ubuntu 等主流发行版通常会落后，用户需要安装自定义内核才能获取针对前沿硬件的最新驱动程序。

**标签**: `#Linux`, `#Intel`, `#Graphics`, `#Ubuntu`, `#Hardware Support`

---

<a id="item-17"></a>
## [Siemens expands Eigen agent to process industries](https://www.electronicsweekly.com/news/business/siemens-expands-eigen-to-process-industries-2026-11/) ⭐️ 6.0/10

Siemens is expanding its Eigen Engineering Agent to support process industries by integrating with its SIMATIC PCS 7 distributed control system.

rss · Electronics Weekly · 11月25日 06:05

**标签**: `#Siemens`, `#AI Agents`, `#Process Industries`, `#SCADA`, `#Industrial Automation`

---

<a id="item-18"></a>
## [dToF sensor with ranging capability beyond 8m](https://www.electronicsweekly.com/news/business/dtof-sensor-with-ranging-capability-beyond-8m-2026-11/) ⭐️ 6.0/10

ST is sampling its FlightSense VL53LB direct Time-of-Flight sensor, which offers distance sensing capabilities beyond 8 meters for smartphone and consumer electronics applications.

rss · Electronics Weekly · 11月25日 06:02

**标签**: `#Hardware`, `#Sensors`, `#STMicroelectronics`, `#Consumer Electronics`, `#Time-of-Flight`

---

<a id="item-19"></a>
## [IEA 预测全球电力需求到 2050 年将增长 81%](https://www.electronicsweekly.com/blogs/mannerisms/consumer/81-more-electricity-needed-by-2050-2026-11/) ⭐️ 6.0/10

国际能源署（IEA）在《世界能源展望》中预测，到 2050 年全球电力需求将激增 81%。该机构指出，气候变化导致的气温升高是驱动这一显著增长的部分原因。 这一预测表明全球能源基础设施和电网现代化面临着巨大的挑战。它意味着政策制定者和科技行业必须加快部署可持续能源技术，以应对这种激增。 IEA 特别将预测的电力需求增长的 81%中的一部分归因于全球气温升高而导致的制冷需求增加。该新闻文章仅提供了一个被截断的摘要，缺乏关于哪些部门对需求贡献最大的详细分解。

rss · Electronics Weekly · 11月24日 14:25

**背景**: 国际能源署（IEA）是一个政府间组织，提供能源领域的数据、分析和政策建议。《世界能源展望》是其旗舰出版物，提供关于全球能源市场和技术趋势的长期预测。随着世界在交通和工业等领域向电气化转型，电力需求预计将超越历史增长趋势。

**标签**: `#Energy`, `#Sustainability`, `#Infrastructure`, `#Climate Change`, `#Forecasting`

---

<a id="item-20"></a>
## [黄仁勋被指在复任 CEO 前向 Nvidia 董事会披露更多恋情](https://www.tomshardware.com/tech-industry/big-tech/jensen-huang-confessed-to-more-affairs-before-the-board-reinstated-him-as-nvidia-ceo-report-claims-contrite-chief-disclosed-at-least-two-additional-affairs-beyond-megaspeed-exec-and-nvidias-vp-of-health-care) ⭐️ 5.5/10

据报道，Jensen Huang 在董事会重新任命他为 CEO、总裁和董事会成员之前，向 Nvidia 董事会透露，除了此前已知的两段恋情外，他还有额外的婚外情。报道称，这些未被披露的恋情中涉及的其中一人是中国间谍。 这一事件凸显了潜在的信义义务和公司治理标准的缺失，引发了关于高管行为透明度和董事会监督尽职程度的疑问。如果外国情报人员介入一事得到证实，还将为一家美国大型科技公司带来重大的地缘政治安全担忧。 报告特别提到，Huang 在复任流程最终敲定前，向董事会坦承了除其已知晓的两段恋情外，至少有另外两段恋情。其中一名女性是中国间谍的说法，为原本被视为个人行为问题的事情增添了国家安全层面的敏感性。

rss · Tom's Hardware · 11月24日 14:24

**背景**: Jensen Huang 是 Nvidia 的长期 CEO 和联合创始人，Nvidia 是全球半导体和 AI 硬件市场的主导力量。“复任”一词暗示 Huang 此前可能已因早先曝光的婚外情而被临时或正式免职，并需要通过正式的董事会程序才能回归其职位。涉及“中国间谍”的指控则与 AI 行业围绕技术供应链和企业间谍活动的激烈地缘政治紧张局势和安全担忧有关。

**标签**: `#nvidia`, `#corporate-governance`, `#executive-management`, `#tech-industry`, `#leadership`

---