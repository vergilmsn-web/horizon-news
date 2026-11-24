---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> 从 108 条内容中筛选出 20 条重要资讯。

---

1. [为什么峰值 FLOPS 是评估推理硬件的错误标准](#item-1) ⭐️ 9.0/10
2. [Windows Server 2028 默认移除 WoW64 32 位兼容层](#item-2) ⭐️ 8.3/10
3. [Ternary Bonsai 2.5 27B 将自主编程能力带入消费级 Mac](#item-3) ⭐️ 8.0/10
4. [GreyNoise 报告针对 Check Point 安全服务器的主动入侵活动](#item-4) ⭐️ 8.0/10
5. [Hacker News 热议 AI 编码代理实现 2035 技术](#item-5) ⭐️ 8.0/10
6. [Cloudflare hides shortcomings of the underlying infrastructure](#item-6) ⭐️ 8.0/10
7. [Moores Lab AI’s Benchmark Push: Measuring Whether AI Can Actually Verify Chips](#item-7) ⭐️ 8.0/10
8. [西门子收购 Breker 对下一代 AI 芯片的重要性](#item-8) ⭐️ 8.0/10
9. [JEDEC 发布 JESD209-6：LPDDR6 标准更新以支持 AI 与移动设备](#item-9) ⭐️ 8.0/10
10. [OpenAI 员工被发现在会议室内安装窃听器](#item-10) ⭐️ 7.5/10
11. [Songe：开源本地 LLM 做梦与微调引擎](#item-11) ⭐️ 7.0/10
12. [Quad9 因强制屏蔽令撤出法国 DNS 服务](#item-12) ⭐️ 7.0/10
13. [Acorn 与 UCLouvain 推进 FDSOI 和 RF-SOI 埋入式应力源技术](#item-13) ⭐️ 7.0/10
14. [美国司法部在全球反诈骗行动中没收 170 亿美元及 1.4 万台设备](#item-14) ⭐️ 6.5/10
15. [Frontier AI employees alarmed that unseen Open AI and Anthropic models are too powerful to release, report claims](#item-15) ⭐️ 6.5/10
16. [Reinstated Nvidia CEO Jensen Huang must still face China congressional and Senate Banking committees](#item-16) ⭐️ 6.5/10
17. [Trump pressured Nvidia to bring Jensen back, called into board meeting to push reinstatement, reports claim](#item-17) ⭐️ 6.5/10
18. [车网互动技术面临重大实际与技术障碍](#item-18) ⭐️ 6.0/10
19. [车辆向电网输电：绝佳创意还是不切实际的幻想？](#item-19) ⭐️ 6.0/10
20. [AMD AGESA 1.3.0.1f 补丁将 Ryzen 8000 最大核心电压限制为 1.4V](#item-20) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [为什么峰值 FLOPS 是评估推理硬件的错误标准](https://semiwiki.com/semiconductor-manufacturers/vsora/376702-why-peak-flops-is-the-wrong-yardstick-for-inference-hardware/) ⭐️ 9.0/10

文章认为峰值 FLOPS 不适合评估 AI 推理硬件，因为推理负载与训练存在根本差异，这需要改变硬件基准测试的方式。

rss · SemiWiki · 11月24日 14:00

**标签**: `#AI Hardware`, `#Inference Optimization`, `#Performance Metrics`, `#Semiconductor Industry`

---

<a id="item-2"></a>
## [Windows Server 2028 默认移除 WoW64 32 位兼容层](https://www.solidot.org/story?sid=85978) ⭐️ 8.3/10

微软宣布 Windows Server 2028 将不再默认安装 WoW64 兼容层，运行 32 位应用需要用户手动启用该可选组件。此变更旨在缩小系统占用空间并提升安全性，通过阻断 32 位恶意代码来加固系统。 此决策迫使开发人员和 IT 管理员将遗留的 32 位软件迁移至 64 位环境，解决了企业安全与系统兼容性的重大痛点。此举顺应了通过淘汰过时的软件组件来降低现代威胁漏洞的业界趋势。 WoW64 子系统自 2008 年起一直存在于所有 64 位版本的 Windows 中，用于连接 32 位用户模式代码与 64 位内核。微软指出，此更改将专门防止 32 位恶意程序的运行，若不手动安装该可选组件，此类恶意程序将无法在新的操作系统上执行。

rss · Solidot · 11月24日 14:04

**背景**: WoW64（Windows 32 位运行于 Windows 64 位）是一个转换和重定向层，允许 32 位应用与 64 位内核共存。它使用包括 Wow64.dll 在内的一组 DLL 拦截内核调用，为旧软件创建虚拟环境。Windows Server 最后一个原生 32 位版本发布于 2008 年，这意味着 32 位支持在过去 15 多年来一直依赖此兼容层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WoW64">WoW64 - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/win32/winprog64/wow64-implementation-details">WOW64 Implementation Details - Win32 apps | Microsoft Learn WOW64 and cross-architecture compatibility | Windows Internals Windows on Windows - Wikipedia Running 32-bit Applications - Win32 apps | Microsoft Learn WOW64 and cross-architecture compatibility: Windows internals ... WoW64: Running 32-bit Processes on 64-bit Windows</a></li>
<li><a href="https://en.wikipedia.org/wiki/Windows_on_Windows">Windows on Windows - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Windows Server`, `#System Administration`, `#Security`, `#Bioengineering`, `#Pharmacology`

---

<a id="item-3"></a>
## [Ternary Bonsai 2.5 27B 将自主编程能力带入消费级 Mac](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 8.0/10

PrismML 发布了 Ternary Bonsai 2.5 27B，这是一款三值量化的 LLM，能够在 Mac M5 Pro 等消费级硬件上执行自主编程任务。它以每秒 22-25 个词元的速度运行，并支持高达 128k 的内存上下文。 此次发布通过允许在主流笔记本电脑上无需昂贵的 GPU 集群即可运行复杂的自主任务，大幅降低了本地 AI 编程助手的硬件门槛。这标志着行业正转向更注重实际效用而非单纯追求基准测试性能的高可访问性低比特 AI 模型。 三值量化将模型权重限制为三个值（-1、0、+1），从而实现了 1.58 比特的精度，大幅降低了内存使用量。尽管该模型在 SWE-bench 上取得了与前沿模型相当的成绩，但其实际表现取决于上下文限制和预填充速度，而不仅仅是生成速度。

hackernews · b0m · 11月24日 20:08 · [社区讨论](https://news.ycombinator.com/item?id=50633922)

**背景**: 标准 LLM 通常使用 16 位浮点权重，这使得它们内存占用大且难以在消费级硬件上运行。三值 LLM（1.58 位）代表了一种极限量化形式，可将模型大小压缩以适应严格的内存预算。自主编程是指 AI 系统能够独立执行编写代码、运行测试和修复错误等多步骤任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/1.58-bit_large_language_model">1.58-bit large language model - Wikipedia</a></li>
<li><a href="https://prismml.com/">PrismML — Concentrating intelligence</a></li>
<li><a href="https://arxiv.org/abs/2406.07177">[2406.07177] TernaryLLM: Ternarized Large Language Model</a></li>

</ul>
</details>

**社区讨论**: 社区用户对 128k 的上下文窗口和预填充速度印象深刻，确认其在自主编程方面的实用性。然而，关于 SWE-bench 成绩在小模型中的有效性存在争议，且需要与其他流行的 1B-10B 量化模型进行直接的硬件对比。部分用户还询问了除 FPGA 之外的特定硬件加速方法。

**标签**: `#LLM`, `#LocalAI`, `#Quantization`, `#AgenticCoding`, `#PrismML`

---

<a id="item-4"></a>
## [GreyNoise 报告针对 Check Point 安全服务器的主动入侵活动](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) ⭐️ 8.0/10

GreyNoise 发现了一起针对多家机构 Check Point 安全管理服务器的主动入侵活动。该攻击涉及利用漏洞逆向工程弱伪随机数生成器，从而伪造管理员会话 Cookie。 攻破 Check Point 等大型企业安全供应商的防护工具，可让攻击者跳板进入敏感网络环境。这显著降低了攻击者访问关键基础设施和客户数据的门槛。 尽管摘要详述了 Check Point 的入侵情况，但网络搜索结果将与该 PRNG 状态重构和会话伪造技术关联到 Rejetto HFS 的严重漏洞（CVE-2026-61500）。攻击者 IP 基础设施涵盖 99 个地址，且据报道该行动受到 LLM 辅助。

hackernews · louiereederson · 11月24日 16:32 · [社区讨论](https://news.ycombinator.com/item?id=50630594)

**背景**: 安全管理服务器是高度敏感的靶标，因为它们通常持有管理整个网络环境的密钥。PRNG 是模拟随机数序列的计算机算法，其内部状态有时可通过观察输出进行预测。伪造会话 Cookie 允许攻击者在无需发现或利用实际身份验证漏洞的情况下冒充合法用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/hackers-compromise-check-point-servers-in-22-organizations/">Hackers compromise Check Point Servers in 22 organizations</a></li>
<li><a href="https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html">Attackers Target Rejetto HFS Flaw That Enables Admin Session ...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对 AI 驱动的网络犯罪团伙日益增大的威胁的担忧。此外，还存在关于攻击者如何最初绕过安全防护的技术争论，以及对 JavaScript 的 Math.random() 在安全关键的会话管理中仍不安全的挫败感。

**标签**: `#cybersecurity`, `#check-point`, `#intrusion-campaign`, `#prng`, `#session-cookie-forgery`

---

<a id="item-5"></a>
## [Hacker News 热议 AI 编码代理实现 2035 技术](https://fzakaria.com/2026/11/23/2035-came-early) ⭐️ 8.0/10

F. Zakaria 分析的高参与度 Hacker News 讨论证实，AI 编码代理已使独立开发者能够构建操作系统内核等复杂系统，从而将原本预计在 2035 年才能实现的能力提前落地。社区通过个人利用 LLM 编排成功创建以往无法达成的软件里程碑的案例，验证了这种转变。 这标志着软件工程领域的重要范式转变，LLM 编排消除了团队规模的历史壁垒，使个人能够执行高复杂度项目。这通过迫使重新评估技术职业轨迹和传统软件开发方法，对整个行业产生了深远影响。 构建复杂系统的能力现在严重依赖 LLM 编排——即协调多个 AI 模型——而非纯粹的手工编码，这在社区成员为期两个月、耗时 100 小时创建裸机操作系统的项目中可见一斑。虽然一些开发者急于发布他们通过代理构建的工作，但这种方法对于基于 Web 的语言的根本实用性和局限性并非没有怀疑。

hackernews · setheron · 11月24日 06:30 · [社区讨论](https://news.ycombinator.com/item?id=50624497)

**背景**: “2035”一词指的是由 Ray Kurzweil 普及的技术奇点概念，预测了一个机器智能达到或超越人类认知极限的未来。目前，软件开发仍主要依靠人类工程师手动编写代码。LLM 编排是管理和协调大语言模型（LLM）以充当自主代理的技术过程，这些代理能够规划并执行复杂的多步骤编码任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technological_singularity">Technological singularity - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/llm-orchestration">What is LLM orchestration? - IBM</a></li>
<li><a href="https://theaiagentindex.com/resources/guides/ai-coding-agents-vs-traditional-ides">AI Coding Agents vs Traditional IDEs: When to Use Each (2026)</a></li>

</ul>
</details>

**社区讨论**: 讨论中展现了兴奋与怀疑的交织，开发者们分享了通过提示 AI 而非手写代码来构建操作系统内核等复杂软件的个人经历。虽然有些人高度赞扬开创这些方法的“软件英雄”，但其他人仍持保留态度，将其与早期 Mozilla 宣称 JavaScript 将取代原生操作系统的观点相提并论。对于必须适应这种新的、代理驱动的开发环境的工程师而言，还存在显著的情感色彩。

**标签**: `#AI Coding Agents`, `#Hacker News`, `#Software Engineering`, `#LLM Orchestration`, `#Operating Systems`

---

<a id="item-6"></a>
## [Cloudflare hides shortcomings of the underlying infrastructure](https://charlie.fish/posts/2026/11/what-cloudflare-doesnt-tell-you/) ⭐️ 8.0/10

A technical analysis exposing the hidden infrastructure shortcomings and configuration complexities of Cloudflare's CDN service, supplemented by a high-quality community debate on security and reliability trade-offs.

hackernews · fishcharlie · 11月24日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=50632883)

**标签**: `#Cloudflare`, `#Network Security`, `#CDN`, `#DevOps`, `#TLS`

---

<a id="item-7"></a>
## [Moores Lab AI’s Benchmark Push: Measuring Whether AI Can Actually Verify Chips](https://semiwiki.com/eda/moores-lab-ai/375754-moores-lab-ais-benchmark-push-measuring-whether-ai-can-actually-verify-chips/) ⭐️ 8.0/10

Moores Lab AI launches a benchmark initiative focused on evaluating the ability of AI systems to verify the correctness of chip designs, shifting the focus from code generation speed to functional accuracy.

rss · SemiWiki · 11月24日 18:00

**标签**: `#AI`, `#Semiconductors`, `#EDA`, `#Verification`, `#Hardware`

---

<a id="item-8"></a>
## [西门子收购 Breker 对下一代 AI 芯片的重要性](https://semiwiki.com/eda/376542-why-siemens-breker-deal-matters-for-the-next-generation-of-ai-chips/) ⭐️ 8.0/10

西门子收购 Breker 旨在解决系统级集成和电源状态 bug，这些问题会导致下一代 AI 芯片即使在单个组件通过标准测试的情况下也无法可靠运行。

rss · SemiWiki · 11月24日 16:00

**标签**: `#Semiconductors`, `#AI Hardware`, `#Chip Verification`, `#Siemens`, `#EDA`

---

<a id="item-9"></a>
## [JEDEC 发布 JESD209-6：LPDDR6 标准更新以支持 AI 与移动设备](https://www.electronicsweekly.com/news/products/memory/jedec-updates-lpddr6-to-address-mobile-and-ai-memory-performance-2026-11/) ⭐️ 8.0/10

固态技术协会 JEDEC 发布了 JESD209-6 标准，这是低功耗双倍数据速率 6（LPDDR6）规范的最新修订版。此次更新专门旨在解决并提升移动设备和 AI 工作负载的内存性能。 该标准定义了下一代内存性能指标，对于设计移动和边缘 AI 硬件的工程师和架构师至关重要。它使未来设备能够在保持电池供电平台所需的能效的同时，处理高强度的 AI 任务。 新标准编号为 JESD209-6，代表 LPDDR6 规范的重大更新。内容未提供具体的带宽或延迟改进数值，但强调了对 AI 特定性能指标的关注。

rss · Electronics Weekly · 11月24日 15:56

**背景**: JEDEC 是制定各种内存（包括 DRAM 和 NAND）规格的全球标准化组织。LPDDR（低功耗 DDR）是一类旨在降低移动和便携式电子产品功耗的内存。随着 AI 工作负载向移动设备迁移，需要新的内存标准以支持更高的数据吞吐量，同时避免过高的功耗。

**标签**: `#LPDDR6`, `#JEDEC`, `#Memory Standards`, `#AI Hardware`, `#Mobile Technology`

---

<a id="item-10"></a>
## [OpenAI 员工被发现在会议室内安装窃听器](https://www.tomshardware.com/tech-industry/artificial-intelligence/saudi-openai-eavesdropper-who-bugged-company-office-had-hundreds-of-private-recordings-was-in-frequent-communication-with-saudi-government-perp-had-dozens-of-recordings-of-discussions-of-trade-secrets) ⭐️ 7.5/10

检察官在 OpenAI 的一间会议室内发现了一个由沙特籍员工安装的秘密窃听器。该设备录下了数百次包含公司商业机密的私人对话，并将这些内容共享给沙特政府。 此事件代表了一次严重的外国政府赞助的间谍活动泄露，使关键的 AI 知识产权面临风险。这凸显了高价值科技公司在面对外国实体针对性企业间谍活动时日益增大的脆弱性。 该员工在拥有数十份敏感讨论录音的同时，还与沙特政府保持着频繁的沟通。该秘密设备被专门放置在会议室内，以监控公司内部通讯。

rss · Tom's Hardware · 11月24日 16:30

**背景**: 在竞争激烈的 AI 行业中，企业间谍活动是一个主要问题，因为竞争对手试图窃取专有的算法和战略规划。虽然大多数企业安全重点在于数字防火墙，但对办公空间和会议室的物理访问仍然是敏感信息的关键漏洞。OpenAI 作为领先的人工智能开发者，是寻求提升自身国家 AI 能力的政府行为者的主要目标。

**标签**: `#AI Security`, `#Espionage`, `#OpenAI`, `#Data Breach`

---

<a id="item-11"></a>
## [Songe：开源本地 LLM 做梦与微调引擎](https://github.com/sous-labs/songe) ⭐️ 7.0/10

Sous Labs 发布了名为 Songe 的开源工具，该工具利用机器的空闲周期对本地大语言模型进行迭代训练。它通过“做梦”过程重放经过用户修正的交互来改进模型表现。 通过利用现有硬件，该项目为个人开发者持续改进模型降低了门槛，无需依赖专门的数据中心。这与端侧 AI 和资源可持续利用的行业趋势相契合。 在训练之前，Songe 会测量设备可用的学习容量，以确保模型能够装入内存。该系统仅在新模型版本成功通过验证检查时才会应用更新。

hackernews · bluepeter · 11月24日 15:03 · [社区讨论](https://news.ycombinator.com/item?id=50629231)

**背景**: 本地大语言模型通常运行在资源有限的消费级硬件上，使得在没有高性能 GPU 的情况下进行传统微调变得困难。人工智能研究中诸如“睡眠”或“做梦”阶段的概念提出，模型可以在非活动期间巩固新数据并纠正错误，这类似于生物大脑处理记忆的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sous-labs/songe">GitHub - sous-labs/ songe : A training engine for your local model...</a></li>
<li><a href="https://souslabs.ai/songe">About Songe · Sous Labs</a></li>

</ul>
</details>

**社区讨论**: 社区对其实用性表现出浓厚兴趣，用户询问每个 Epoch 的具体量化改进以及低端机器的硬件要求。关于创建类似 SETI@home 的分布式计算网络以利用集体闲置资源的讨论也引起了广泛关注。

**标签**: `#local-llm`, `#fine-tuning`, `#open-source`, `#distributed-computing`, `#python`

---

<a id="item-12"></a>
## [Quad9 因强制屏蔽令撤出法国 DNS 服务](https://quad9.net/news/blog/quad9-service-deactivation-in-france/) ⭐️ 7.0/10

非营利 DNS 服务商 Quad9 于 2026 年 11 月 24 日关闭了其在法国的公共解析服务，以拒绝执行屏蔽特定域名的法律命令。 该事件突显了法律审查指令与公共 DNS 基础设施完整性之间的冲突，为欧盟的数字主权与用户隐私敲响了警钟。 用户可以通过 DiG 验证该服务拒绝，其返回“REFUSED”状态，并包含一个表明因法国法律限制导致服务禁止的扩展 DNS 错误（EDE）代码。

hackernews · farrokhi · 11月24日 08:33 · [社区讨论](https://news.ycombinator.com/item?id=50625384)

**背景**: Quad9 是一家全球性的非营利 DNS 解析服务商，为个人、企业和政府提供免费的可靠 DNS 服务。此次撤出的法律命令由法国法院发布，旨在打击未授权体育转播和盗版行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/quad9-withdrawal-from-france/">Quad9’s withdrawal from France: A canary in the coal mine</a></li>
<li><a href="https://cyberinsider.com/quad9-to-leave-france/">Quad9 to leave France after court orders piracy-related DNS ...</a></li>
<li><a href="https://techstackups.com/articles/quad9-leaves-france-dns-blocking/">Quad9 Is Leaving France: Why DNS Resolvers Are the Wrong ...</a></li>

</ul>
</details>

**社区讨论**: 社区立即开始共享开源 DNS 代理配置，通过缓存和转发请求来绕过本地封锁，支持 DoH、DoT 及 IPv4/IPv6。此外，用户分享了 DiG 技术输出以确认拒绝代码，并指出该限制还影响了部分德国服务器。

**标签**: `#DNS`, `#Privacy`, `#Infrastructure`, `#Legal`, `#Networking`

---

<a id="item-13"></a>
## [Acorn 与 UCLouvain 推进 FDSOI 和 RF-SOI 埋入式应力源技术](https://www.electronicsweekly.com/news/business/research-boost-for-fdsoi-and-rf-soi-2026-11/) ⭐️ 7.0/10

Acorn Technologies 和 UCLouvain 的研究人员展示了 FDSOI 和 RF-SOI 半导体平台埋入式应力源技术的进展。此次合作成功将该特定技术应用于硅基绝缘体（SOI）工艺以提升其性能。 在这些平台上推进埋入式应力源技术，能够实现复杂器件的集成，并提高性能、降低功耗。这在射频前端集成领域尤为重要，RF-SOI 在消费电子和电信领域有广泛应用。 该研究涉及总部位于圣地亚哥附近 La Jolla 的半导体 IP 公司 Acorn Technologies 以及 UCLouvain 大学的 Jean-Pierre Raskin 教授。所开发的特定技术被称为 Acorn Buried Stressor。

rss · Electronics Weekly · 11月24日 06:12

**背景**: FDSOI（全耗尽绝缘体硅）和 RF-SOI（射频绝缘体硅）是先进的半导体制造技术，其薄硅层位于绝缘层之上，区别于标准体硅 CMOS。埋入式应力源技术涉及对地下层进行工程化以管理应力，从而优化器件特性并实现专业组件的更好集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gf.com/technologies/cmos/fdx-fd-soi/">FDX™ FD-SOI technology | GlobalFoundries</a></li>
<li><a href="https://www.everythingrf.com/community/what-is-rf-soi">What is RF SOI? - everything RF RF-SOI technology | GlobalFoundries RF-SOI - STMicroelectronics The Ultimate Guide to RF-SOI - AnySilicon SOI in Integrated Circuits — CMOS, RF, MEMS & Photonics SOI Wafers Explained: Pros, Cons, and Applications</a></li>

</ul>
</details>

**标签**: `#Semiconductor`, `#FDSOI`, `#RF-SOI`, `#Research`, `#IP`

---

<a id="item-14"></a>
## [美国司法部在全球反诈骗行动中没收 170 亿美元及 1.4 万台设备](https://www.tomshardware.com/tech-industry/cyber-security/us-doj-touts-largest-ever-crackdown-on-scammers-across-the-globe-as-it-seizes-14-000-devices-and-usd17-billion-in-illicit-funds-operation-results-in-800-defendants-and-frees-2-200-forced-laborers) ⭐️ 6.5/10

美国司法部宣布，其史上最大规模的反诈骗行动已扣押 14,000 台设备和 170 亿美元的非法资金，共起诉 800 余名被告，并解救 2,200 名被强迫劳工。此次行动已挽回 80 亿美元的预计受害者损失。 此次行动展示了美国政府加强打击跨国有金融诈骗的坚定决心，以应对困扰全球数字经济的欺诈问题。被没收资产的巨大规模凸显了网络欺诈对国际受害者和金融体系构成的严重威胁。 此次打击行动的显著成果包括挽回了 80 亿美元的预计受害者损失，并解救 2,200 名可能受非法网络剥削的强迫劳工。

rss · Tom's Hardware · 11月24日 22:30

**背景**: 全球网络诈骗活动的激增已成为重大关切，这类活动往往涉及跨越多国司法管辖区的复杂金融犯罪和人口贩运网络。美国司法部通过协调此类行动，以破坏这些跨境犯罪活动并追回被盗资产，从而减轻对全球受害者的伤害。

**标签**: `#Cybersecurity`, `#Law-Enforcement`, `#Anti-Fraud`, `#Policy`

---

<a id="item-15"></a>
## [Frontier AI employees alarmed that unseen Open AI and Anthropic models are too powerful to release, report claims](https://www.tomshardware.com/tech-industry/artificial-intelligence/frontier-ai-employees-alarmed-that-unseen-open-ai-and-anthropic-models-are-too-powerful-to-release-report-claims-worry-spreads-that-executives-are-out-of-touch-with-severity-of-risks-will-choose-profit-over-safety) ⭐️ 6.5/10

Reports suggest that employees at OpenAI and Anthropic are concerned that unreleased frontier models are too powerful and pose significant risks if released without adequate safety controls, with executives prioritizing profit.

rss · Tom's Hardware · 11月24日 21:00

**标签**: `#AI Safety`, `#OpenAI`, `#Anthropic`, `#Tech Industry`, `#Model Risks`

---

<a id="item-16"></a>
## [Reinstated Nvidia CEO Jensen Huang must still face China congressional and Senate Banking committees](https://www.tomshardware.com/tech-industry/policy/reinstated-nvidia-ceo-jensen-huang-must-still-face-china-congressional-and-senate-banking-committees-senators-and-representatives-demand-answers-from-nvidia-ceo-on-national-security-threats-and-export-controls) ⭐️ 6.5/10

Nvidia CEO Jensen Huang is scheduled to testify before US congressional committees on December 1 and 3 regarding national security concerns and export control enforcement in China.

rss · Tom's Hardware · 11月24日 16:00

**标签**: `#Nvidia`, `#Geopolitics`, `#Export Controls`, `#AI Industry`, `#Semiconductors`

---

<a id="item-17"></a>
## [Trump pressured Nvidia to bring Jensen back, called into board meeting to push reinstatement, reports claim](https://www.tomshardware.com/tech-industry/policy/trump-pressured-nvidia-to-bring-jensen-back-called-into-board-meeting-to-push-reinstatement-reports-claim-president-concerned-over-falling-stock-prices-with-huangs-return-reversing-slide) ⭐️ 6.5/10

Reports indicate that President Donald Trump allegedly intervened in Nvidia's corporate governance by pressuring the board to reinstate Jensen Huang to stabilize the company's falling stock prices.

rss · Tom's Hardware · 11月24日 13:45

**标签**: `#Nvidia`, `#Jensen Huang`, `#US Politics`, `#Market Regulation`, `#Tech Industry`

---

<a id="item-18"></a>
## [车网互动技术面临重大实际与技术障碍](https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream-part-2/) ⭐️ 6.0/10

本文探讨了阻碍车网互动系统普及的技术和实际挑战。文中强调了关于电池老化、电网基础设施、充电接入和用户便利性的担忧。 解决这些关键障碍对于智能电网整合和可再生能源管理的未来至关重要。该分析对评估双向充电技术商业可行性的汽车制造商和能源提供商具有重要意义。 分析特别指出，电池健康度衰减和缺乏健壮的电网基础设施是主要的技术瓶颈。此外，所需设备涉及的经济成本以及电动汽车驾驶员面临的实际不便也是采用过程中的主要障碍。

rss · EE Times · 11月24日 11:53

**背景**: 车网互动（V2G）技术允许电动汽车将多余电力回馈到电网，从而作为移动储能设备发挥作用。虽然它可以帮助稳定电网并整合可再生能源，但目前需要专用的双向充电基础设施，而这在当下非常罕见。

**标签**: `#Vehicle-to-Grid`, `#Energy Systems`, `#Battery Technology`, `#Smart Grid`, `#Automotive Electronics`

---

<a id="item-19"></a>
## [车辆向电网输电：绝佳创意还是不切实际的幻想？](https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream/) ⭐️ 6.0/10

本文批判性地审视了车网互动技术的潜力，指出尽管其技术前景广阔，但用户行为和“人为因素”可能会限制其实际效果。

rss · EE Times · 11月24日 08:40

**标签**: `#Vehicle-to-Grid`, `#Energy Systems`, `#Infrastructure`, `#Sustainability`, `#Power Electronics`

---

<a id="item-20"></a>
## [AMD AGESA 1.3.0.1f 补丁将 Ryzen 8000 最大核心电压限制为 1.4V](https://www.techpowerup.com/355153/amd-agesa-1-3-0-1f-patch-arrives-to-limit-max-vcore-on-ryzen-8000-series) ⭐️ 5.5/10

AMD 已发布 AGESA 1.3.0.1f 补丁 A，为特定型号的 Ryzen 8000 系列桌面 APU 引入了 1.4V 的最大核心电压限制。华硕（ASUS）和微星（MSI）等主板厂商正在分发相应的 BIOS 更新，以实施该限制并改善内存训练的可视性。 此更新对使用 Ryzen 8000 系列 APU 的系统稳定性至关重要，因为将电压限制在 1.4V 有助于防止因功耗过大导致的硬件老化和系统不稳定。它确保了 AM5 平台上这些特定处理器用户系统的长期可靠性。 该补丁还增加了额外的 POST 代码，以增强对内存训练过程的可视性，使用户能更好地区分正常初始化和无响应状态。电压限制专门适用于特定型号的 Ryzen 8000 系列桌面 APU，高于此上限的手动超频可能会受到影响或受到限制。

rss · TechPowerUp News · 11月24日 13:31

**背景**: AGESA（AMD 通用封装软件架构）是主板制造商用于执行 AMD 处理器平台初始化的过程库。它充当 CPU 固件与主板 BIOS 之间的桥梁，管理硬件组件在启动过程中的初始化与调控。Ryzen 8000 系列指的是 AMD 最近一代将 CPU 和 GPU 集成在单一封装内的 APU 产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AGESA">AGESA - Wikipedia</a></li>
<li><a href="https://www.techpowerup.com/355153/amd-agesa-1-3-0-1f-patch-arrives-to-limit-max-vcore-on-ryzen-8000-series">AMD AGESA 1.3.0.1f Patch Arrives to Limit Max vCore on Ryzen ...</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Ryzen 8000`, `#BIOS`, `#AGESA`, `#Hardware`

---