---
layout: default
title: "Horizon Summary: 2026-07-30 (ZH)"
date: 2026-07-30
lang: zh
---

> 从 117 条内容中筛选出 20 条重要资讯。

---

1. [Linux 内核补丁大幅降低 Steam Deck 游戏卡顿，性能提升 31%](#item-1) ⭐️ 8.5/10
2. [月之暗面据报使用受禁 Nvidia Blackwell 芯片训练 Kimi K3](#item-2) ⭐️ 8.5/10
3. [文档型 AI 蠕虫能够通过 Word 版 Copilot 自我传播](#item-3) ⭐️ 8.0/10
4. [研究表明：长策略文档无法可靠约束 AI 智能体行为](#item-4) ⭐️ 8.0/10
5. [台积电 Fab 20 工厂 2nm 制程月产能达 2 万片晶圆](#item-5) ⭐️ 8.0/10
6. [HRL 展示可自主运行的硅基量子处理器](#item-6) ⭐️ 7.5/10
7. [GlobalFoundries 获 3 亿美元 CHIPS 法案资金，美国政府持股 1%](#item-7) ⭐️ 7.5/10
8. [铠侠发布 UFS 5.0 嵌入式闪存器件](#item-8) ⭐️ 7.5/10
9. [希捷将于 2027 年开始对创纪录的 50TB 硬盘进行验证 —— 大部分硬盘已售罄至 2028 年](#item-9) ⭐️ 7.5/10
10. [Apacer 首席执行官警告：2027 年内存模组厂商 DRAM 供应或下降超 70%](#item-10) ⭐️ 7.5/10
11. [英特尔完成 RAMP-C 国防项目，验证 18A 代工工艺](#item-11) ⭐️ 7.5/10
12. [月之暗面 Kimi 完成超 35 亿美元 F 轮融资，估值达 350 亿美元](#item-12) ⭐️ 7.3/10
13. [微软新增数据中心租约超 1300 亿美元](#item-13) ⭐️ 7.3/10
14. [AI 顶级初创公司越来越不发表研究论文](#item-14) ⭐️ 7.0/10
15. [Vision Pro 最酷的用途](#item-15) ⭐️ 7.0/10
16. [Show HN：开源引擎可在任何 M 系列 Mac 上以 2 GB 内存运行 Gemma 4 26B](#item-16) ⭐️ 7.0/10
17. [Superlogical](#item-17) ⭐️ 7.0/10
18. [动态 AI 需求推动存储多元化](#item-18) ⭐️ 7.0/10
19. [光子技术从机架级向芯粒级集成演进](#item-19) ⭐️ 7.0/10
20. [新思科技联合英伟达展示自主设计验证智能体](#item-20) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Linux 内核补丁大幅降低 Steam Deck 游戏卡顿，性能提升 31%](https://www.techpowerup.com/351189/linux-cpu-driver-patches-massively-reduce-game-stuttering-on-steam-deck) ⭐️ 8.5/10

Linux 内核开发者 David Vernet（来自 Meta）向 AMD P-State 驱动提交了一套新补丁，引入了 epp_boost 功能，可对忙碌的 CPU 核心实现逐核心的能源性能偏好（EPP）提升。早期基准测试显示，该补丁可将 AMD CPU 的 1% 最低帧率提升高达 31.8%，显著降低 Steam Deck 及类似 Linux 游戏系统上的感知卡顿。 1% 最低帧率是衡量游戏中感知卡顿和流畅度的关键指标，约 31% 的提升对 Steam Deck 用户以及更广泛的 Linux 游戏社区来说意味着无需更换硬件即可获得巨大的体验改善。这种内核级优化表明，开源驱动工作正在持续缩小 Linux 与 Windows 游戏性能之间的差距，直接惠及 Valve 基于 SteamOS 的掌机设备。 当启用 epp_boost 时，一个钩子会以每 10 毫秒一次的频率采样每个核心的 C0 占用率（MPERF 增量与 TSC 增量之比）；如果某个核心至少 50% 处于忙碌状态，则其 MSR_AMD_CPPC_REQ 中的 EPP 字段会被设置为 performance（0），并保持该状态直到 300 毫秒内未再出现忙碌采样。该补丁目前仅作为提案提交在 linux-pm 邮件列表中，尚未合并入主线内核，因此 Steam Deck 用户需要运行自定义内核或等待上游集成。

rss · TechPowerUp News · 7月29日 15:44

**背景**: AMD P-State 是 Linux 上用于 AMD 处理器的现代 CPU 频率调节驱动，取代了较旧的 acpi-cpufreq 驱动，能更精确地控制性能和能耗状态。EPP（Energy Performance Preference，能源性能偏好）提示用于告知处理器在性能和能效之间如何取舍：EPP 值越低越偏向性能，越高则越偏向能效。1% 最低帧率是指最慢的 1% 帧的平均帧率，被广泛用作衡量卡顿和流畅度的指标，而非平均帧率。Steam Deck 是 Valve 推出的掌上游戏 PC，运行基于 Linux 的 SteamOS 系统，搭载定制版 AMD APU，因此内核级的 AMD 优化对其用户群尤为重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/AMD-P-State-Better-1p-Lows">AMD P-State Linux Driver Patches Can Boost 1%-Low FPS Gaming Performance By 31% - Phoronix</a></li>
<li><a href="https://www.pcgamer.com/hardware/handheld-gaming-pcs/linux-kernel-patch-can-boost-the-steam-decks-1-percent-low-frame-rate-by-as-much-as-31-percent-in-early-testing/">Linux kernel patch can boost the Steam Deck's 1% low frame rate by as much as 31% in early testing | PC Gamer</a></li>
<li><a href="https://www.xda-developers.com/this-linux-kernel-patch-could-give-steamdeck-surprising-performance-boost/">This Linux kernel patch could give the Steam Deck a surprising performance boost</a></li>

</ul>
</details>

**社区讨论**: 在 Phoronix、PC Gamer 和 XDA Developers 等媒体的报道中，反馈普遍非常积极，评论者强调仅通过软件在现有硬件上实现约 31% 的 1% 最低帧率提升是极为罕见且出色的。一些技术导向的读者则提出了关于功耗和 Steam Deck 续航的问题，指出逐核心 EPP 提升可能在持续高负载下增加能耗，对掌机的影响比对台式机更大。

**标签**: `#Linux`, `#AMD`, `#Steam Deck`, `#kernel`, `#performance`

---

<a id="item-2"></a>
## [月之暗面据报使用受禁 Nvidia Blackwell 芯片训练 Kimi K3](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-moonshot-ai-reportedly-used-nvidia-blackwell-chips-for-training-kimi-k3-company-circumvented-both-u-s-export-and-chinese-import-controls-to-acquire-compute) ⭐️ 8.5/10

据报道，月之暗面（Moonshot AI）使用 Nvidia Blackwell 芯片训练其 Kimi K3 模型，同时绕过了美国的出口管制和中国的进口管制。该公司据称获取了本不应被中国 AI 实验室合法使用的受限算力。 这则报道暴露了美国为减缓中国 AI 发展而实施的出口管制措施存在的重大漏洞，因为 Blackwell 芯片是当前最先进的 AI 训练硬件。这也引发了关于中国进口管制执行力的问题，并凸显了美中前沿 AI 实验室之间日益激烈的算力军备竞赛。 Kimi K3 是一个拥有 2.8 万亿参数的开源权重多模态推理模型，上下文窗口超过 100 万 token。Nvidia Blackwell B100/B200 加速器采用台积电 3nm 工艺节点制造，自发布以来一直是对华出口限制的主要目标。

rss · Tom's Hardware · 7月29日 10:00

**背景**: 美国于 2022 年 10 月对中国实施了全面的半导体出口管制措施，并在 2023 年和 2024 年进一步扩大，目标包括 Nvidia 的 H100 和 Blackwell 系列等先进 AI 芯片，同时与日本和荷兰等盟友进行协调。月之暗面是中国领先的 AI 初创公司之一，以其 Kimi 聊天机器人和具有竞争力的开源权重大语言模型而闻名。中国公司据称同时绕过国内进口限制，这一事实反映了美国遏制措施与北京并行推动半导体自给自足的双重压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_New_Export_Controls_on_Advanced_Computing_and_Semiconductors_to_China">United States New Export Controls on Advanced Computing and Semiconductors to China - Wikipedia</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K3 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.congress.gov/crs-product/R48642">U.S. Export Controls and China: Advanced Semiconductors | Congress.gov | Library of Congress</a></li>

</ul>
</details>

**标签**: `#AI`, `#Nvidia`, `#ExportControls`, `#China`, `#Geopolitics`

---

<a id="item-3"></a>
## [文档型 AI 蠕虫能够通过 Word 版 Copilot 自我传播](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/) ⭐️ 8.0/10

安全研究人员展示了 AI 蠕虫如何通过嵌入在共享文档中的提示注入，在 Microsoft Word 的 Copilot 中自我传播，利用了指令与数据之间的混淆问题。

hackernews · Canopy9560 · 7月29日 11:44 · [社区讨论](https://news.ycombinator.com/item?id=49096188)

**标签**: `#ai-security`, `#prompt-injection`, `#microsoft-copilot`, `#vulnerability-research`, `#llm-attacks`

---

<a id="item-4"></a>
## [研究表明：长策略文档无法可靠约束 AI 智能体行为](https://arxiv.org/abs/2607.25398) ⭐️ 8.0/10

一项名为「Handbook.md」的新研究通过实证表明，像 CLAUDE.md、AGENTS.md 等长策略文档无法在真实任务中可靠约束 AI 智能体的行为。该论文对智能体遵守长篇书面策略的程度进行了基准测试，发现即使策略内容在模型上下文窗口范围之内，仍然存在显著且系统性的失效模式。 这一发现直接挑战了当前越来越普遍的做法——团队依赖持久化指令文件来引导 Claude Code、Cursor、Copilot 等 AI 编程智能体在生产工作流中的行为。如果智能体无法可靠地遵守这些文档，组织可能需要重新思考 AI 辅助软件开发的治理策略，从声明式策略文件转向运行时强制执行、更小范围的指令或基于工具的约束。 该论文将指令遵循视为一个基准问题，认为达到超人类水平的遵守能力将意味着超人类的认知能力，并将其与人类自身在面对长策略文档时众所周知的局限性进行了类比。社区讨论中提到的技术因素包括：长上下文中的极端 KV 缓存量化、部署推理栈中激进的采样器行为，以及随着系统提示增长，相关注意力信号被稀释的问题。

hackernews · spIrr · 7月29日 13:01 · [社区讨论](https://news.ycombinator.com/item?id=49096969)

**背景**: Claude Code、Codex、Cursor 等 AI 编程智能体通常通过放在项目根目录的纯文本指令文件进行配置（如 CLAUDE.md、AGENTS.md、.cursorrules、.github/copilot-instructions.md），这些文件会在每一轮对话中被预置到模型的上下文中。开发者将这些文件视为持久化的项目记忆，用来编码编码规范、首选库和行为规则。「Handbook.md」这篇论文检验了「只要把规则放进这种文件就一定会被执行」这一假设，发现随着策略变长以及对话推进，遵守程度会显著下降。相关研究同样表明，LLM 的指令遵循率在轻微的提示扰动下可能下降高达 61%，而埋在提示中段的指令比首尾位置的指令获得的注意力更少。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/data-science-collective/the-complete-guide-to-ai-agent-memory-files-claude-md-agents-md-and-beyond-49ea0df5c5a9">The Complete Guide to AI Agent Memory Files (CLAUDE.md, AGENTS.md, and Beyond)</a></li>
<li><a href="https://siliconopera.com/why-a-longer-system-prompt-usually-makes-llms-worse/">Why a Longer System Prompt Usually Makes LLMs... — Silicon Opera</a></li>
<li><a href="https://artoftruth.org/llm-instruction-following-compliance-gap/">LLM instruction following drops 61%: devastating AI crisis</a></li>

</ul>
</details>

**社区讨论**: 讨论整体上与论文结论高度一致。高赞评论将失败归因于工程层面的原因——极端的 KV 缓存量化、有损的采样器以及长上下文的注意力稀释，其中一位评论者指出本地推理引擎在保持指令遵循方面往往远好于托管 API。一位资深实践者反馈，Claude 在大约十分钟内能较好地遵守 CLAUDE.md 中的指令，但之后就会绕过；而同样的指令如果以内联方式写在当前提示中，则能被可靠执行。另一位评论者则认为「智能体式 AI」本身就是一个通过在精选数据集上进行后训练强化学习而「硬塞」进去的合成能力，实验室没有专门训练过的任何策略默认都会被忽略。

**标签**: `#AI-agents`, `#LLM-evaluation`, `#system-prompts`, `#context-windows`, `#alignment`

---

<a id="item-5"></a>
## [台积电 Fab 20 工厂 2nm 制程月产能达 2 万片晶圆](https://www.electronicsweekly.com/news/business/tsmc-fab-20-running-20k-2nm-wpm-2026-07/) ⭐️ 8.0/10

台积电 Fab 20 工厂的 2nm 制程已达到月产 2 万片晶圆的里程碑，标志着其前沿制程产能正在加速爬坡。

rss · Electronics Weekly · 7月29日 05:38

**标签**: `#TSMC`, `#semiconductors`, `#2nm`, `#fabrication`, `#manufacturing`

---

<a id="item-6"></a>
## [HRL 展示可自主运行的硅基量子处理器](https://www.techpowerup.com/351204/hrl-demonstrates-a-silicon-quantum-processor-that-runs-itself) ⭐️ 7.5/10

HRL 实验室在《Nature》发表论文，展示了一种与定制低温 CMOS 控制芯片集成的硅基量子处理器，该系统能够自主运行量子纠错程序，用放置在极低温环境下的芯片取代了成排的外部控制电子设备。 这解决了量子计算中最核心的可扩展性障碍之一：控制大量量子比特所需的难以管理的布线和室温电子设备。将控制电子设备直接与量子比特集成，被视为迈向容错量子计算的关键一步。 控制芯片采用与硅量子比特制造兼容的 CMOS 技术，在 3 K 低温环境下运行，而量子比特本身则在约 20 mK 温度下工作。通过将控制器放置在量子比特旁边的低温环境中，HRL 消除了在室温与稀释制冷机之间运行数千条信号线的需求，系统可在无外部干预的情况下自主执行纠错。

rss · TechPowerUp News · 7月29日 19:44

**背景**: 量子纠错对于构建有用的量子计算机至关重要，因为量子比特极易受到噪声和退相干的影响。表面码是最主流的拓扑纠错方案之一，将单个逻辑量子比特编码到多个物理量子比特上——例如，纠正任意单量子比特错误至少需要五个物理量子比特。硅自旋量子比特将量子信息编码在囚禁于硅纳米结构中的单电子自旋态上，由于可以利用与现代晶体管相同的 CMOS 制造生态系统，因此备受青睐。然而，传统控制方案依赖通过同轴电缆连接到量子比特的整排室温仪器，当量子比特数量扩展到容错运算所需的数千甚至数百万个时，这种布线复杂度成为主要瓶颈。低温 CMOS 控制芯片于 2021 年首次被用于简单的量子比特操控，其目标是将控制硬件直接移入稀释制冷机内部。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-021-03469-4">CMOS-based cryogenic control of silicon quantum circuits | Nature</a></li>
<li><a href="https://link.aps.org/doi/10.1103/PRXQuantum.5.010326">Using Cryogenic CMOS Control Electronics to Enable a Two-Qubit Cross-Resonance Gate | PRX Quantum</a></li>
<li><a href="https://en.wikipedia.org/wiki/Surface_code">Surface code - Wikipedia</a></li>

</ul>
</details>

**标签**: `#quantum-computing`, `#hardware`, `#silicon-photonics`, `#error-correction`, `#research-breakthrough`

---

<a id="item-7"></a>
## [GlobalFoundries 获 3 亿美元 CHIPS 法案资金，美国政府持股 1%](https://www.techpowerup.com/351199/globalfoundries-receives-usd-300m-for-silicon-photonics-u-s-government-acquires-1-stake) ⭐️ 7.5/10

美国商务部在特朗普政府期间与 GlobalFoundries 签署了一份意向书，向该公司提供 3 亿美元的 CHIPS 法案资金，并获得约 1%的股权，以推进下一代硅光子技术。 这标志着美国政府正在直接持有半导体公司股权，政策方向发生了显著转变；同时该投资表明硅光子技术对 AI 基础设施的战略重要性，因为传统电互联正成为数据传输的瓶颈。 该资金将用于在 GlobalFoundries 位于纽约州马耳他和佛蒙特州伯灵顿的工厂开发近封装光学（NPO）、共封装光学（CPO）、3D 混合键合以及新型材料。该公司的 SCALE（硅光子共封装先进光引擎）平台已支持 400 Gb/s 的封装传输速率，并具有高能效。

rss · TechPowerUp News · 7月29日 17:30

**背景**: 硅光子技术是以硅作为光学介质，利用光而非电信号传输数据，从而实现更快、更节能的数据传输。共封装光学（CPO）将光引擎直接集成在交换 ASIC 和加速器旁边，将电互联距离从英寸级缩短到毫米级，以应对 AI 工作负载的能耗需求。GlobalFoundries 曾在行业向 7nm 过渡期间退出了前沿制程节点的研发，但此后转向以 AI 扩展驱动的硅光子技术和先进封装作为增长领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Silicon_photonics">Silicon photonics - Wikipedia</a></li>
<li><a href="https://www.ansys.com/blog/what-is-co-packaged-optics">What is Co-packaged Optics?</a></li>
<li><a href="https://blogs.sw.siemens.com/semiconductor-packaging/2026/02/05/five-key-trends-of-co-packaged-optics-cpo-in-2026/">Five Key Trends of Co-Packaged Optics (CPO) in 2026 - Semiconductor Packaging</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#CHIPS-Act`, `#silicon-photonics`, `#GlobalFoundries`, `#AI-infrastructure`

---

<a id="item-8"></a>
## [铠侠发布 UFS 5.0 嵌入式闪存器件](https://www.techpowerup.com/351183/kioxia-announces-ufs-5-0-embedded-flash-memory-devices) ⭐️ 7.5/10

铠侠发布了基于 JEDEC UFS 5.0 标准的嵌入式闪存解决方案，提供 1 TB 和 512 GB 的商业样品，单通道理论接口速率高达 46.6 Gb/s，双通道有效读写性能约 10.8 GB/s。该器件将于 2026 年底开始量产，并将在 FMS（存储器与存储未来大会）上展示。 随着大语言模型、多模态 AI 和实时推理迁移到端侧设备，存储读取性能已成为移动和边缘 AI 工作负载的关键瓶颈。UFS 5.0 将带宽较 UFS 4.1 提升约一倍，可消除这一瓶颈，实现更快的模型加载速度，并为下一代智能手机及 AI 边缘设备带来更高的响应能力。 该器件采用 MIPI M-PHY v6.0 物理层和 UniPro v3.0 协议，并支持 HS-Gear6 工作模式，使用支持全双工并发读写的串行接口。10.8 GB/s 的数值代表双通道的有效吞吐量，是一次重大飞跃，直接满足了端侧大语言模型和先进成像管线的数据传输需求。

rss · TechPowerUp News · 7月29日 08:39

**背景**: 通用闪存（UFS）是由 JEDEC 制定的闪存规范，旨在取代手机、相机和消费电子设备中的 eMMC 和 SD 卡，采用支持全双工通信的串行接口。UFS 依赖分层协议：MIPI M-PHY 物理层负责高速信号传输，而 MIPI UniPro 协议栈（结构类似于 OSI 第 1–4 层）则管理主机与存储设备之间的数据单元处理。从 UFS 4.1 升级到 UFS 5.0 引入了新一代的 M-PHY（v6.0）和 UniPro（v3.0），能够提供满足端侧 AI 模型数据饥渴所需的高带宽。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/351183/kioxia-announces-ufs-5-0-embedded-flash-memory-devices">Kioxia Announces UFS 5 . 0 Embedded Flash Memory... | TechPowerUp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_Flash_Storage">Universal Flash Storage - Wikipedia</a></li>
<li><a href="https://www.mipi.org/specifications/unipro-specifications">MIPI UniPro | MIPI</a></li>

</ul>
</details>

**标签**: `#storage`, `#UFS 5.0`, `#flash memory`, `#edge AI`, `#mobile hardware`

---

<a id="item-9"></a>
## [希捷将于 2027 年开始对创纪录的 50TB 硬盘进行验证 —— 大部分硬盘已售罄至 2028 年](https://www.tomshardware.com/pc-components/hdds/seagate-to-start-qualifying-record-setting-50tb-hdds-in-2027-most-drives-are-sold-out-through-2028) ⭐️ 7.5/10

希捷将于 2027 年末开始对 50TB HAMR 硬盘进行验证，并于 2028 年开始出货，由于 AI 驱动的强劲需求，其产量已基本售罄至 2028 年。

rss · Tom's Hardware · 7月29日 16:40

**标签**: `#storage`, `#HAMR`, `#Seagate`, `#hard-drives`, `#AI-infrastructure`

---

<a id="item-10"></a>
## [Apacer 首席执行官警告：2027 年内存模组厂商 DRAM 供应或下降超 70%](https://www.tomshardware.com/pc-components/ram/dram-chip-supply-to-module-makers-could-drop-by-more-than-70-percent-year-on-year-in-2027-says-apacer-ceo-demand-for-hbm-and-server-ram-continues-to-devour-manufacturing-capacity) ⭐️ 7.5/10

Apacer 首席执行官 C.K. Chang 警告称，到 2027 年，独立内存模组厂商获得的 DRAM 芯片配额可能仅为 2026 年水平的 30%，同比降幅超过 70%。这一供应短缺源于 AI 驱动的 HBM（高带宽内存）和服务器内存需求激增，占据了主要 DRAM 厂商大部分晶圆产能。 如果这一预测成真，消费级内存产品（如 SSD、DDR4/DDR5 内存条和移动 DRAM）的供应将受到严重挤压，终端用户和 PC 装机者的购入成本可能大幅上涨。这一趋势凸显了 AI 基础设施需求正在重塑整个内存供应链，非 AI 下游客户不得不承担产能重新分配的代价。 该警告特别针对独立内存模组厂商，它们从三星、SK 海力士和美光等 DRAM 巨头处采购芯片，而非这些 IDM 内部的内存部门。HBM 通过硅通孔（TSV）技术将多颗 DRAM 裸片进行 3D 堆叠，每颗 HBM 消耗的晶圆面积远高于普通 DDR 芯片，从而放大了对标准 DRAM 产能的挤压效应。

rss · Tom's Hardware · 7月29日 10:30

**背景**: DRAM（动态随机存取内存）是计算机、服务器和移动设备中使用的主要易失性内存。HBM（高带宽内存）是一种专用的 3D 堆叠内存变体，可提供远高于普通内存的带宽和更低的功耗，是 NVIDIA 和 AMD 等公司 AI GPU 和加速器的核心组件。三星、SK 海力士和美光等主要 DRAM 厂商需要在不同产品线之间分配晶圆制造产能，而 HBM 订单的不断增长正逐步将产能从传统 DDR4、DDR5 和 LPDDR 产品中分流出去。Apacer 等独立模组厂商从这些晶圆厂采购 DRAM 芯片，用于组装零售内存模组和 SSD。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.msn.com/en-gb/money/other/dram-chip-supply-to-memory-module-makers-could-drop-by-more-than-70-in-2027-says-apacer-ceo/ar-AA28YDsr">DRAM chip supply to memory module makers could drop by more...</a></li>
<li><a href="https://supplyics.com/insights/market-intelligence/2026-hbm-dram-memory-supply-chain-analysis/">2026 HBM and DRAM Supply Chain Analysis: Navigating... - SupplyICs</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#HBM`, `#AI infrastructure`, `#supply chain`, `#memory pricing`

---

<a id="item-11"></a>
## [英特尔完成 RAMP-C 国防项目，验证 18A 代工工艺](https://www.tomshardware.com/tech-industry/intel-closes-out-the-defense-program-that-paid-nvidia-and-others-to-run-test-chips-on-18a) ⭐️ 7.5/10

英特尔代工部门（Intel Foundry）宣布已完成 RAMP-C 项目——这是一项于 2021 年授予该公司的美国国防项目，曾向包括英伟达在内的外部合作伙伴支付费用，让其在英特尔的 18A 工艺节点上运行测试芯片。该项目的目标是为国家安全应用建立一个本土的先进制程芯片制造生态系统。 RAMP-C 的成功完成标志着英特尔代工业务雄心的一次重大信誉验证，表明英伟达等主要芯片设计厂商愿意验证英特尔最先进的 18A 工艺。该项目也推进了美国在先进制程国防和商用硅片领域减少对台积电等亚洲代工厂依赖的战略目标。 英特尔 18A 是 1.8 纳米级别的工艺节点，引入 RibbonFET（环绕栅极）晶体管和 PowerVia 背面供电技术，这些技术旨在让英特尔重回半导体制造的前沿。该项目专门针对先进制程的安全国产化生产，而非纯粹的商用量产。

rss · Tom's Hardware · 7月29日 09:30

**背景**: RAMP-C 项目是美国为确保国防和国家安全工作负载能够获得本土先进制程芯片制造能力而设立的，其背景是对台湾和韩国供应链集中度的担忧。英特尔的 18A 节点是该公司最先进的制造工艺，在 1.8 纳米级别世代中与台积电的 N2 和三星的 2nm 工艺竞争。代工服务（即芯片设计公司将设计方案交由第三方制造）已成为战略竞争焦点，英特尔正试图挑战占据主导地位的台积电。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.globalsmt.net/advanced-packaging/intel-reaches-3nm-milestone/">Intel reaches 3nm milestone - Electronics Manufacturing News</a></li>
<li><a href="https://wccftech.com/tsmc-wins-intel-order-for-two-3nm-cpus-to-regain-market-share-lost-to-amd/">TSMC Wins Intel Order For Two 3nm CPUs To Regain Market Share...</a></li>

</ul>
</details>

**标签**: `#Intel`, `#semiconductors`, `#RAMP-C`, `#chip-manufacturing`, `#national-security`

---

<a id="item-12"></a>
## [月之暗面 Kimi 完成超 35 亿美元 F 轮融资，估值达 350 亿美元](https://36kr.com/p/3916547493965442?f=rss) ⭐️ 7.3/10

月之暗面已完成超 35 亿美元的 F 轮融资，投后估值涨至 350 亿美元，因超募 3 倍多而提前关闭；原定 8 月开启的 Pre-IPO G 轮也提前启动，投前估值升至 500 亿美元。此外，阿里旗下瓴羊推出 AgentOne 平台的四名 AI 员工上岗，联电宣布在台南新建晶圆厂以满足 AI 需求。 这是全球最大规模的 AI 融资之一，表明投资人对中国大模型公司信心极强，月之暗面也因此大幅提前 IPO 时间表。瓴羊 AgentOne 的 AI 员工落地和联电新建晶圆厂则体现了中国科技生态中 AI 智能体商业化与支撑 AI 需求的硬件建设的全面推进。 月之暗面是中国六大'AI 虎'之一，总部位于北京，目标是与美国前沿 AI 实验室竞争。瓴羊 AgentOne 采用了前沿部署工程师（FDE）模式——一种源自 Palantir 的工程师岗位，深入客户场景构建定制方案——帮助企业在四个开箱即用的 AI 员工（销售、客服、运营、营销）之外打造专属的'X 员工'。

rss · 36氪 · 7月29日 11:04

**背景**: 月之暗面是一家总部位于北京的 AI 初创公司，是中国六大'AI 虎'之一，这些获得大额融资的中国 AI 实验室正竞相打造可与 OpenAI、Anthropic 相媲美的前沿模型，其 Kimi 系列模型以长上下文能力著称。FDE（前沿部署工程师）岗位源自 Palantir，由工程师直接嵌入企业客户内部构建定制化软件，而非单纯销售或咨询。瓴羊是阿里云旗下企业数据与 AI 服务品牌，将 AgentOne 定位为可将 AI'数字员工'部署到真实业务流程中的平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://www.aibase.com/news/21570">Alibaba Lingyang Launches AgentOne Platform to Promote...</a></li>
<li><a href="https://www.futureventures.ca/insights/understanding-the-forward-deployed-engineering-model">Understanding the Forward Deployed Engineering ( FDE ) Model</a></li>

</ul>
</details>

**标签**: `#AI funding`, `#Moonshot AI`, `#semiconductor`, `#Chinese tech`, `#AI agents`

---

<a id="item-13"></a>
## [微软新增数据中心租约超 1300 亿美元](https://36kr.com/newsflashes/3917435911007621?f=rss) ⭐️ 7.3/10

微软在第四季度披露了超过 1300 亿美元的新增未履约数据中心租约承诺，使其租约承诺总额达到 3291 亿美元，标志着其 AI 算力基础设施扩张正在加速。

rss · 36氪 · 7月30日 01:01

**标签**: `#Microsoft`, `#AI Infrastructure`, `#Data Centers`, `#Cloud Computing`, `#AI Investment`

---

<a id="item-14"></a>
## [AI 顶级初创公司越来越不发表研究论文](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research) ⭐️ 7.0/10

《科学》杂志的一项分析显示，顶级 AI 初创公司发表的研究论文越来越少，主要原因是竞争压力和知识产权保护方面的考量。该研究使用引用次数作为衡量 AI 独角兽公司研究产出的代理指标。 这一趋势扩大了工业界与学术界 AI 研究之间的差距，可能会减缓更广泛的科学界获取突破性方法的速度，并使独立研究者更难验证或构建尖端工作。这也标志着该领域从最初定义的开放研究精神发生了根本性转变。 该研究通过引用次数而非直接发表论文数量来衡量研究产出，OpenAI 位居榜首，其后依次为 MEGVII、Hugging Face、Waymo、Momenta、Preferred Networks、Anthropic、Owkin、Databricks 和 Aibee。Google 因不属于独角兽公司而被排除在外，作者承认引用次数只是研究重要性的一个不完美的代理指标。

hackernews · YeGoblynQueenne · 7月29日 21:25 · [社区讨论](https://news.ycombinator.com/item?id=49103285)

**背景**: AI 研究的透明度一直是该领域的传统特征，像 OpenAI 这样的机构最初是以开放研究的原则创立的。随着 AI 公司之间竞争加剧，特别是在 GPT-3 和 GPT-4 等大语言模型发布后，向封闭式研究实践的转变速度加快。初创公司面临战略困境：发表创新成果可以吸引人才和信誉，但也将专有方法暴露给可能快速复制的竞争对手。使用引用次数作为研究产出代理指标存在固有局限性，因为引用可能被自我引用、媒体炒作或审稿人网络所膨胀，而不仅仅反映科学重要性。

**社区讨论**: 有初创公司直接经验的评论者强烈验证了文章的观点，其中一位解释说他目前在当前的初创公司不再发表论文，因为之前经历过发表论文的阻力以及害怕六个月的成果被 OpenAI 或 Anthropic 复制。另一位评论者赞扬了一位在 YC 选拔前主动发表关于递归自我改进研究的创始人，同时也有人对 AI 研究的'博客化'以及用可能游戏化实验环境中的数据来支持论断表示担忧。一位热心的评论者澄清了原论文的方法论，解释了哪些公司被纳入以及 Google 为何被排除。

**标签**: `#AI research`, `#industry-vs-academia`, `#transparency`, `#AI startups`, `#research publishing`

---

<a id="item-15"></a>
## [Vision Pro 最酷的用途](https://christianselig.com/2026/07/vision-pro-house/) ⭐️ 7.0/10

一个使用 Vision Pro 在施工前以虚拟现实方式漫步于已完整设计好的住宅的实用展示，社区讨论也证实了这种工作流程已在众多建筑设计公司中得到广泛采用。

hackernews · robbiet480 · 7月29日 20:39 · [社区讨论](https://news.ycombinator.com/item?id=49102774)

**标签**: `#vision-pro`, `#vr-ar`, `#architecture`, `#design-tools`, `#spatial-computing`

---

<a id="item-16"></a>
## [Show HN：开源引擎可在任何 M 系列 Mac 上以 2 GB 内存运行 Gemma 4 26B](https://github.com/drumih/turbo-fieldfare) ⭐️ 7.0/10

一款名为 TurboFieldfare 的开源 Swift/Metal 推理引擎，可通过从 SSD 流式传输所需的路由专家，同时将共享权重和 KV 缓存常驻内存，从而仅用 2GB 内存在任何 M 系列 Mac 上运行 Gemma 4 26B（MoE）。

hackernews · gitpusher42 · 7月29日 15:05 · [社区讨论](https://news.ycombinator.com/item?id=49098510)

**标签**: `#ai-inference`, `#apple-silicon`, `#mixture-of-experts`, `#edge-ai`, `#open-source`

---

<a id="item-17"></a>
## [Superlogical](https://www.superlogical.com/) ⭐️ 7.0/10

Mitchell Hashimoto 推出了新公司 Superlogical，该公司在已捐赠给非营利组织的开源 Ghostty 终端模拟器基础上，构建终端基础设施平台。

hackernews · yan · 7月29日 15:41 · [社区讨论](https://news.ycombinator.com/item?id=49098965)

**标签**: `#open-source`, `#ghostty`, `#mitchell-hashimoto`, `#terminal`, `#startup`

---

<a id="item-18"></a>
## [动态 AI 需求推动存储多元化](https://www.eetimes.com/dynamic-ai-demands-drive-memory-diversity/) ⭐️ 7.0/10

EE Times 分析指出，AI 工作负载正在加剧容量、延迟与功耗之间的存储权衡，而非催生全新的存储类别。

rss · EE Times · 7月29日 18:00

**标签**: `#AI infrastructure`, `#memory architecture`, `#hardware`, `#data center`, `#semiconductors`

---

<a id="item-19"></a>
## [光子技术从机架级向芯粒级集成演进](https://www.eetimes.com/from-co-packaged-optics-to-nanolasers-photonics-moves-inward/) ⭐️ 7.0/10

CEA-Leti、Scintil Photonics 和 NcodiN 三家机构正各自推进光互连技术，从数据中心机架级向共封装光学（CPO）和芯粒级通信迈进，其中 NcodiN 展示了集成纳米激光器的硅光子芯片，能效低于 0.1 pJ/bit。 随着 AI 工作负载推动芯片间带宽呈指数级增长，传统电互连正成为瓶颈；将光子技术向封装内和芯粒级推进，有望在能效、带宽密度和延迟方面带来显著提升，直接影响下一代 AI 加速器和数据中心架构的可扩展性。 共封装光学（CPO）将激光器、光子引擎和光纤连接器直接集成在与 ASIC 或交换机同一封装内；而光学 I/O 则更进一步，作为封装在单一 IC 中的芯粒级互连；NcodiN 的方案结合了 FPGA 控制器与片上纳米激光器，实现了低于 0.1 pJ/bit 的能效。

rss · EE Times · 7月29日 08:02

**背景**: 共封装光学（CPO）是一种先进的封装技术，将激光器、调制器和光纤连接器等光学部件直接放置在与电子芯片（如交换机或 ASIC）同一封装内，与传统的板级可插拔光模块形成对比。芯粒（chiplet）是一种小型集成电路裸片，设计用于与其他芯粒在封装内组合形成更大的系统，从而实现模块化扩展。光学 I/O 进一步延伸了这一概念，将基于芯粒的光互连封装到单一 IC 中，支持如 UCIe Optical 等标准化接口。纳米激光器是可以直接集成在硅光子芯片上的极小尺寸半导体激光器，有望实现完全片上光通信。这些技术共同代表了将光信号尽可能靠近计算单元的演进趋势，以克服高带宽 AI 系统中铜互连的局限性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chiplet-marketplace.com/wiki/co-packaged-optics">Co - Packaged Optics - Semi IP Hub Wiki</a></li>
<li><a href="https://picmagazine.net/article/124637/Ncodin’s_nanolasers_eye_AI_infrastructure">Ncodin’s nanolasers eye AI infrastructure - Photonic Integrated ...</a></li>
<li><a href="https://ayarlabs.com/blog/demystifying-optical-i-o-12-key-terms-to-know/">Demystifying Optical I/O: 12 Key Terms to Know | Ayar Labs</a></li>

</ul>
</details>

**标签**: `#photonics`, `#co-packaged-optics`, `#chiplets`, `#semiconductors`, `#optical-interconnects`

---

<a id="item-20"></a>
## [新思科技联合英伟达展示自主设计验证智能体](https://www.electronicsweekly.com/news/business/synopsys-unveils-autonomous-workflows-agents-2026-07/) ⭐️ 7.0/10

在完成收购 Ansys 一周年之际，新思科技展示了面向 EDA 和 CAE 工作流程的自主设计验证智能体（agent），这些智能体是与英伟达合作开发的，基于 NVIDIA Agent Toolkit 和 CUDA-X 库构建。 这是智能体式 AI（agentic AI）在芯片设计与仿真流程中首批生产级部署之一，有望改变工程师执行验证、热分析以及多物理场仿真的方式。同时也验证了新思科技斥巨资收购 Ansys 的战略逻辑——将仿真能力直接嵌入由 AI 驱动的设计闭环。 这些智能体面向电子热分析的完全自主 CAE 工作流程，依托英伟达的 GPU 加速计算栈。该发布恰逢更广泛的行业趋势——包括西门子在 DAC 2026 上推出竞争性的智能体平台——表明 agentic AI 正快速从演示走向 EDA 领域的实际部署。

rss · Electronics Weekly · 7月29日 15:28

**背景**: EDA（电子设计自动化）指用于设计和验证半导体的软件工具，而 CAE（计算机辅助工程）涵盖更广泛的物理现象仿真，如热学、结构力学和电磁行为——这历来是 Ansys 的核心领域。新思科技于 2025 年中完成了对 Ansys 约 350 亿美元的收购，旨在将芯片设计工具与多物理场仿真相结合。Agentic AI（智能体式 AI）指能够自主规划、调用工具并以最少人工监督执行多步工程任务的 AI 系统，与传统仅响应提示的聊天机器人有本质区别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.engineering.com/synopsys-and-nvidia-advance-agentic-ai-for-chip-design/">Synopsys and NVIDIA advance agentic AI for chip design</a></li>
<li><a href="https://www.forbes.com/sites/marcochiappetta/2025/07/18/synopsys-finalizes-ansys-acquisition-to-enable-leading-simulation-enhanced-design/">Synopsys Ansys Acquisition Enables Leading Simulation Enhanced...</a></li>
<li><a href="https://www.techtimes.com/articles/321690/20260727/dac-2026-live-ai-chip-design-agents-hit-production-nobel-laureate-joins-debate.htm">DAC 2026 Live: AI Chip Design Agents Hit Production as Nobel...</a></li>

</ul>
</details>

**标签**: `#EDA`, `#Synopsys`, `#Nvidia`, `#autonomous-agents`, `#chip-design`

---