---
layout: default
title: "Horizon Summary: 2026-10-26 (ZH)"
date: 2026-10-26
lang: zh
---

> 从 46 条内容中筛选出 11 条重要资讯。

---

1. [修改者破解固件限制，提升 RTX GPU AI 计算性能最高达 2 倍](#item-1) ⭐️ 8.5/10
2. [十年前的 CNN 在皮肤癌诊断中胜过前沿 LLM](#item-2) ⭐️ 8.0/10
3. [OpenAI 与 Anthropic 将 LLM 价格下调高达 80%](#item-3) ⭐️ 8.0/10
4. [英伟达考虑为企业级 AI 智能体平台收取 2000 美元年度 GPU 费用](#item-4) ⭐️ 7.5/10
5. [英伟达探索将德国退役核电站改建为 AI 数据中心](#item-5) ⭐️ 7.5/10
6. [三星电视被发现收集音频和截图用于广告定向](#item-6) ⭐️ 7.5/10
7. [英伟达 CEO 黄仁勋估算 AI 代理的年度 GPU 成本为 2000 美元](#item-7) ⭐️ 6.5/10
8. [Playden 让越狱 PS5 通过 Wine 运行 Steam 游戏](#item-8) ⭐️ 6.5/10
9. [Linux 工具使旧主板上的 Intel Arc 显卡支持 Resizable BAR](#item-9) ⭐️ 5.5/10
10. [AI 驱动的科技巨头与标普 500 间的财务鸿沟加剧](#item-10) ⭐️ 5.5/10
11. [乌克兰无人机打击俄罗斯财政部戈罗杰茨数据中心](#item-11) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [修改者破解固件限制，提升 RTX GPU AI 计算性能最高达 2 倍](https://www.techpowerup.com/354110/geforce-unlocked-modders-boost-rtx-20-rtx-30-and-rtx-40-compute-performance-by-up-to-2x) ⭐️ 8.5/10

修改者为英伟达 RTX 30 系列和 40 系列消费级 GPU 开发了固件补丁，移除了人为的指令速率限制。这些解锁使 FP16 和 BF16 张量吞吐量提升高达 2 倍，使消费级显卡在 AI 工作负载中能够达到高端专业版 RTX 6000 GPU 的性能。 这一发现通过为现有硬件提供免费的、显著的性价比提升，对 AI 和机器学习从业者产生了重大影响。它通过证明底层硅片完全有能力实现更高的吞吐量，挑战了英伟达消费级与专业级 GPU 之间的人为价格差距。 具体测试显示，解锁后 RTX 4090 的 FP16 张量吞吐量达到 331.6 万亿次浮点运算（TeraFLOPS），而其标准值为 165.6 TeraFLOPS。报告指出，解锁前后的输出结果在比特级别保持一致，证实改进在于速度而非计算精度。

rss · TechPowerUp News · 10月25日 08:14

**背景**: 英伟达生产的消费级 GeForce GPU 和专业版 RTX PRO/DAVID GPU 基于相同的物理芯片裸片。然而，消费级显卡在销售时带有固件限制，从而限制了其在计算密集型任务中的指令发射速率。这些限制旨在保护价格远高于消费级对应产品的专业级产品线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Zagitta/gpu-unlock">Zagitta/gpu-unlock: Unlock FP/ BF 16 instruction issue rate on Nvidia ...</a></li>
<li><a href="https://daily.dev/posts/gpu-unlock-fp-bf16-instruction-issue-rate-on-nvidia-3000-s-cards-kbbkhu5nr">GPU-unlock: FP/ BF 16 instruction issue rate on Nvidia ...</a></li>
<li><a href="https://www.techpowerup.com/354110/geforce-unlocked-modders-boost-rtx-20-rtx-30-and-rtx-40-compute-performance-by-up-to-2x">GeForce Unlocked: Modders Boost RTX 20, RTX 30, and RTX 40 ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#GPU`, `#AI`, `#Hardware`, `#Performance`

---

<a id="item-2"></a>
## [十年前的 CNN 在皮肤癌诊断中胜过前沿 LLM](https://lynchlab.net/llm-skin-cancer) ⭐️ 8.0/10

一个使用 Inception v3 的十年前的卷积神经网络（CNN）在皮肤癌病灶分类任务中优于两个前沿大语言模型（LLM）。这一结论基于在保留测试集上的特定对比得出。 该结果凸显了在医学影像等高风险、领域特定的视觉任务中，专业化的小型模型依然具有优势，从而挑战了通用 LLM 能替代所有 AI 任务的观点。此外，它也引发了人们对 LLM 评估中可能存在的数据泄露或不公平基准测试的担忧。 该 CNN 使用单个 H100 GPU 在 ISIC Archive 的 68,011 张图像上进行微调，同时严格将特定测试病灶从所有训练集和验证集中剔除，以防止数据污染。评论者指出，这种严格的剔除可以被视为“基准测试作弊”（benchmaxxing），即模型被专门调优以在特定基准测试中胜出，而缺乏真正的实用性。

hackernews · sungam · 10月25日 17:15 · [社区讨论](https://news.ycombinator.com/item?id=50233779)

**背景**: 像 Inception v3 这样的卷积神经网络（CNN）是专门设计用于从图像中提取空间特征的建筑结构，使其在图像分类方面非常高效。大语言模型（LLM）是原本为文本设计的通用 Transformer，它们已被适配用于视觉任务，但在特定的诊断任务中，它们往往缺乏专门 CNN 的空间专门性和效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2505.23503v2">Can Large Language Models Challenge CNNs in Medical Image ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员强烈认同专门的分类器在狭窄领域优于 LLM，并类比了计算器在数学上胜过 LLM，或专门的围棋 AI 在围棋上胜过 LLM。然而，关于方法论也存在激烈的辩论，有人认为严格的排除数据是一种人为的“基准测试作弊”（benchmaxxing），其目的仅仅是证明 LLM 的劣势，而非展示真正的临床价值。

**标签**: `#Machine Learning`, `#Computer Vision`, `#LLM Limitations`, `#Medical AI`, `#Model Benchmarking`

---

<a id="item-3"></a>
## [OpenAI 与 Anthropic 将 LLM 价格下调高达 80%](https://minimaxir.com/2026/10/cheap-llms/) ⭐️ 8.0/10

OpenAI 和 Anthropic 在几个月内将 LLM API 价格大幅下调了高达 80%。这一激进的定价调整加剧了大语言模型市场的竞争。 这场价格战大幅降低了开发者和企业采用 AI 的门槛。它可能表明行业正转向由有限需求和 GPU 产能利用率驱动的基于销量的竞争。 社区分析表明，DeepSeek 高效的成本结构（如单 GPU 的高 Token 吞吐量）促使大型玩家优化自身的推理成本。此外，人们还担心这些补贴价格是否掩盖了数据隐私风险，或是否是旨在禁止开源竞争对手的战略性监管手段。

hackernews · minimaxir · 10月25日 21:11 · [社区讨论](https://news.ycombinator.com/item?id=50236102)

**背景**: 大型语言模型（LLM）通常通过按百万 Token 计费的 API 访问。推理成本严重依赖于 GPU 效率和优化技术。近期，市场见证了来自 Kimi 和 GLM 等中国开源模型的激烈竞争，这些模型提供更低的价格和更少的内容限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.businessinsider.com/sam-altman-dario-amodei-anthropic-openai-rivalry-timeline-2026-2">A Timeline of Anthropic and OpenAI 's Rivalry - Business Insider</a></li>
<li><a href="https://venkyrao.medium.com/llm-the-good-and-the-bad-e9cb32fddb6d">LLMs : The Good and The Bad. A Comparative Study on the Cost of</a></li>

</ul>
</details>

**社区讨论**: 用户们辩论称，降价是由真正的竞争驱动，还是为了游说政府禁止来自中国的开源模型而进行的战略性举措。一些人指出了 DeepSeek 单 GPU 的低收入，而另一些人则对数据隐私以及使用用户生成内容来补贴成本表示担忧。未使用 GPU 容量的高昂成本也被认为是迫使降价的一个因素。

**标签**: `#LLM`, `#AI-Pricing`, `#OpenAI`, `#Anthropic`, `#Tech-Industry`

---

<a id="item-4"></a>
## [英伟达考虑为企业级 AI 智能体平台收取 2000 美元年度 GPU 费用](https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform) ⭐️ 7.5/10

据报道，英伟达 CEO 黄仁勋正在考虑为其新企业级 AI 智能体平台收取每块 GPU 约 2000 美元的年度软件费。若售出 500 万份许可证，该模式每年可能产生高达 100 亿美元收入，但具体定价和时间表尚未确认。 从一次性硬件销售转向经常性软件收入，增强了英伟达在 AI 基础设施生态系统中的绑定效应。这一战略契合行业趋势，即云服务商和企业越来越多地为优化的 AI 智能体能力付费，而不仅仅是购买原始算力。 据报道，每块 GPU 2000 美元的费用已是英伟达现有企业级 AI 软件平台收费的两倍以上。100 亿美元的潜在收入目标假设将售出 500 万份许可证，这需要拥有庞大的现有 GPU 安装基础。

rss · Tom's Hardware · 10月25日 13:00

**背景**: 英伟达目前的收入主要来自 GPU 和 AI 硬件销售，但其正通过其 NIM 和 NeMo 软件栈，借助智能体工具提升附加值。NIM 提供加速推理微服务以运行 AI 模型，而 NeMo 提供用于数据准备和智能体护栏的库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intelligenthq.com/nvidia-ecosystem/solutions/enterprise-ai-agents/">Enterprise AI and Agents with NVIDIA NIM , NeMo and... | IntelligentHQ</a></li>
<li><a href="https://developer.nvidia.com/nim">NIM for Developers | NVIDIA Developer</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI Infrastructure`, `#Business Strategy`, `#SaaS`, `#Enterprise AI`

---

<a id="item-5"></a>
## [英伟达探索将德国退役核电站改建为 AI 数据中心](https://www.tomshardware.com/tech-industry/data-centers/nvidia-eyes-converting-old-nuclear-plants-into-massive-ai-data-centers-reusing-shut-down-german-energy-sites-could-reduce-the-cost-and-timeline-of-building-from-scratch) ⭐️ 7.5/10

英伟达与普鲁士电力公司正在开展联合研究，评估德国的退役核电厂址能否被改造为 AI 数据中心。该计划旨在利用现有的工业基础设施来加速 AI 部署周期。 改造前核电站址可能通过免去数年的土地审批和高压电网连接难题，大幅降低建设大规模 AI 设施的成本并缩短部署时间。该策略直接缓解了当前阻碍全球 AI 发展的关键基础设施和能源瓶颈。 该项目并非利用现役核电进行计算，而是重新利用退役核电站遗留的土地、冷却水基础设施和现有电网连接。目前项目仍处于探索阶段，尚无具体投资或选址决定。

rss · Tom's Hardware · 10月25日 10:30

**背景**: 普鲁士电力公司负责德国八座核电站的退役工作，并正寻求对这些场址进行有效再利用。新建 AI 数据中心在获取土地、冷却水源和高压电网接入方面面临巨大阻力，而前核电站场址恰好具备提供这些资源的独特优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.preussenelektra.de/de/newsroom/pressemitteilungen/pressemitteilungen-2026/2026-pel-and-nvidia-explore-former-nuclear-power-plant-sites-for-ai-factories.html">PreussenElektra and NVIDIA explore former nuclear power plant ...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/data-centers/nvidia-eyes-converting-old-nuclear-plants-into-massive-ai-data-centers-reusing-shut-down-german-energy-sites-could-reduce-the-cost-and-timeline-of-building-from-scratch">The plan does not involve using nuclear power . | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Data Centers`, `#Energy`, `#Nvidia`, `#Sustainability`

---

<a id="item-6"></a>
## [三星电视被发现收集音频和截图用于广告定向](https://www.tomshardware.com/tech-industry/cyber-security/hacker-finds-own-samsung-tv-collecting-scary-amounts-of-user-information-and-gets-banned-by-openai-for-cyber-abuse-tv-runs-an-ai-model-that-collects-audio-screenshots-and-plenty-of-other-user-data-for-ad-targeting) ⭐️ 7.5/10

一名网络安全赏金猎人逆向工程了自己的三星电视，发现其 AI 模型会秘密收集音频和截图用于广告定向。该设备还会生成跨设备追踪 ID（即 AID），以监控用户在其他平台上的活动。 该披露揭示了现代智能家居物联网设备中的严重隐私漏洞，其中 AI 驱动的数据收集极大地削弱了用户信任。调查结果表明，这些设备的性能问题可能源于对用户数据的 intensive 后处理。 研究人员推测，计算机视觉模型和 AID 追踪的繁重处理导致了电视的迟钝反应。此外，由于在网络安全研究过程中违反了相关政策，该安全研究人员的 OpenAI 账户被禁止访问。

rss · Tom's Hardware · 10月25日 10:00

**背景**: 智能电视是功能强大的计算机，运行 AI 模型并处理用户数据以实现个性化广告。AID（即 Android ID）是一种跨设备追踪标识符，允许广告商在多个智能家居设备中构建个人用户档案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/hacker-finds-own-samsung-tv-collecting-scary-amounts-of-user-information-and-gets-banned-by-openai-for-cyber-abuse-tv-runs-an-ai-model-that-collects-audio-screenshots-and-plenty-of-other-user-data-for-ad-targeting">Cybersecurity bounty hunter says Samsung TVs... | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#privacy`, `#iot`, `#consumer-electronics`, `#security-bug`

---

<a id="item-7"></a>
## [英伟达 CEO 黄仁勋估算 AI 代理的年度 GPU 成本为 2000 美元](https://www.techpowerup.com/354113/nvidia-eyes-software-revenue-with-a-usd-2-000-per-gpu-yearly-figure-from-huang) ⭐️ 6.5/10

在 GTC 柏林大会上，英伟达 CEO 黄仁勋透露，为 AI 代理运行其软件栈的成本约为每块 GPU 每年 2000 美元。这一言论标志着英伟达正明确将其商业模式向软件许可收入流转移。 该估算凸显了一个日益壮大的商业生态系统，企业不仅支付硬件费用，还支付 AI 基础设施和专门软件的费用。它为大规模应用规划提供了关键的基准，明确了代理式 AI 部署的总拥有成本。 2000 美元的报价明显低于官方许可指南中列出的英伟达 AI Enterprise 套件每块 GPU 4500 美元的一年期订阅费用。目前尚不清楚该价格是否涵盖完整套件、较窄的代理专用软件包，还是代表一种未来更实惠的许可模式。

rss · TechPowerUp News · 10月25日 15:21

**背景**: 英伟达 GTC 大会是该公司聚焦于数据中心和 AI GPU 硬件的旗舰活动，如今在 AI 代理领域投入了大量精力。历史上周，英伟达的收入主要依赖于芯片销售以及名为 AI Enterprise 的高级软件套件，该套件提供了用于在其 GPU 上运行大型语言模型的预优化工具。随着行业向更复杂的多代理工作流发展，公司正日益寻求在软件层面实现变现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.buildfastwithai.com/blogs/nvidia-nemo-vs-hugging-face-vs-ollama-2026-guide">NVIDIA NeMo vs Hugging Face vs Ollama (2026 Guide)</a></li>
<li><a href="https://blogs.nvidia.com/blog/gtc-berlin-2026-keynote/">GTC Berlin 2026: Live Updates From NVIDIA CEO Jensen Huang’s ...</a></li>
<li><a href="https://aifoss.dev/blog/ollama-vs-openrouter-vs-groq-vs-nvidia-nim-llm-serving-2026/">Ollama vs OpenRouter vs Groq vs NVIDIA NIM in 2026</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI Business Model`, `#Software Licensing`, `#Enterprise AI`, `#Jensen Huang`

---

<a id="item-8"></a>
## [Playden 让越狱 PS5 通过 Wine 运行 Steam 游戏](https://www.tomshardware.com/video-games/playstation/jailbroken-ps5s-can-now-run-steam-pc-games-you-can-now-sign-in-with-your-steam-account-and-install-games-from-your-library-directly-to-the-console) ⭐️ 6.5/10

一款名为 Playden 的自制软件工具现在允许越狱的 PS5 主机登录 Steam 并在本地运行 PC 游戏，无需依赖 PC。每个下载的游戏都被打包为独立的应用程序，拥有自己的主屏幕图标。 这一里程碑模糊了 PC 与主机游戏之间的界限，表明受限硬件可以通过 Wine 运行完整的 Windows 环境。它使发烧友社区能够绕过平台锁定，在 traditionally 专为专有内容设计的设备上访问其数字库。 Playden 使用 prospero-win（Wine 的自定义移植版）在 PS5 上创建一个干净的 Windows 环境。它确保运行时套件完整，并将每个游戏的文件和设置隔离，以防止崩溃影响其他游戏。

rss · Tom's Hardware · 10月25日 12:40

**背景**: 越狱 PS5 是指利用软件漏洞打破主机的安全限制，从而允许安装自制软件。Wine 是一个兼容层，允许 Windows 软件在其他操作系统上运行。由于硬件和内核的限制，过去在主板上运行复杂的 PC 游戏几乎是不可能的，但近年来逆向工程取得了显著进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/leolobato/playden-ps5">GitHub - leolobato/playden-ps5: Play your Steam library's ...</a></li>
<li><a href="https://www.indiekings.com/2026/10/playden-steam-games-run-directly-on.html">Playden: Steam Games Run Directly on Jailbroken PS5</a></li>

</ul>
</details>

**标签**: `#PS5`, `#Jailbreaking`, `#Steam`, `#Gaming Hardware`, `#Reverse Engineering`

---

<a id="item-9"></a>
## [Linux 工具使旧主板上的 Intel Arc 显卡支持 Resizable BAR](https://www.techpowerup.com/354116/new-linux-tool-brings-resizable-bar-to-intel-arc-gpus-on-old-motherboards) ⭐️ 5.5/10

开发者 Rod Burlamaqui 发布了名为“arc-rebar”的 Linux 工具，该工具能够启用 Intel Arc 显卡的 Resizable BAR 功能，且无需修改 BIOS。该工具在每次启动时从 initramfs 运行，且在 GPU 驱动加载之前生效，从而有效解锁旧系统的性能。 这为使用旧硬件的 Intel Arc 用户带来了关键的性能提升，因为 Intel 和评测者都指出 Resizable BAR 对于发挥显卡的全部潜力至关重要。它解决了旧主板因缺乏相应 BIOS 选项而无法启用此 PCIe 功能导致的重大瓶颈。 该工具针对 Arc 显卡上的 PCIe 交换芯片，可将 CPU 可见的 VRAM 窗口从小至 256 MiB 扩展至完整容量，例如 B580 的 12 GiB，并显著改善带宽。与需要修改固件的先前替代方案不同，此解决方案不会触及 BIOS、内核或 Intel 驱动程序。

rss · TechPowerUp News · 10月25日 16:40

**背景**: Resizable BAR (ReBAR) 是一项 PCIe 技术，允许 CPU 一次访问整个 GPU 内存池，从而提升性能。Linux 使用 initramfs（在启动时加载的临时文件系统）在主要操作系统接管之前执行脚本。Intel 的 Alchemist 和 Battlemage 架构高度依赖此功能，以至于 Intel 此前建议不具备该功能（选项）的用户考虑其他品牌。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Initial_ramdisk">Initial ramdisk - Wikipedia</a></li>
<li><a href="https://www.corsair.com/us/en/explorer/glossary/what-is-resizable-bar/">What is Resizable BAR ? | CORSAIR</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intel_Arc">Intel Arc - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Intel Arc`, `#Linux`, `#Hardware Optimization`, `#Resizable BAR`, `#GPU`

---

<a id="item-10"></a>
## [AI 驱动的科技巨头与标普 500 间的财务鸿沟加剧](https://www.tomshardware.com/tech-industry/artificial-intelligence/big-tech-is-cashing-in-on-ai-while-the-rest-of-corporate-america-sees-no-financial-returns-report-outlines-how-rising-token-costs-threaten-to-squeeze-corporate-profit-margins) ⭐️ 5.5/10

一份新报告凸显了美国最大的科技公司与标普 500 其余公司之间日益扩大的财务鸿沟，科技巨头从 AI 中获利，而其他公司则面临没有回报的局面。分析指出，由于不断上升的 AI 代币成本，“七巨头”的每员工收入正在稳步超越其余的 493 家标普 500 公司。 这种不断扩大的差异具有重大意义，因为它表明 AI 盈利能力高度集中在少数大型基础设施构建者手中，使普通企业面临高昂成本的脆弱性。对于更广泛的商业生态而言，它凸显了优化 AI 支出以防止利润空间被挤压的必要性。 驱动这种差异的关键技术因素包括构建专有 AI 推理基础设施所需的资本支出以及不断消耗 AI 代币所产生的运营支出。对于无法复制科技巨头大规模内部收入生成的公司而言，这些不断上升的成本威胁着压缩其利润空间。

rss · Tom's Hardware · 10月25日 15:25

**背景**: “七巨头”是指一组资本规模庞大的大型科技股，它们目前大约占据了标普 500 总市值的 35%。在 AI 术语中，代币是大语言模型处理或生成数据的单位，使得代币成本成为企业 AI 部署的核心运营指标。因此，处理或扩大代币生成的能力决定了其 AI 成本效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fool.com/research/magnificent-seven-sp-500/">The Magnificent Seven’s Market Cap vs. the S&P 500 | The ...</a></li>
<li><a href="https://www.nvidia.com/en-us/solutions/ai/tokenomics-guide/">Tokenomics Guide: Case Studies and More | NVIDIA AI</a></li>
<li><a href="https://www.bcg.com/publications/2026/managing-ai-token-costs">How Enterprises Can Control AI Token Costs | BCG</a></li>

</ul>
</details>

**标签**: `#AI Economics`, `#Big Tech`, `#Corporate Finance`, `#Business Analysis`

---

<a id="item-11"></a>
## [乌克兰无人机打击俄罗斯财政部戈罗杰茨数据中心](https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drone-attacks-hammer-russias-finance-ministry-data-center-damaged-facility-reportedly-holds-tax-databases-facility-also-holds-other-important-state-registry-data) ⭐️ 5.5/10

乌克兰无人机的袭击损坏了俄罗斯财政部位于戈罗杰茨（Gorodets）的数据中心，据报道该设施存放着联邦税务局税务数据库和重要的国家登记数据。 此事件表明数据中心已成为现代冲突中关键的国家基础设施目标，将风险从传统 IT 领域扩展到了核心政府行政和税务系统。 受损的戈罗杰茨设施位于克里姆林宫以东约 230 英里处，距前线超过 600 英里，作为两个主要处理中心之一，与杜布纳（Dubna）和耶尔佐夫卡（Yerzovka）组成地理分布架构。

rss · Tom's Hardware · 10月25日 14:05

**背景**: 数据中心在物理上承载服务器和网络，存储一个国家最敏感的电子记录，包括税务数据、企业登记和国有财产数据库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/AWS/ukrainian-drones-strike-russian-finance-ministry-data-center-in-gorodets-25190443">Ukrainian Drones Strike Russian Finance Ministry Data Center ...</a></li>
<li><a href="https://mezha.net/eng/news/mezha-a48312b74195a4b00cfa1886_drones_hit_russian/">Drones hit Russian Finance Ministry data center; tax ...</a></li>

</ul>
</details>

**标签**: `#data-center`, `#geopolitics`, `#security`, `#infrastructure`, `#physical-security`

---