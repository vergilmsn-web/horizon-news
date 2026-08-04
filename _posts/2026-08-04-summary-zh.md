---
layout: default
title: "Horizon Summary: 2026-08-04 (ZH)"
date: 2026-08-04
lang: zh
---

> 从 109 条内容中筛选出 20 条重要资讯。

---

1. [AMD 发布 Helios：72 颗 GPU 机架级 AI 系统](#item-1) ⭐️ 8.5/10
2. [FFmpeg 9.0 "雷" 重大版本发布，支持 Vulkan APV 解码](#item-2) ⭐️ 8.3/10
3. [大语言模型奖励专业能力，而非实现编程民主化](#item-3) ⭐️ 8.0/10
4. [Lilian Weng 提出面向 AI 自我改进的 Harness 工程学](#item-4) ⭐️ 8.0/10
5. [DRAM 供应紧张将持续至 2027 年，NVIDIA 或降低 Rubin Ultra 的 HBM 规格](#item-5) ⭐️ 8.0/10
6. [美国禁止进口外国制造的人形机器人，主要针对中国](#item-6) ⭐️ 8.0/10
7. [铠侠与闪迪推出第 10 代 332 层 QLC NAND，接口速率达 4.8 Gb/s](#item-7) ⭐️ 7.5/10
8. [长鑫存储进入 LPDDR6 风险量产阶段，推出 12.8 Gbps 内存芯片](#item-8) ⭐️ 7.5/10
9. [三大存储厂商 2027 年产能售罄，转向长期合约](#item-9) ⭐️ 7.5/10
10. [台积电目标：2026 年底 N2 晶圆月产能达 10 万片](#item-10) ⭐️ 7.5/10
11. [德州暂停 1800 个数据中心申请，电力请求达 474 吉瓦](#item-11) ⭐️ 7.5/10
12. [Sandisk 与 SK hynix 发布 HBF 规范，为 GPU 扩展 TB 级存储](#item-12) ⭐️ 7.5/10
13. [中国芯片制造设备路线图解析——北京新兴光刻设备瞄准年产量五台的 DUV 生产，以及尚无芯片的 EUV 原型机](#item-13) ⭐️ 7.5/10
14. [据报道，三大 PC 制造商现采用中国内存以应对"前所未有的内存短缺"——惠普、华硕和宏碁在面向非美国市场的部分笔记本中少量使用长鑫存储（CXMT）芯片](#item-14) ⭐️ 7.5/10
15. [Anthropic 与 AI 云初创公司签署 100 亿美元算力协议](#item-15) ⭐️ 7.3/10
16. [台积电扩大 CoWoS 封装外包，GPU 订单挤压产能](#item-16) ⭐️ 7.3/10
17. [DeepSeek V4 Flash 在单块 AMD MI300X 上实现 150+ tokens/秒推理](#item-17) ⭐️ 7.0/10
18. [Xbox 服务宕机，玩家无法运行自己拥有的实体光盘游戏](#item-18) ⭐️ 7.0/10
19. [Swiftlet 在 Mac 4.3GB 内存运行 80B Qwen，在 iPhone 运行 35B 模型](#item-19) ⭐️ 7.0/10
20. [数学与理论计算机科学的十项进展](#item-20) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AMD 发布 Helios：72 颗 GPU 机架级 AI 系统](https://www.servethehome.com/amd-helios-architecture-deep-dive-amd-broadcom-hardware-combined/) ⭐️ 8.5/10

在 Advancing AI 2026 大会上，AMD 发布了其首款机架级 AI 系统 Helios，该系统将 72 颗 Instinct MI455X 加速器与 AMD EPYC "Venice" CPU 以及 Pensando Vulcano AI NIC 通过 UALink over Ethernet 互联，整合为统一的单一平台。 Helios 是 AMD 迄今为止最具雄心的端到端 AI 基础设施布局，直接对标 NVIDIA 的 NVL 机架级平台，标志着 AMD 正在从单纯的加速器竞争升级到全系统层面的竞争。 该系统采用行业支持的多供应商互连协议 UALink 实现 GPU 间高速通信，MI455X 平台支持 64 位 Linux，体现出其面向大规模 AI 训练与推理工作负载的定位。

rss · ServeTheHome · 8月3日 19:00

**背景**: 机架级架构将整个机架而非单台服务器视为统一的计算平台，针对需要大规模并行计算的 AI 工作负载优化计算、内存和网络资源。NVIDIA 通过其 NVL 机架级系统率先采用了这一方案。UALink 是一种新兴的开放标准，旨在实现多供应商加速器之间的高速低延迟通信，是 NVIDIA 专有 NVLink 互连协议的抗衡力量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servethehome.com/amd-helios-architecture-deep-dive-amd-broadcom-hardware-combined/">AMD Helios Architecture Deep Dive: The Power of... - ServeTheHome</a></li>
<li><a href="https://www.amd.com/en/products/rackscale-solutions/helios.html">AMD Helios</a></li>
<li><a href="https://www.datacenterknowledge.com/servers/what-is-rack-scale-computing-and-why-is-it-relevant-again-">What Is Rack-Scale Computing?</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Helios`, `#rackscale-architecture`, `#MI455X`, `#AI-datacenter`

---

<a id="item-2"></a>
## [FFmpeg 9.0 "雷" 重大版本发布，支持 Vulkan APV 解码](https://www.solidot.org/story?sid=85003) ⭐️ 8.3/10

FFmpeg 9.0 "雷" 作为重大版本发布，引入了 Vulkan 加速的 APV（Advanced Professional Video）解码、Apple ProRes RAW 的 Vulkan 加速、NVIDIA CUDA 转置滤镜、动画 WebP 解码和解复用、AMD AMF 增强以及 AVX-512 CPU 优化。它还扩展了 AMF 色彩转换器（vf_vpp_amf）的 HDR 功能，并为 MP4 复用器增加了对 LCEVC 音轨复用的支持。 FFmpeg 是最广泛使用的开源多媒体框架之一，是整个行业中无数视频处理、流媒体、编码和播放应用的基石。本次重大版本带来了显著的 GPU 加速（Vulkan、CUDA）和 CPU 级优化（AVX-512），可提升专业视频工作流程（包括 Apple ProRes 和新兴的 APV 编解码器）的性能。 APV 是一种专业视频编解码器，通过 Vulkan 着色器实现，与 FFmpeg 现有的 ProRes Vulkan 加速方式类似。AVX-512 是 x86 CPU 的 512 位 SIMD 指令集扩展，由 Intel 于 2016 年在 Xeon Phi x200 中首次实现，每条指令可处理八个双精度或十六个单精度浮点数。LCEVC（MPEG-5 Part 2）是 ISO/IEC 增强层标准，可与任何基础视频编解码器结合以生成增强视频流。

rss · Solidot · 8月4日 09:52

**背景**: FFmpeg 是一个免费的开源项目，包含用于处理多媒体数据的库和程序，包括 libavcodec（编解码库）、libavformat（容器格式库）以及 ffmpeg 和 ffplay 等命令行工具。它支持几乎所有广泛使用的音频和视频格式，并已集成到 VLC、HandBrake、OBS Studio 和各种流媒体服务等众多软件产品中。Vulkan 是一个跨平台的图形和计算 API，除了游戏外，还越来越多地用于通用 GPU 计算任务，如视频解码和编码。APV（Advanced Professional Video，高级专业视频）是一种较新的专业编解码器，专为高质量视频工作流程而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/FFmpeg-Vulkan-Encoder-APV">FFmpeg Introduces Vulkan APV Encoder - Phoronix</a></li>
<li><a href="https://en.wikipedia.org/wiki/AVX-512">AVX-512 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/LCEVC">LCEVC - Wikipedia</a></li>

</ul>
</details>

**标签**: `#FFmpeg`, `#open-source`, `#multimedia`, `#biology`, `#caves`

---

<a id="item-3"></a>
## [大语言模型奖励专业能力，而非实现编程民主化](https://www.seangoedecke.com/llms-reward-expertise/) ⭐️ 8.0/10

一篇广为传播的文章指出，大语言模型（LLM）本质上是「放大镜」——它们反映并放大用户已有的领域知识和提示工程能力，而非取而代之。作者认为，所谓 AI「让软件开发民主化」的说法具有误导性，因为具备深厚专业知识的从业者始终能从这些工具中获取更大的价值。 这一观点挑战了「LLM 为非程序员消除了技术壁垒」的主流叙事，也动摇了人们对 AI 对软件行业影响的普遍假设。它对团队如何评估生产力提升、组织如何安排培训、以及个人开发者如何利用 AI 辅助工作流都具有实际意义。 文章将提示 LLM 比作临床问诊：熟练的用户会用开放式、结构化的问题引导对话，并在适当时机收敛到具体细节，同时避免强行指定精确输出。评论者还指出，用户自身的词汇量、问题框架能力和世界知识会直接影响模型的回复质量——将 LLM 视为思维延伸的人，远比将其视为思维替代品的人表现更好。

hackernews · MaxMussio · 8月3日 21:13 · [社区讨论](https://news.ycombinator.com/item?id=49161518)

**背景**: 大语言模型（LLM）是在海量文本语料上训练的 AI 系统，通过统计预测序列中的下一个词来生成语言。提示工程（Prompt Engineering）指的是精心设计输入以引导 LLM 产出期望结果的方法，已发展为充分发挥 LLM 效能的关键学科。自 2023 年以来，一种流行观点认为 LLM「让软件开发民主化」，使非程序员也能通过自然语言指令构建应用程序；但批评者指出，输出质量仍然高度依赖用户评估、调试和引导 AI 工作的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>
<li><a href="https://www.promptingguide.ai/techniques">Prompting Techniques | Prompt Engineering Guide</a></li>
<li><a href="https://aws.amazon.com/what-is/large-language-model/">What is LLM? - Large Language Models Explained - AWS</a></li>

</ul>
</details>

**社区讨论**: 社区广泛认同文章的核心论点。评论者提供了富有启发性的类比——一位用户将提示 LLM 比作医生采集病史（引导患者而非替患者作答）；另一位则分享了自己观察一位非工程师朋友尝试引导 LLM 完成一个简单 Web 应用、尽管 AI 本身具备编码能力却始终无法得到正确结果的经历。部分评论者呼吁对该效应进行正式的经验研究，指出轶事式经验存在确认偏差的风险，并观察到那些撰写详细、具体提示的严谨工程师，其产出始终优于只输入简短模糊问题的同事。

**标签**: `#LLMs`, `#AI-assistants`, `#prompting`, `#software-engineering`, `#expertise`

---

<a id="item-4"></a>
## [Lilian Weng 提出面向 AI 自我改进的 Harness 工程学](https://lilianweng.github.io/posts/2026-07-04-harness/) ⭐️ 8.0/10

前 OpenAI 安全负责人 Lilian Weng（目前专注于递归自我改进方向）发表了一篇详尽的技术博文，将「harness 工程」定义为围绕 AI agent 设计脚手架——包括上下文传递、工具接口、规划产物、验证循环、记忆系统和沙盒环境——的一门学科，旨在让模型能够在原始权重之外实现递归式自我改进。 这一框架标志着一个范式的转变：当原始模型训练的边际收益递减时，agent 能力的下一次跃迁可能来自围绕模型的基础设施设计。它也将 harness 设计定位为前沿实验室潜在的竞争护城河，以及自我改进研究的核心阵地。 Weng 将 harness 工程定位为与自动研究、进化式程序搜索、模型自博弈、合成数据、测试时训练和持续学习等领域相关但又有所区别的方向。Weco AI 的 AIDE² 等相关工作已经为递归自我改进的 Level 1 提供了初步的实验证据，而 LangChain 的《Agent Harness 解剖》则用实践模式补充了 Weng 的理论框架。

hackernews · tosh · 8月4日 06:17 · [社区讨论](https://news.ycombinator.com/item?id=49164896)

**背景**: 在 AI agent 语境中，「harness」指的是包裹在基础语言模型外部的软件脚手架——包括提示模板、工具调用、记忆存储、验证脚本和编排逻辑——使模型能够以有用的 agent 形式运作。递归自我改进（RSI）是一个假想过程：AI 系统改写或改进自身的代码，理论上可能触发「智能爆炸」。harness 工程将这一思想向下延伸了一层：agent 不是改写权重，而是迭代式地重新设计围绕自身的脚手架，从而引导出更好的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>
<li><a href="https://www.langchain.com/blog/the-anatomy-of-an-agent-harness">The Anatomy of an Agent Harness</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同这一框架。一位开发者分享了自己通过 agent 编辑散文来构建统一理论的项目；另一位则请 Weng 未来再写一篇关于自动研究与进化式程序搜索的文章。Document.bot 的开发者反馈称已经在 Codex 中使用爬山法（hillclimb）实验来改进他们的应用。一个引发热议的问题是：harness 设计是否是前沿实验室可以建立持久护城河的地方——这也是多条回复中讨论到的开放性战略问题。还有一位评论者用「Torment Nexus（受难装置）」梗来暗讽相关安全问题。

**标签**: `#AI-agents`, `#self-improvement`, `#harness-engineering`, `#recursive-self-improvement`, `#Lilian-Weng`

---

<a id="item-5"></a>
## [DRAM 供应紧张将持续至 2027 年，NVIDIA 或降低 Rubin Ultra 的 HBM 规格](https://www.dramexchange.com/WeeklyResearch/Post/2/12789.html) ⭐️ 8.0/10

TrendForce 报告称 DRAM 供应紧张将持续到 2027 年，这可能迫使 NVIDIA 降低其即将推出的 Rubin Ultra AI 加速器的 HBM 规格。这一供需紧张反映了 AI 工作负载需求持续超过内存制造产能的压力。 HBM 是下一代 AI 训练和推理的关键瓶颈，Rubin Ultra 上 HBM 容量或带宽的任何缩减都可能直接影响 NVIDIA 旗舰 AI 平台的性能和相对于 AMD 及定制 ASIC 方案的竞争力。这一信号对计划围绕 2027 年 NVIDIA 硬件部署算力的超大规模云厂商和 AI 初创公司也有更广泛的影响。 Rubin Ultra 预计将于 2027 年基于台积电 3nm 工艺和 GR110 GPU 推出，最初规格为最高 1,024 GB 的 HBM4e 内存。TrendForce 的分析显示，被削减的配置可能涉及减少 HBM 堆栈数量、降低单堆栈容量，或转向比原计划稍早的 HBM 世代。

rss · DRAMeXchange (TrendForce) · 8月4日 17:26

**背景**: 高带宽内存（HBM）是一种 3D 堆叠 DRAM 技术，可提供远高于传统 GDDR 内存的带宽，已成为 AI 加速器的标准内存解决方案，因为训练大模型需要向 GPU 计算单元传输海量数据。最新的 HBM4e 将每引脚数据速率翻倍至 16 Gb/s，每个堆栈可提供超过 4 TB/s 的带宽。NVIDIA 的产品路线图从 Hopper（H100）演进到 Blackwell（B200）和 Blackwell Ultra（B300，2025 年下半年），随后是 2027 年的 Vera Rubin 和 Rubin Ultra，其中 Rubin Ultra 是旨在进一步提升 AI 训练和推理性能的高端继任者。由 AI 驱动的需求爆发式增长以及三星、SK 海力士和美光有限的晶圆产能扩张，DRAM 供应紧张已成为整个 AI 硬件生态系统的战略性关切。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://arstechnica.com/ai/2025/03/nvidia-announces-rubin-ultra-and-feynman-ai-chips-for-2027-and-2028/">Nvidia announces “ Rubin Ultra ” and “Feynman” AI... - Ars Technica</a></li>
<li><a href="https://www.techpowerup.com/gpu-specs/rubin-ultra-gpu.c4426">NVIDIA Rubin Ultra GPU Specs | TechPowerUp GPU Database</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#HBM`, `#DRAM`, `#AI hardware`, `#supply chain`

---

<a id="item-6"></a>
## [美国禁止进口外国制造的人形机器人，主要针对中国](https://www.electronicsweekly.com/blogs/mannerisms/dilemmas/the-rise-of-the-humanoids-2026-08/) ⭐️ 8.0/10

美国政府上周禁止进口国外制造的新型先进机器人设备，此举主要针对中国。美国联邦通信委员会（FCC）宣布了这项禁令，理由是网络安全和国家安全方面的担忧，该禁令特别适用于最先进的人形机器人。 这项政策标志着中美贸易紧张关系向快速增长的人形机器人领域的显著升级，可能会重塑全球机器人供应链。此举影响尤为重大，因为据报道中国企业在 2025 年出口的人形机器人数量是美国竞争对手的 25 倍，占据了全球市场约 85%的份额。 此次禁令由 FCC 而非传统的贸易或商业机构主导，依据是网络安全和供应链风险方面的理由。北京方面谴责这一行动是保护主义行为，将损害美国企业和消费者的利益，这表明可能会出现报复性措施或外交层面的进一步升级。

rss · Electronics Weekly · 8月4日 13:30

**背景**: 人形机器人是指设计成类似人类外形并能执行类似人类任务的机器人，它将先进的人工智能与传感器、电机和控制系统相结合，用于行走、操作和导航等任务。该领域已迅速从研究阶段发展进入商业部署平台，用于工业和家庭场景，中美两国的主要企业都在争夺市场主导地位。FCC 是监管通信技术的美国机构，其参与表明该禁令是基于联网设备网络安全方面的考量，而非传统的关税贸易政策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chinadailyasia.com/hk/article/637135">China blasts US import ban on humanoid robots</a></li>
<li><a href="https://www.webpronews.com/america-draws-the-line-why-the-u-s-banned-chinese-humanoid-robots-after-they-flooded-the-market/">America Draws the Line: Why the U . S . Banned Chinese Humanoid ...</a></li>
<li><a href="https://roboticsandautomationnews.com/2026/02/07/the-state-of-humanoid-robotics-from-research-labs-to-real-world-potential/98732/">The state of humanoid robotics: assessing the capabilities, limitations, and commercial potential of leading platforms</a></li>

</ul>
</details>

**社区讨论**: 行业报道普遍关注该禁令可能割裂全球人形机器人供应链并加速中美科技脱钩的潜在影响。中国官员和评论人士将这项政策定性为保护主义，认为最终会因限制美国消费者获得更低价机器人而损害其利益，而美国的支持者则强调供应链安全以及培育国产替代方案的必要性。

**标签**: `#humanoid-robots`, `#robotics`, `#trade-policy`, `#us-china-trade`, `#import-restrictions`

---

<a id="item-7"></a>
## [铠侠与闪迪推出第 10 代 332 层 QLC NAND，接口速率达 4.8 Gb/s](https://www.techpowerup.com/351353/kioxia-and-sandisk-unveil-10th-gen-332-layer-qlc-nand-with-4-8-gb-s-interface-speeds) ⭐️ 7.5/10

铠侠（Kioxia）与闪迪（Sandisk）联合发布了其第 10 代四层单元（QLC）3D NAND 闪存技术，采用 332 层堆叠，位密度突破 37 Gb/mm²（较第 8 代提升 60%），并以 4.8 Gb/s 的接口速率成为业界首款达到该速度的 QLC 闪存。该技术采用了 CMOS 直接键合到阵列（CBA）架构，将 CMOS 逻辑电路与存储阵列分别在不同的晶圆上制造，然后再进行高精度键合。 这一发布在密度、速度和单位比特成本三个维度上推动了存储行业的进步，将直接惠及数据中心、AI 工作负载及消费级设备所需的大容量 SSD。4.8 Gb/s 的接口速率尤为关键，因为 QLC NAND 由于每个单元存储更多比特，传统上在性能上落后于 TLC，如今缩小这一性能差距有望加速 QLC 在对性能敏感的场景中的采用。 CBA（CMOS 直接键合到阵列）技术是较旧的 CMOS 下置阵列（CuA）单片工艺的演进，允许 CMOS 逻辑和存储阵列各自独立优化后再通过晶圆对晶圆混合键合，从而提高高堆叠层数下的良率和可扩展性。332 层架构和 37 Gb/mm²的密度均为业界领先水平，但作为新闻稿，本次发布尚未透露单颗芯片容量、耐久度评级或量产时间表。

rss · TechPowerUp News · 8月4日 13:38

**背景**: NAND 闪存通过浮栅晶体管以电荷形式存储数据；每个单元存储的比特数越多，密度越高，但通常速度和耐久度会下降。QLC（四层单元）每个单元存储 4 比特，是大容量驱动器中性价比最高的方案，但比 TLC 或 SLC 更慢且寿命更短。传统 3D NAND 将存储单元层垂直堆叠，但当层数超过 200 层时，制造难度显著增加；CBA 架构通过将 CMOS 控制逻辑与存储阵列分离到不同晶圆、再进行混合键合来解决这一难题，从而实现更精细的工艺控制和持续的可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.electronicdesign.com/technologies/embedded/article/55307984/imec-unlocking-z-pitch-scaling-for-next-generation-3d-nand-flash">Unlocking Z-Pitch Scaling for Next-Generation 3 D NAND Flash</a></li>
<li><a href="https://www.silicon-power-industrial.com/news-center-detail/bics8/">BiCS8 3 D NAND : Next-Gen Edge & Embedded Storage Guide</a></li>
<li><a href="https://filtron.co/flash-memory-explained-why-your-devices-are-faster-than-ever-3gh">Flash Memory Explained : Why Your Devices Are Faster Than... - Filtron</a></li>

</ul>
</details>

**标签**: `#NAND flash`, `#storage technology`, `#Kioxia`, `#Sandisk`, `#semiconductor`

---

<a id="item-8"></a>
## [长鑫存储进入 LPDDR6 风险量产阶段，推出 12.8 Gbps 内存芯片](https://www.techpowerup.com/351350/cxmt-enters-lpddr6-risk-production-with-12-8-gbps-memory-chips) ⭐️ 7.5/10

中国内存制造商长鑫存储已启动 LPDDR6 芯片的风险量产，速率达 12.8 Gbps，在新一代移动 DRAM 技术上与三星、SK 海力士及美光并驾齐驱。

rss · TechPowerUp News · 8月4日 12:59

**标签**: `#LPDDR6`, `#CXMT`, `#memory`, `#semiconductors`, `#DRAM`

---

<a id="item-9"></a>
## [三大存储厂商 2027 年产能售罄，转向长期合约](https://www.techpowerup.com/351344/memory-makers-seal-2027-deals-no-room-for-new-buyers) ⭐️ 7.5/10

三星、SK 海力士和美光已提前数年售罄 2027 年全部内存产能，并迫使客户签订附带预付款的 3-5 年长期合约。由于只能满足约 60-70%的预估需求，2027 年将成为近年来内存短缺最严重的一年。 这标志着在 AI 基础设施需求推动下，内存市场出现了根本性转变，小型买家将被排挤在供应之外，DRAM 价格可能在未来数年持续走高。未锁定产能的硬件 OEM、PC 厂商和 AI 实验室将面临产能受限和组件成本上涨的风险，这种状况将持续到 2028 年。 预付款模式要求客户预先支付未来内存产能的费用，合约按客户逐个谈判。据业内人士透露，每年 7 月和 8 月是锁定下一年产能分配的关键月份，而相关消息一直被保密，以免现有客户失去已分配份额。

rss · TechPowerUp News · 8月4日 09:04

**背景**: DRAM（动态随机存取存储器）是服务器、PC 及几乎所有计算设备中使用的核心易失性存储器。全球 DRAM 产能高度集中，超过 90%的供应由少数大型制造商掌控，这些厂商使用 300mm 晶圆生产线。近期 AI 工作负载（特别是大语言模型训练与推理）的激增，大幅推高了对高带宽内存和传统 DRAM 的需求，从而重塑了整个半导体行业的供需格局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.industryresearch.co/blog/top-dram-wafer-companies-12">DRAM Wafer Market Outlook 2026–2035 | Growth & Trends</a></li>
<li><a href="https://www.linkedin.com/posts/futurum-group-hq_ai-semiconductors-memory-activity-7488859988816384001-omoe">#ai # semiconductors #memory #futurum | The Futurum Group</a></li>

</ul>
</details>

**标签**: `#memory-market`, `#DRAM`, `#semiconductors`, `#AI-infrastructure`, `#supply-chain`

---

<a id="item-10"></a>
## [台积电目标：2026 年底 N2 晶圆月产能达 10 万片](https://www.techpowerup.com/351326/tsmc-targets-100-000-n2-wafers-per-month-by-the-end-of-2026) ⭐️ 7.5/10

台积电正快速扩大其 2 纳米 N2 制程的产能，目标是在 2026 年底前将月产量从约 2 万片晶圆提升至 10 万片，在大约四个月内实现五倍增长。同时，来自英伟达、AMD 和博通的需求已将 N3 系列制程的月产能推至 18 万片晶圆，超出了台积电原定的 2026 年第四季度目标。 这一激进的扩产计划反映了市场对尖端 AI 和消费级芯片需求的激增，并表明 2 纳米制程将从小众产品转型为重要的收入驱动力，在台积电营收占比中从 3%跃升至超过 10%。产能扩张的速度也表明前沿代工市场依然紧张，这对芯片定价、供应链规划以及台积电的竞争对手都有重要影响。 N2 晶圆的单价约为 3 万美元，比上一代 3 纳米制程高出约 20%，使 N2 成为全球科技供应链中最昂贵的产能资源之一。N2 制程在台积电的宝山工厂量产，并采用全环绕栅极（GAA）晶体管架构，相比 N3 所用的 FinFET 晶体管可提供更佳的性能和能效。

rss · TechPowerUp News · 8月3日 17:12

**背景**: 台积电的 N2 是该公司首个 2 纳米级别的制程节点，标志着从 FinFET 向全环绕栅极（GAA）晶体管架构的代际转变，GAA 架构中栅极完全包围沟道，可实现更好的电流控制和更低的漏电。当前的营收分布显示 N5 占 33%、N3 占 30%、N2 仅占 3%，凸显了新制程通常从小规模起步再逐步放量的特点。据广泛报道，苹果是 N2 的主要客户，高通、联发科、AMD 和英伟达预计将在后续陆续跟进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tweaktown.com/news/112989/tsmc-is-ramping-up-2nm-production-100k-monthly-wafers-by-the-end-of-2026/index.html">TSMC is ramping up 2 nm production, 100K monthly wafers by the end...</a></li>
<li><a href="https://faq.com.tw/en/hardware/2026-05-18-tsmc-n2-2nm-chip-ramp-ai-hardware-en/">TSMC 's 2 nm Chip Production Surges Toward 140,000 Wafers a Month...</a></li>
<li><a href="https://cambashi-insights.com/encyclopedia/gate-all-around/">Gate - All - Around ( GAA ) - Cambashi Insights</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#TSMC`, `#manufacturing`, `#2nm`, `#silicon`

---

<a id="item-11"></a>
## [德州暂停 1800 个数据中心申请，电力请求达 474 吉瓦](https://www.tomshardware.com/tech-industry/data-centers/texas-slams-on-the-breaks-for-1-800-data-centers-power-grid-requirements-are-five-times-higher-than-peak-record-demand-474-gigawatts-of-power-requests-are-now-subject-to-new-moratorium) ⭐️ 7.5/10

德克萨斯州州长 Greg Abbott 已指示德州公用事业委员会（PUCT）和 ERCOT 暂停所有数据中心申请并进行全面的审计。此次暂停涉及约 1800 个项目，合计请求 474 吉瓦的电力——大约是该州历史峰值需求的五倍——而 377 家运营商中仅有 28 家遵守了信息披露要求。 这次暂停暴露了 AI 基础设施建设中的一个关键瓶颈：电网容量正成为比芯片或资本更紧迫的约束。这表明州级监管机构开始对无序的数据中心扩张进行反击，可能会重塑超大规模云服务商和 AI 公司选择新建设施地点的决策。 ERCOT 管理着德州约 90%的电力负荷，而 474 吉瓦的待审批容量远远超过电网实际约 80-90 吉瓦的峰值需求。极低的合规率（377 家中仅 28 家）表明数据中心规划存在系统性不透明问题，使得审计成为任何有意义的电网可靠性评估的前提。

rss · Tom's Hardware · 8月4日 14:57

**背景**: ERCOT（德州电力可靠性委员会）是负责管理德州约 90%电力负荷流动的独立电网运营商。德州公用事业委员会（PUCT）是监管 ERCOT 并为投资者所有的公用事业制定规则的州级监管机构。数据中心——尤其是为 AI 训练和推理工作负载提供算力的设施——消耗大量电力和冷却用水，它们在德州的快速扩张得益于廉价的土地、有利的税收政策以及该州独立的电网（不受联邦跨州监管约束）。德州在 2021 年冬季风暴 Uri 期间经历了重大电网故障，这使得电网可靠性成为一个政治敏感议题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacenterdynamics.com/en/news/texas-governor-directs-puct-ercot-to-audit-all-data-centers-seeking-grid-connection/">Texas governor directs PUCT , ERCOT to audit all data centers seeking...</a></li>
<li><a href="https://www.battleswarmblog.com/?p=72588">The Texas Data Center Dilemma « Lawrence Person's BattleSwarm Blog</a></li>
<li><a href="https://texasborderbusiness.com/turning-on-the-juice/">Turning on the Juice! - Texas Border Business</a></li>

</ul>
</details>

**标签**: `#data-centers`, `#ai-infrastructure`, `#power-grid`, `#regulation`, `#texas`

---

<a id="item-12"></a>
## [Sandisk 与 SK hynix 发布 HBF 规范，为 GPU 扩展 TB 级存储](https://www.tomshardware.com/pc-components/ssds/sandisk-and-sk-hynix-unveil-hbf-spec-up-to-16-hi-nand-stacks-3-tb-s-bandwidth-ucie) ⭐️ 7.5/10

Sandisk 与 SK hynix 通过开放计算项目（OCP）正式发布了高带宽闪存（HBF）技术规范，目标带宽高达 3 TB/s，并通过 UCIe 接口支持最高 16 层堆叠的 NAND。在标准化过程中，Google 和 Tenstorrent 加入了该联盟，但目前仅有四家公司参与该技术。 HBF 有望以高带宽为 GPU 提供 TB 级的额外内存容量，直接缓解制约大型 AI 推理工作负载的内存瓶颈问题。若被广泛采用，它可能通过提供比 HBM 更便宜、容量更大的替代方案或补充方案，重塑 AI 加速器的经济性，从而降低 AI 推理系统的总拥有成本。 该规范目标支持最高 16 层堆叠的 NAND 并采用 TSV（硅通孔）技术，同时使用 UCIe 芯粒互连标准实现封装级集成。3 TB/s 的带宽数字是目标值而非现有产品的能力，且本次发布的是规范文档，并非已出货的硬件或量产 AI 服务器。

rss · Tom's Hardware · 8月4日 14:42

**背景**: 高带宽存储器（HBM）是目前 GPU 和 AI 加速器使用的高带宽内存标准，但它价格昂贵且每颗堆叠容量有限。NAND 闪存每美元容量远高于 HBM，但传统上速度太慢，无法被计算加速器直接使用。HBF 试图通过垂直堆叠 NAND 裸片（最多 16 层，使用 TSV 硅通孔技术）并通过 UCIe 芯粒互连接口将其暴露出来，从而弥合这一差距，使大型闪存池能够足够靠近计算单元，以服务 AI 推理工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.skhynix.com/en/hbf-at-fms-2026/">SK hynix Unveils First HBF Standard Specifications with Sandisk ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.uciexpress.org/">Home | UCIe Consortium</a></li>

</ul>
</details>

**标签**: `#GPU`, `#memory-technology`, `#NAND`, `#UCIe`, `#AI-infrastructure`

---

<a id="item-13"></a>
## [中国芯片制造设备路线图解析——北京新兴光刻设备瞄准年产量五台的 DUV 生产，以及尚无芯片的 EUV 原型机](https://www.tomshardware.com/tech-industry/semiconductors/chinese-chipmaking-tool-roadmap-examined) ⭐️ 7.5/10

分析中国新兴光刻设备路线图，考察其雄心勃勃的 DUV 生产目标（年产五台）与仅有原型、尚无成品芯片的 EUV 项目之间的差距，并质疑该计划能否成为成熟厂商的真正竞争对手。

rss · Tom's Hardware · 8月4日 13:15

**标签**: `#semiconductors`, `#lithography`, `#DUV`, `#EUV`, `#China-tech`, `#chip-manufacturing`, `#geopolitics`

---

<a id="item-14"></a>
## [据报道，三大 PC 制造商现采用中国内存以应对"前所未有的内存短缺"——惠普、华硕和宏碁在面向非美国市场的部分笔记本中少量使用长鑫存储（CXMT）芯片](https://www.tomshardware.com/tech-industry/three-major-pc-makers-now-using-chinese-memory-to-fight-unprecedented-memory-shortage-report-claims-hp-asus-and-acer-using-small-amounts-of-cxmt-chips-in-limited-number-of-notebooks-for-non-us-market) ⭐️ 7.5/10

据报道，惠普、华硕和宏碁已在面向非美国市场的有限笔记本产品中开始使用长鑫存储（CXMT）的中国内存芯片，以应对持续的内存短缺问题。

rss · Tom's Hardware · 8月4日 10:15

**标签**: `#memory-shortage`, `#supply-chain`, `#CXMT`, `#PC-manufacturing`, `#semiconductors`

---

<a id="item-15"></a>
## [Anthropic 与 AI 云初创公司签署 100 亿美元算力协议](https://36kr.com/newsflashes/3925172170324099?f=rss) ⭐️ 7.3/10

据中国财经媒体第一财经报道，Anthropic 已与一家 AI 云初创公司签署了一项价值 100 亿美元的算力协议。该简短的快讯中未透露合作方名称、合同期限或具体的算力承诺等细节。 100 亿美元规模的算力交易凸显了训练和部署前沿 AI 模型所需的巨额资本开支，并表明 Anthropic 在与 OpenAI、Google DeepMind 及其他主要 AI 实验室竞争中的积极基础设施战略。这也反映出市场对 AWS、Google Cloud 和 Azure 等传统超大规模云厂商之外的专用 AI 云提供商的需求正在增长。 该消息以单行快讯形式发布，未透露初创公司合作伙伴、合同期限或是否涉及 GPU 集群、自研芯片或数据中心容量等具体信息。Anthropic 此前主要依赖 Amazon Web Services 和 Google Cloud 作为主要算力合作伙伴，因此向一家初创公司投入 100 亿美元将标志着其算力供应链的显著多元化。

rss · 36氪 · 8月4日 12:11

**背景**: Anthropic 是一家总部位于旧金山的 AI 安全导向型公益公司，也是 Claude 大语言模型系列的开发方，与 OpenAI 的 GPT 系列和 Google 的 Gemini 直接竞争。这一规模的 AI 算力合同通常涵盖多年期内使用数万个 GPU 或专用 AI 加速器的访问权限，因为训练一个前沿模型可能需要数万个 NVIDIA H100 或同等芯片运行数月。"算力瓶颈"已成为 AI 发展的核心制约因素之一，众多专用 AI 云初创公司正涌现出来，为占主导地位的超大规模云厂商提供替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://www.mayerbrown.com/en/insights/publications/2026/06/portability-of-ai-compute-infrastructure-in-ai-acquisitions">Portability of AI Compute Infrastructure in AI Acquisitions | Mayer Brown</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI infrastructure`, `#cloud computing`, `#deal`, `#AI industry`

---

<a id="item-16"></a>
## [台积电扩大 CoWoS 封装外包，GPU 订单挤压产能](https://36kr.com/newsflashes/3925154441787525?f=rss) ⭐️ 7.3/10

由于英伟达 GPU 订单激增导致台积电封装产线满载，台积电决定将其 AI 芯片核心封装技术 CoWoS 中的 CoW（晶圆上芯片）环节进一步外包给日月光等 OSAT 封测厂商。 CoWoS 封装是将 AI 处理器与高带宽内存集成的关键技术，此举表明 AI 芯片供应链存在严重瓶颈。这一调整反映出 AI 需求的爆炸式增长正迫使全球领先的代工厂重新分配产能，可能影响全球 AI 基础设施的部署节奏。 CoWoS 是台积电的 2.5D 封装技术，分为 CoWoS-S、CoWoS-R 和 CoWoS-L 三种类型，分别使用不同的中介层材料。台积电已完成 5.5 倍光罩尺寸的 CoWoS 技术验证，计划于 2026 年量产，显示 AI 芯片封装正向更大尺寸方向发展。

rss · 36氪 · 8月4日 11:53

**背景**: CoWoS（晶圆上芯片-基板封装）是台积电开发的 2.5D 先进封装技术，将 AI 处理器置于中心，HBM（高带宽内存）堆栈环绕四周，通过中介层互连。日月光等 OSAT（外包半导体封装测试）厂商专注于芯片封装与测试的后端环节。HBM 由三星、AMD 和 SK 海力士联合开发，是一种 3D 堆叠内存技术，为英伟达 H200、B200 及即将推出的 Vera Rubin 等 AI 加速器提供数据支撑。2025 年第二季度 SK 海力士占据约 62%的 HBM 出货量，整个 AI 芯片堆栈——从封装到内存——都面临供应紧张。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vcnh.top/blog/36/">TSMC will manufacture unprecedented giant chips - vcnh.top</a></li>
<li><a href="https://currentaffairs.adda247.com/pm-modi-inaugurates-cg-semi-osat-facility-in-sanand-strengthening-indias-semiconductor-ecosystem/">PM Modi Inaugurates CG Semi OSAT Facility in Sanand...</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#CoWoS`, `#NVIDIA`, `#semiconductor supply chain`, `#AI chips`, `#packaging`

---

<a id="item-17"></a>
## [DeepSeek V4 Flash 在单块 AMD MI300X 上实现 150+ tokens/秒推理](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 7.0/10

开发者 ryanzhou 展示了在单块 AMD MI300X GPU 上运行 DeepSeek V4 Flash（2840 亿参数的 MoE 模型），在保留完整推理权重的前提下实现了每秒超过 150 个 token 的生成速度，但上下文窗口从原始的 1M 缩减至 256k tokens。 此次演示凸显了在非 NVIDIA 硬件上以更易获取的成本部署前沿规模开源权重模型的可行性，有望降低研究人员和小型组织在 NVIDIA GPU 生态之外尝试最先进模型的门槛。 该方案保留了完整精度的推理权重（未进行激进量化），但牺牲了上下文长度；MI300X 的大容量 HBM 是容纳该模型的关键，不过原始的 DeepSeek V4 Flash 设计为支持 1M token 上下文，且论文报告在 H800 上可达到约 15k tokens/秒/GPU，表明仍有较大优化空间。

hackernews · zhoutong · 8月4日 10:00 · [社区讨论](https://news.ycombinator.com/item?id=49166386)

**背景**: DeepSeek V4 Flash 是一款混合专家（MoE）模型，总参数量为 2840 亿，每个 token 激活约 130 亿参数，远小于其 V4-Pro 兄弟模型（1.6 万亿参数）。AMD MI300X 是一款数据中心 GPU，以其大容量 HBM 显存（192GB）著称，非常适合承载大语言模型。在单块 GPU 上运行完整的前沿 MoE 模型——而非需要多卡或多节点部署——意义重大，因为它大幅降低了基础设施复杂度和成本，尽管这通常需要以上下文窗口或量化精度为代价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 Explained: V 4 -Pro 1.6T vs V 4 - Flash 284B (2026)</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://www.remio.ai/post/deepseek-v4-flash-reportedly-outperforms-its-larger-sibling-on-agent-tasks">DeepSeek V 4 Flash Reportedly Outperforms Its Larger Sibling on...</a></li>

</ul>
</details>

**社区讨论**: 评论者们提出了务实的技术和实践观点：有人指出 MI300X 通常只能以 8 卡配置（约 25 万欧元）购买，无法单卡采购；另一位评论者强调，虽然此次演示保留了完整推理权重（不同于降级量化），但从 1M 降至 256k 的上下文窗口是主要让步，这与 Codex 的范围相当。来自 doubleword.ai 的评论者分享了使用 2 块 MI300X 的相关先验工作，并推荐 hotaisle.xyz 用于 MI300X 实验。最后，有参与者指出，DeepSeek 在 H800 上自身的数据（15k tok/s/GPU）表明 MI300X 仍有可观的优化空间。

**标签**: `#DeepSeek`, `#AMD MI300X`, `#LLM inference`, `#GPU deployment`, `#model optimization`

---

<a id="item-18"></a>
## [Xbox 服务宕机，玩家无法运行自己拥有的实体光盘游戏](https://birchtree.me/blog/xbox-goes-down-you-cant-play-games-you-own-on-disc/) ⭐️ 7.0/10

Xbox 服务器故障导致用户无法运行自己持有的实体光盘游戏，此事件引发了关于数字所有权、数字版权管理（DRM）以及现代游戏中消费者权益受损问题的讨论。

hackernews · surprisetalk · 8月4日 12:01 · [社区讨论](https://news.ycombinator.com/item?id=49167448)

**标签**: `#gaming`, `#DRM`, `#digital-ownership`, `#consumer-rights`, `#xbox`

---

<a id="item-19"></a>
## [Swiftlet 在 Mac 4.3GB 内存运行 80B Qwen，在 iPhone 运行 35B 模型](https://github.com/leonickson1/Swiftlet) ⭐️ 7.0/10

开发者 leonickson1 在 GitHub 上发布了 Swiftlet 工具，通过激进的量化和内存交换技术，仅用 4.3GB 内存即可在 Mac 上运行 800 亿参数的 Qwen 模型，并在 iPhone 上以约每秒 1 个 token 的速度运行 350 亿参数的模型。 这一演示将端侧大模型推理的极限向前推进，表明超大参数模型可以在资源极为有限的消费级硬件上运行，预示着未来强大的人工智能可能在本地运行而无需昂贵的 GPU 机架。它也反映了苹果更广泛的战略押注，即消费级 AI 将越来越多地在设备端而非云端运行。 Swiftlet 基于早期的 TurboFieldfare 项目，通过激进的量化（将模型权重精度降低到 4 位甚至更低）结合到 SSD 的内存交换来实现极低的内存占用。其代价也很明显：iPhone 上的推理速度仅约每秒 1 个 token，频繁的 SSD 交换也引发了关于长期存储磨损的担忧，不过在配备 24-32GB 内存的 Mac 上增加 RAM 缓存可以显著提升速度。

hackernews · leonickson · 8月3日 16:54 · [社区讨论](https://news.ycombinator.com/item?id=49158333)

**背景**: 像阿里巴巴 Qwen 系列这样的大语言模型（LLM）通常需要巨大的内存——以标准 16 位精度运行的 80B 模型大约需要 160GB 内存。量化是一种压缩技术，通过降低模型权重的数值精度（通常从 16 位降至 4 位甚至 3 位），以牺牲部分模型质量为代价大幅缩小内存占用。Apple Silicon 芯片采用统一内存架构，CPU 和 GPU 可以共享同一内存池，这对于 AI 工作负载非常有利。内存交换则通过将不常用的数据溢出到 SSD 存储来扩展可用内存，使模型能够突破物理 RAM 的限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pub.towardsai.net/llm-quantisation-quantise-hugging-face-model-with-gptq-awq-and-bitsandbytes-a4ad45cd8b48">LLM Quantization : Quantize Model with GPTQ, AWQ... | Towards AI</a></li>
<li><a href="https://huggingface.co/Qwen">Org profile for Qwen on Hugging Face, the AI community building the...</a></li>
<li><a href="https://strongmocha.com/ai-infrastructure-data-centers/apple-silicon-s-quiet-memory-advantage-2/">Apple Silicon ’s Quiet Memory Advantage - StrongMocha</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区对该项目反响热烈，尽管存在实际限制，评论者仍认为这代表了有意义的进展。评论者强调，正是这类实验推动了真正的技术进步，预测苹果正在战略性地押注消费级端侧 AI，并指出在内存更大的 Mac（24-32GB）上增加 RAM 缓存可以显著提升推理速度。一位正在测试的用户证实了该方法的实用性，而 TurboFieldfare 的原作者则感谢 Swiftlet 致谢了其工作。

**标签**: `#on-device-ai`, `#llm-inference`, `#quantization`, `#apple-silicon`, `#edge-computing`

---

<a id="item-20"></a>
## [数学与理论计算机科学的十项进展](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 7.0/10

OpenAI 重点介绍了借助 AI 推理模型在数学和理论计算机科学领域取得的十项具体进展，由此引发了学界围绕机器驱动数学发现本质的热议。

hackernews · milkshakes · 8月3日 16:27 · [社区讨论](https://news.ycombinator.com/item?id=49157930)

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#reasoning-models`, `#research-frontier`

---