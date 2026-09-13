---
layout: default
title: "Horizon Summary: 2026-09-13 (ZH)"
date: 2026-09-13
lang: zh
---

> 从 27 条内容中筛选出 11 条重要资讯。

---

1. [伊朗和胡塞叛军滥用 Anthropic 的 Claude 锁定军舰并研发导弹](#item-1) ⭐️ 7.5/10
2. [非官方 Mod 为 RTX 40 系列显卡解锁 DLSS 多帧生成功能](#item-2) ⭐️ 7.5/10
3. [苹果 A20 Pro 2 纳米芯片打破 Geekbench 7 单核跑分纪录](#item-3) ⭐️ 7.5/10
4. [Real-SWE：基于私有真实企业代码库的 AI 模型基准评测](#item-4) ⭐️ 7.0/10
5. [英伟达：AI 界的"中央银行"](#item-5) ⭐️ 7.0/10
6. [我们必须把握前沿发展的节奏](#item-6) ⭐️ 7.0/10
7. [除我之外，所有人都应放慢 AI 发展步伐](#item-7) ⭐️ 6.0/10
8. [我制作了一个构建可视化工具来理解 Bun 的编译时间](#item-8) ⭐️ 6.0/10
9. [伊朗可能逆向工程捕获的美军 Anduril Dive-LD 水下无人机](#item-9) ⭐️ 5.5/10
10. [工程师用模拟果蝇大脑构建加密货币日内交易机器人](#item-10) ⭐️ 5.5/10
11. [d-Matrix 加入 NVIDIA NVLink Fusion 平台以扩展 Raptor AI 加速器](#item-11) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [伊朗和胡塞叛军滥用 Anthropic 的 Claude 锁定军舰并研发导弹](https://www.tomshardware.com/tech-industry/artificial-intelligence/iran-and-houthi-rebels-used-anthropics-claude-ai-to-target-us-warships-and-build-hypersonic-missiles-houthi-rebels-also-used-the-bot-to-code-ballistic-missile-guidance-systems) ⭐️ 7.5/10

一份最新报告显示，伊朗和胡塞叛军利用 Anthropic 的 Claude AI 聊天机器人执行军事任务，包括锁定美国军舰、研发高超音速导弹，以及编写弹道导弹制导系统的代码。 这一披露凸显了商用 AI 工具正被敌对国家和非国家行为体武器化，引发了人们对 AI 扩散、出口管制以及 AI 实验室有责任防止其模型在冲突地区被滥用的紧迫担忧。 Anthropic 的 Claude 是一系列以 AI 安全为核心的大语言模型，但据报道对手绕过了安全护栏以获取可操作的军事协助；高超音速导弹飞行速度超过 5 马赫（约每小时 3,800 英里），而弹道导弹制导系统依赖传感器、推进系统和轨迹控制来在发射后保持正确航向。

rss · Tom's Hardware · 9月12日 15:03

**背景**: Anthropic 是一家由前 OpenAI 研究人员创立的、专注于 AI 安全的公司，Claude 是其旗舰聊天机器人，与 OpenAI 的 ChatGPT 和 Google 的 Gemini 竞争。高超音速导弹代表了一类新型先进武器系统，能以极快速度打击全球目标，因此具有战略上的不稳定影响。弹道导弹制导系统利用传感器、雷达和控制机制将弹头沿预定轨迹引导至目标。此次被披露的滥用事件表明，AI 实验室的安全政策与对手将民用 AI 重新用于战争的决心之间存在日益扩大的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ballistic_missile">Ballistic missile - Wikipedia</a></li>
<li><a href="https://old.bitchute.com/video/aqVtmjX5WWm8/">How hypersonic missles work</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI security`, `#Anthropic`, `#military AI`, `#geopolitics`

---

<a id="item-2"></a>
## [非官方 Mod 为 RTX 40 系列显卡解锁 DLSS 多帧生成功能](https://www.tomshardware.com/pc-components/gpus/we-tested-dlss-multi-frame-generation-on-rtx-40-series-gpus-new-mod-brings-rtx-50-series-exclusive-feature-to-older-cards-and-it-really-works) ⭐️ 7.5/10

Tom's Hardware 测试了一款名为'MFGAdaUnlock-RenoDx'的非官方 Mod，成功在较旧的 RTX 40 系列显卡上启用了 DLSS 多帧生成功能——这一功能此前是 RTX 50 系列的独占特性。该 Mod 通过 ReShade 插件实现 3 倍、4 倍及以上的帧生成，在《赛博朋克 2077》中的测试证实 MFG 确实可以在 Ada Lovelace 架构上正常运行。 这一发现对数百万此前无法使用 NVIDIA 最新帧生成技术的 RTX 40 系列显卡用户具有重要意义，可能延长其硬件的使用寿命。这也引发了人们对 NVIDIA 硬件级功能区分策略的质疑，并凸显了 NVIDIA 与 Mod 社区之间持续的攻防博弈。 该 Mod 基于 ReShade 注入层实现，而非直接修改 DLSS 驱动；NVIDIA 此前曾尝试封锁一次，但 Mod 作者立即重新解锁。NVIDIA 警告称，RTX 40 系列上的 MFG 属于非官方功能，缺乏与 RTX 50 系列实现相同的测试和支持，用户可能遇到稳定性或画质问题。

rss · Tom's Hardware · 9月12日 14:08

**背景**: DLSS（深度学习超采样）是 NVIDIA 基于 AI 驱动的超采样和帧生成技术，通过在传统渲染帧之间生成额外帧来提升游戏性能。DLSS 4 于 2025 年 1 月 30 日发布，引入了多帧生成（MFG）功能，每一帧传统渲染帧可生成多个 AI 帧，在 RTX 50 系列显卡上于 1440p 分辨率下可将帧率提升至最高 6.1 倍。NVIDIA 将 MFG 限制在其基于 Blackwell 架构的新款 RTX 50 系列显卡上，很可能是因为该功能依赖这些 GPU 的新硬件能力——不过这一 Mod 表明 Ada Lovelace 架构的实际能力可能比官方宣传的要更强。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/geforce/news/dlss-4-multi-frame-generation-out-now/">DLSS 4 With Multi Frame Generation & Enhancements For All ...</a></li>
<li><a href="https://videocardz.com/newz/modders-discover-unlock-for-dlss-multi-frame-generation-on-rtx-40-nvidia-blocks-it-modders-immediately-unlock-it-again">Modders discover unlock for DLSS Multi Frame Generation on RTX 40, NVIDIA blocks it, modders immediately unlock it again - VideoCardz.com</a></li>
<li><a href="https://overclock3d.net/news/gpu-displays/mod-unlocks-dlss-multi-frame-generation-mfg-on-rtx-40-series-gpus/">Mod unlocks DLSS MFG on RTX 40 series GPUs - OC3D</a></li>

</ul>
</details>

**标签**: `#DLSS`, `#NVIDIA`, `#RTX-40-series`, `#GPU-modding`, `#frame-generation`

---

<a id="item-3"></a>
## [苹果 A20 Pro 2 纳米芯片打破 Geekbench 7 单核跑分纪录](https://www.tomshardware.com/pc-components/cpus/apples-a20-pro-shatters-geekbench-7-single-core-record-2nm-chip-beats-desktop-intel-core-i9-and-amd-ryzen-9-by-up-to-32-percent) ⭐️ 7.5/10

苹果即将推出的 A20 Pro 智能手机 SoC 采用 2 纳米制程，据报道在 Geekbench 7 中创下单核跑分新高，单核性能领先桌面级英特尔 Core i9 和 AMD Ryzen 9 处理器多达 32%。 这一里程碑表明，基于 ARM 架构的移动芯片已在单线程工作负载中决定性地追平甚至超越高端桌面级 x86 芯片，验证了苹果垂直整合的战略路线，也给英特尔和 AMD 带来了更大的竞争压力。 相关数据来自发布前泄露的跑分，并非经过独立验证的结果，且 Geekbench 合成跑分并不总能直接反映实际性能；此外，此次对比仅限于单核性能，而桌面级处理器通常凭借更多核心数和更好的散热余量在多核负载中保持领先。

rss · Tom's Hardware · 9月12日 10:48

**背景**: 2 纳米制程节点代表了半导体制造技术的最先进一代，可实现更高的晶体管密度、更强的性能和更低的功耗。SoC（片上系统）将 CPU 核心、GPU、内存控制器和 AI 加速器等组件集成在同一芯片上，这种设计方式在智能手机中很常见，并越来越多地应用于笔记本电脑。Geekbench 7 是一个跨平台基准测试工具，可衡量处理器在视频会议、流媒体和游戏物理等负载下的单核与多核性能，近期还新增了对 CUDA、OpenCL、Vulkan 和 Metal 等 GPU 测试 API 的支持。苹果的芯片路线图已从为 iPhone 提供动力的 A 系列扩展到为 Mac 提供动力的 M 系列，全部采用 ARM 架构并由台积电代工。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.geekbench.com/blog/2026/07/geekbench-7/">Geekbench 7 - Geekbench Blog</a></li>
<li><a href="https://www.rapidus.inc/en/tech/te0006/">2nm semiconductor challenges: Exploring Rapidus’ technological breakthroughs | Rapidus Corporation</a></li>

</ul>
</details>

**标签**: `#Apple`, `#ARM`, `#silicon`, `#benchmarks`, `#CPU`

---

<a id="item-4"></a>
## [Real-SWE：基于私有真实企业代码库的 AI 模型基准评测](https://withspecific.com/benchmarks/real-swe) ⭐️ 7.0/10

Real-SWE 推出了一个基准测试，通过评估 AI 编程模型在私有企业代码库上的表现来避免数据污染，发现前沿模型的成功率约为 30%，与从业者的实际体验相符。

hackernews · theanonymousone · 9月12日 20:25 · [社区讨论](https://news.ycombinator.com/item?id=49676820)

**标签**: `#ai-benchmarks`, `#code-generation`, `#model-evaluation`, `#enterprise-software`, `#training-contamination`

---

<a id="item-5"></a>
## [英伟达：AI 界的"中央银行"](https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai) ⭐️ 7.0/10

《经济学人》指出，英伟达凭借逾 5000 亿美元的巨额资本承诺，实际上左右着 AI 经济的"货币条件"，堪称 AI 界的"中央银行"。

hackernews · tolugenius · 9月12日 15:08 · [社区讨论](https://news.ycombinator.com/item?id=49673098)

**标签**: `#Nvidia`, `#AI industry`, `#economics`, `#capital investment`, `#data centers`

---

<a id="item-6"></a>
## [我们必须把握前沿发展的节奏](https://darioamodei.com/post/we-must-pace-the-frontier) ⭐️ 7.0/10

Anthropic 首席执行官 Dario Amodei 呼吁对前沿 AI 发展进行'节奏把控'，主张通过自我监管来管理风险。然而 Hacker News 的评论者们就此展开了激烈辩论——有人视其为负责任的领导力体现，也有人认为这是监管俘获及对自身竞争劣势的默认。

hackernews · apsec112 · 9月12日 14:10 · [社区讨论](https://news.ycombinator.com/item?id=49672510)

**标签**: `#AI policy`, `#AI safety`, `#AI regulation`, `#Anthropic`, `#frontier AI`

---

<a id="item-7"></a>
## [除我之外，所有人都应放慢 AI 发展步伐](https://xeiaso.net/notes/2026/everyone-slowdown-but-me/) ⭐️ 6.0/10

一篇挑衅性的评论文章，批评 AI 安全倡导者，指控他们所主张的监管只会让自己受益，同时为开放和公共 AI 发展设置竞争壁垒。

hackernews · xena · 9月13日 00:30 · [社区讨论](https://news.ycombinator.com/item?id=49678683)

**标签**: `#AI regulation`, `#AI safety`, `#tech policy`, `#regulatory capture`, `#industry critique`

---

<a id="item-8"></a>
## [我制作了一个构建可视化工具来理解 Bun 的编译时间](https://lalitm.com/post/buildprof/) ⭐️ 6.0/10

一位开发者构建了一个可视化工具，用于分析和理解 Bun 的编译时间，具有类似于 Electric Insight 的全面性能分析功能。

hackernews · lalitmaganti · 9月12日 14:45 · [社区讨论](https://news.ycombinator.com/item?id=49672842)

**标签**: `#build-systems`, `#bun`, `#performance-profiling`, `#developer-tools`, `#compilers`

---

<a id="item-9"></a>
## [伊朗可能逆向工程捕获的美军 Anduril Dive-LD 水下无人机](https://www.tomshardware.com/tech-industry/drones/iran-could-potentially-reverse-engineer-captured-u-s-underwater-drone-several-iranian-embassies-mock-us-over-capture-as-u-s-military-downplays-the-situation) ⭐️ 5.5/10

据信伊朗已经捕获了一架美国海军的 Anduril Dive-LD 自主水下无人机，这引发了人们对德黑兰可能对其进行逆向工程的担忧。与此同时，多个伊朗大使馆公开嘲讽美国丢失无人机一事，而美国海军则淡化该事件，声称该载具存在缺陷且属于非机密级别。 即使是捕获一架非机密级的水下无人机，也可能让敌方接触到 Anduril 的专有技术，例如其自主导航和模块化载荷系统。该事件还凸显了无人军事资产在海上行动中被缴获的脆弱性，以及无人机丢失事件所带来的地缘政治观感。 Dive-LD 是一种大直径自主水下航行器（LDUUV），采用 3D 打印船体，额定下潜深度可达 6,000 米，长度约 5.8 米，排水量 3 吨，续航时间达 10 天。该装备于 2024 年进入美国海军服役，配备模块化载荷，可用于水雷对抗和海床测绘等任务。

rss · Tom's Hardware · 9月12日 11:30

**背景**: Anduril Industries 是一家美国国防技术公司，以开发自主系统而闻名，包括为其众多产品提供支持的 Lattice 软件平台。Dive-LD 是 Anduril 海上力量（Seapower）自主系统家族的一部分，该家族还包括更大的 Dive-XL、Copperhead 水雷对抗系统以及 Seabed Sentry 海床监视平台。对一架被捕获的军用无人机进行逆向工程，即使软件层面的知识产权并未存储在物理平台上，也可能让某个国家研究其船体设计、传感器集成方式以及自主导航算法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anduril.com/dive-ld">Dive-LD | Anduril</a></li>
<li><a href="https://www.globalmilitary.net/ships/dive-ld/">Dive-LD (LDUUV) Unmanned vessel: Full Specs & Armament</a></li>
<li><a href="https://www.anduril.com/sea/seapower">Seapower | Anduril</a></li>

</ul>
</details>

**标签**: `#defense-tech`, `#Anduril`, `#drones`, `#geopolitics`, `#military-technology`

---

<a id="item-10"></a>
## [工程师用模拟果蝇大脑构建加密货币日内交易机器人](https://www.tomshardware.com/tech-industry/artificial-intelligence/engineer-turns-simulated-fly-brain-into-a-crypto-day-trader-posts-downloadable-sim-to-github-166-700-virtual-neurons-read-candlestick-charts-for-dopamine-hits) ⭐️ 5.5/10

一位 Coinbase 工程师创建了名为 'Stonkfly' 的开源加密货币日内交易系统，该系统由模拟果蝇大脑的 116,700 个虚拟神经元驱动，通过多巴胺奖励信号学习解读 K 线图（candlestick chart）。该项目已发布在 GitHub 上供他人下载和使用。 该项目展示了大规模生物真实性神经模拟（此前仅限于神经科学实验室使用）如何被重新用于金融交易等非常规的实际任务。它也凸显了全脑连接组数据和脉冲神经网络模拟器对爱好者和动手实践者来说正变得日益触手可及。 Stonkfly 使用受果蝇连接组启发的脉冲神经网络架构——该连接组是近年神经科学研究绘制的包含约 125,000–139,000 个神经元和 5000 万个突触连接的完整线路图。学习机制由多巴胺调节的脉冲时序依赖可塑性（STDP）驱动，这是一种生物学上合理的学习规则，其中盈利交易充当奖励信号，强化有用的突触连接。

rss · Tom's Hardware · 9月12日 10:00

**背景**: 果蝇连接组是成年果蝇大脑中所有神经元和化学突触的完整图谱，由大规模神经科学合作项目完成并于 2024 年发表。脉冲神经网络（SNN）是一类通过离散电脉冲（而非连续数值）进行通信的神经网络模型，更接近真实生物神经元的工作方式。多巴胺调节的学习机制源于真实的神经科学原理：大脑中多巴胺的释放代表奖励信号，帮助动物（包括果蝇）将特定行为与积极结果关联起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.berkeley.edu/2024/10/02/researchers-simulate-an-entire-fly-brain-on-a-laptop-is-a-human-brain-next/">Researchers simulate an entire fly brain on a laptop. Is a human brain next? - Berkeley News</a></li>
<li><a href="https://www.nature.com/articles/s41586-024-07763-9">A Drosophila computational brain model reveals sensorimotor processing | Nature</a></li>
<li><a href="https://en.wikipedia.org/wiki/Drosophila_connectome">Drosophila connectome - Wikipedia</a></li>

</ul>
</details>

**标签**: `#computational-neuroscience`, `#neural-networks`, `#cryptocurrency`, `#open-source`, `#bio-inspired-computing`

---

<a id="item-11"></a>
## [d-Matrix 加入 NVIDIA NVLink Fusion 平台以扩展 Raptor AI 加速器](https://www.servethehome.com/d-matrix-joins-the-nvidia-nvlink-fusion-platform/) ⭐️ 5.5/10

d-Matrix 宣布将采用 NVIDIA 的 NVLink Fusion 平台，对其下一代 Raptor AI 加速器进行纵向和横向扩展。Raptor 加速器是 d-Matrix 首款采用其 3D 内存内计算（3DIMC）技术的产品，瞄准生成式 AI 推理工作负载。 此次合作标志着 NVIDIA 在 AI 加速器互联生态系统中的影响力正在扩大，允许 d-Matrix 等第三方芯片厂商直接接入 NVIDIA 的机架级基础设施（如 NVL72 风格的系统）。通过让 d-Matrix 访问 NVIDIA 的高带宽、低延迟互联架构以实现 AI 工厂级部署，这验证了 d-Matrix 基于 3D DRAM 的创新内存内计算方案。 Raptor 采用 3DIMC 技术，并与 Andes 的 RISC-V CPU IP（2025 年 11 月宣布）配套集成；根据 d-Matrix 自有基准测试，其 3D DRAM 架构在密度和每 GB/s 功耗方面声称优于 HBM4 和 NVIDIA Rubin R200。NVLink Fusion 将 NVIDIA 的专有互联技术扩展到来自 Marvell、Qualcomm 和 MediaTek 等厂商的第三方 XPU 和 CPU。

rss · ServeTheHome · 9月12日 21:42

**背景**: NVIDIA NVLink 是一种高速专有互联技术，使 GPU 和加速器之间能够以极高的带宽和低延迟进行通信，是 NVIDIA 的 NVL72 等机架级 AI 系统的核心。NVLink Fusion 是 NVIDIA 开放该互联技术给第三方芯片的项目，允许其他厂商的自定义 XPU、加速器以及数据中心 CPU 接入 NVIDIA 的 AI 工厂基础设施。d-Matrix 是一家专注于生成式 AI 推理计算的初创公司，其 Raptor 加速器采用了独特的 3D 堆叠 DRAM 方法（3DIMC），将内存带宽和容量拉近计算单元，旨在解决限制大语言模型推理吞吐量的内存瓶颈问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/d-matrix-nvlink-fusion/">d-Matrix Adopts NVIDIA NVLink Fusion for Rack-Scale... | NVIDIA Blog</a></li>
<li><a href="https://www.servethehome.com/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026/">d-Matrix Raptor 3D-DRAM Accelerator for Generative Inference ...</a></li>
<li><a href="https://www.d-matrix.ai/announcements/d-matrix-and-andes-team-on-worlds-highest-performing-most-efficient-accelerator-for-ai-inference-at-scale/">d-Matrix and Andes Team on World's Highest Performing, Most ...</a></li>

</ul>
</details>

**标签**: `#AI accelerators`, `#NVIDIA`, `#d-Matrix`, `#NVLink`, `#interconnect`

---