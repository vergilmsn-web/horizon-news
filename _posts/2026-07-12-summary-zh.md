---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 44 条内容中筛选出 13 条重要资讯。

---

1. [SK 海力士 CEO 警告：2027 年将是内存短缺最严重的一年，短缺将持续至 2030 年](#item-1) ⭐️ 9.5/10
2. [Colibrì 概念验证：仅用 25GB 内存运行 1.5TB AI 模型](#item-2) ⭐️ 7.5/10
3. [伪造 Go DNS 扫描工具通过 222 个 GitHub 仓库传播恶意软件](#item-3) ⭐️ 7.5/10
4. [ClickHouse 将 PgBouncer 吞吐量提升至 4 倍](#item-4) ⭐️ 7.0/10
5. [UPI 架构解析：深入了解印度的实时支付巨头](#item-5) ⭐️ 7.0/10
6. [Nvidia RTX 5070 Ti 因导热硅脂涂抹不当在 107°C 降频，热点温度被隐藏](#item-6) ⭐️ 6.5/10
7. [微软碳排放因 AI 扩张激增 25%，2030 气候目标承压](#item-7) ⭐️ 6.5/10
8. [Flock 摄像头误将汽车测评博主识别为"被盗"车辆——警方在商场停车场将其拦截并拘留一小时](#item-8) ⭐️ 6.5/10
9. [智谱 CEO 唐杰发内部信："GLM 时刻"和万亿俱乐部之后，什么是更重要的事](#item-9) ⭐️ 6.3/10
10. [布朗大学教授揭露大规模 AI 作弊；苹果起诉 OpenAI；JAXA 测试可回收火箭](#item-10) ⭐️ 6.3/10
11. [英伟达、CoreWeave 与 Nebius：GPU 热潮背后的循环融资内幕](#item-11) ⭐️ 6.0/10
12. [倡导在 SQLite 中使用 STRICT 表以强制类型约束](#item-12) ⭐️ 6.0/10
13. [AIC 推出配备 32 个 SSD 盘位的闪存 JBOF 服务器，专为键值缓存设计](#item-13) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [SK 海力士 CEO 警告：2027 年将是内存短缺最严重的一年，短缺将持续至 2030 年](https://www.tomshardware.com/pc-components/dram/sk-hynix-says-2027-will-be-the-worst-year-for-memory-shortage-forecasts-crunch-to-last-until-2030-ceo-shares-grim-outlook-on-the-day-sk-hynix-gets-listed-on-nasdaq) ⭐️ 9.5/10

SK 海力士 CEO 郭鲁忠（Kwak Noh-jung）警告称，目前的内存短缺情况将在 2027 年进一步恶化，并表示这一年将是供应紧张的高峰期，紧张的 RAM 供应状况将至少持续到 2030 年。这一严峻展望是在 SK 海力士登陆纳斯达克交易当天发表的。 作为全球三大内存芯片制造商之一，SK 海力士的这一预测对全球科技供应链具有重大影响，预示着 DRAM 和 NAND 闪存的价格将在本十年末之前持续走高，影响消费者、PC 组装商、服务器以及智能手机制造商。短缺的根本原因在于 AI 驱动的 HBM 和高容量内存需求激增，超过了产能扩张的速度。 此次警告的核心集中在 DRAM，特别是用于 AI 加速器的高带宽内存（HBM），其供应受到先进制程产能的限制。SK 海力士通过公司上市主体登陆纳斯达克，使全球投资者能够直接投资一家处于供应高度紧张时期的纯内存芯片公司。

rss · Tom's Hardware · 7月11日 13:00

**背景**: SK 海力士是全球领先的内存半导体制造商之一，主要与三星和美光在 DRAM 和 NAND 闪存市场竞争。内存芯片是几乎所有计算设备的核心组件，从 PC 和智能手机到数据中心和 AI 服务器都离不开它。当需求超过制造产能时，就会出现内存短缺，推高价格并限制整个行业的硬件供应。最近几个周期在很大程度上受到人工智能工作负载的影响，AI 训练和运行大型语言模型需要大量堆叠式 DRAM 构成的高带宽内存（HBM），而这一需求类别在几年前几乎不存在。

**标签**: `#DRAM`, `#SK Hynix`, `#memory-shortage`, `#hardware-supply-chain`, `#semiconductors`

---

<a id="item-2"></a>
## [Colibrì 概念验证：仅用 25GB 内存运行 1.5TB AI 模型](https://www.tomshardware.com/tech-industry/artificial-intelligence/colibri-proof-of-concept-gains-frontier-level-1-5-tb-ai-model-novel-approach-runs-on-only-25gb-of-ram-and-shows-promise-for-local-ai-setups) ⭐️ 7.5/10

Colibrì 是一个用纯 C 语言编写的概念验证项目，展示了通过按需从磁盘流式加载专家（expert），仅用约 25GB 内存和普通 CPU 即可运行前沿级 1.5TB AI 模型（据报道为 GLM-5.2，744B 参数的 MoE 模型）。 如果该方案得到验证，将显著降低本地运行前沿级别模型的硬件门槛，使爱好者和小机构无需数据中心 GPU 或昂贵的高内存工作站就能体验最先进的 AI 模型。 Colibrì 利用混合专家（MoE）架构，对每个 token 反复加载和卸载所需的专家，密集常驻内存仅约 9.9GB。已公布的基准测试速度极慢，仅为 0.05–1 tokens/s，并采用 MTP（多 token 预测）推测解码；目前尚未披露与 Unsloth 或 llama.cpp 的正式质量或延迟对比数据。

rss · Tom's Hardware · 7月11日 11:30

**背景**: 大语言模型（LLM）通常需要与其参数量成正比的内存——1.5TB 的 FP16 模型一般需要超过 1TB 的 RAM 或显存。混合专家（MoE）模型（如 GLM-5.2）在每个 token 上仅激活一小部分参数，这为将大部分权重保留在磁盘上并按需加载提供了可能。量化（如 4-bit 或 8-bit）和 CPU 卸载是将大模型适配到普通硬件的成熟技术，llama.cpp 和 Unsloth 等工具已经使消费级机器本地推理数百亿参数以内的模型成为现实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/colibri-proof-of-concept-gains-frontier-level-1-5-tb-ai-model-novel-approach-runs-on-only-25gb-of-ram-and-shows-promise-for-local-ai-setups">Colibrì proof - of - concept gains frontier-level 1.5-TB AI model — novel...</a></li>
<li><a href="https://explainx.ai/blog/colibri-glm-5-2-streaming-disk-25gb-ram-july-2026">Colibrì GLM-5.2 — 25 GB RAM Local Guide | explainx. ai ... | explainx. ai</a></li>
<li><a href="https://markaicode.com/memory-optimization-techniques-large-models-limited-ram/">Memory Optimization Techniques: Running Large Models on Limited RAM | Markaicode</a></li>

</ul>
</details>

**社区讨论**: 该新闻未附社区评论，但相关报道反映出谨慎乐观的态度：观察者指出，虽然按需从磁盘流式加载专家是针对 MoE 的巧妙技巧，但 0.05–1 tok/s 的速度使其目前难以用于交互式场景，更像是研究演示而非可直接部署的方案。

**标签**: `#local-ai`, `#model-compression`, `#edge-compute`, `#LLM`, `#memory-optimization`

---

<a id="item-3"></a>
## [伪造 Go DNS 扫描工具通过 222 个 GitHub 仓库传播恶意软件](https://www.tomshardware.com/tech-industry/cyber-security/fake-go-dns-scanner-published-700-malicious-versions-before-researchers-traced-it-to-222-github-repos) ⭐️ 7.5/10

一个伪装成 Go DNS 扫描工具的恶意软件包，被命名为"Operation Muck and Load"行动，自今年 1 月 24 日以来已在 222 个 GitHub 仓库中发布了 700 个恶意版本，累计版本数超过 1,200 个。 该攻击活动针对 Go 生态系统，而 Go 广泛应用于云基础设施和后端服务，因此无意间导入这些包的开发者可能已经将构建流水线和生产系统暴露给恶意软件。 恶意软件利用 GitHub 的开源托管服务通过包管理器分发恶意代码，攻击者使用了异常高的版本号（超过 1,200 个），可能是为了规避 Go 模块中常用的简单版本锁定防御措施。

rss · Tom's Hardware · 7月11日 11:00

**背景**: 供应链攻击是指网络犯罪分子入侵受信任的第三方软件或依赖项，从而渗透用户系统。Go 模块是 Go 语言的依赖管理系统，允许开发者为其项目指定和版本化管理外部包，以实现可复现的构建。由于 Go 项目通常直接从 GitHub 等公共仓库拉取依赖，伪装成 DNS 扫描工具等合法工具的恶意包很容易被开发者无意中导入。DNS 扫描工具是一种用于查询和审计 DNS 记录以进行故障排除和安全评估的实用程序，因此伪造版本对网络管理员和开发者来说是合理的诱饵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/learning/security/what-is-a-supply-chain-attack/">What is a supply chain attack?</a></li>
<li><a href="https://earthly.dev/blog/go-modules/">Understanding Go Package Management and Modules - Earthly Blog</a></li>
<li><a href="https://go.dev/ref/mod">Go Modules Reference - The Go Programming Language</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#supply-chain-attack`, `#Go`, `#malware`, `#GitHub`

---

<a id="item-4"></a>
## [ClickHouse 将 PgBouncer 吞吐量提升至 4 倍](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres) ⭐️ 7.0/10

ClickHouse 发布了一篇详细的工程实践文章，介绍了他们如何在托管 Postgres 服务上将 PgBouncer 的吞吐量提升至 4 倍，重点解决了会话池化、实例间 peering 以及取消请求处理等方面的挑战。 PgBouncer 是最广泛使用的 PostgreSQL 连接池之一，在大规模场景下进行高效的连接池化管理是运行高吞吐量 Postgres 工作负载的团队的常见痛点。本文为水平扩展 PgBouncer 同时保留查询取消等关键功能提供了实用的实践方案，对任何大规模运行 Postgres 的团队都具有参考价值。 其解决的核心问题是：在单一入口后运行多个 PgBouncer 实例会破坏取消请求的路由——取消请求如果落在从未拥有该查询的进程上就会被静默丢弃。PgBouncer 的 peering 功能可以将取消请求转发给正确持有会话的对等进程，从而解决该问题。ClickHouse 团队在 Kubernetes 上部署了该方案，充分利用了 Kubernetes 天然适合多进程和分布式部署的特性。

hackernews · saisrirampur · 7月11日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=48872874)

**背景**: PgBouncer 是 PostgreSQL 的轻量级连接池，部署在客户端和数据库服务器之间，通过复用少量后端连接来服务大量客户端连接。它支持多种池化模式——会话池（只在客户端断开时才归还连接）、事务池（每个事务结束后归还）和语句池。当通过运行多个 PgBouncer 实例来提升吞吐量时，PostgreSQL 的取消请求协议会出现问题：取消消息包含绑定到特定 PgBouncer 进程所持有的后端连接的密钥，如果取消请求到达了错误的进程，就会丢失。PgBouncer 的 peering 机制允许实例之间互相感知，并将取消请求转发给正确的对等进程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pgbouncer.org/config.html">PgBouncer config</a></li>
<li><a href="https://www.crunchydata.com/blog/postgres-at-scale-running-multiple-pgbouncers">Postgres at Scale: Running Multiple PgBouncers | Crunchy Data Blog</a></li>
<li><a href="https://www.pgbouncer.org/changelog.html">PgBouncer changelog</a></li>

</ul>
</details>

**社区讨论**: 评论者深入参与了技术细节的讨论：一位用户对 PostgreSQL 中 peering 的底层工作原理提出了澄清性问题，另一位用户推荐了 Yandex 的 Odyssey（可扩展的连接池）作为替代方案，还有一位用户分享了自己使用 pgdog 的良好体验。多位评论者指出，在 Kubernetes 中运行多个 PgBouncer 实例非常简单，并且有助于缓解云服务商滚动重启导致的故障。也有用户质疑 peering 在独立 Kubernetes Pod 之间能否正常工作，因为每个 Pod 都拥有独立的连接池。

**标签**: `#postgresql`, `#pgbouncer`, `#database`, `#scaling`, `#infrastructure`

---

<a id="item-5"></a>
## [UPI 架构解析：深入了解印度的实时支付巨头](https://timeseriesofindia.com/economy/reads/upi-architecture/) ⭐️ 7.0/10

一篇详细的技术分析文章深入拆解了印度的统一支付接口（UPI）如何通过 NPCI 交换机路由和处理数十亿笔交易，该交换机由印度国家支付公司（NPCI）运营。文章从虚拟支付地址（VPA）、银行集成到结算与对账流程，系统性地分析了其分层架构。 UPI 是全球最大的实时支付系统，每日处理超过 6.4 亿笔交易，超越了 Visa。对于系统架构师和金融科技工程师来说，了解 UPI 如何以相对精简的基础设施实现如此规模，对于学习分布式系统设计、互操作性和公共数字基础设施具有重要参考价值。 2025 年 8 月，UPI 处理了约 200 亿笔交易，总金额达 25 万亿卢比（约 2930 亿美元），平均每秒约 7500 笔，且高峰时段会出现显著峰值。与银行卡网络不同，UPI 使用虚拟支付地址而非交换银行卡号，并通过银行端集成而非集中的代币化账本进行操作，从而降低了单点故障风险。

hackernews · prtk25 · 7月11日 16:33 · [社区讨论](https://news.ycombinator.com/item?id=48873457)

**背景**: UPI 由印度国家支付公司（NPCI）于 2016 年推出，建立在即时支付服务（IMPS）基础设施之上，是一个实时银行间支付系统。它允许任何银行账户持有人使用虚拟支付地址（VPA），例如手机号码或用户名，进行收付款，无需共享银行账号或 IFSC 代码。UPI 采用四方模型，涉及付款方、收款方、付款方 PSP（支付服务提供商）银行和收款方 PSP 银行，NPCI 充当中央交换机和清算实体。基于移动二维码的支付已成为主流用例，使包括街头小贩在内的任何规模的商户都能接受数字支付。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unified_Payments_Interface">Unified Payments Interface - Wikipedia</a></li>
<li><a href="https://www.pib.gov.in/PressNoteDetails.aspx?ModuleId=3&NoteId=154912&reg=3&lang=2">India's UPI Revolution</a></li>
<li><a href="https://dev.to/zeeshanali0704/system-design-upi-unified-payment-interface-2ng3">System Design: UPI ( Unified Payment Interface ) - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 社区评论者对 UPI 背后的工程团队表达了深切敬意，同时也提出了批判性观点。一位评论者计算出 NPCI 交换机平均约 700 QPS，并与 Nasdaq 高峰期超过 10 万 QPS 进行比较，认为其工作量在技术上可控。另一位评论者则对集中化、KYC 要求以及它是私人货币网络这一事实表示担忧。第三位评论者指出，与中国的支付宝和微信支付相比（后者在约 2010 年就已流行），移动二维码支付在技术上并无创新，但承认 UPI 在处理如此规模交易量方面取得了非凡成就。

**标签**: `#payments`, `#distributed-systems`, `#architecture`, `#fintech`, `#india`

---

<a id="item-6"></a>
## [Nvidia RTX 5070 Ti 因导热硅脂涂抹不当在 107°C 降频，热点温度被隐藏](https://www.tomshardware.com/pc-components/gpus/hotspot-temperature-sensor-on-nvidias-blackwell-gaming-gpus-is-still-accessible-if-you-have-access-to-nvidias-internal-mods-tool-nvidia-rtx-5070-ti-caught-throttling-at-107-c-over-poor-tim-application) ⭐️ 6.5/10

Nvidia 已将其 Blackwell RTX 50 系列显卡公开可读的热点温度传感器数据移除，但 Nvidia 自家的内部诊断工具 MODS（模块化诊断软件）仍能读取这些隐藏数据。使用 MODS 检测发现，至少有一块 RTX 5070 Ti 的热点温度达到 107°C 并触发热降频，原因很可能是 GPU 核心与散热器之间的导热界面材料（TIM）涂抹不当。 此事值得关注，因为它暗示 Nvidia 故意向消费者隐藏了热点温度数据，可能是因为部分 RTX 5070 Ti 存在导热不良导致严重降频的问题。依赖 HWiNFO 或 GPU-Z 等标准监控工具的买家和发烧友已无法轻松检测这种过热情况，从而难以识别有缺陷的产品或根据热点温度数据提出保修索赔。 热点传感器测量的是 GPU 核心上最热的那一个点，温度可能远高于平均边缘温度，现代 Nvidia 显卡的热点温度超过 110°C 通常会触发降频。MODS 是 Nvidia 内部的一套诊断工具，从公司泄露后被第三方维修店广泛使用；它能提供比消费级工具详细得多的遥测数据，包括对隐藏传感器的访问权限。

rss · Tom's Hardware · 7月11日 16:18

**背景**: GPU 上的热点温度传感器测量的是处理器核心上温度最高的那个点，通常比向消费者显示的平均温度要高。导热界面材料（TIM），一般是导热硅脂，涂在 GPU 核心和散热器之间以传导热量；如果涂抹不均匀或用量不足，就会产生空气间隙，大幅降低散热效率。Nvidia 的 MODS（模块化诊断软件）是一套内部诊断工具，最初从公司泄露，目前被维修技术人员和硬件评测者广泛使用，可以访问标准消费级软件无法获取的详细 GPU 遥测数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rkblog.dev/posts/pc-hardware/nvidia-modular-diagnostic-software-mods/">Nvidia Modular diagnostic software - MODS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Thermal_paste">Thermal paste - Wikipedia</a></li>
<li><a href="https://www.needsomefun.net/gpu-hotspot-temperature-monitor-fix/">GPU Hotspot Temperature : How to Monitor It and Fix 90°C+...</a></li>

</ul>
</details>

**标签**: `#nvidia`, `#rtx-5070-ti`, `#gpu-thermals`, `#blackwell`, `#hardware`

---

<a id="item-7"></a>
## [微软碳排放因 AI 扩张激增 25%，2030 气候目标承压](https://www.tomshardware.com/tech-industry/big-tech/microsoft-struggles-to-fulfill-its-2030-sustainability-promise-amid-carbon-heavy-ai-expansions-the-companys-chief-sustainability-officer-claims-the-target-is-still-feasible) ⭐️ 6.5/10

微软 2025 财年的碳排放量因 AI 数据中心的快速扩张而上升了 25%，尽管公司在节水和减废方面取得了一定进展。微软首席可持续发展官仍坚持认为，2030 年实现碳负排放的目标是可以达成的。 这一进展凸显了 AI 行业巨大的能源需求与企业气候承诺之间日益加剧的矛盾，影响着公司在技术增长与环境责任之间如何取得平衡。它表明，即使是拥有大量可持续发展资源的科技巨头，也难以将 AI 基础设施的扩张与净零排放承诺相协调。 即便微软在节水和减废方面取得了进展，碳排放仍然增加了 25%，这表明数据中心的电力消耗（很可能用于 AI 训练和推理工作负载）是推高碳足迹的主要因素。微软的 2030 承诺超越了碳中和，目标是实现碳负排放，即计划从大气中清除的碳量超过其排放量。

rss · Tom's Hardware · 7月11日 12:45

**背景**: 碳中和是指企业排放的温室气体与从大气中清除的等量温室气体相平衡，而碳负排放更进一步——要求企业清除的碳量超过其排放量。微软在 2020 年 1 月做出了这一雄心勃勃的 2030 年碳负排放承诺，同时还承诺到 2050 年清除自 1975 年成立以来公司排放的所有碳。当前的挑战反映出，AI 工作负载（尤其是大语言模型训练和推理）需要巨大的计算资源和能源，使得 AI 的快速扩张与激进的减排时间表从根本上存在冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2020/jan/16/microsoft-carbon-emissions-negative-2030">Microsoft pledges to be ' carbon negative ' by 2030 | The Guardian</a></li>
<li><a href="https://www.microsoft.com/en-us/corporate-responsibility/sustainability/carbon-removal-program">Carbon Removal Program | Microsoft CSR</a></li>

</ul>
</details>

**标签**: `#microsoft`, `#sustainability`, `#AI-infrastructure`, `#carbon-emissions`, `#data-centers`

---

<a id="item-8"></a>
## [Flock 摄像头误将汽车测评博主识别为"被盗"车辆——警方在商场停车场将其拦截并拘留一小时](https://www.tomshardware.com/tech-industry/big-tech/flock-cameras-mistakenly-track-car-reviewer-over-stolen-tags-police-ambush-tester-in-store-parking-lot-and-detain-him-for-an-hour) ⭐️ 6.5/10

Flock AI 车牌识别摄像头误读了一块非标准的新泽西州车牌，触发虚假的"被盗车牌"警报，导致警方将一名汽车测评博主拘留了一小时。

rss · Tom's Hardware · 7月11日 10:30

**标签**: `#computer-vision`, `#AI-failures`, `#surveillance`, `#license-plate-recognition`, `#public-safety`

---

<a id="item-9"></a>
## [智谱 CEO 唐杰发内部信："GLM 时刻"和万亿俱乐部之后，什么是更重要的事](https://36kr.com/newsflashes/3891162734689031?f=rss) ⭐️ 6.3/10

智谱 AI CEO 唐杰发布内部信，标志公司战略转向——从短期商业化转向基础 AGI 研究。此前公司市值增长了 10 倍，并进入万亿港元估值俱乐部。

rss · 36氪 · 7月11日 11:35

**标签**: `#Zhipu AI`, `#AGI`, `#Chinese AI`, `#AI strategy`, `#corporate announcement`

---

<a id="item-10"></a>
## [布朗大学教授揭露大规模 AI 作弊；苹果起诉 OpenAI；JAXA 测试可回收火箭](https://www.solidot.org/story?sid=84806) ⭐️ 6.3/10

本期新闻摘要涵盖三个事件：(1) 布朗大学经济学教授 Roberto Serrano 发现学生在家完成期中考试时大部分获得满分或接近满分，怀疑大规模使用 AI 作弊，于是将期末考试改为线下——结果 18 名学生退课，期末平均分降至历史最低的 48.6%。(2) 苹果起诉 OpenAI，指控其窃取商业机密，涉及 OpenAI 首席硬件官 Tang Tan 和前苹果工程师 Chang Liu，指控 Tan 指导从苹果跳槽的员工规避安全流程，Liu 则被控下载机密硬件文件。(3) JAXA 成功测试了可回收火箭原型 RV-X，悬停至 11 米高度，完成水平移动和垂直着陆，整个飞行持续约 40 秒。 这些报道共同揭示了 AI 时代的紧张关系：AI 工具正以超出检测能力的速度侵蚀学术诚信，科技巨头之间的人才流动引发了可能重塑 AI 硬件开发的知识产权战争，而在可回收火箭领域，日本明显落后于中国，全球竞争正在加剧。AI 作弊案件对那些努力在大型语言模型时代维持评估有效性的教育工作者来说尤为紧迫。 期中考与期末考成绩差距惊人：期末考试成绩此前从未低于 65%，改为线下考试后，9 名学生未参加期末考试，3 人得零分，平均分降至 48.6%。在苹果案件中，Liu 据称通过认证漏洞访问了同事的笔记本电脑，并留下'LOL'的信息。JAXA 的 RV-X 计划取代不可回收的 H-3 火箭，未来测试目标为 100 米高度，项目有法国和德国参与合作。

rss · Solidot · 7月11日 16:40

**背景**: 以 ChatGPT 为代表的大型语言模型自 2022 年末发布以来，让学生能够轻松生成高质量的论文和考试答案，引发了持续的学术诚信危机。苹果起诉 OpenAI 反映了 AI 硬件人才竞争日益激烈，据报道 OpenAI 开出价值数百万美元的薪酬包来吸引苹果等竞争对手的专家。JAXA 的 RV-X 加入了目前由 SpaceX 的猎鹰 9 号和中国公司引领的全球可回收火箭竞赛——中国在 2026 年 7 月 10 日成功着陆了可回收的长征十号乙火箭，仅比 JAXA 的测试早一天。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aa.com.tr/en/asia-pacific/japan-tests-prototype-reusable-rocket/3994840">Anadolu Ajansı: Japan tests prototype reusable rocket</a></li>
<li><a href="https://www.indiatoday.in/world/story/japan-reusable-rocket-test-jaxa-rv-x-completes-first-flight-and-landing-ptag-2945400-2026-07-11">Japan reusable rocket test: JAXA 's RV - X completes first... - India Today</a></li>
<li><a href="https://newspaceeconomy.ca/2026/07/11/what-does-japans-reusable-rocket-test-mean-for-h3-mhi-and-the-launch-market/">What Does Japan ’s Reusable Rocket Test... | New Space Economy</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#education`, `#Apple`, `#OpenAI`, `#space technology`

---

<a id="item-11"></a>
## [英伟达、CoreWeave 与 Nebius：GPU 热潮背后的循环融资内幕](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) ⭐️ 6.0/10

本文分析了英伟达与 GPU 新云服务商（CoreWeave、Nebius）之间的投资关系，并探讨在更广泛的 AI 基础设施资本流动背景下，针对循环融资的担忧是否被夸大。

hackernews · adletbalzhanov · 7月11日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48873836)

**标签**: `#AI infrastructure`, `#Nvidia`, `#investment analysis`, `#GPU cloud`, `#industry economics`

---

<a id="item-12"></a>
## [倡导在 SQLite 中使用 STRICT 表以强制类型约束](https://evanhahn.com/prefer-strict-tables-in-sqlite/) ⭐️ 6.0/10

Evan Hahn 发表了一篇文章，建议开发者优先使用 SQLite 的 STRICT 表功能来强制列类型约束。作为回应，Simon Willison 为他的 sqlite-utils 工具新增了 `transform` 命令，方便在严格表和非严格表之间轻松转换。 SQLite 默认的动态类型机制可能让类型不匹配的问题悄无声息地破坏数据，当多个应用共享同一数据库时风险更大。采用 STRICT 表可以在 schema 层面提供更强的数据完整性保障，类似于传统静态类型数据库。 STRICT 表（于 2021 年 11 月 27 日随 SQLite 3.37.0 引入）只允许五种类型：INT、INTEGER、REAL、TEXT、BLOB 和 ANY。然而，SQLite 本身不提供原生的 ALTER TABLE 迁移方式，转换需要复制数据——这正是 sqlite-utils 新增的 `transform` 命令所填补的空白。

hackernews · ingve · 7月11日 17:33 · [社区讨论](https://news.ycombinator.com/item?id=48873940)

**背景**: 与大多数 SQL 数据库不同，SQLite 使用动态（manifest）类型机制，意味着它会尝试将插入的值强制转换为列所声明的类型亲和性，而不是拒绝不匹配的值。STRICT 表（随 SQLite 3.37.0 引入）则放弃了这种灵活性，会拒绝与声明类型不精确匹配的值。支持者认为这可以防止静默的数据损坏，而 SQLite 的维护者则认为动态类型让错误更容易被发现和修复——这是一场设计哲学的争论，文章和评论对此进行了探讨。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://antonz.org/sqlite-strict-tables/">STRICT tables in SQLite</a></li>
<li><a href="https://www.sqlite.org/datatype3.html">Datatypes In SQLite</a></li>

</ul>
</details>

**社区讨论**: 讨论显示社区普遍认同 STRICT 表的价值，尤其是那些来自企业 SQL 背景、此前对 SQLite 持怀疑态度的开发者。一个关键分歧在于：一部分用户希望 STRICT 成为默认行为，而 SQLite 维护者（根据 flextypegood.html 的解释）则认为灵活性更可取。Simon Willison 贡献的迁移工具获得了广泛赞赏，但也有用户指出实际使用中的局限性，例如严格表中缺少原生的 Date 类型。

**标签**: `#sqlite`, `#databases`, `#type-systems`, `#sql`, `#data-integrity`

---

<a id="item-13"></a>
## [AIC 推出配备 32 个 SSD 盘位的闪存 JBOF 服务器，专为键值缓存设计](https://www.servethehome.com/aic-gets-flashy-with-32-ssd-bay-jbof-server-for-key-value-caching/) ⭐️ 5.5/10

AIC 发布了一款 2U JBOF 服务器，配备 32 个 E3 SSD 盘位，专为键值缓存设计，并搭配 BlueField-4 DPU，面向 Rubin Vera GPU 时代。

rss · ServeTheHome · 7月11日 17:00

**标签**: `#storage`, `#JBOF`, `#key-value-caching`, `#AI-infrastructure`, `#DPU`

---