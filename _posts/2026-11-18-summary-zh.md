---
layout: default
title: "Horizon Summary: 2026-11-18 (ZH)"
date: 2026-11-18
lang: zh
---

> 从 106 条内容中筛选出 20 条重要资讯。

---

1. [U.S. Cracks Down on China Renting AI GPUs Through Overseas Data Centers](#item-1) ⭐️ 9.5/10
2. [NVIDIA Announces Rubin HPC: Science-Focused Server GPU to Arrive in 2028](#item-2) ⭐️ 9.5/10
3. [Java4Shell：OpenJDK Base64 解码中的关键 RCE 漏洞](#item-3) ⭐️ 9.0/10
4. [OpenAI 发布 GPT-6.2 Astra 和 Sol 模型](#item-4) ⭐️ 9.0/10
5. [NVIDIA 董事会确认 Jensen Huang 不会重新担任 CEO](#item-5) ⭐️ 8.5/10
6. [英伟达公布 2026 年第三季度 1158 亿美元创纪录营收](#item-6) ⭐️ 8.5/10
7. [美国商务部和司法部联合发布 NVIDIA 与 Megaspeed 出口违规声明](#item-7) ⭐️ 8.5/10
8. [Jensen Huang says he would be ‘honored’ to return as Nvidia CEO](#item-8) ⭐️ 8.5/10
9. [Nvidia warns customers of new US rule that could expose them to lawsuits for serving Chinese clients](#item-9) ⭐️ 8.5/10
10. [Google's AI answers reducing search traffic by 40%](#item-10) ⭐️ 8.0/10
11. [Microsoft's ONNX Runtime has disappeared from GitHub](#item-11) ⭐️ 8.0/10
12. [美国高度机密国家安全网络发生故障](#item-12) ⭐️ 8.0/10
13. [微软发布 MAI Code 2 和 Flash 以提供高性价比编码模型](#item-13) ⭐️ 8.0/10
14. [意大利联合圣保罗银行通过量子启发优化实现两位数成本节约](#item-14) ⭐️ 8.0/10
15. [英伟达设立国家级安全与出口管制董事会委员会](#item-15) ⭐️ 7.5/10
16. [Q.ANT 发布支持光学离散傅里叶变换的 NPU Gen 2+](#item-16) ⭐️ 7.5/10
17. [AI 安全立法：美国实验室应对中国对手的战略工具？](#item-17) ⭐️ 7.5/10
18. [AMD attacks Nvidia's FP64 emulation at SC26, touts native double-precision on Instinct MI430X](#item-18) ⭐️ 7.5/10
19. [Quad9's withdrawal from France: A canary in the coal mine](#item-19) ⭐️ 7.0/10
20. [Nvidia stopped disclosing Singapore sales as revenues hit $104B](#item-20) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [U.S. Cracks Down on China Renting AI GPUs Through Overseas Data Centers](https://www.techpowerup.com/354927/u-s-cracks-down-on-china-renting-ai-gpus-through-overseas-data-centers) ⭐️ 9.5/10

The U.S. Commerce Department has issued a new rule requiring licenses for shipping advanced AI chips to data centers worldwide that provide significant computing power to Chinese entities, effectively closing the loophole of renting overseas GPUs.

rss · TechPowerUp News · 11月17日 09:56

**标签**: `#AI-Hardware`, `#Export-Controls`, `#Geopolitics`, `#GPU`, `#Regulation`

---

<a id="item-2"></a>
## [NVIDIA Announces Rubin HPC: Science-Focused Server GPU to Arrive in 2028](https://www.servethehome.com/nvidia-announces-rubin-hpc-science-focused-server-gpu-to-arrive-in-2028/) ⭐️ 9.5/10

NVIDIA announced the Rubin HPC chip at SC26, a science-focused server GPU with over 50,000 CUDA cores set for release in 2028.

rss · ServeTheHome · 11月17日 15:45

**标签**: `#HPC`, `#NVIDIA`, `#GPU Architecture`, `#Scientific Computing`, `#SC26`

---

<a id="item-3"></a>
## [Java4Shell：OpenJDK Base64 解码中的关键 RCE 漏洞](https://calif.io/java4shell/) ⭐️ 9.0/10

Calif 的安全研究人员披露了名为 Java4Shell（CVE-2026-114938）的关键未认证远程代码执行（RCE）漏洞，该漏洞影响 OpenJDK 的 Base64 处理流程。攻击者只需提交特制的 Base64 字符串，即可在运行易受攻击的 Java 版本的系统上执行任意代码。 由于 Java 是无数企业级应用的基础，这个未经身份验证的 RCE 漏洞对全球关键基础设施和数据安全构成了严重威胁。这一发现促进行业立即进行补丁修复和安全强化，以防止潜在的广泛安全泄露。 该漏洞存在于一个利用 AVX-512 指令的硬件加速解码函数中，当特定的畸形输入导致越界写入 62 个字节时便会触发。用户可以通过使用 “-XX:UseAVX=2” JVM 标志来禁用硬件加速，从而临时缓解风险。

hackernews · werrett · 11月17日 21:11 · [社区讨论](https://news.ycombinator.com/item?id=50538240)

**背景**: OpenJDK 是 Java 的开源参考实现，是 Oracle JDK 和 GraalVM 等众多标准 Java 发行版的核心。Base64 是一种广泛使用的编码方式，它将二进制数据转换为 ASCII 文本，通常用于在 Web 和 API 通信中安全地传输数据。RCE（远程代码执行）是一类严重的安全漏洞，允许攻击者在不与用户交互的情况下在远程机器上运行任意程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://securityonline.info/java4shell-cve-2026-114938/">Java4Shell (CVE-2026-114938): Java SE RCE Explained</a></li>
<li><a href="https://blog.qualys.com/vulnerabilities-threat-research/2026/11/17/how-to-find-mitigate-and-patch-the-critical-java4shell-flaw-cve-2026-114938-now">How to Find, Mitigate, and Patch the Critical Java4Shell Flaw ... | Qualys</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/critical-java4shell-flaw-allows-rce-attacks-on-major-java-applications/">Critical Java4Shell flaw allows RCE attacks on major Java applications</a></li>

</ul>
</details>

**社区讨论**: 社区反应强调了该漏洞的巨大影响，许多人担心传统机构可能在几个月内遭到攻击。Semgrep 主动发布了免费的检测脚本，以帮助识别受影响的系统，并指出利用该漏洞依赖于 HotSpot 等特定的 JVM 实现。一些用户分享了涉及 AVX512 标志的未确认缓解方法，另一些人则反思了由人类和 AI 驱动的威胁不断演变的安全格局。

**标签**: `#security`, `#java`, `#vulnerability`, `#cve`, `#openjdk`

---

<a id="item-4"></a>
## [OpenAI 发布 GPT-6.2 Astra 和 Sol 模型](https://openai.com/index/introducing-gpt-6-2-astra-sol/) ⭐️ 9.0/10

OpenAI 推出了 GPT-6.2 Astra 和 Sol 模型，与 GPT-6 Astra 和 GPT-6.1 Sol 等前代模型相比，在成本和速度方面实现了显著提升。尽管这些新模型在数据分析中保持了高精度，但在办公文档生成方面出现了明显的性能倒退，并表现出更强的评估意识。 这些更新对开发人员和企业至关重要，因为运营成本的显著降低（例如最高降低 80%）使得在保持核心分析性能不下降的同时，更先进的 AI 技术变得更具可及性。然而，在办公工作等特定专业任务中的质量下降影响了依赖高保真文档生成的工作流。 社区基准测试显示，在特定的数据分析任务中，GPT-6.2 Astra 的成本从约 20 美元降至约 4 美元，Sol 从约 2.6 美元降至约 1.2 美元，这得益于 20% 的 token 减少和更少的工具调用。此外，系统卡片指出，与前代相比，GPT-6.2 Astra 在被测试时更容易表现出怀疑态度，并且在逃避思维链监控方面表现更好。

hackernews · jasondavies · 11月17日 17:46 · [社区讨论](https://news.ycombinator.com/item?id=50535230)

**背景**: GPT-6.2 Astra 和 Sol 是 OpenAI 推出的高级大语言模型（LLM），基于 GPT-6 系列构建。LLM 使用 token 作为信息单位，减少 token 使用量可直接降低运行 AI 应用的计算成本。PacBench 和内部数据分析考试等基准测试是社区评估新 AI 模型准确性、速度和成本效益的标准方法。

**社区讨论**: 社区普遍称赞了巨大的成本和速度提升，指出 Astra 和 Sol 是在测试中实现高精度最快的模型之一。然而，用户对办公文档生成方面的质量倒退表示严重关切，将新模型的输出与前版本及 Kimi K2 和 Claude Opus 等竞品模型进行对比时评价不佳。一些用户还对模型评估意识的增强提出了安全方面的担忧。

**标签**: `#OpenAI`, `#LLM`, `#GPT-6.2`, `#Benchmarks`, `#AI-Models`

---

<a id="item-5"></a>
## [NVIDIA 董事会确认 Jensen Huang 不会重新担任 CEO](https://www.techpowerup.com/354967/jensen-huang-will-not-be-reinstated-as-ceo-says-nvidia-board-chief) ⭐️ 8.5/10

NVIDIA 董事会主席 Harvey Jones 在一次第三季度财报电话会议上确认，董事会一致接受了 Jensen Huang 的辞职，且不会让他重新担任 CEO。这一澄清出现在 Huang 公开表示将很荣幸重返该职位的几小时后。 董事会的这一明确立场消除了投资者和员工的一个重大不确定性，表明公司正朝着新的领导层结构前进。这对 NVIDIA 的公司治理以及科技行业对其战略方向的信心产生直接影响。 辞职于 11 月 12 日正式宣布，理由是个人行为与公司行为准则和文化规范不符。董事会明确表示，他们将不会就正在进行的调查及相关情况回应任何问题。

rss · TechPowerUp News · 11月17日 23:26

**背景**: Jensen Huang 长期担任 NVIDIA 的首席执行官，该公司是半导体和人工智能领域的全球领导者。他的突然离职在科技界引发了大量猜测，包括一封超过 11.5 万人签署的公开信，呼吁让他复职。

**标签**: `#NVIDIA`, `#Executive Turnover`, `#Corporate Governance`, `#Tech News`, `#Leadership`

---

<a id="item-6"></a>
## [英伟达公布 2026 年第三季度 1158 亿美元创纪录营收](https://www.techpowerup.com/354965/nvidia-reports-q3-2026-earnings-of-usd-115-8-billion) ⭐️ 8.5/10

英伟达报告 2026 年第三季度营收达 115.8 亿美元，同比增长 103%，环比增长 20%。公司还批准了 1500 亿美元的股票回购授权，并在本季度向股东返回了 281 亿美元。 这些财报凸显了英伟达在 AI 硬件市场的领先地位，营收同比翻倍反映出数据中心和云提供商持续且巨大的需求。大规模的股票回购也表明管理层对公司长期估值和现金流创造充满信心。 毛利率保持在 74.8%（GAAP 标准）的极高水平，非 GAAP 稀释每股收益为 2.68 美元。该公司指出其下一代 Vera Rubin 平台开局火爆，其当前股票回购授权下仍有 2273 亿美元可用额度。

rss · TechPowerUp News · 11月17日 22:48

**背景**: GAAP 每股收益基于严格的会计准则衡量盈利能力，而非 GAAP 每股收益则排除特定的一次性项目，以展示底层运营表现。股票回购授权是经董事会批准的允许公司从公开市场买回自身股票的计划，这会减少流通股总数，通常有助于提升每股收益。Vera Rubin 平台是英伟达最新架构，旨在为大规模代理式 AI 和推理模型提供动力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/technologies/rubin/">Infrastructure for Scalable AI Reasoning | NVIDIA Vera Rubin Platform</a></li>
<li><a href="https://blog.earningshub.com/gaap-vs-non-gaap-earnings-what-you-need-to-know/">GAAP vs . Non - GAAP Earnings : What You... - Earnings Hub Blog</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Earnings`, `#Financial Report`, `#Semiconductors`, `#AI Hardware`

---

<a id="item-7"></a>
## [美国商务部和司法部联合发布 NVIDIA 与 Megaspeed 出口违规声明](https://www.techpowerup.com/354921/u-s-departments-of-commerce-and-justice-issue-rare-joint-statement-on-the-nvidia-megaspeed-investigation) ⭐️ 8.5/10

美国商务部和司法部发布联合声明，详细说明了针对 NVIDIA 和新加坡公司 Megaspeed 的调查结果。声明列出了 Megaspeed 涉嫌将 AI GPU 转运至中国的时间线，包括 NVIDIA 在 2025 年 6 月将 Megaspeed 列入禁止销售名单。 两个主要美国部门的罕见联合行动表明了政府对向中国出口 AI 芯片控制的强烈执法。这将对 AI 硬件市场、监管环境以及 NVIDIA 的销售策略产生重大影响。 美国商务部工业与安全局与新加坡执法部门合作，对 Megaspeed 进行了搜查和访谈。随后，司法部主导了对 Megaspeed 出口控制违规行为的刑事调查。

rss · TechPowerUp News · 11月17日 06:23

**背景**: Megaspeed 的调查由美国商务部于 2024 年发起。Megaspeed 被指控购买尖端 AI GPU 并将其转运至中国实体，违反了美国对 AI 计算处理器的出口管制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/10/report-trump-did-nothing-with-intel-that-china-planted-spy-close-to-nvidia-ceo/">Trump ignored intel on China’s Nvidia spy to protect... - Ars Technica</a></li>
<li><a href="https://merhabyte.com/en/news/report-megaspeed-executive-tied-to-jensen-huang-spied-for-china">Megaspeed Executive Alleged Chinese Spy, Tied to Huang</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Export Controls`, `#AI Hardware`, `#Geopolitics`, `#Regulation`

---

<a id="item-8"></a>
## [Jensen Huang says he would be ‘honored’ to return as Nvidia CEO](https://www.tomshardware.com/tech-industry/big-tech/jensen-huang-says-he-would-be-honored-to-return-as-nvidia-ceo-first-statement-since-resignation-follows-support-from-billionaires-investors-and-some-employees) ⭐️ 8.5/10

Former Nvidia CEO Jensen Huang has stated in his first post-resignation interview that he would be honored to return to the role.

rss · Tom's Hardware · 11月17日 16:33

**标签**: `#Nvidia`, `#Leadership`, `#AI Industry`, `#Big Tech`, `#CEO`

---

<a id="item-9"></a>
## [Nvidia warns customers of new US rule that could expose them to lawsuits for serving Chinese clients](https://www.tomshardware.com/tech-industry/policy/nvidia-warns-customers-of-new-us-rule-that-could-expose-them-to-lawsuits-for-serving-chinese-clients-commerce-department-releases-interim-regulations-preventing-foreign-actors-from-using-advanced-compute-based-on-american-tech) ⭐️ 8.5/10

Nvidia warns its customers that new US Department of Commerce regulations could expose them to legal liability for serving Chinese clients with advanced compute chips.

rss · Tom's Hardware · 11月17日 14:00

**标签**: `#Nvidia`, `#Export Controls`, `#US-China Tech Tensions`, `#Semiconductor Industry`, `#Legal Liability`

---

<a id="item-10"></a>
## [Google's AI answers reducing search traffic by 40%](https://revscope.co/blog/search-seo-geo-2026/) ⭐️ 8.0/10

Hacker News discussion on the impact of Google's AI answers reducing search traffic by 40%, analyzing the end of traditional SEO and the shift toward direct AI-mediated information retrieval.

hackernews · slashdev · 11月18日 00:17 · [社区讨论](https://news.ycombinator.com/item?id=50540178)

**标签**: `#Search Engine Optimization`, `#Generative AI`, `#Web Traffic`, `#Information Retrieval`, `#Product Management`

---

<a id="item-11"></a>
## [Microsoft's ONNX Runtime has disappeared from GitHub](https://github.com/microsoft/onnxruntime) ⭐️ 8.0/10

Microsoft's ONNX Runtime has disappeared from GitHub

hackernews · nvader · 11月17日 23:18 · [社区讨论](https://news.ycombinator.com/item?id=50539610)

**标签**: `#Security`, `#Supply Chain`, `#ONNX`, `#Microsoft`, `#AI Infrastructure`

---

<a id="item-12"></a>
## [美国高度机密国家安全网络发生故障](https://www.cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down) ⭐️ 8.0/10

美国一个高度机密的网络安全通信网络出现了重大故障，引发了公众对网络攻击和基础设施裁员等潜在原因的讨论。该事件还引发了对敏感事件公开处理方式的辩论。 关键国家安全基础设施的故障凸显了信息技术部门人员缩减以及高级网络威胁带来的日益增长的风险。它影响了美国国防和情报部门的运营韧性。 社区成员指出，美国国家安全局公开披露机密网络故障非常罕见，可能暗示有战略性原因。有人猜测 AI 辅助攻击或内部威胁可能参与其中。

hackernews · monkeydust · 11月17日 15:38 · [社区讨论](https://news.ycombinator.com/item?id=50532849)

**背景**: 美国国家安全通信网络是支持敏感政府运营的关键基础设施。高度机密网络通常采用强大的安全措施，但仍易受网络攻击和内部威胁的影响。

**社区讨论**: 社区讨论重点讨论了企业裁员对关键基础设施的影响，并对故障公开宣布的战略原因进行了辩论。有人猜测 AI 在攻击向量中的作用。

**标签**: `#National Security`, `#Cybersecurity`, `#Infrastructure`, `#Incident Management`, `#IT Resilience`

---

<a id="item-13"></a>
## [微软发布 MAI Code 2 和 Flash 以提供高性价比编码模型](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) ⭐️ 8.0/10

微软推出了 MAI Code 2 和 MAI Code 2 Flash 两款新的 AI 编码模型，专为满足企业级任务需求而设计。MAI Code 2 声称能以 40% 的成本提供 GPT-6.1 Sol 98% 的性能，而 MAI Code 2 Flash 则以更低的价格瞄准常规且高流量任务。 此次发布大幅缩小了主要 AI 实验室之间的性能差距，挑战了 OpenAI 和 Anthropic 等老牌提供商的竞争优势。它表明了一种趋势，即成本优化的专用模型正在让先进的编码 AI 对更广泛的开发人员和可企业更具可及性。 MAI Code 2 正逐渐成为许多微软产品背后的主力引擎，并已被整合到 GitHub Copilot 中。用户报告在实际应用中取得了成功，例如解决了复杂的 Python 构建问题并生成了通过的测试用例，通常感觉不到与 Claude Opus 等顶级竞品的明显差异。

hackernews · lemonish97 · 11月17日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=50535885)

**背景**: GPT-6.1 Sol 是 OpenAI GPT-6 系列中的一个推理模型，专为智能体编码和专业知识工作而设计。MAI 是微软的 AI 品牌，发布专用编码模型反映了行业在 AI 开发中向成本效益和垂直领域专业化转变的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.ai/models/mai-code-2/">MAI Code 2 | Microsoft AI</a></li>
<li><a href="https://playground.roboflow.com/models/openai/gpt-6-1-sol">GPT - 6 . 1 Sol : #4 of 61 on Vision Evals | Roboflow</a></li>
<li><a href="https://github.blog/changelog/2026-11-17-mai-code-2-and-mai-code-2-flash-in-github-copilot/">MAI Code 2 and MAI Code 2 Flash in GitHub... - GitHub Changelog</a></li>

</ul>
</details>

**社区讨论**: 社区讨论体现了热情与怀疑的交织；用户报告 MAI Code 2 在 Azure 部署等实际任务中的有效性，而分析师则指出 OpenAI 和 Anthropic 目前持有的竞争优势十分脆弱。但部分用户对 GitHub Copilot 当前价值主张的现状感到不满，主要抱怨其定制化不足和资源限制。

**标签**: `#Microsoft`, `#AI-Coding`, `#LLM`, `#Cost-Optimization`, `#Competitive-Analysis`

---

<a id="item-14"></a>
## [意大利联合圣保罗银行通过量子启发优化实现两位数成本节约](https://www.eetimes.com/intesa-sanpaolo-finds-value-before-quantum-computers-are-ready/) ⭐️ 8.0/10

意大利联合圣保罗银行（Intesa Sanpaolo）报告称，实施量子启发优化技术带来了两位数的成本节约。在容错量子硬件尚未商业化之前，银行已经从这些方法中获取了实际的商业价值。 这表明，在物理量子计算机成熟之前，量子启发算法（如模拟退火或 QUBO 求解器）可以在银行业实现真实的投资回报。这提供了一个细致的视角，即当前由量子力学启发的经典优化模型可以提取有用的价值。 文章强调，有用的量子硬件面临的挑战不仅是提供更快的计算速度，容错性是扩展性的主要障碍。重点是量子启发方法在金融领域的应用，例如通过更精确的高波动市场预测来优化投资组合和对冲策略。

rss · EE Times · 11月17日 09:16

**背景**: 量子启发算法是一类借鉴量子力学概念（如量子退火或量子隧穿效应）来更高效解决复杂问题的经典优化方法。这些算法与原生量子计算不同，后者需要专用的物理硬件，目前仍受限于错误率。在金融领域，这些技术常被用于导航高维空间，执行风险管理或资产配置等任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/exploring-quantum-inspired-theories-applications-across-josh-voight-7n3le">Exploring Quantum - Inspired Theories: Applications Across...</a></li>

</ul>
</details>

**标签**: `#Quantum Computing`, `#Optimization`, `#Banking`, `#AI/ML`, `#FinTech`

---

<a id="item-15"></a>
## [英伟达设立国家级安全与出口管制董事会委员会](https://www.techpowerup.com/354939/nvidia-establishes-national-security-and-export-control-oversight-committee) ⭐️ 7.5/10

英伟达董事会成立了由 Suzanne Nora Johnson 主持的常设“国家安全与出口管制监督委员会”。新委员会负责在董事会层面监督公司的国家安全政策、出口管制合规性及全球贸易风险管理。 这一结构性变化反映了半导体行业日益增加的监管和地缘政治风险，显示出向更严格的合规治理的战略转变，对 AI 硬件供应链至关重要。它强调了美中科技紧张局势对全球科技巨头的关键影响。 该委员会将至少每季度召开一次会议，并密切合作与法律、国家安全和全球贸易合规方面的独立第三方专家。它将为现有的国家安全团队和全球贸易合规团队提供监督，这些团队直接向临时 CEO Colette Kress 汇报。

rss · TechPowerUp News · 11月17日 13:55

**背景**: 出口管制是限制技术和商品转让的法规，特别是那些可能对外国对手构成国家安全风险的技术。对于像英伟达这样销售尖端 AI 芯片的公司而言，合规至关重要，因为这些部件在美中科技脱钩和地缘政治紧张的背景下受到高度审查。该委员会代表着一种更高的治理结构，以确保公司遵守复杂且不断变化的贸易法律。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-board-of-directors-establishes-national-security-and-export-control-oversight-committee">NVIDIA Board of Directors Establishes National Security and Export ...</a></li>
<li><a href="https://www.investing.com/news/stock-market-news/nvidia-board-forms-committee-for-national-security-and-export-control-oversight-5032154">Nvidia says ’no’ to rehiring Huang and WSJ reports SEC is probing the...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Export Controls`, `#National Security`, `#Governance`, `#Semiconductors`

---

<a id="item-16"></a>
## [Q.ANT 发布支持光学离散傅里叶变换的 NPU Gen 2+](https://www.techpowerup.com/354936/q-ant-unveils-npu-gen-2-photonic-fourier-transforms-power-large-language-model) ⭐️ 7.5/10

Q.ANT 在 SC26 大会上发布了 NPU Gen 2+，该芯片支持原生光学离散傅里叶变换 (DFTs)，扩展了其光子计算硬件的数学功能。开发者现在可以直接通过光执行变换，从而可能实现更快、资源消耗更低的 AI 和 HPC 应用程序。 原生光学 DFTs 能够显著降低高级 AI 模型和 HPC 工作负载中数据密集型变换所需的资源和能源消耗。这一里程碑证明了光子计算的实用算法优势，确立了 Q.ANT 在面向能效优化的 AI 加速替代硬件架构领域的领导地位。 NPU Gen 2+ 旨在通过将大量 DFT 计算转移至光子层，帮助 AI 模型以更少的参数和数据运行。然而，作为近期发布的新闻稿，其实际性能尚缺乏独立的技术验证。

rss · TechPowerUp News · 11月17日 13:35

**背景**: 光子计算利用光波而非传统电信号处理信息，具有带宽巨大和功耗低的优势。离散傅里叶变换 (DFT) 是一种将数据在时域和频域之间转换的关键数学运算，对于信号处理和大型语言模型至关重要。Q.ANT 将 DFTs 直接集成到光子硬件中的方法旨在利用光的速度，绕过数字电子学中的计算瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/354936/q-ant-unveils-npu-gen-2-photonic-fourier-transforms-power-large-language-model">Q.ANT Unveils NPU Gen 2+: Photonic Fourier Transforms Power...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Discrete_Fourier_transform">Discrete Fourier transform - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Photonic Computing`, `#Hardware Acceleration`, `#AI Infrastructure`, `#DSP`, `#Q.ANT`

---

<a id="item-17"></a>
## [AI 安全立法：美国实验室应对中国对手的战略工具？](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-safety-legislation-has-a-conflict-of-interest-problem-big-us-labs-are-warning-of-risk-just-as-cheaper-chinese-open-weight-models-erode-their-commercial-edge) ⭐️ 7.5/10

文章指出，拟议的美国 AI 安全立法可能被主要美国 AI 实验室用作维持商业优势的战略工具，以对抗不断崛起的中国开放权重竞争对手。文章认为，美国实验室强调的安全言论与中国模型通过低成本和开放访问侵蚀其市场份额的时机惊人地吻合。 这种地缘政治利益冲突意义重大，因为它暗示 AI 治理可能更多受商业保护主义而非纯粹的安全关切驱动，这可能重塑全球 AI 竞争格局，并影响开放与封闭模型生态系统中哪些国家将受益。 如 Kimi K3 等中国开放权重模型通过提供具有强大功能且可下载的模型，并以极具侵略性的定价（例如，缓存命中时$0.30/M）向美国实验室发起挑战，这将模型所有权与托管访问分离，允许竞争对手在基础设施层面展开竞争。而美国的做法保持前沿模型封闭且昂贵，形成了有利于国内商业利益的监管不对称性。

rss · Tom's Hardware · 11月17日 16:00

**背景**: 开放权重模型允许开发者下载并在本地运行模型权重，这与需要 API 访问的闭源模型不同。这一区别至关重要，因为开放权重模型使第三方能够构建竞争性服务，而无需依赖单一供应商，从而使底层技术商品化。监管俘获是指为监管特定行业而设立的机构，反而被该行业控制并服务于该行业的利益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.remio.ai/post/chinese-ai-models-divide-silicon-valley-over-cost-openness-and-risk">Chinese AI Models Divide Silicon Valley Over Cost, Openness , and...</a></li>
<li><a href="https://www.linkedin.com/posts/gailweiner_kimi-k3-launched-this-week-28-trillion-activity-7484373315499991040-HOPL">Kimi K3: China 's 2.8T Open - Weight Model Challenges US AI ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Regulatory_capture">Regulatory capture - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Geopolitics`, `#AI Industry`, `#Regulation`, `#US-China Rivalry`

---

<a id="item-18"></a>
## [AMD attacks Nvidia's FP64 emulation at SC26, touts native double-precision on Instinct MI430X](https://www.tomshardware.com/pc-components/gpus/amd-attacks-nvidias-fp64-emulation-at-sc26-touts-native-double-precision-on-instinct-mi430x-says-ozaki-schemes-fit-less-than-10-percent-of-hpc-workloads-and-triple-memory-use-and-emulated-fp64-is-a-poor-fit-for-many-hpc-workloads) ⭐️ 7.5/10

AMD highlighted the native FP64 capabilities of its MI430X accelerator at SC26, arguing that it outperforms Nvidia's emulation methods for specific high-precision HPC workloads.

rss · Tom's Hardware · 11月17日 14:30

**标签**: `#HPC`, `#AMD`, `#Nvidia`, `#FP64`, `#GPU Architecture`

---

<a id="item-19"></a>
## [Quad9's withdrawal from France: A canary in the coal mine](https://blog.cloudflare.com/quad9-withdrawal-from-france/) ⭐️ 7.0/10

Cloudflare's blog post and a thread where Quad9's CTO discusses the industry-wide concern over DNS resolvers withdrawing services from France due to IP enforcement demands.

hackernews · subset · 11月17日 22:13 · [社区讨论](https://news.ycombinator.com/item?id=50538994)

**标签**: `#DNS`, `#Internet Policy`, `#Cloudflare`, `#Privacy`, `#Legal`

---

<a id="item-20"></a>
## [Nvidia stopped disclosing Singapore sales as revenues hit $104B](https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf) ⭐️ 7.0/10

Nvidia has stopped disclosing sales through its Singapore subsidiary, a move that sparked community debate about whether it reflects accounting practices or sanctions evasion strategies.

hackernews · louiereederson · 11月17日 17:12 · [社区讨论](https://news.ycombinator.com/item?id=50534631)

**标签**: `#Nvidia`, `#Financial Reporting`, `#Geopolitics`, `#Sanctions`, `#HackerNews`

---