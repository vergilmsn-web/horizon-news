---
layout: default
title: "Horizon Summary: 2026-07-07 (ZH)"
date: 2026-07-07
lang: zh
---

> 从 105 条内容中筛选出 20 条重要资讯。

---

1. [英特尔 Nova Lake 将 AVX-512 带回混合核心架构](#item-1) ⭐️ 8.5/10
2. [因 PCB 问题，英伟达 Kyber NVL144 机架推迟至 2028 年发布](#item-2) ⭐️ 8.5/10
3. [华为携昇腾 950 芯片进军韩国 AI 市场](#item-3) ⭐️ 8.5/10
4. [GLM 5.2 凸显 AI 利润率的即将崩溃](#item-4) ⭐️ 8.0/10
5. [小型 AI 模型在不可靠网络环境中日益普及](#item-5) ⭐️ 8.0/10
6. [Anthropic 提出用于大语言模型可解释性的全局工作区框架](#item-6) ⭐️ 8.0/10
7. [在原始硬件限制下于雅达利 Jaguar 运行 Linux](#item-7) ⭐️ 8.0/10
8. [AI 需求推动 MLCC 订单出货比创纪录，警告 2026 年可能出现短缺](#item-8) ⭐️ 8.0/10
9. [加密货币矿工如何转型成为 AI 繁荣的基础设施](#item-9) ⭐️ 8.0/10
10. [Orbital Compute 提议部署十万颗卫星星座以提供 10GW 算力](#item-10) ⭐️ 8.0/10
11. [Linux 7.3 内核增加对更多 Intel Nova Lake-S 桌面 GPU 的支持](#item-11) ⭐️ 7.5/10
12. [美光在广岛启动 93 亿美元 HBM 工厂扩建项目](#item-12) ⭐️ 7.5/10
13. [Xbox 裁员 3200 人启动重大重组计划](#item-13) ⭐️ 7.5/10
14. [英特尔专利曝光 XBM 内存架构，旨在取代昂贵的 HBM 硅中介层](#item-14) ⭐️ 7.5/10
15. [三星芯片部门 2026 年利润超越过去 40 年总和](#item-15) ⭐️ 7.5/10
16. [AMD Ryzen AI Halo 评测：本地 AI 盒子性能落后于英伟达 GB10](#item-16) ⭐️ 7.5/10
17. [开源应用将索尼耳机变为 PC 头部追踪器](#item-17) ⭐️ 7.5/10
18. [美国 AI 芯片供应链缺口：Blackwell 封装仍依赖海外](#item-18) ⭐️ 7.5/10
19. [字节 Seedance 2.0：2000 亿参数规模化确立 AI 视频领先地位](#item-19) ⭐️ 7.3/10
20. [OpenClaw 超越 React 登顶 GitHub，AI Agent 时代来临](#item-20) ⭐️ 7.3/10

---

<a id="item-1"></a>
## [英特尔 Nova Lake 将 AVX-512 带回混合核心架构](https://www.techpowerup.com/350572/intel-nova-lake-to-feature-avx-512-on-both-p-cores-and-e-cores) ⭐️ 8.5/10

英特尔即将推出的 Nova Lake 处理器将正式在 Coyote Cove 性能核和 Arctic Wolf 能效核上重新引入 AVX-512 支持。这一决定确保了混合架构中所有核心类型的指令集架构（ISA）一致性。 这一改变解决了因不同核心类型之间 ISA 不匹配而导致的线程迁移运行时错误问题。它还使英特尔的客户端产品线能够更好地处理高级 AI 推理工作负载，与 AMD 的 Zen 4 和 Zen 5 架构展开竞争。 此次重新引入通过实施针对客户端的 AVX-512 指令集，解决了第 11 代 Rocket Lake 时代的过热担忧。与之前能效核缺乏支持的世代不同，现在两种核心类型都将共享相同的 ISA 功能。

rss · TechPowerUp News · 7月7日 08:30

**背景**: Intel's hybrid architecture combines Performance-cores (P-cores) for heavy tasks and Efficient-cores (E-cores) for background processes. Thread migration allows the operating system to move running threads between these different core types to optimize performance and power efficiency. However, if the cores support different Instruction Sets, migrating a thread executing specialized instructions can lead to crashes or errors.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/350572/intel-nova-lake-to-feature-avx-512-on-both-p-cores-and-e-cores">Intel "Nova Lake" to Feature AVX-512 on Both P-cores and E ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nova_Lake_(microprocessor)">Nova Lake (microprocessor) - Wikipedia</a></li>
<li><a href="https://wccftech.com/intel-nova-lake-coyote-cove-p-core-arctic-wolf-e-core-diamond-rapids-panther-cove/">Intel Confirms Coyote Cove P - Core & Arctic Wolf E - Core For Nova...</a></li>

</ul>
</details>

**标签**: `#Intel`, `#Hardware`, `#AVX-512`, `#CPU Architecture`, `#Nova Lake`

---

<a id="item-2"></a>
## [因 PCB 问题，英伟达 Kyber NVL144 机架推迟至 2028 年发布](https://www.tomshardware.com/pc-components/gpus/nvidias-kyber-rack-for-rubin-ultra-slips-to-2028) ⭐️ 8.5/10

英伟达为 Rubin Ultra 架构设计的 Kyber NVL144 机架已推迟至 2028 年发布，比原计划晚了超过 12 个月。此次延期是由于专用 PCB 中板制造困难以及客户对初步替代方案的强烈反对所致。 这一延迟打破了英伟达激进的年度发布节奏，并影响了下一代 AI 超级计算基础设施的时间表。它表明高速 PCB 制造可能存在瓶颈，这可能波及更广泛的 AI 硬件生态系统。 主要的技术障碍涉及 Rubin Ultra 平台所需的高速 PCB 中板的信号完整性挑战。此外，Rubin Ultra 预计将配备 16 层 HBM4E 内存，这进一步增加了设计复杂性。

rss · Tom's Hardware · 7月6日 13:33

**背景**: Kyber NVL144 是一个大型 AI 机架系统，旨在容纳多个 Rubin Ultra GPU，以为高级 AI 训练提供巨大的计算能力。PCB 中板是关键的互连组件，用于在卡之间促进高速数据传输，随着速度提升，保持信号完整性变得越来越困难。Rubin Ultra 代表英伟达的下一个主要 GPU 架构，接替 Blackwell 系列，旨在推动下一波 AI 基础设施升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/06/nvidia-kyber-rack-system-delays-manufacturing-taiwan-rubin-chips-.html">Nvidia's Kyber rack system delayed to 2028 over manufacturing ...</a></li>
<li><a href="https://letsdatascience.com/news/nvidia-delays-kyber-nvl144-rack-system-to-2028-acf20053">Nvidia Delays Kyber NVL144 Rack System to 2028</a></li>
<li><a href="https://www.nextplatform.com/compute/2025/03/19/nvidia-draws-gpu-system-roadmap-out-to-2028/1653528">Nvidia Draws GPU System Roadmap Out To 2028</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Hardware`, `#AI Infrastructure`, `#Rubin Architecture`, `#Supply Chain`

---

<a id="item-3"></a>
## [华为携昇腾 950 芯片进军韩国 AI 市场](https://www.tomshardware.com/tech-industry/semiconductors/chinas-huawei-to-enter-south-korean-ai-chip-market-with-new-atlas-superpods-clusters-pack-8-192-ascend-950-accelerators-per-deployment-reportedly-challenges-nvidia-dominance-with-tripled-inference-performance-of-h20-at-one-quarter-the-cost) ⭐️ 8.5/10

华为正计划使用其昇腾 950 芯片和 Atlas 950 超级集群进入韩国 AI 加速器市场，每个部署包含 8,192 个加速器。该公司声称，与英伟达 H20 相比，这些集群的推理性能提高了三倍，而成本仅为四分之一。 此举对英伟达在全球 AI 基础设施市场的主导地位构成了重大挑战，尤其是在华为将其生态系统扩展至中国之外时。它为寻求高性价比和高性能 AI 解决方案的韩国企业引入了一个有力的竞争替代方案。 昇腾 950 系列针对推理的解码阶段和模型训练进行了优化，采用定制硅片并配备华为首款自研 HBM 内存。Atlas 950 超级集群在 FP8 下可提供高达 8 EFLOPS 的性能，在 FP4 下可达 16 EFLOPS，互连带宽为 16 PB/s。

rss · Tom's Hardware · 7月6日 12:31

**背景**: 昇腾 950 是一种专有 AI 加速器架构，旨在直接与英伟达 H20 和 H100 等 GPU 竞争。华为的 Atlas 超级集群架构允许数千个芯片作为单个逻辑计算机运行，以满足大规模 AI 部署中的可扩展性需求。该技术依赖于华为的 CANN 软件层来促进模型执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.huawei.com/en/news/2025/9/hc-superpod-innovation">Huawei Launches Open-Access SuperPoD Architecture for... - Huawei</a></li>
<li><a href="https://www.artificialintelligence-news.com/news/huawei-ai-chips-superpod-technology/">Inside Huawei 's plan to make thousands of AI chips think like one...</a></li>
<li><a href="https://www.techradar.com/pro/huawei-ascend-950-vs-nvidia-h200-vs-amd-mi300-instinct-how-do-they-compare">Huawei’s Ascend 950 goes head-to-head with Nvidia ’s H200 and...</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#Huawei`, `#Semiconductors`, `#Market Competition`, `#South Korea`

---

<a id="item-4"></a>
## [GLM 5.2 凸显 AI 利润率的即将崩溃](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/) ⭐️ 8.0/10

文章分析了 GLM 5.2 的竞争力和低成本如何预示着 AI 利润率的潜在崩溃。它指出，计算成本的下降可能不会导致消费者价格降低，而是加剧大型云服务商的市场主导地位。 这一分析挑战了技术成本降低必然使消费者受益的假设。它揭示了在高固定成本和网络效应作用下，即使技术趋于商品化，现有巨头仍能维持高利润的经济动态。 GLM 5.2 是一个开源权重模型，在代码基准测试中与 GPT-5.5 等专有模型相媲美，但定价显著更低。讨论指出，尽管存在这些成本效率，谷歌和微软等公司仍继续享受类似历史软件垄断的高利润率。

hackernews · martinald · 7月6日 20:14 · [社区讨论](https://news.ycombinator.com/item?id=48809877)

**背景**: 在 AI 行业中，训练大语言模型涉及巨大的前期基础设施投资，导致高昂的固定成本但每次推理的边际成本极低。这种经济结构产生了强烈的规模激励，往往导致赢家通吃的市场，主导企业利用其规模优势维持高利润率，而不管底层计算效率如何提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mindstudio.ai/blog/what-is-glm-5-2-open-weight-model">What Is GLM 5.2? The Open-Weight Model Beating GPT 5.5 on Design Benchmarks | MindStudio</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM-5.2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>

</ul>
</details>

**社区讨论**: 社区成员争论低计算成本是否会转化为更低的价格，一些人以 GSuite 和 Office 为例，指出免费替代品未能破坏主导企业的利润率。另一些人则认为，低边际成本结构迫使实验室积极扩大用户群以覆盖固定成本，从而可能通过竞争压低价格。

**标签**: `#AI Economics`, `#Market Analysis`, `#LLMs`, `#Business Strategy`

---

<a id="item-5"></a>
## [小型 AI 模型在不可靠网络环境中日益普及](https://spectrum.ieee.org/small-language-models-ai-pharmaceuticals) ⭐️ 8.0/10

小型语言模型（SLM）正越来越多地被部署在网络连接不稳定或不可用的边缘计算场景中。这种转变凸显了人们越来越倾向于使用本地化、资源高效的 AI 解决方案，而非依赖云端的大型模型。 这一趋势对需要实时处理和高可靠性的行业（如医疗和紧急服务）产生了重大影响，因为它降低了延迟和对互联网基础设施的依赖。它标志着 AI 架构向专业化、去中心化智能的战略转变。 与大型语言模型相比，小型语言模型提供更快的处理速度和更低的计算成本，使其成为硬件资源有限设备的理想选择。然而，它们可能缺乏大型模型那样的广泛上下文理解和复杂推理能力。

hackernews · sscaryterry · 7月6日 23:59 · [社区讨论](https://news.ycombinator.com/item?id=48812055)

**背景**: Edge computing involves performing data processing near the source of data generation rather than relying on centralized cloud servers. Small Language Models are a subset of AI models designed to run efficiently on local devices like smartphones, IoT sensors, or embedded systems, often utilizing techniques like quantization and pruning to reduce size.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/11/11/explore-ai-models-key-differences-between-small-language-models-and-large-language-models/">Explore AI models: Key differences between small language ...</a></li>
<li><a href="https://asktodo.ai/blog/edge-ai-inference-optimization">Edge AI and Inference Optimization: Running Powerful ...</a></li>

</ul>
</details>

**社区讨论**: 社区预计未来将出现由通用层协调的超专用微型模型，这与通过扩大规模实现 AGI 的路径不同。用户还表达了对应急物资包等实际应用的兴趣，并讨论了在没有本地计算资源的情况下训练小型语言模型的挑战。

**标签**: `#Small Language Models`, `#Edge Computing`, `#AI Trends`, `#Hacker News`

---

<a id="item-6"></a>
## [Anthropic 提出用于大语言模型可解释性的全局工作区框架](https://www.anthropic.com/research/global-workspace) ⭐️ 8.0/10

Anthropic 发布了引入“全局工作区”框架的研究，旨在分析大型语言模型中的共享推理空间。该研究确定了特定的功能属性，并证明阻止模型访问此“J 空间”会导致其丧失高阶认知功能，同时保留基本的交互能力。 这项研究为理解大语言模型如何处理信息提供了新的视角，弥合了神经网络内部机制与认知科学理论之间的差距。它通过提供识别和操作复杂模型中特定推理路径的具体方法，极大地推进了人工智能可解释性领域的发展。 研究人员根据特定层中微小扰动对最终逻辑输出变化的影响程度来定义“J 空间”，这类似于信息几何的概念。实验表明，虽然模型仍能进行交互，但阻断该工作区会专门损害其执行复杂多步推理任务的能力。

hackernews · in-silico · 7月6日 17:44 · [社区讨论](https://news.ycombinator.com/item?id=48808002)

**背景**: 神经科学中的全局工作区理论认为，当信息被广播到各个脑模块均可访问的中心工作区时，意识觉知便会产生。在人工智能领域，研究人员越来越倾向于在深度学习模型中寻找类似的结构，以解释涌现行为并提高模型的透明度。可解释性研究旨在通过将内部激活映射到特定的逻辑操作，来解码神经网络的“黑盒”性质。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/global-workspace">A global workspace in language models \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (AI) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员就“意识”一词的使用是否恰当展开了辩论，有人认为这仅仅揭示了抽象的推理子空间，而非真正的觉知。另一些人则提到了通过复制层来提升数学能力的类似技术，表明人们对手动操纵特定模型权重以增强功能有着浓厚的兴趣。

**标签**: `#AI Research`, `#LLM Interpretability`, `#Anthropic`, `#Machine Learning`, `#Cognitive Science`

---

<a id="item-7"></a>
## [在原始硬件限制下于雅达利 Jaguar 运行 Linux](https://cakehonolulu.github.io/linux-for-jaguar/) ⭐️ 8.0/10

一名开发者成功将 Linux 移植到雅达利 Jaguar 上，在无需专用硬件的情况下，仅利用主机原始的 2MB 内存限制便实现了 Busybox Shell。该项目涉及针对摩托罗拉 68000 架构的特定内核补丁，并因现有代码质量获得了内核维护者的验证与认可。 该实现完全在原始硬件上运行，无需任何闪存卡或外部辅助工具，严格遵守 2MB 内存限制。该端口包含了针对 68k CPU 的必要内核修改，并引发了关于内核时间基础设施潜在性能优化的讨论。

hackernews · cakehonolulu · 7月6日 18:35 · [社区讨论](https://news.ycombinator.com/item?id=48808663)

**背景**: 雅达利 Jaguar 于 20 世纪 90 年代中期发布，采用复杂的多芯片架构，其中包括主要用于 I/O 任务的摩托罗拉 68000 处理器。虽然由于开发困难导致该主机商业上失败，但 68000 芯片曾驱动过许多标志性系统，如 Commodore Amiga 和世嘉 Genesis。Linux 对 m68k 架构的支持已存在数十年，但通常需要对非标准或遗留配置进行大量修补。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Atari_Jaguar">Atari Jaguar - Wikipedia</a></li>
<li><a href="https://forum.beyond3d.com/threads/atari-jaguar-architecture-discussion.58306/">Atari Jaguar architecture discussion | Beyond3D Forum</a></li>
<li><a href="https://www.linuxjournal.com/article/2090">Linux/m68k: Linux on Motorola's 68000 Processor | Linux Journal</a></li>

</ul>
</details>

**社区讨论**: 社区成员对这一努力表示惊叹，指出 Linux 内核中对 68000 的支持此前被认为被忽视或存在细微缺陷。一些用户讨论了该芯片在各种平台上的历史意义，而另一些人则欣赏这一技术壮举，尽管他们更倾向于将主机用于游戏。

**标签**: `#Linux`, `#Embedded Systems`, `#Retro Computing`, `#Kernel Development`, `#68000`

---

<a id="item-8"></a>
## [AI 需求推动 MLCC 订单出货比创纪录，警告 2026 年可能出现短缺](https://www.dramexchange.com/WeeklyResearch/Post/2/12759.html) ⭐️ 8.0/10

集邦咨询报告称，激增的 AI 服务器需求和定制 ASIC 的增长已将日本和韩国 MLCC 供应商的订单出货比推至疫情后高位。这种对高端 MLCC 需求的集中表明，2026 年下半年可能出现结构性短缺。 这一趋势凸显了 AI 基础设施供应链中的关键瓶颈，组件短缺可能会延迟服务器部署。它强调了在 AI 硬件军备竞赛中，村田等无源元件制造商日益增强的议价能力。 短缺风险源于对特定高端 MLCC 规格的集中需求，加上云服务提供商（CSP）定制 ASIC 频繁的设计变更，进一步加剧了这一情况。村田等主要供应商表示，目前高端 AI 服务器 MLCC 的订单量已超过其产能的两倍。

rss · DRAMeXchange (TrendForce) · 7月6日 14:00

**背景**: MLCC（多层陶瓷电容器）是几乎所有电子设备中用于稳定电压和过滤噪声的关键无源元件。订单出货比是供应链中的一个关键指标，当该比率高于 1.0 时，表明新订单超过出货量，通常会导致未来的供应紧张。云服务提供商（CSP）正越来越多地开发定制专用集成电路（ASIC），以优化 AI 训练效率，这需要专门的高端电容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://passive-components.eu/trendforce-csp-in-house-ai-asic-boom-reshapes-high-end-mlcc-demand/">TrendForce: CSP AI ASICs and looming high ‑ end MLCC shortage</a></li>
<li><a href="https://cosolvic.com/blog/murata-mlcc-price-increase-2026-ai-server-impact/">Murata’s 15–35% MLCC Price Hike: What AI Server Demand Means...</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Supply Chain`, `#Electronics Components`, `#Market Analysis`

---

<a id="item-9"></a>
## [加密货币矿工如何转型成为 AI 繁荣的基础设施](https://semiwiki.com/artificial-intelligence/370845-the-accidental-infrastructure-how-crypto-miners-built-the-foundation-of-the-ai-boom/) ⭐️ 8.0/10

前以太坊矿工 CoreWeave 于 2026 年 6 月 22 日加入纳斯达克 100 指数，距离其首次公开募股仅十五个月，标志着其从加密货币挖矿成功转型为 AI 基础设施提供商。该公司已从小型挖矿业务转变为价值 230 亿美元的 GPU 云提供商，服务于主要的 AI 工作负载。 这一转变凸显了加密货币挖矿时代剩余的 GPU 基础设施如何成为当前 AI 繁荣的基础硬件。它展示了市场的重大演变，即像 CoreWeave 这样的公司利用现有硬件来满足对 AI 计算能力爆炸性增长的需求。 CoreWeave 通过开创液冷和裸机架构来支持这些高要求的 AI 任务，并利用其早期管理大规模 GPU 矿机的经验。该公司的快速崛起强调了专业云提供商在半导体和 AI 生态系统中的关键作用。

rss · SemiWiki · 7月6日 21:00

**背景**: The transition of Ethereum from proof-of-work to proof-of-stake significantly reduced the demand for GPU mining, leaving many miners with idle infrastructure. CoreWeave, originally founded as Atlantic Crypto, repurposed these GPUs to serve AI developers, filling a critical gap in cloud computing resources for machine learning models.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://introl.com/blog/coreweave-gpu-cloud-ai-infrastructure-deep-dive-2025">CoreWeave Deep Dive | Introl Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>
<li><a href="https://sustainableatlas.org/post/case-study-proof-of-stake-sustainable-consensus-ethereum-merge-network-transition-lessons-1687">Case study: Ethereum's Merge to proof-of-stake — energy ...</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Cryptocurrency Mining`, `#CoreWeave`, `#Semiconductor Industry`, `#Market Trends`

---

<a id="item-10"></a>
## [Orbital Compute 提议部署十万颗卫星星座以提供 10GW 算力](https://www.electronicsweekly.com/news/orbital-compute-gears-up-for-10-gigawatts-of-ai-compute-in-space-2026-07/) ⭐️ 8.0/10

Orbital Compute 已向美国联邦通信委员会（FCC）提交提案，计划部署多达 10 万颗卫星的星座，旨在太空中提供 100 亿瓦（10GW）的 AI 计算能力。 这一举措标志着云计算基础设施向低地球轨道的激进扩展，有望缓解地面为大规模 AI 工作负载提供的能源和土地压力，同时也带来了重大的监管和工程挑战。 该计划涉及配备多个 GPU 节点和高带宽地面链路的专业卫星，旨在利用太空太阳能，尽管在轨道上进行如此高密度的计算需要复杂的散热管理。

rss · Electronics Weekly · 7月6日 15:40

**背景**: 太空数据中心是概念性的设施，利用轨道环境进行计算，通常依赖丰富的太阳能和真空环境的被动冷却。然而，将高功率 AI 硬件移至轨道面临诸多障碍，例如抗辐射加固、维护困难以及相比地面液冷系统所需的高效散热问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://interestingengineering.com/space/us-firm-files-fcc-application-for-100000-satellite-data-center-constellation">US startup proposes 100,000-satellite data center constellation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Space-based_data_center">Space-based data center - Wikipedia</a></li>
<li><a href="https://orbital.inc/">Orbital — Data Centers in Space</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Space Technology`, `#Satellites`, `#Cloud Computing`

---

<a id="item-11"></a>
## [Linux 7.3 内核增加对更多 Intel Nova Lake-S 桌面 GPU 的支持](https://www.techpowerup.com/350563/more-intel-nova-lake-s-desktop-gpus-appear-in-linux-7-3) ⭐️ 7.5/10

针对 Linux 7.3 的内核补丁将 Intel Nova Lake-S 桌面 GPU 的设备 ID 支持扩展至七个，暗示了可能的 SKU 多样性。此外，受保护 Xe 路径（PXP）功能不再需要在内核中加载 HuC 固件，而是将其移至用户空间处理。 这一更新提供了 Intel 即将推出的 Nova Lake-S 系列的具体证据，该系列采用 Xe3 图形架构，旨在提升游戏和 AI 工作负载的性能。PXP 处理的架构变更简化了内核维护，并反映了 Intel 驱动程序栈中的持续优化。 驱动程序更新添加了设备 ID 0xD74A 和 0xD748，同时移除了 0xD744，使受支持的 Nova Lake-S 桌面 GPU 总数达到七个。媒体引擎的改进具体影响了受保护 Xe 路径，从 Media 35 引擎开始，取消了内核空间对 HuC 固件的依赖。

rss · TechPowerUp News · 7月6日 22:37

**背景**: Intel Nova Lake-S 是下一代桌面 CPU 架构，预计将集成 Xe3 图形技术，取代之前的 Lunar Lake 等代际。Xe3 架构在 Xe2 的基础上发展而来，为集成和独立显卡解决方案提供了显著的性能提升和更好的吞吐量优化。HuC 固件传统上用于 Intel GPU 的视频解码和保护内容处理，但其在内核中的集成方式正在演变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linux-7.3-More-Nova-Lake-S-IDs">Linux 7.3 Adding More Graphics PCI IDs For Intel Nova Lake S</a></li>
<li><a href="https://wccftech.com/intel-xe3-graphics-official-50-percent-faster-than-xe2-xe3p-next-gen-arc-family/">Intel Xe3 Graphics Official: Over 50% Faster Than Xe2 ...</a></li>

</ul>
</details>

**标签**: `#Intel`, `#Linux Kernel`, `#Hardware`, `#Nova Lake`, `#Drivers`

---

<a id="item-12"></a>
## [美光在广岛启动 93 亿美元 HBM 工厂扩建项目](https://www.techpowerup.com/350561/micron-breaks-ground-on-usd-9-3-billion-hiroshima-fab-expansion) ⭐️ 7.5/10

美光已在广岛正式启动价值 1.5 万亿日元（约 93 亿美元）的工厂扩建项目，该扩建将专注于为人工智能基础设施生产高带宽内存（HBM）。日本政府为该计划提供高达 5000 亿日元的资助，设备预计将于 2028 年下半年开始安装。 此次扩建对于确保高带宽内存（HBM）的全球供应链至关重要，而 HBM 是高性能计算和数据中心不可或缺的关键组件。由于美光是日本境内唯一的海外 DRAM 制造商，该项目对东京保持半导体产业的韧性具有重要的战略意义。 新工厂所需的大约 80%材料将在日本本地采购，从而增强供应链的稳定性。广岛工厂具有历史意义，因为美光在 2013 年收购尔必达后，正是在这里生产了其首批 HBM 晶圆。

rss · TechPowerUp News · 7月6日 20:26

**背景**: 高带宽内存（HBM）是一种特殊的 DRAM，它通过硅通孔技术垂直堆叠存储芯片，从而实现极高的数据传输速率，使其成为 AI 加速器和 GPU 的理想选择。美光在日本的业务源于其 2013 年对尔必达的收购，尔必达当时是全球最大的 DRAM 生产商之一，此次收购使美光成为日本境内唯一的海外 DRAM 制造商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eenewseurope.com/en/micron-hiroshima-fab-hbm-expansion/">Micron Hiroshima fab starts $9.3bn HBM expansion</a></li>
<li><a href="https://icharles.com/articles/micron-hiroshima-hbm-expansion-groundbreaking">Micron Breaks Ground on $9.3B Hiroshima HBM Plant - iCharles</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Semiconductors`, `#HBM`, `#Supply Chain`, `#Japan`, `#Manufacturing`

---

<a id="item-13"></a>
## [Xbox 裁员 3200 人启动重大重组计划](https://www.techpowerup.com/350549/xbox-to-lay-off-3-200-workers-in-year-long-reset) ⭐️ 7.5/10

微软 Xbox 部门宣布将在 2027 财年裁员 3,200 人，占员工总数的 20%。首席执行官阿莎·夏尔马表示，收入下降和主机销量低迷是此次为期一年的重组策略的主要推动因素。 这一大规模裁员凸显了 Xbox 硬件部门与软件及订阅服务相比所面临的财务困境。重组信号表明战略重心正从传统的硬件主导地位转向更精简、更具成本效益的运营模式。 Compulsion Games 和 Double Fine Productions 等关键工作室将成为独立实体，而 Ninja Theory 和 Undead Labs 则被新所有者收购。管理层级将简化为最多五级，供应商支出目标削减 50%。

rss · TechPowerUp News · 7月6日 16:15

**背景**: Xbox Series X|S 主机于 2020 年底发布，面临索尼 PlayStation 5 的激烈竞争，导致装机量低于预期。为了弥补这一差距，微软大力推广 Game Pass 和多平台发行策略，但其硬件利润率仍远低于竞争对手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xbox_Series_X_and_Series_S">Xbox Series X and Series S - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Xbox_Game_Pass">Xbox Game Pass - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Xbox`, `#Layoffs`, `#Microsoft`, `#Gaming Industry`, `#Corporate Restructuring`

---

<a id="item-14"></a>
## [英特尔专利曝光 XBM 内存架构，旨在取代昂贵的 HBM 硅中介层](https://www.tomshardware.com/tech-industry/semiconductors/intel-patent-reveals-new-xbm-memory-architecture-that-ditches-hbms-costly-silicon-interposer-backend-transistor-dram-stack-uses-ucie-links-and-built-in-repair-to-ease-ais-memory-bottleneck) ⭐️ 7.5/10

英特尔公布了一项关于新型 XBM 内存架构的专利，该架构利用后端晶体管 DRAM 和 UCIe 链接，消除了传统 HBM 堆栈中所需的昂贵硅中介层。 这项创新通过提供比 HBM4 更便宜的替代方案，解决了 AI 硬件中的关键成本和封装瓶颈，可能会重塑下一代处理器中高带宽内存的集成方式。 拟议的设计采用 1T1C 后端 DRAM 单元，其中晶体管位于后端金属层中，通过 UCIe 芯片接口实现 32 GT/s 的速度，并内置修复逻辑。

rss · Tom's Hardware · 7月7日 10:00

**背景**: 高带宽内存（HBM）目前依赖硅中介层来连接多个 DRAM 裸片，这显著增加了制造成本和复杂性。UCIe 是一种开放的裸片间互连标准，允许不同的芯片无缝通信，促进了半导体设计的模块化方法。后端晶体管 DRAM 将开关晶体管移至存储电容上方的金属层，与传统的前端实现相比，简化了 3D 堆叠工艺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/intel-patent-reveals-new-xbm-memory-architecture-that-ditches-hbms-costly-silicon-interposer-backend-transistor-dram-stack-uses-ucie-links-and-built-in-repair-to-ease-ais-memory-bottleneck">Intel patent reveals new XBM memory architecture that ditches ...</a></li>
<li><a href="https://wccftech.com/intel-xbm-memory-takes-aim-at-hbm4-32-gt-s-speeds-lower-costs-through-ucie-links/">Intel’s XBM Memory Takes Aim At HBM4, Promising 32 GT/s ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/UCIe">UCIe - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Semiconductors`, `#AI Hardware`, `#Memory Architecture`, `#Intel`, `#HBM Alternatives`

---

<a id="item-15"></a>
## [三星芯片部门 2026 年利润超越过去 40 年总和](https://www.tomshardware.com/tech-industry/samsungs-chip-division-expects-to-out-earn-its-entire-40-year-history-in-2026) ⭐️ 7.5/10

经纪商共识预测三星 2026 年全年营业利润将达到约 30 万亿韩元，超过其 40 年历史的累计利润。这一财务里程碑使三星有望超越英伟达成为世界上最赚钱的公司。 这一增长突显了先进半导体制造和高带宽内存（HBM）在当前人工智能驱动经济中的关键作用。它标志着全球科技盈利能力的重大转变，证明了存储和代工创新如何推动前所未有的企业价值。 三星正利用其在 HBM 4E 样品方面的领先地位（提供 3.6 TB/s 带宽）来抢占市场份额，领先于 SK 海力士等竞争对手。该公司还专注于提高其 2 纳米工艺节点的良率，以吸引大客户并维持这种盈利能力。

rss · Tom's Hardware · 7月7日 09:30

**背景**: 受人工智能芯片和先进内存解决方案需求的推动，半导体行业目前正处于繁荣期。三星的代工部门一直在努力通过 2 纳米等下一代节点恢复对台积电的竞争力，而其内存部门则在现代 GPU 所需的关键 HBM 市场占据主导地位。高带宽内存（HBM）通过将多个 DRAM 芯片垂直堆叠，为现代 GPU 提供巨大的数据吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tweaktown.com/news/106256/samsung-foundry-stakes-survival-on-2nm-process-node-with-new-special-directive-to-fight-tsmc/index.html">Samsung Foundry stakes survival on 2nm process node with a new...</a></li>
<li><a href="https://www.techtimes.com/articles/317400/20260530/samsung-ships-industry-first-hbm4e-samples-36-tb-s-bandwidth-beats-sk-hynix-six-months.htm">Samsung Ships Industry-First HBM 4E Samples: 3.6 TB/s Bandwidth...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#Samsung`, `#financial news`, `#market analysis`, `#Nvidia`

---

<a id="item-16"></a>
## [AMD Ryzen AI Halo 评测：本地 AI 盒子性能落后于英伟达 GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review) ⭐️ 7.5/10

《Tom's Hardware》对 AMD Ryzen AI Halo 进行了评测，这是一款基于 Ryzen AI Max+ 395 处理器的开箱即用本地 AI 开发系统，虽然其软件支持全面，但性能仍落后于英伟达的 GB10，且价格昂贵。 这篇评测为开发者在选择基于 x86 的本地 AI 解决方案和英伟达专有硬件之间提供了关键见解，表明虽然 AMD 提供了强大的统一内存能力，但目前其在原始 AI 性能和生态系统成熟度方面仍不及竞争对手。 Ryzen AI Halo 配备了拥有 16 个 Zen 5 核心的 Ryzen AI Max+ 395 APU，最多支持 128GB 统一内存，使其能够在本地运行大型语言模型，但其应用兼容性和速度均不如英伟达 GB10 平台。

rss · Tom's Hardware · 7月6日 15:00

**背景**: 像 Ryzen AI Halo 和英伟达 GB10 这样的本地 AI 设备旨在让用户在不依赖云服务的情况下私密地运行大型语言模型。Ryzen AI Max+ 395（又名 Strix Halo）是一款高性能片上系统，它集成了 CPU、GPU 和 NPU 功能以及巨大的统一内存带宽，这对于高效加载大型 AI 模型至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review">AMD Ryzen AI Halo review: AMD builds a DGX... | Tom's Hardware</a></li>
<li><a href="https://www.phoronix.com/review/amd-ryzen-ai-halo">AMD Ryzen AI Halo Is An Excellent & Powerful Mini PC... - Phoronix</a></li>
<li><a href="https://hottrendline.com/16313/amd-strix-halo-ai-mini-pc-challenges-nvidia-in-the-local-ai-race/">AMD Strix Halo AI Mini PC Challenges Nvidia in the Local AI Race</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Local AI`, `#Hardware Review`, `#Ryzen AI`, `#GPU`

---

<a id="item-17"></a>
## [开源应用将索尼耳机变为 PC 头部追踪器](https://www.tomshardware.com/video-games/pc-gaming/you-can-now-use-your-sony-headphones-as-a-real-time-head-tracker-for-race-and-flight-simulators-on-pc-several-hundred-games-already-supported-enthusiast-creates-open-source-app-that-translates-live-sensor-data-into-in-game-camera-controls) ⭐️ 7.5/10

开发者尼古拉斯·斯拉特里创建了一个名为“索尼头部追踪器”的开源应用程序，该程序可从兼容的索尼耳机和耳塞中提取原始传感器数据。这些数据被转换为与 OpenTrack 兼容的输入信号，从而支持在 200 多款 PC 游戏中实现头部追踪功能。 该工具为希望以低成本体验沉浸式头部追踪的模拟游戏爱好者提供了一种无需购买昂贵专用硬件的解决方案。它通过使用现有的音频设备让玩家自然地环顾四周，显著提升了赛车和飞行模拟游戏的真实感。 该应用程序充当桥梁，通过 UDP 向 OpenTrack 软件发送头部追踪数据，随后由该软件将方向数据转发给支持的游戏。它特别支持如 Android Head Tracker 等协议，并以度为单位报告偏航、俯仰和滚转角。

rss · Tom's Hardware · 7月6日 14:36

**背景**: Head tracking technology uses Inertial Measurement Units (IMUs) to detect head movement and adjust the in-game camera view accordingly. OpenTrack is a popular open-source software framework that aggregates data from various cheap sensors to provide this functionality for PC gaming, typically requiring specific hardware drivers.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NicholasSlattery/sony-head-tracker/blob/main/docs/PROTOCOL.md">sony- head - tracker /docs/ PROTOCOL .md at main...</a></li>
<li><a href="https://opentrack-opentrack.mintlify.app/protocols/flightgear">FlightGear - OpenTrack</a></li>

</ul>
</details>

**标签**: `#PC Gaming`, `#Open Source`, `#Simulation`, `#Hardware Hacking`, `#Head Tracking`

---

<a id="item-18"></a>
## [美国 AI 芯片供应链缺口：Blackwell 封装仍依赖海外](https://www.tomshardware.com/tech-industry/nvidia-and-intel-tout-chips-built-in-america-but-every-arizona-made-blackwell-die-is-still-packaged-in-taiwan) ⭐️ 7.5/10

尽管英伟达和英特尔都在宣传其国内制造能力，但英伟达 Blackwell GPU 的关键先进封装技术至少在 2028 年之前仍位于台湾。这凸显了美国本土芯片制造与高性能 AI 硬件所需的离岸组装之间存在显著脱节。 这种对外国封装基础设施的依赖表明，美国目前尚无法宣称拥有完全自给自足的 AI 供应链，这可能造成瓶颈并带来地缘政治风险。它强调了国内投资先进封装技术以支持日益增长的 AI 加速器需求的紧迫性。 英伟达的 Blackwell 数据中心 GPU 采用台积电的 CoWoS-L 封装技术，将计算芯片与 HBM3e 堆栈通过硅中介层配对。由于目前所有的 CoWoS 产能都位于台湾，因此每一颗在亚利桑那州制造的 Blackwell 芯片都必须运往海外进行最终封装。

rss · Tom's Hardware · 7月6日 12:51

**背景**: 像 CoWoS（基板上的晶圆上芯片）这样的先进封装技术对于在现代 AI 芯片中将高带宽内存（HBM）与逻辑芯片集成至关重要。虽然美国在芯片设计方面处于领先地位，并且根据《芯片法案》扩大了制造工厂，但目前缺乏这些复杂 2.5D/3D 封装工艺的专业产能，而这些工艺主要由亚洲代工厂主导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/nvidia-and-intel-tout-chips-built-in-america-but-every-arizona-made-blackwell-die-is-still-packaged-in-taiwan">Nvidia and Intel tout homegrown American chip ... | Tom's Hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advanced_packaging_(semiconductors)">Advanced packaging ( semiconductors ) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Semiconductors`, `#Supply Chain`, `#Nvidia`, `#Intel`, `#Manufacturing`

---

<a id="item-19"></a>
## [字节 Seedance 2.0：2000 亿参数规模化确立 AI 视频领先地位](https://36kr.com/p/3885177884078083?f=rss) ⭐️ 7.3/10

字节跳动的 Seedance 2.0 视频生成模型扩展至 2000 亿参数，克服了内部质疑并确立了显著的技术领先优势。该模型已成为公司的主要收入来源，自 2026 年以来贡献了火山引擎 MaaS 收入的一半以上。 这一成功标志着字节跳动在竞争激烈的 AI 格局中的战略逆转，证明了与饱和的大语言市场相比，高利润率视频生成是一个可行的商业模式。它验证了像 DiT 这样的架构选择和激进扩展在实现行业领导地位方面的重要性。 团队从效果较差的基于 2D UNet 的架构转向原生扩散 Transformer（DiT）结构，以更好地利用缩放定律。尽管使用的 GPU 性能不如竞争对手，但对数据质量和模型结构的关注使 Seedance 2.0 实现了卓越的性能和高毛利率。

rss · 36氪 · 7月7日 07:30

**背景**: 字节跳动的 Seed 实验室在 2024 年由吴永辉等领导者重组，以整合早期因团队分散和架构次优而面临的困境。转向原生多模态架构和招募顶尖人才是追赶快手可灵等竞争对手的关键步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/">ByteDance Seed</a></li>
<li><a href="https://www.together.ai/models/seedance-2-0">ByteDance Seedance 2 . 0 API | Together AI</a></li>

</ul>
</details>

**标签**: `#AI Video Generation`, `#ByteDance`, `#Large Language Models`, `#Model Scaling`, `#Tech Industry Analysis`

---

<a id="item-20"></a>
## [OpenClaw 超越 React 登顶 GitHub，AI Agent 时代来临](https://36kr.com/p/3885061350617350?f=rss) ⭐️ 7.3/10

OpenClaw 在 GitHub 上的星标数已达到 25.2 万，正式超越 Meta 的 React，成为历史上星标最多的开源项目。这一里程碑标志着开发者兴趣的重大转变，从单纯生成文本转向能够执行任务的自主 AI 智能体。 这一事件标志着 AI 智能体范式的广泛认可，即软件作为跨平台复杂工作流的执行者。它凸显了对能够深度融入日常运营（如邮件管理和办公软件自动化）的工具的日益增长的需求。 OpenClaw 是一个自托管、本地优先的网关，将 Discord 和 iMessage 等聊天应用连接到 AI 智能体以执行任务。尽管功能强大，但其安装涉及 Node.js 和命令行配置等技术技能，导致付费安装服务激增以及基于云的一键部署解决方案的出现。

rss · 36氪 · 7月7日 06:23

**背景**: 由 Meta 开发的 React 长期以来一直是构建 Web 应用程序用户界面的主导前端库。OpenClaw 代表了 AI 工具的新类别，超越了对话界面，能够在用户设备上执行实际操作，例如管理文件、发送消息以及通过自然语言命令自动化工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.openclaw.ai/">OpenClaw is a multi-channel gateway for AI agents that runs on any...</a></li>
<li><a href="https://github.com/openclaw/openclaw/blob/main/README.md">openclaw /README.md at main · openclaw / openclaw · GitHub</a></li>
<li><a href="https://www.hostinger.com/tutorials/what-is-openclaw">What is OpenClaw ? How the local AI agent works</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Open Source`, `#GitHub Trends`, `#Software Engineering`, `#Tech Industry`

---