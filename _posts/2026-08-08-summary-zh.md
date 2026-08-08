---
layout: default
title: "Horizon Summary: 2026-08-08 (ZH)"
date: 2026-08-08
lang: zh
---

> 从 44 条内容中筛选出 20 条重要资讯。

---

1. [AI 设计出 16 种全新噬菌体，生物安全监管严重滞后](#item-1) ⭐️ 8.5/10
2. [DeepMind 的 WeatherNext 模型在气旋预报上取得突破](#item-2) ⭐️ 8.0/10
3. [DeepSeek V4 Flash 0731](#item-3) ⭐️ 8.0/10
4. [科学家称内存价格已回升至 2007 年水平，AI 短缺在数月内抹去 20 年发展成果——内存价格数十年来一直呈指数级下降](#item-4) ⭐️ 7.5/10
5. [AMD 收购 Taalas，这家初创公司把模型权重直接刻进芯片](#item-5) ⭐️ 7.3/10
6. [美国能源部启动 Genesis 开放模型计划](#item-6) ⭐️ 7.0/10
7. [NASA 通过巧妙电力调整延长旅行者 2 号任务寿命](#item-7) ⭐️ 7.0/10
8. [大规模管理 AI 编程成本](#item-8) ⭐️ 7.0/10
9. [亚马逊德州数据中心将使用美国污染最严重的发电厂](#item-9) ⭐️ 7.0/10
10. [Nixpkgs 核心团队已解散](#item-10) ⭐️ 7.0/10
11. [英特尔与台积电在 High-NA EUV 上各走不同路线](#item-11) ⭐️ 7.0/10
12. [AMD RDNA 4m 集成显卡支持已合并至开源 Mesa GPU 驱动](#item-12) ⭐️ 6.5/10
13. [中国长鑫存储在 AMD 平台上实现 DDR5-8800 超频突破](#item-13) ⭐️ 6.5/10
14. [英特尔提议用轨道数据中心管理 LEO 卫星星座](#item-14) ⭐️ 6.5/10
15. [硬件研究人员启动"CPU 反优化"项目，寻找最慢的单条 x86 指令并创建耻辱榜——最严重的违规者执行耗时高达 1980 亿个周期，横跨 62 秒](#item-15) ⭐️ 6.5/10
16. [玩家通过自制 HID 工具将 Steam Controller 触觉马达改成立体声扬声器](#item-16) ⭐️ 6.5/10
17. [亚马逊因智能体 AI 算力紧张限制内部 EC2 使用](#item-17) ⭐️ 6.5/10
18. [Kioxia GP1 PCIe Gen6 SSD 在 FMS 2026 展示超 1000 万 IOPS](#item-18) ⭐️ 6.5/10
19. [Imagination Technologies 放弃 CPU/NPU 计划，第七任 CEO 领导下重回 GPU IP](#item-19) ⭐️ 6.0/10
20. [Chiplet 架构：可扩展汽车算力的实用路径](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [AI 设计出 16 种全新噬菌体，生物安全监管严重滞后](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-creates-16-new-viruses-that-never-existed-in-nature-after-learning-dnas-pattern-from-9-trillion-nucleotides-experts-warn-such-applications-are-way-ahead-of-necessary-guardrails) ⭐️ 8.5/10

研究人员利用在 9 万亿个 DNA 核苷酸上训练的 Evo AI 模型，成功设计出 16 种全新的、可在大肠杆菌内感染并复制的功能性噬菌体基因组。该研究表明，生成式基因组模型能够创造出自然界中从未出现过的功能性生物实体，引发了人们对 AI 驱动病原体设计发展速度远超监管框架的担忧。 这一成果标志着 AI 驱动的合成生物学达到了一个重要里程碑，表明在基因组数据上训练的基础模型能够直接产生有生命、可复制的生物系统，而不仅仅是预测序列。其双重用途风险巨大：同样的能力既可以用于开发对抗抗生素耐药性的新型抗菌疗法，但也可能被滥用以绕过核酸合成筛查、设计危险病原体，使生物安全政策成为当务之急。 Evo 2 模型使用 400 亿参数，具有 1 兆碱基的上下文长度，基于 StripedHyena 架构构建，可实现近线性的计算和内存扩展，从而进行单核苷酸分辨率的建模。配套的基因组语言模型框架能够生成完整的噬菌体基因组；专家指出，目前的生物安全筛查主要依赖序列数据库比对，而这种方法是 AI 设计的新型基因组可能规避的。

rss · Tom's Hardware · 8月8日 11:00

**背景**: 噬菌体是专门感染细菌的病毒，长期以来一直被视为传统抗生素的替代方案而备受关注。Evo 等生成式 AI 基础模型在海量基因组数据集上进行训练，以学习 DNA 的统计模式，从而能够预测和设计新的生物序列。由于这些模型可以生成与任何已知生物都不匹配的序列，它们有可能规避 DNA 合成服务商目前使用的生物安全筛查系统——后者目前是通过与现有数据库比对来标记危险序列的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10176-5">Genome modelling and design across all domains of life with Evo 2 | Nature</a></li>
<li><a href="https://arcinstitute.org/tools/evo">Evo 2: DNA Foundation Model | Arc Institute</a></li>
<li><a href="https://www.insideprecisionmedicine.com/topics/precision-medicine/ai-designed-viral-genomes-raise-biosecurity-concerns/">AI-Designed Viral Genomes Raise Biosecurity Concerns | Inside Precision Medicine</a></li>

</ul>
</details>

**标签**: `#AI`, `#synthetic-biology`, `#biosecurity`, `#generative-AI`, `#genome-design`

---

<a id="item-2"></a>
## [DeepMind 的 WeatherNext 模型在气旋预报上取得突破](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/) ⭐️ 8.0/10

DeepMind 宣布其 WeatherNext AI 模型在气旋预报方面取得突破，相比之前的方法可多提供约一天的预警时间。该模型已在 GitHub 上以 google-deepmind/weathernext 仓库的形式开源。 多一天的台风预警可以挽救生命，并为受灾地区提供更充分的疏散和资源调配时间。模型开源使全球气象机构、研究人员和开发者都能在此基础上进行改进，有望加速 AI 驱动天气预报的普及。 WeatherNext 代码库包含用于单步预测的 GraphCast 架构（graphcast.py），而后续的 WeatherNext 2 版本则使用 32 维高斯噪声向量来生成集合扰动。AI 天气模型相比传统数值天气预报（NWP）系统通常所需的算力大幅减少，同时准确度持平甚至更高。

hackernews · bhavansig · 8月8日 09:18 · [社区讨论](https://news.ycombinator.com/item?id=49220126)

**背景**: 数值天气预报（NWP）几十年来一直是天气预报的核心，通过超级计算机利用 NOAA/NWS、探空气球和卫星等数据模拟大气物理。近年来，以 DeepMind 的 GraphCast 为代表的深度学习模型已证明，AI 可以在中期预报中匹配甚至超越传统 NWP 系统，同时计算消耗大幅降低。气旋（飓风/台风）预报尤为困难，因为这类风暴具有混沌且快速演变的特性，预报提前期的任何提升都格外有价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/google-deepmind/weathernext/blob/main/README.md">weathernext /README.md at main · google- deepmind / weathernext</a></li>
<li><a href="https://deepmind.google/science/weathernext/">WeatherNext 2 — Google DeepMind</a></li>
<li><a href="https://e360.yale.edu/features/artificial-intelligence-weather-forecasting">A.I. Is Quietly Powering a Revolution in Weather Prediction - Yale E360</a></li>

</ul>
</details>

**社区讨论**: 社区整体情绪偏正面，评论者称赞这一 AI 应用相比编程智能体等用例具有更直接的现实价值。一位评论者幽默地想象 DeepMind 管理层在面对竞争对手时推介这一突破的场景；另一位则强调了政府运营的地面实况天气数据基础设施（如 NOAA/NWS、探空气球、卫星）才是支撑这些模型取得成功的关键。还有用户分享了 zoom.earth 等实用的台风追踪资源。

**标签**: `#AI`, `#weather-forecasting`, `#DeepMind`, `#deep-learning`, `#open-source`

---

<a id="item-3"></a>
## [DeepSeek V4 Flash 0731](https://arcprize.org/results/deepseek-v4-flash-0731) ⭐️ 8.0/10

DeepSeek V4 Flash 0731 版本在实际使用中展现出强大的性价比，实践者反馈它足以应对大多数任务，成本几乎可以忽略不计，并且在 Blackwell 硬件上实现了令人印象深刻的本地推理速度。

hackernews · tosh · 8月7日 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49214008)

**标签**: `#DeepSeek`, `#LLM`, `#AI`, `#local-inference`, `#model-release`

---

<a id="item-4"></a>
## [科学家称内存价格已回升至 2007 年水平，AI 短缺在数月内抹去 20 年发展成果——内存价格数十年来一直呈指数级下降](https://www.tomshardware.com/pc-components/ram/scientist-says-ram-pricing-has-reverted-to-normalized-2007-levels-memory-prices-have-been-falling-exponentially-for-decades-but-the-ai-shortage-undid-20-years-of-progress-in-a-matter-of-months) ⭐️ 7.5/10

据分析师 Lemire 表示，AI 需求导致内存价格回退至 2007 年水平，仅用数月时间便抹去了 20 年的指数级降价进程。

rss · Tom's Hardware · 8月7日 16:58

**标签**: `#RAM`, `#hardware-pricing`, `#AI-demand`, `#memory-shortage`, `#semiconductor-market`

---

<a id="item-5"></a>
## [AMD 收购 Taalas，这家初创公司把模型权重直接刻进芯片](https://www.solidot.org/story?sid=85035) ⭐️ 7.3/10

AMD 收购了成立于 2023 年的 AI 硬件初创公司 Taalas，该公司研发将模型权重直接刻入芯片的模型专用集成电路（MSIC）。Taalas 采用台积电 6nm 工艺制造的测试芯片 HC1 能以每秒 16,960 个 tokens 的速度处理 Meta 的 Llama 3.1 8B 模型，速度比英伟达 GPU 快 48 倍，比 Cerebras 加速器快 8.5 倍。 这次收购标志着 AMD 战略性地转向一种可能颠覆现有格局的推理架构——通过在芯片层面消除运行时的权重加载，彻底绕开 GPU 范式。如果 MSIC 能在速度和成本上兑现承诺，可能会冲击英伟达在 AI 推理领域的主导地位，并改变 AI 模型的大规模部署方式。 Taalas 计划今夏推出第二代 HC2 芯片，目标支持 200 亿参数模型。其主要局限在于每颗芯片只能运行被烧录的当前模型，切换到新模型需要重新设计芯片，但 Taalas 表示只需更换两层金属层，既便宜又快速。

rss · Solidot · 8月7日 15:23

**背景**: 模型专用集成电路（MSIC）是专用集成电路（ASIC）的一种极端形态，其芯片的逻辑和物理布线围绕单个神经网络的权重和架构设计，而非作为通用计算引擎。传统 AI 推理依赖 GPU 或可编程加速器在运行时从内存加载权重，这会带来延迟和能耗成本。通过将权重直接硬编码到硅片中，MSIC 消除了内存带宽瓶颈，可以实现惊人的吞吐量提升——代价是灵活性下降，因为每颗芯片只能用于单一用途。AMD 的收购使其与英伟达、Cerebras、Groq 以及其他瞄准 AI 推理市场的定制芯片厂商形成直接竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Application-specific_integrated_circuit">Application-specific integrated circuit - Wikipedia</a></li>
<li><a href="https://english.ihep.cas.cn/nw/han/y26/202608/t20260804_1186878.html">BESIII Experiment Identifies X (2370) as a Glueball Dominated ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Glueball">Glueball - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#AMD`, `#model-specific integrated circuits`, `#particle physics`, `#browser extensions`

---

<a id="item-6"></a>
## [美国能源部启动 Genesis 开放模型计划](https://genesisopenmodels.anl.gov/) ⭐️ 7.0/10

美国能源部启动了 Genesis 开放模型计划（Genesis Open Models Initiative），这是一项由政府支持的项目，旨在开发开放权重的基础模型，以减少对外国 AI 系统的依赖。该计划设在阿贡国家实验室，是能源部更广泛的 Genesis 任务的一部分。 此计划是在美国对华 AI 模型担忧加剧、美国开放权重模型稀缺的关键时刻推出的，代表了美国联邦政府对开放权重 AI 开发的重大投资。它可能通过提供一个政府支持、在地缘政治上可信的替代方案，来重塑开源 AI 生态——尤其是在 DeepSeek 等模型已在某些国家实验室被禁的背景下。 该计划聚焦于广义的'基础模型'，而非特定于大语言模型，许多当前提案涉及非 LLM 架构和非文本数据，例如智能体框架和科学工作流。社区评论者指出，该计划在后训练和强化学习方面仍有相当大的差距，才能与国际上领先的开放权重模型竞争。

hackernews · moelf · 8月7日 22:24 · [社区讨论](https://news.ycombinator.com/item?id=49216946)

**背景**: 开放基础模型是指其数值参数（权重）公开发布的 AI 模型，允许开发者进行微调并在其基础上构建。美国在专有 AI 领域（如 OpenAI、Anthropic）历来处于领先地位，但与中国的 DeepSeek 和法国的 Mistral 相比，被广泛使用的开放权重模型较少。能源部的 Genesis 任务于 2025 年 11 月 24 日启动，联合全部 17 个 DOE 国家实验室、大学和产业界，共同构建一个用于能源、科学和国家安全挑战的 AI 驱动科学平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.energy.gov/undersecretaryforscience/genesis-mission/genesis-mission">The Genesis Mission - Department of Energy</a></li>
<li><a href="https://www.energy.gov/articles/energy-department-launches-genesis-mission-transform-american-science-and-innovation">Energy Department Launches ‘Genesis Mission’ to Transform ...</a></li>
<li><a href="https://www.medianama.com/2024/03/223-us-department-commerce-invites-feedback-benefits-risks-open-ai-foundation-models/">US Department of Commerce Invites Feedback on Open AI Models</a></li>

</ul>
</details>

**社区讨论**: 社区表达了乐观和怀疑两种态度。一些人指出美国开放权重模型的稀缺（仅提到 Gemma、GPT-OSS 和 Mira Murati 的 Inkling），而另一些人质疑 Genesis 是否能产出真正具有竞争力的模型，尤其是考虑到 DeepSeek 已在 LLNL 等国家实验室被禁。一个关键观察是，该计划有意避免使用'LLM'一词，而是涵盖非语言类的基础模型。最持怀疑态度的评论者认为，在实际模型权重（如 Hugging Face 上的 GGUF 文件）发布之前，这一宣布毫无意义。

**标签**: `#open-source`, `#government-policy`, `#foundation-models`, `#AI-research`, `#DOE`

---

<a id="item-7"></a>
## [NASA 通过巧妙电力调整延长旅行者 2 号任务寿命](https://www.space.com/space-exploration/voyager/nasa-figured-out-how-to-keep-its-48-year-old-voyager-2-probe-running-for-yet-another-year) ⭐️ 7.0/10

NASA 工程师于 2026 年 8 月 4 日完成了一次高风险的电力切换，成功为已有 48 年历史的旅行者 2 号探测器释放出足够能量，使其最后的科学仪器至少能再传输一年数据，避免了今年晚些时候不得不关闭仪器的命运。 旅行者 2 号是人类历史上唯一造访过天王星和海王星的探测器，与孪生兄弟旅行者 1 号一起，也是人类在日光层之外的唯一活跃使者，能提供不可替代的星际空间就地探测数据，而这些数据无法通过其他途径获得。 探测器由放射性同位素热电发电机（RTG）供电，通过钚-238 衰变产生的热量转化为电能，但放射性燃料在数十年间持续衰减，迫使 NASA 在电力余量缩小时逐步关闭各类仪器。

hackernews · wglb · 8月8日 01:49 · [社区讨论](https://news.ycombinator.com/item?id=49218179)

**背景**: 旅行者 2 号于 1977 年 8 月 20 日发射，先后于 1979 年飞掠木星、1981 年飞掠土星、1986 年飞掠天王星、1989 年飞掠海王星，随后进入延展任务期飞向星际空间。它已穿越日球层顶——太阳粒子保护泡的边界——进入星际空间，其仪器仍在太阳系外测量宇宙射线、磁场和等离子体波。由于探测器最初的设计主任务仅四年，每延长一年的运行都需要通过创造性的工程手段来管理不断老化的部件和逐渐枯竭的电力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jpl.nasa.gov/missions/voyager-2/">Voyager 2 | NASA Jet Propulsion Laboratory (JPL)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Voyager_2">Voyager 2 - Wikipedia</a></li>
<li><a href="https://science.nasa.gov/mission/voyager/voyager-2/">Voyager 2 - Science@NASA Where are Voyager 1 and Voyager 2 Now? - Science@NASA Voyager 2 - Wikipedia NASA’s ‘Big Bang’ Saves Voyager 2’s Last Three Interstellar ... NASA Engineers Successfully Free Up Power on Voyager 2 To ... NASA figured out how to keep its 48-year-old Voyager 2 probe ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应几乎全是崇敬之情。一位曾在 JPL 工作的研究人员分享了一个震撼的第一手见闻：大约八年前，整个实验室只有一个人掌握编写旅行者 2 号指令序列的专业知识——这种正在消失的专业技能让每一次任务延期都更加紧迫。其他评论者则提到了 2023 年从 150 亿英里之外手动修复旅行者 1 号内存损坏的壮举，并推荐了纪录片《It's Quieter in the Twilight》（2022），以了解仍在照看这些老旧探测器的小型团队。

**标签**: `#space-exploration`, `#voyager`, `#engineering`, `#NASA`, `#deep-space-missions`

---

<a id="item-8"></a>
## [大规模管理 AI 编程成本](https://www.databricks.com/blog/managing-ai-coding-costs-scale) ⭐️ 7.0/10

Databricks 分享了在企业规模下管理 AI 编程工具成本的策略，引发了社区关于 token 效率、智能体设计以及 AI 辅助开发经济学的热烈讨论。

hackernews · moonikakiss · 8月7日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=49214468)

**标签**: `#ai-coding`, `#cost-management`, `#developer-tools`, `#enterprise`, `#llm-agents`

---

<a id="item-9"></a>
## [亚马逊德州数据中心将使用美国污染最严重的发电厂](https://www.nytimes.com/2026/08/08/climate/amazon-data-center-texas-pollution.html) ⭐️ 7.0/10

据《纽约时报》报道，亚马逊计划在德克萨斯州建设的数据中心将由美国污染最严重的一座发电厂供电。这座设施凸显了超大规模 AI 和云基础设施正在如何推动对专用、重度依赖化石燃料的能源需求。 该项目体现了 AI 算力爆发与脱碳目标之间日益加剧的环境矛盾，因为生成式 AI 工作负载的能耗比早期的任务专用 AI 高出 10 到 30 倍。它同时也引发了一个问题：当后置式燃气发电厂是获取电力的最快途径时，企业的可持续发展承诺是否还能兑现。 后置式天然气发电厂（建在数据中心园区内或紧邻园区）已成为 AI 园区的首选电力方案，因为它们可以绕开电网接入排队的等待时间，但研究表明，新的燃气调峰机组的总排放量可能高于它们所替代的旧式低效机组。美国约占全球新增燃气轮机项目管道的四分之一，其中超过三分之一的新增美国发电容量专门用于数据中心。

hackernews · sbulaev · 8月8日 10:07 · [社区讨论](https://news.ycombinator.com/item?id=49220350)

**背景**: 数据中心是塞满服务器的大型设施，用于存储和处理数据；像亚马逊这样的"超大规模"数据中心为数百万用户提供云和 AI 工作负载。"后置式"发电指的是在客户场地内或附近发电，而不是从公共电网取电；燃气"调峰"电厂通常在用电高峰时段运行。生成式 AI 的训练和推理（运行大语言模型）所需的电量和冷却远超传统云计算，因为 GPU 温度高且长时间满负荷运转。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grist.org/energy/data-centers-natural-gas-methane-behind-the-meter/">Data centers are scrambling to power the AI boom with natural gas</a></li>
<li><a href="https://www.americanactionforum.org/insight/ai-data-centers-why-are-they-so-energy-hungry/">AI Data Centers: Why Are They So Energy Hungry? - AAF</a></li>
<li><a href="https://www.theenergymix.com/new-gas-peaker-plants-can-produce-more-emissions-than-older-less-efficient-units-study/">New Gas Peaker Plants Can Produce More Emissions than Older...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对政策制定者的不满：尽管选民越来越反对数据中心，纽约和德克萨斯州已实施建设暂停令，但政策制定者仍然拒绝制定具有环保意识的能源或水资源政策。一些评论员将亚马逊的项目与 xAI 未经监管的燃气轮机进行了尖锐对比，并认为 AI 实验室正将近期生态危害的责任转嫁到推测性的存在性风险叙事上。还有人指出，虽然世界其他国家正在建造新的核电站，但美国却没有在建项目，这形成了一个先有鸡还是先有蛋的难题——因为核电站的建设周期远长于数据中心的部署需求。

**标签**: `#data-centers`, `#ai-infrastructure`, `#environmental-impact`, `#amazon`, `#energy-policy`

---

<a id="item-10"></a>
## [Nixpkgs 核心团队已解散](https://discourse.nixos.org/t/the-nixpkgs-core-team-has-disbanded/79413) ⭐️ 7.0/10

Nixpkgs 核心团队因治理结构不可持续和贡献者过度疲劳而解散，这引发了关于开源项目可持续性和制度改革的广泛讨论。

hackernews · Meleagris · 8月8日 01:12 · [社区讨论](https://news.ycombinator.com/item?id=49217993)

**标签**: `#nix`, `#open-source-governance`, `#maintainer-burnout`, `#package-management`, `#ecosystem-news`

---

<a id="item-11"></a>
## [英特尔与台积电在 High-NA EUV 上各走不同路线](https://semiwiki.com/semiconductor-manufacturers/tsmc/371838-intel-and-tsmc-take-different-paths-to-high-na-euv/) ⭐️ 7.0/10

英特尔和台积电在采用高数值孔径极紫外光刻（High-NA EUV）方面采取了不同的策略。英特尔早早开始开发和集成 High-NA EUV，而台积电则选择了另一种不同的路线。 High-NA EUV 是关键的下一代光刻技术，能够在先进制程节点上制造更小、更快、更节能的半导体芯片。两大行业龙头的不同策略将影响先进制程的扩展速度、制造成本以及在尖端代工和逻辑芯片市场的竞争格局。 文章正文被截断，但发布于半导体行业分析平台 SemiWiki。High-NA EUV 系统（由 ASML 搭配 ZEISS 光学元件提供）使用更高的数值孔径（0.55，而标准 EUV 为 0.33），以相同的 13.5 nm EUV 波长实现更精细的分辨率，有望支持亚 8 nm 的图案化。

rss · SemiWiki · 8月7日 15:00

**背景**: EUV（极紫外）光刻技术使用波长为 13.5 nm 的光在硅晶圆上打印极其精细的电路图案，是制造最先进制程芯片的关键技术。High-NA EUV 是其下一代演进，采用更高数值孔径的光学系统，在标准 EUV 基础上进一步提升分辨率，支持更小的特征尺寸。该系统的唯一商用供应商是 ASML，核心光学元件由 ZEISS 提供。采用 High-NA EUV 涉及巨额资本投入和集成挑战，因此各公司在其推广路线上采取了不同的策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EUV_lithography">EUV lithography - Wikipedia</a></li>
<li><a href="https://www.zeiss.com/semiconductor-manufacturing-technology/inspiring-technology/high-na-euv-lithography.html">High-NA-EUV Lithography: the next EUV generation | ZEISS SMT</a></li>
<li><a href="https://spie.org/Publications/Proceedings/Volume/13686">International Conference on Extreme Ultraviolet Lithography ... | SPIE</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#lithography`, `#Intel`, `#TSMC`, `#EUV`

---

<a id="item-12"></a>
## [AMD RDNA 4m 集成显卡支持已合并至开源 Mesa GPU 驱动](https://www.techpowerup.com/351431/amd-rdna-4m-igpu-support-arrives-in-open-source-mesa-gpu-driver) ⭐️ 6.5/10

AMD 神秘的 RDNA 4m 集成显卡（GFX1171）已合并至 Mesa 26.3，支持 INT8 和原生 FSR 4，但由于 AMD 计划在 2029 年前继续保留 RDNA 3.5 集成显卡，其确切用途尚不明确。

rss · TechPowerUp News · 8月7日 16:39

**标签**: `#AMD`, `#RDNA`, `#Mesa`, `#open-source`, `#GPU drivers`

---

<a id="item-13"></a>
## [中国长鑫存储在 AMD 平台上实现 DDR5-8800 超频突破](https://www.tomshardware.com/pc-components/ram/chinas-memory-making-champion-smashes-ddr5-8800-barrier-on-amd-platform-cxmt-chips-close-the-gap-with-sk-hynix) ⭐️ 6.5/10

中国 DRAM 制造商长鑫存储（CXMT）在 AMD AM5 平台上成功实现了 DDR5-8800 内存超频，主板合作伙伴七彩虹（Colorful）在搭载 CXMT 集成电路的新内存套件上展示了这一成果。该成绩凸显了 CXMT DDR5 芯片的超频潜力，以及其与 SK 海力士等领先厂商之间日益缩小的性能差距。 这一突破意义重大，因为 CXMT 是中国唯一具有重要规模的国产 DRAM 制造商，在当前美国出口管制背景下，高速内存能力的提升将降低中国对外国内存供应商的依赖。展示出与一线厂商相当的超频潜力，表明中国 DRAM 已不再局限于入门级或低端市场。 DDR5-8800 是通过 AMD EXPO 技术实现的超频速度，而非 JEDEC 标准规范，目前 JEDEC DDR5 最高标准仅为 5600 MT/s，基础频率为 4800 MT/s，因此 8800 相较基线提升了约 83%。DDR5 超频存在实际风险，包括对模块上 PMIC 电源管理芯片的电压压力以及可能的保修影响。

rss · Tom's Hardware · 8月8日 12:35

**背景**: DDR5 是当前主流桌面和服务器 DRAM 内存规格，取代 DDR4，提供更高带宽并在内存条上集成电源管理。JEDEC 是定义官方速度和时序标准的机构，任何运行速度高于 JEDEC 额定值的内存都属于超频，通常通过 Intel XMP 或 AMD AM5 平台上的 AMD EXPO 等厂商配置文件启用。CXMT（长鑫存储）成立于 2016 年，总部位于安徽合肥，是中国最大的 DRAM 制造商，主要以 DDR4 产品闻名，并正逐步扩展至 DDR5 领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.amd.com/en/products/processors/technologies/expo.html">AMD EXPO ™ Technology for AMD Ryzen™ Processors for Socket AM 5</a></li>
<li><a href="https://www.overclockers.com/ddr5-overclocking-guide/">DDR5 Overclocking Guide: Make it Faster - Overclockers JEDEC vs. Intel DDR5 specs – timings tRRD_S, tRRD_L, tFAW and ... JEDEC vs. XMP: Guide to Enabling, Tuning, & Fixing RAM Speed Who Is High-Speed DDR5 Memory Actually For? - LTT Labs There are three JEDEC speed bins for DDR5 5600. The highest ...</a></li>

</ul>
</details>

**标签**: `#DDR5`, `#CXMT`, `#memory`, `#overclocking`, `#China-semiconductors`

---

<a id="item-14"></a>
## [英特尔提议用轨道数据中心管理 LEO 卫星星座](https://www.tomshardware.com/tech-industry/space/intels-proposed-orbital-data-centers-would-manage-thousands-of-simple-leo-satellites-two-tier-network-puts-the-brains-of-satellite-constellations-in-higher-orbit) ⭐️ 6.5/10

英特尔提出了一种两层轨道数据中心架构：由少量位于较高轨道的强大卫星来管理和协调大量相对简单的近地轨道（LEO）卫星，从而减少对大量地面控制中心的依赖。 这一提议表明主要半导体公司对天基计算基础设施日益增长的兴趣。如果得以推进，可能改变 Starlink、Amazon Leo 和 OneWeb 等巨型星座的运营方式——将编排逻辑从地面转移到轨道，从而实现更快速、更自主的卫星网络。 该概念将边缘计算原理应用于太空：计算密集型任务（路由、协同、AI 推理）在较高轨道的"大脑"卫星上完成，而 LEO 卫星则充当更简单的数据采集或中继节点。目前尚未披露时间表、硬件规格或发射合作伙伴，该提议仍处于概念阶段。

rss · Tom's Hardware · 8月8日 11:45

**背景**: 近地轨道（LEO）卫星星座——如 SpaceX 的 Starlink 和亚马逊的 Project Kuiper（即 Amazon Leo）——通常依赖地面站来管理路由、切换和网络协调。随着星座规模扩展到数千颗卫星，基于地面的控制所带来的延迟和运营成本成为瓶颈。较高轨道（MEO 或 GEO）可以用更少的卫星提供更广泛的覆盖，因此非常适合承担监督角色。天基或轨道数据中心（ODC）是一个新兴概念，旨在利用持续太阳能和太空级散热直接在轨道上运行 AI 和计算负载。Starcloud 等公司已使用 Nvidia 硬件在太空中训练了小型 AI 模型，而 Google、SpaceX 和中国机构据称也在探索类似的轨道计算概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/space/intels-proposed-orbital-data-centers-would-manage-thousands-of-simple-leo-satellites-two-tier-network-puts-the-brains-of-satellite-constellations-in-higher-orbit">Intel's proposed orbital data centers would manage thousands ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Space-based_data_center">Space-based data center - Wikipedia</a></li>
<li><a href="https://www.cbo.gov/system/files/2023-05/58794-satellite-primer.pdf">Large Constellations of Low-Altitude Satellites: A Primer</a></li>
<li><a href="https://blog.spacecomputer.io/orbital-comute-101/">What Is Orbital Compute? A Guide to Space-Based Data Centers</a></li>

</ul>
</details>

**标签**: `#satellite-networks`, `#orbital-computing`, `#Intel`, `#edge-computing`, `#space-infrastructure`

---

<a id="item-15"></a>
## [硬件研究人员启动"CPU 反优化"项目，寻找最慢的单条 x86 指令并创建耻辱榜——最严重的违规者执行耗时高达 1980 亿个周期，横跨 62 秒](https://www.tomshardware.com/pc-components/cpus/hardware-researcher-spins-up-cpu-deoptimization-project-to-find-the-slowest-machine-code-worst-offender-takes-198-billion-cycles-to-execute) ⭐️ 6.5/10

硬件研究员 Christopher Domas 创建了一个"CPU 反优化"排行榜，以寻找可能存在的最慢 x86 指令，其中最糟糕的情况执行耗时达 1980 亿个周期（62 秒）。

rss · Tom's Hardware · 8月8日 11:20

**标签**: `#x86`, `#CPU-architecture`, `#hardware-research`, `#reverse-engineering`, `#performance-analysis`

---

<a id="item-16"></a>
## [玩家通过自制 HID 工具将 Steam Controller 触觉马达改成立体声扬声器](https://www.tomshardware.com/peripherals/controllers-gamepads/modder-turns-steam-controller-trackpad-haptics-into-stereo-speakers-with-custom-hid-tool-wired-connection-transmits-16-bit-audio-that-sounds-surprisingly-full) ⭐️ 6.5/10

一位玩家制作了一款自定义 HID（人机接口设备）工具，通过 USB 数据线将 16-bit 音频流直接传输到 Steam Controller 的触觉触摸板马达上，成功将其改造成立体声扬声器，音质出人意料地饱满。虽然通过 Steam Controller 无线 puck 的无线连接能力有限，但有线 USB 连接却能为这款本身没有扬声器的设备带来真正令人印象深刻的音频表现。 这一改装展示了将触觉执行器重新用作声音换能器的创意潜力，也凸显了 USB HID 协议的灵活性——它可以传输远超传统输入设备命令的任意数据流。它可能会启发其他玩家探索类似的音频/振动跨界改装项目，并挑战人们对低成本振动硬件能力的固有认知。 Steam Controller 的触觉触摸板使用音圈式 LRA（线性谐振执行器），其机械结构与微型扬声器驱动单元非常相似，这就是它们在直接驱动时能够还原音频的原因。16-bit 音频流通过自定义 HID 描述符传输，无需安装专用 USB 音频驱动，因为 Windows 内置了 HID 类驱动程序。

rss · Tom's Hardware · 8月8日 10:00

**背景**: Steam Controller 由 Valve 于 2015 年发布，其标志性设计是配备了两块触觉触摸板，使用音圈式线性谐振执行器（LRA）在用户点击或滑动时提供触觉反馈。音圈的工作原理是让电流通过悬挂于磁场中的线圈，这与传统动圈式扬声器驱动单元的原理完全相同——唯一的区别在于设计意图和频率响应的调校。HID（人机接口设备）协议是 USB 标准中为键盘、鼠标、游戏手柄等外设设计的设备类别，但其灵活的描述符结构允许开发者自定义数据格式，从而实现将音频数据传输到非传统终端等创意用途。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://partner.steamgames.com/doc/features/steam_controller/device/steam_controller">Steam Controller (Steamworks Documentation)</a></li>
<li><a href="https://www.usb.org/hid">Human Interface Devices ( HID ) Specifications and Tools | USB -IF</a></li>
<li><a href="https://github.com/hallohallovb-collab/DS4Windows-with-SteamController-2026-Support-/blob/main/README.md">DS4Windows-with-SteamController-2026-Support-/README.md at...</a></li>

</ul>
</details>

**标签**: `#hardware-modding`, `#steam-controller`, `#haptics`, `#audio`, `#DIY`

---

<a id="item-17"></a>
## [亚马逊因智能体 AI 算力紧张限制内部 EC2 使用](https://www.tomshardware.com/pc-components/cpus/amazon-cracks-down-on-cpu-waste-among-engineers-as-agentic-ai-crunch-intensifies-cpu-demand-makes-low-utilization-ec2-instances-a-hot-commodity) ⭐️ 6.5/10

亚马逊网络服务（AWS）正在指示其工程师减少内部 EC2 使用量，因为公司需要优先满足由智能体 AI 工作负载驱动的、外部客户对 CPU 容量的激增需求。随着 AWS 重新分配资源，低利用率的 EC2 实例已成为抢手资源。 这表明由智能体 AI 需求驱动的计算资源严重短缺，对整个行业的云基础设施可用性都产生影响。这也揭示了即使是全球最大的云服务商也感受到了 AI 算力紧张带来的压力，可能会影响 AWS 客户的服务质量。 这些限制不仅影响外部客户，也影响到亚马逊自己的工程团队，显示了公司内部容量紧张的严重程度。这反映出一种更广泛的行业趋势：计算资源正被优先分配给 AI 驱动的工作负载，而非传统云服务使用。

rss · Tom's Hardware · 8月7日 15:49

**背景**: Amazon EC2（弹性计算云）是 AWS 的基础服务之一，提供可扩展的虚拟服务器实例，于 2006 年推出，是首批主要的云计算服务之一。EC2 实例类型是针对不同资源组合专门构建的虚拟服务器配置。智能体 AI（Agentic AI）指的是能够根据预定义规则自主执行任务的 AI 系统，超越了仅根据提示生成内容的生成式 AI。与生成文本、图像或代码的生成式 AI 不同，智能体 AI 会进行规划、使用工具并跨多个步骤采取行动以完成目标，通常需要持续的计算资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.coursera.org/articles/generative-ai-vs-agentic-ai">Generative AI vs. Agentic AI: What Is the Difference? - Coursera</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai-vs-generative-ai">Agentic AI vs. generative AI - IBM</a></li>
<li><a href="https://aws.amazon.com/ec2/instance-types/">Instance Types | Amazon Web Services , Inc.</a></li>

</ul>
</details>

**标签**: `#AWS`, `#cloud-infrastructure`, `#AI-demand`, `#compute-scarcity`, `#EC2`

---

<a id="item-18"></a>
## [Kioxia GP1 PCIe Gen6 SSD 在 FMS 2026 展示超 1000 万 IOPS](https://www.servethehome.com/a-10m-iops-kioxia-gp1-ssd-shown-running-at-fms-2026/) ⭐️ 6.5/10

在 FMS 2026 上，Kioxia 在自家展位现场展示了其 GP1 PCIe Gen6 NVMe SSD，实测 IOPS 略超 1000 万。这是首批公开演示达到该性能水平的 PCIe Gen6 级别消费级 NVMe SSD 之一。 1000 万 IOPS 是 NVMe 存储领域的重要里程碑，标志着 PCIe Gen6 SSD 正从规格走向实际硅片实现。对数据中心、AI 工作负载以及对极致低延迟存储有需求的高性能计算环境而言，这一代际跃升将带来直接收益。 Kioxia GP1 采用 PCIe Gen6 接口，其单通道带宽是 PCIe Gen5 的两倍，并将信号调制方式从 Gen5 的 NRZ 升级为 PAM4。本次 1000 万以上 IOPS 的数据来自展会现场演示，而非受控基准测试环境，因此供应商公布的峰值与独立测试结果可能存在差异。

rss · ServeTheHome · 8月7日 19:00

**背景**: PCIe（外围组件互连高速总线）是连接 SSD 与 CPU 的标准高速互连协议，每一代大约将带宽翻倍，其中 Gen6 单通道速率可达约 64 GT/s。NVMe（非易失性存储器高速接口）是一种基于 PCIe 运行的低延迟存储协议，用于取代最初为机械硬盘设计的老旧 SATA/AHCI 接口。Flash Memory Summit（FMS）每年在圣克拉拉举办，是 NAND 闪存和 SSD 厂商发布和展示新存储技术的首要行业盛会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.logic-fruit.com/blog/pcie/pcie-gen-4-vs-gen-5-vs-gen-6/">PCIe Gen 4 vs Gen 5 vs Gen 6: A Definitive Guide</a></li>
<li><a href="https://www.westerndigital.com/en-ie/company/newsroom/events/flash-memory-summit-conference-expo">Flash Memory Summit Conference & Expo | WD</a></li>

</ul>
</details>

**标签**: `#storage`, `#SSD`, `#PCIe Gen6`, `#NVMe`, `#Kioxia`

---

<a id="item-19"></a>
## [Imagination Technologies 放弃 CPU/NPU 计划，第七任 CEO 领导下重回 GPU IP](https://www.eetimes.com/after-seven-ceos-in-10-years-imagination-is-sticking-to-its-strategy/) ⭐️ 6.0/10

Imagination Technologies 放弃了其 CPU 和 NPU 的雄心，在十年内的第七任 CEO 领导下，重新专注于核心 GPU IP 业务，尤其瞄准中国市场。这一战略转型标志着公司在多年多元化尝试之后大幅收缩业务范围。 这一转型反映了半导体 IP 市场的激烈竞争——ARM、Synopsys 和 Cadence 等老牌巨头占据主导地位，而十年内七位 CEO 的频繁更替表明公司存在严重的组织不稳定问题。在中美科技紧张和出口管制不确定性持续的背景下，明确聚焦中国市场是一项具有重大意义的赌注。 Imagination 最知名的产品是 PowerVR GPU 架构，该架构始于 1992 年，并于 2022 年迎来 30 周年，广泛授权应用于移动和嵌入式 SoC。该公司于 2017 年 11 月从伦敦证券交易所退市，并被 Canyon Bridge 收购。

rss · EE Times · 8月7日 22:00

**背景**: Imagination Technologies 是一家总部位于英国的半导体 IP 公司，专注于为芯片设计商提供 GPU 知识产权授权，而非自己制造芯片。IP 授权模式可将芯片设计商的自研成本从 1-2 亿美元和 3-4 年开发周期，降至 1000-5000 万美元和约一半的时间。NPU（神经网络处理单元）是面向 AI 工作负载的专用加速器，在某些推理任务上比 GPU 功耗更低，而 GPU 在 AI 训练和通用并行计算方面则更加灵活。Imagination 的 PowerVR 架构开创了基于分块的延迟渲染（tile-based deferred rendering）技术，这项节能图形处理技术在整个移动 GPU 行业产生了深远影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Imagination_Technologies">Imagination Technologies - Wikipedia</a></li>
<li><a href="https://www.imaginationtech.com/news/imagination-powervr-architecture-marks-30-anniversary/">Imagination’s PowerVR architecture marks its 30th anniversary</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#GPU`, `#Imagination Technologies`, `#industry news`, `#chip design`

---

<a id="item-20"></a>
## [Chiplet 架构：可扩展汽车算力的实用路径](https://www.eetimes.com/chiplet-architectures-as-a-practical-path-to-scalable-automotive-compute/) ⭐️ 6.0/10

EE Times 发表文章指出，Chiplet（芯粒）架构为汽车厂商提供了一条可行的路径，可以在不承担单体 SoC 所带来的成本和软件复杂性的前提下，扩展软件定义汽车（SDV）所需的算力。 文章将 Chiplet 定位为摆脱臃肿单体 SoC 的'出路'，强调通过模块化的多芯片封装来扩展 SDV 算力，同时控制硅片和软件两方面的成本。

rss · EE Times · 8月7日 13:56

**背景**: Chiplet 是一种小型集成电路，仅实现定义明确的功能子集，并设计为通过中介层（interposer）与其他 Chiplet 在同一封装内组合，形成更复杂的处理器或系统。相比将所有功能集成到单一单体芯片上，这种模块化方式能够提高良率、降低制造成本并增加设计灵活性。软件定义汽车（SDV）则是指将核心功能（包括 ADAS、信息娱乐、动力总成控制等）通过软件实现和更新，而非依赖固定硬件的汽车，其运作模式类似于智能手机通过 OTA 获得新功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chiplet">Chiplet - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Software_Defined_Vehicle">Software Defined Vehicle - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/software-defined-vehicle">What is a Software Defined Vehicle? - IBM</a></li>

</ul>
</details>

**标签**: `#chiplets`, `#automotive`, `#semiconductors`, `#SDV`, `#SoC-architecture`

---