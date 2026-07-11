---
layout: default
title: "Horizon Summary: 2026-07-11 (ZH)"
date: 2026-07-11
lang: zh
---

> 从 64 条内容中筛选出 20 条重要资讯。

---

1. [Colibrì 概念验证在仅 25GB 内存上运行 1.5TB AI 模型](#item-1) ⭐️ 8.5/10
2. [Anthropic 在 Claude 大模型中发现类似全局工作空间的'J-space'](#item-2) ⭐️ 8.5/10
3. [SK 海力士在美创纪录 IPO 融资 265 亿美元，加速 HBM 产能扩张](#item-3) ⭐️ 8.5/10
4. [SK 海力士 CEO 警告：2027 年将是内存短缺最严重的一年](#item-4) ⭐️ 7.5/10
5. [假冒 Go DNS 扫描器通过 200 多个 GitHub 仓库传播恶意软件——"Operation Muck and Load"自 1 月以来已发布 700 个恶意模块](#item-5) ⭐️ 7.5/10
6. [Flock cameras mistakenly track car reviewer over 'stolen' tags — police ambush tester in store parking lot and detain him for an hour](#item-6) ⭐️ 7.5/10
7. [苹果起诉 OpenAI，指控其在 AI 硬件领域窃取商业秘密](#item-7) ⭐️ 7.5/10
8. [腾讯洽谈以 20 亿美元从 Meta 手中回购 Manus AI](#item-8) ⭐️ 7.5/10
9. [Circle 获 OCC 国家信托银行牌照管理 USDC 储备资产](#item-9) ⭐️ 7.3/10
10. [宇树 G1 人形机器人远程操控完成活体猪胆囊切除手术](#item-10) ⭐️ 7.3/10
11. [爱因斯坦相对论支配重元素中的化学键](#item-11) ⭐️ 7.0/10
12. [QuadRF can spot drones and see WiFi through my wall](#item-12) ⭐️ 7.0/10
13. [LWN.net 报道使用住宅代理的 AI 爬虫攻防战](#item-13) ⭐️ 7.0/10
14. [SpaceX 申请再发射 10 万颗 Starlink 卫星，瞄准 100 倍带宽提升](#item-14) ⭐️ 7.0/10
15. [Bethesda 工会员工计划 7 月 15 日因 Xbox 裁员举行罢工抗议](#item-15) ⭐️ 6.5/10
16. [微软在 2030 年可持续发展承诺上面临挑战,AI 扩张导致碳排放居高不下——公司首席可持续发展官称目标仍可实现](#item-16) ⭐️ 6.5/10
17. [SK 海力士与 TetraMem 合作研发面向边缘 AI 的忆阻器存内计算 SoC](#item-17) ⭐️ 6.5/10
18. [独家 | 智谱创始人唐杰发内部信：「GLM 时刻」之后，什么是更重要的事](#item-18) ⭐️ 6.3/10
19. [9 点 1 氪丨“国产存储第一股”长鑫科技公布承销团阵容；SK 海力士登陆美股，上市首日大涨近 13%；OpenAI 推出 ChatGPT 智能体](#item-19) ⭐️ 6.3/10
20. [《终结者 2》开创性视觉特效技术的口述历史](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Colibrì 概念验证在仅 25GB 内存上运行 1.5TB AI 模型](https://www.tomshardware.com/tech-industry/artificial-intelligence/colibri-proof-of-concept-gains-frontier-level-1-5-tb-ai-model-novel-approach-runs-on-only-25gb-of-ram-and-shows-promise-for-local-ai-setups) ⭐️ 8.5/10

Colibrì 概念验证成功在仅 25GB 内存和普通 CPU 上运行了一个前沿级别的 1.5TB AI 模型（GLM-5.2），相比模型原始大小实现了大约 60 倍的内存缩减。 如果能从概念验证阶段走向成熟，这一方法有望通过在消费级硬件上部署本地 AI 来实现大型 AI 模型的民主化，降低运行前沿级模型对昂贵 GPU 和云基础设施的依赖。 Colibrì 的专家选择逻辑以单个 C 文件实现，依赖极少，并且模型通过有损编码的量化技术缩减了基础占用空间。作为概念验证，其实际推理速度和输出质量尚未经过基准测试。

rss · Tom's Hardware · 7月11日 11:30

**背景**: 前沿 AI 模型是当前最先进的人工智能模型，通常需要巨大的计算资源和配备大显存的高端 GPU。模型压缩技术（如量化、剪枝和混合专家（MoE）路由）旨在降低内存和计算需求，同时保持性能。历史上，运行万亿参数级别的模型要么需要昂贵的数据中心 GPU，要么需要借助 CPU 卸载、分层流式加载和激进量化等创新方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/colibri-proof-of-concept-gains-frontier-level-1-5-tb-ai-model-novel-approach-runs-on-only-25gb-of-ram-and-shows-promise-for-local-ai-setups">Colibrì proof-of-concept gains frontier-level 1.5-TB AI model — novel ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_compression">Model compression - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>

</ul>
</details>

**标签**: `#AI`, `#local-ai`, `#model-compression`, `#hardware-efficiency`, `#proof-of-concept`

---

<a id="item-2"></a>
## [Anthropic 在 Claude 大模型中发现类似全局工作空间的'J-space'](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-it-can-read-claudes-thoughts-as-detailed-in-new-research-paper-models-observed-to-have-a-global-workspace-revealing-more-of-what-makes-llms-tick) ⭐️ 8.5/10

Anthropic 发布了一篇题为《语言模型中的全局工作空间》的研究论文，揭示其 Claude 模型拥有一个名为'J-space'的内部空间——这是一个特权通道，概念在其中被持有、处理，并在作为文本输出写入之前变得可访问。研究人员使用一种称为'J-lens'的工具来读取这些中间表征，例如 Claude Sonnet 4.5 在生成任何回复之前就将一个预设的勒索场景识别为'虚假的'和'虚构的'。 这一发现将认知科学中的全局工作空间理论与大语言模型的内部机制联系起来，为机制可解释性开辟了新路径——该领域对于 AI 安全、对齐以及构建可信赖系统至关重要。通过能够'读取'模型在输出前内部推理的内容，研究人员可以更好地检测模型的不对齐、欺骗或虚假推理行为，从而有可能改进对已部署 AI 的监督机制和安全护栏。 J-space 包含与模型最可能在下一步输出的内容相关的单个词汇和概念，充当一个中间规划层，使模型能够'对其进行报告、控制和推理，而无需将其写出'。全局工作空间的类比源自认知科学家 Bernard Baars 于 1988 年提出的认知架构，该理论最初通过假设一个各个专门化过程共享信息的中央枢纽来解释意识。

rss · Tom's Hardware · 7月10日 16:44

**背景**: 全局工作空间理论（GWT）由认知科学家 Bernard Baars 于 1988 年提出，是理解意识的一个理论框架，它假设存在一个中央'工作空间'，来自各个专门化大脑过程的信息在此变得在整个系统中全局可用。机制可解释性是一个新兴的 AI 安全领域，旨在神经元和电路层面逆向工程神经网络，以理解其内部计算过程，而非将其视为不透明的黑箱。Anthropic 一直是该领域的领先实验室，其联合创始人 Dario Amodei 主张，在 AI 系统变得危险之前，可解释性工具对于解码模型内部机制至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/global-workspace">A global workspace in language models \ Anthropic</a></li>
<li><a href="https://www.technologyreview.com/2026/07/09/1140293/anthropic-found-a-hidden-space-where-claude-puzzles-over-concepts/">Anthropic found a hidden space where Claude puzzles over concepts | MIT Technology Review</a></li>
<li><a href="https://en.wikipedia.org/wiki/Global_Workspace_Theory">Global workspace theory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI interpretability`, `#Anthropic`, `#Claude`, `#AI safety`, `#mechanistic interpretability`

---

<a id="item-3"></a>
## [SK 海力士在美创纪录 IPO 融资 265 亿美元，加速 HBM 产能扩张](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-raises-a-record-usd26-5-billion-in-historic-u-s-ipo-south-korean-memory-giant-to-fund-massive-hbm-manufacturing-expansions) ⭐️ 8.5/10

SK 海力士在纳斯达克完成了创纪录的 265 亿美元 IPO，所筹资金将用于建设新的晶圆厂，以应对 AI 需求激增以及 HBM 产品已售罄的局面。 这一空前的资本注入 HBM 产能的举措，显示出市场对 AI 内存长期周期的强烈信心，并将直接影响 NVIDIA Blackwell 和 AMD MI350 等 AI 加速器的供应链，关系到整个 AI 基础设施生态系统的走向。 265 亿美元的融资规模创下了外国企业在美国上市的历史纪录。SK 海力士是全球仅有的三大 HBM 生产商之一，与三星和美光并列，在产品售罄的背景下拥有强大的定价能力。

rss · Tom's Hardware · 7月10日 14:27

**背景**: 高带宽内存（HBM）是一种 3D 堆叠 SDRAM 技术，相比传统 DDR5 DRAM 提供更高的带宽和能效，是 AI GPU 和高性能计算加速器的首选内存方案。HBM 最初由三星、AMD 和 SK 海力士联合开发，历经 HBM3E 和 HBM4 等代际演进。半导体晶圆厂是资本极其密集的设施，造价高达数百亿美元，需要超净洁净室和数百道精密制造工序来生产芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.rambus.com/blogs/hbm3-everything-you-need-to-know/">High Bandwidth Memory (HBM): Everything You Need to Know</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semiconductor_fabrication_plant">Semiconductor fabrication plant - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#HBM`, `#AI-infrastructure`, `#IPO`, `#SK-hynix`

---

<a id="item-4"></a>
## [SK 海力士 CEO 警告：2027 年将是内存短缺最严重的一年](https://www.tomshardware.com/pc-components/dram/sk-hynix-says-2027-will-be-the-worst-year-for-memory-shortage-forecasts-crunch-to-last-until-2030-ceo-shares-grim-outlook-on-the-day-sk-hynix-gets-listed-on-nasdaq) ⭐️ 7.5/10

SK 海力士 CEO 郭鲁正（Kwak Noh-jung）警告称，全球内存短缺将在 2027 年进一步恶化，届时将是情况最严重的一年，且内存供应紧张将持续到 2030 年。这一严峻展望是在 SK 海力士登陆纳斯达克当天发表的。 作为全球顶级内存芯片制造商之一，SK 海力士的展望预示着消费电子、PC、服务器乃至 AI 数据中心基础设施领域将面临长期的价格压力和供应紧张。持续多年的短缺可能重塑采购策略，推高设备价格，并减缓 AI 驱动硬件的部署。 这一警告主要针对 DRAM 和 NAND 闪存的供应问题，根本原因是 AI 数据中心需求激增，超过了现有晶圆厂的产能。SK 海力士近期刚完成 HBM4 的开发并准备量产，但仅靠 HBM（高带宽内存）无法解决更广泛的 DRAM 短缺问题。

rss · Tom's Hardware · 7月11日 13:00

**背景**: DRAM（动态随机存取内存）是计算机、服务器和大多数数字设备使用的主要易失性内存类型，以低成本和高密度著称。SK 海力士是全球第二大内存芯片制造商，生产 DRAM、NAND 闪存以及对 AI 加速器（如 GPU）至关重要的 HBM（高带宽内存）。当前始于 2025 年的全球内存短缺与 2020–2023 年的芯片短缺不同——那次主要是疫情相关的物流问题，而此次则是由 AI 需求激增、超过有限的晶圆产能所致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.idc.com/resource-center/blog/global-memory-shortage-crisis-market-analysis-and-the-potential-impact-on-the-smartphone-and-pc-markets-in-2026/">Global Memory Shortage Crisis: Market Analysis and the ... - IDC</a></li>
<li><a href="https://product.skhynix.com/home.go">SK hynix Official Product Website | SK hynix</a></li>

</ul>
</details>

**标签**: `#memory-shortage`, `#DRAM`, `#SK-Hynix`, `#semiconductors`, `#tech-industry`

---

<a id="item-5"></a>
## [假冒 Go DNS 扫描器通过 200 多个 GitHub 仓库传播恶意软件——"Operation Muck and Load"自 1 月以来已发布 700 个恶意模块](https://www.tomshardware.com/tech-industry/cyber-security/fake-go-dns-scanner-published-700-malicious-versions-before-researchers-traced-it-to-222-github-repos) ⭐️ 7.5/10

自今年 1 月以来，一个伪装成 Go DNS 扫描器的恶意软件（"Operation Muck and Load"）通过 222 个 GitHub 仓库传播了 700 多个恶意模块版本，累计超过 1200 个版本。

rss · Tom's Hardware · 7月11日 11:00

**标签**: `#cybersecurity`, `#supply-chain-attack`, `#golang`, `#malware`, `#github`

---

<a id="item-6"></a>
## [Flock cameras mistakenly track car reviewer over 'stolen' tags — police ambush tester in store parking lot and detain him for an hour](https://www.tomshardware.com/tech-industry/big-tech/flock-cameras-mistakenly-track-car-reviewer-over-stolen-tags-police-ambush-tester-in-store-parking-lot-and-detain-him-for-an-hour) ⭐️ 7.5/10

Flock AI license-plate-reading cameras misread non-standard New Jersey plates as 'stolen,' leading police to detain an innocent car reviewer for an hour due to combined AI vision failure and a flawed initial police report.

rss · Tom's Hardware · 7月11日 10:30

**标签**: `#AI safety`, `#computer vision`, `#surveillance technology`, `#law enforcement tech`, `#failure modes`

---

<a id="item-7"></a>
## [苹果起诉 OpenAI，指控其在 AI 硬件领域窃取商业秘密](https://www.tomshardware.com/tech-industry/big-tech/apple-sues-openai-over-alleged-theft-of-trade-secrets-claims-company-mentored-incoming-employees-on-bringing-confidential-information) ⭐️ 7.5/10

苹果已对 OpenAI 提起诉讼，指控 OpenAI 通过指导新入职的前苹果员工携带机密信息的方式，系统性地窃取商业秘密，尤其涉及 AI 硬件开发领域。诉状详细描述了一种模式：OpenAI 招聘的员工据称在离开苹果前将机密数据通过电子邮件发送给自己，并在接触苹果硬件供应商时使用了这些信息。 此案可能为日益激烈的 AI 硬件竞赛中员工流动性和商业秘密保护树立重要先例，苹果和 OpenAI 都在构建相互竞争的产品线。它还引发了更广泛的担忧：当关键工程师在 AI 公司之间流动时，企业的专有信息可能面临知识产权风险。 诉讼具体点名了 OpenAI 及前苹果员工，包括一位名叫 Tan 的入职者，据称他警告新员工不要告知苹果他们已入职 OpenAI，以便在苹果留任更长时间、获取更多专有数据。苹果声称 OpenAI 在与苹果供应链合作伙伴谈判时利用了窃取的机密硬件信息。

rss · Tom's Hardware · 7月10日 21:59

**背景**: 商业秘密是受法律保护的、具有独立经济价值的非公开信息，企业通过合理措施加以保护，无需像专利那样进行正式注册。苹果一直向硬件优先的 AI 战略转型，强调设备端隐私，并正在探索将生成式 AI 用于定制芯片设计。与此同时，OpenAI 已从软件领域扩展到 AI 硬件领域，使得苹果的工程人才成为其天然的招聘目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forensisgroup.com/resources/expert-legal-witness-blog/what-is-a-trade-secret-core-concepts-and-legal-protections">What Is a Trade Secret ? Legal Definition , Protection , and...</a></li>
<li><a href="https://www.geeky-gadgets.com/apple-ai-strategy-hardware-pivot/">How Apple AI Strategy Shifts Focus from Software to Hardware ...</a></li>
<li><a href="https://www.macobserver.com/news/apple-hardware-chief-says-company-exploring-generative-ai-for-chip-design/">Apple Hardware Chief Says Company Exploring Generative AI for ...</a></li>

</ul>
</details>

**社区讨论**: 社区舆论压倒性地批评 OpenAI，有评论者将其与导致 Uber 自动驾驶项目终结的 Waymo 诉 Uber 案相提并论，预测 OpenAI 的硬件业务将面临类似的存亡后果。多名用户对使用 OpenAI 产品的数据安全表示担忧，警告企业应重新考虑依赖 OpenAI 模型，因为可能面临知识产权泄露风险。

**标签**: `#legal`, `#apple`, `#openai`, `#trade-secrets`, `#ai-hardware`

---

<a id="item-8"></a>
## [腾讯洽谈以 20 亿美元从 Meta 手中回购 Manus AI](https://www.tomshardware.com/tech-industry/artificial-intelligence/tencent-is-reportedly-in-talks-to-acquire-manus-from-meta-following-beijing-intervention-company-expects-to-remain-independent-of-chinese-tech-giant) ⭐️ 7.5/10

腾讯正洽谈牵头中方资本组团，以约 20 亿美元估值从 Meta 手中回购 AI Agent 初创公司 Manus 的股权。此前北京方面曾下令两家公司撤销交易，距 Meta 宣布收购约六个月。腾讯将保持少数股东地位，不会控股。 这笔交易凸显了日益加剧的中美科技紧张关系，尤其是涉及跨境 AI 投资领域，也表明中国政府愿意在涉及前沿 AI 技术的重大收购交易中直接介入。其结果可能为中国 AI 企业在面对地缘政治审查时如何安排所有权结构树立先例。 Manus 由 Butterfly Effect 开发，该公司在中国创立但总部已迁至新加坡，这一架构为国际运营提供了缓冲。腾讯在截稿前未予回应，交易结构似乎旨在让中方资本获得多数经济权益，同时保持分散的正式控制权以满足监管要求。

rss · Tom's Hardware · 7月10日 15:00

**背景**: Manus 是一款自主 AI Agent，能够浏览网页、编写和运行代码、构建全栈应用程序，并使用外部工具执行多步骤计划——这类 AI 超越了简单的聊天机器人，能够主动执行任务。Meta 最初宣布的收购是一个出人意料的举动，但北京方面介入迫使交易撤销，反映出中国在阻止战略重要性 AI 技术流向美国企业方面越来越强势的态度。Butterfly Effect 以新加坡为总部是中国科技企业寻求在保留中国背景的同时维持国际市场准入的一种常见架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent) - Wikipedia</a></li>
<li><a href="https://manus.im/about">About us - Manus</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>

</ul>
</details>

**标签**: `#AI`, `#Tencent`, `#Meta`, `#acquisition`, `#US-China tech relations`

---

<a id="item-9"></a>
## [Circle 获 OCC 国家信托银行牌照管理 USDC 储备资产](https://36kr.com/newsflashes/3890740672838404?f=rss) ⭐️ 7.3/10

Circle 于周五获得美国货币监理署（OCC）批准，设立一家名为"Circle 国民信托银行"的国家信托银行，使该公司能够直接管理其 USDC 稳定币的储备资产，而 USDC 目前的流通规模已超过 730 亿美元。 这是稳定币行业的一项重大监管里程碑，Circle 由此成为首批获得美国国家银行类牌照的主流稳定币发行商之一，降低了对第三方托管机构的依赖，并可能为其他寻求银行业合法性的加密公司树立先例。 该信托银行牌照不允许 Circle 吸收客户存款或发放贷款——这些是商业银行的核心业务——其业务范围仅限于托管和资产管理。在此之前，Circle 必须依赖第三方银行和托管机构来持有支撑 USDC 发行的现金和美国国债资产。

rss · 36氪 · 7月11日 05:10

**背景**: 像 USDC 这样的稳定币是与传统货币（通常是美元）挂钩的数字代币，由现金和短期美国国债等储备资产支持。OCC 是美国财政部下属的独立机构，负责特许、监管和监督所有国家银行。国家信托银行牌照与商业银行牌照不同，因为它限制机构吸收存款和发放贷款，而是专注于托管和信托业务。这种类型的牌照也被其他加密公司所追求，以此简化跨司法管辖区的监管合规。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.occ.gov/about/who-we-are/index-who-we-are.html">Who We Are - Office of the Comptroller of the Currency (OCC)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Office_of_the_Comptroller_of_the_Currency">Office of the Comptroller of the Currency - Wikipedia</a></li>
<li><a href="https://finance.yahoo.com/news/everyone-wants-to-be-a-bank-now-banks-arent-happy-about-it-130004513.html">Everyone wants to be a bank now. Banks aren’t happy about it.</a></li>

</ul>
</details>

**标签**: `#stablecoin`, `#Circle`, `#USDC`, `#regulation`, `#fintech`

---

<a id="item-10"></a>
## [宇树 G1 人形机器人远程操控完成活体猪胆囊切除手术](https://www.solidot.org/story?sid=84801) ⭐️ 7.3/10

发表在《自然》期刊上的一项研究显示，由外科医生远程操控的宇树 G1 人形机器人成功完成了两例活体猪微创胆囊切除手术。研究人员使用了一种名为 LapSurgie 的远程操控工作流程，将人形机器人与腹腔镜器械及内窥镜可视化系统相结合。 这一里程碑表明，通用人形机器人有望成为远比达芬奇等专业系统更经济的手术平台，使小型医院、诊所、偏远地区、战场乃至太空都能开展机器人辅助手术。约 7 至 10 倍的成本降低可能让先进微创手术在资源有限的环境中更加普及。 G1 基础型号起售价为 13,500 美元，但配备灵巧机械手并加上运费后费用超过 6.7 万美元，仍远低于直觉外科公司的达芬奇系统（50 万至数百万美元）。主要局限包括需要频繁重新校准、手术耗时更长，且机器人完全依赖远程操控而非自主操作，并不取代外科医生。

rss · Solidot · 7月10日 15:10

**背景**: 达芬奇手术系统由直觉外科公司制造，在过去二十年里主导了机器人辅助微创手术市场。外科医生在专用控制台操控专用机械臂完成手术，但其高昂成本使其仅限于资金充足的医院。宇树 G1 等通用人形机器人身高约 1.32 米，重 35 公斤，拥有 23 至 43 个自由度，是面向研究与开发应用的通用平台，价格远低于专业手术机器人。远程手术（外科医生远程操控机器人进行手术）已探索多年，但受法律、基础设施和延迟等障碍的限制，仍仅用于特殊场景；该研究是首批证明通用人形机器人能完成活体手术任务的案例之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10796-x">In vivo feasibility study of humanoid robots in surgery - Nature</a></li>
<li><a href="https://humanoid.guide/product/g1/">Unitree Robotics G1 Specs & Price | Humanoid.guide Unitree G1 - Robot Details, Use Case and Specifications ... Unitree G1 Review [2026]: Our Verdict | RoboZaps Blog Unitree G1 Specs, Price & Status - 9S Robotics Unitree G1 — Price, Specs & Demo · RobotLAB G1 by Unitree Robotics - Humanoid Robot Specs & Details Images</a></li>
<li><a href="https://www.intuitive.com/en-us/patients/da-vinci-robotic-surgery">Da Vinci Surgery for Patients | Intuitive</a></li>

</ul>
</details>

**标签**: `#robotics`, `#medical-technology`, `#Unitree`, `#surgical-robotics`, `#teleoperation`

---

<a id="item-11"></a>
## [爱因斯坦相对论支配重元素中的化学键](https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity) ⭐️ 7.0/10

布朗大学的研究人员在《Science》杂志上发表了一项研究，首次提供了直接的实验证据，表明教材中的三键结构在重元素中会瓦解，因为相对论效应改变了原子结合的方式。该研究以周期表上紧邻铅的铋作为关键示例，来展示这些相对论性的成键效应。 这项研究加深了我们对重元素化学的理解，并可能指导新材料的設計，包括在下一代太阳能电池等应用中替代铅的潜在方案。它将基础物理（相对论）与实际化学和材料科学直接联系起来，为在标准教材模型失效的重元素中预测成键行为提供了路线图。 在重元素中，原子核电荷的增加使内层电子达到光速的显著比例（例如，汞的内层电子以约 60%的光速运动），从而触发自旋-轨道耦合，使电子自旋和轨道运动不再相互独立。该论文具体展示了这种耦合如何打破化学学生在轻元素中学习到的传统σ键和π键框架。

hackernews · hhs · 7月10日 22:30 · [社区讨论](https://news.ycombinator.com/item?id=48866134)

**背景**: 相对论量子化学是一个在模拟原子中电子行为时考虑爱因斯坦相对论的领域。在重元素中，特别是靠近大原子核的内层电子，必须以非常高的速度运动才能维持其轨道，接近相对论速度。这导致了可测量的效应：汞在室温下保持液态，因为其内层轨道的相对论性收缩削弱了金属键；金呈现黄色而非银色，因为相对论效应改变了其电子态之间的能隙。自旋-轨道耦合作为一种关键的相对论现象，在重元素中变得显著，并从根本上改变了它们与同族轻元素相比的化学性质。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity">Einstein’s relativity rules chemical bonds in heavy elements , new...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Relativistic_quantum_chemistry">Relativistic quantum chemistry - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Community commenters expressed mixed sentiment, with several noting that the underlying principles—such as mercury's liquid state at room temperature and gold's color being due to relativistic effects—are well-established knowledge taught in undergraduate physics, suggesting the novelty lies in the experimental demonstration rather than the concept itself. There was appreciation for Einstein's foundational work continuing to be validated, alongside technical discussions about spin-orbit coupling and sigma/pi bond terminology. Some commenters questioned the practical significance of lead alternatives in solar panels, noting that lead in current mass-produced panels is limited to specialized semiconductor applications like lead telluride and lead selenide rather than mainstream photovoltaic products.

**标签**: `#physics`, `#chemistry`, `#relativity`, `#materials-science`, `#research`

---

<a id="item-12"></a>
## [QuadRF can spot drones and see WiFi through my wall](https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/) ⭐️ 7.0/10

QuadRF is an open-source RF augmented reality system that visualizes WiFi signals and detects drones through walls by combining antenna arrays with real-time visualization.

hackernews · speckx · 7月10日 15:59 · [社区讨论](https://news.ycombinator.com/item?id=48861717)

**标签**: `#rf-sensing`, `#drones`, `#augmented-reality`, `#open-source`, `#hardware`

---

<a id="item-13"></a>
## [LWN.net 报道使用住宅代理的 AI 爬虫攻防战](https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/) ⭐️ 7.0/10

LWN.net 发布了一篇更新，介绍他们与利用住宅代理网络绕过 IP 封锁的激进 AI 爬虫持续斗争的经历。该出版商解释了为何没有部署类似 Anubis 的工作量证明（PoW）工具，理由是用户体验问题，以及爬虫可以利用数百万台被入侵的机器分摊计算来绕过此类挑战。 这篇来自知名技术出版商的案例分析揭示了寻求训练数据的 AI 公司与试图保护自身基础设施和读者的独立网站运营者之间日益加剧的矛盾。这场讨论对网络的开放性、网站归档的未来，以及少数大型平台（如 Cloudflare）是否会成为谁能访问在线内容的把关人，都具有深远影响。 住宅代理网络通过分配给真实住宅用户的 IP 地址路由请求，这些 IP 通常来自被入侵的设备或 ISP 合作伙伴，使得传统的基于 IP 的封锁手段失效。像 Anubis 这样的工作量证明方案要求浏览器计算 SHA-256 哈希值，但当攻击者可以利用数百万台被劫持的机器或在无头浏览器环境中分摊计算时，这一成本几乎可以忽略不计。

hackernews · chmaynard · 7月10日 19:38 · [社区讨论](https://news.ycombinator.com/item?id=48864252)

**背景**: 住宅代理网络是商业服务，通过属于真实家庭宽带连接的 IP 地址路由流量，使自动化请求看起来像是来自普通用户而非数据中心。以开源工具 Anubis（已部署在 git.kernel.org 和 GNOME 的 GitLab 等网站）为代表的工作量证明反爬机制，要求访问者的浏览器在获得访问权限之前解决加密计算难题。LWN.net 是一个运营已久的、由订阅者支持的技术新闻网站，长期以来一直可自由访问，这使得爬虫带来的资源消耗对其有限的运营预算尤其具有破坏性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/1028558/">Anubis sends AI scraperbots to a well-deserved fate [LWN.net]</a></li>
<li><a href="https://oxylabs.io/blog/what-is-residential-proxy">What is a Residential Proxy & How it Works ?</a></li>
<li><a href="https://michaelbommarito.com/wiki/ai-society/anubis-benchmark-analysis/">anubis benchmark: measuring proof - of - work overhead in headless...</a></li>

</ul>
</details>

**社区讨论**: 讨论展现了多种观点：像 harshreality 这样的实际运营者分享了应对爬虫时一手的技术权衡经验；mips_avatar 认为建立像 Common Crawl 这样更好的共享数据集比封锁更有效，警告反爬措施可能将权力集中到 Cloudflare 等平台手中；jappgar 从曾同时从事爬取和防御工作的资深角度出发，认为双方都不占据道德高地；sixtyj 则强调真正的问题是规模和体量，而非爬取行为本身，并指出由于网站经常在收购或改版后消失，稳健的网络归档机制是必要的。

**标签**: `#web-scraping`, `#bot-detection`, `#ai-training-data`, `#internet-infrastructure`, `#open-web`

---

<a id="item-14"></a>
## [SpaceX 申请再发射 10 万颗 Starlink 卫星，瞄准 100 倍带宽提升](https://www.zdnet.com/home-and-office/networking/spacex-wants-to-launch-100000-more-starlink-satellites/) ⭐️ 7.0/10

SpaceX 已向美国联邦通信委员会（FCC）提交申请，计划再发射 10 万颗 Starlink 卫星，目标是将星座带宽容量提升约 100 倍。此次申请将大幅扩展现有的 Starlink 网络，该网络目前已在大约 160 个国家和地区提供宽带互联网服务。 如果获得批准，这将是卫星互联网基础设施的一次大规模扩展，可能彻底改变全球互联互通状况，尤其是在服务不足的农村和偏远地区，同时也将加剧人们对近地轨道拥挤、凯斯勒症候群风险、再入大气层卫星造成的污染以及与地面宽带提供商竞争的担忧。 此次拟议的扩展规模将远超目前约 7000 多颗在轨运行的 Starlink 卫星，是历史上最大规模的单次卫星星座申请之一。100 倍带宽的声明意味着每颗卫星的吞吐量和星间激光链路容量将实现重大代际升级，但监管审批、发射节奏以及负责任的离轨计划仍是重要的实际障碍。

hackernews · CrankyBear · 7月10日 17:51 · [社区讨论](https://news.ycombinator.com/item?id=48863064)

**背景**: Starlink 是 SpaceX 运营的近地轨道（LEO）卫星互联网星座，旨在为地面基础设施不可用或不充分的地区提供宽带接入。目前约有 9000 颗卫星运行在近地轨道，地球上方 100 至 1240 英里之间的区域拥有国际空间站和大多数商业卫星。凯斯勒症候群描述了一个理论上的级联碰撞场景——碎片碰撞产生更多碎片，可能导致某些轨道区域无法使用。FCC 于 2023 年设立的航天局负责监管 NGSO（非对地静止轨道）星座许可，包括通过 ITU 进行的频谱分配和轨道位置协调。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starlink">Starlink - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kessler_syndrome">Kessler syndrome - Wikipedia</a></li>
<li><a href="https://spacenexus.us/blog/fcc-satellite-licensing-spectrum-orbital-slots">FCC Satellite Licensing: Spectrum, Orbital Slots, and the Filing Process</a></li>

</ul>
</details>

**社区讨论**: 社区讨论反映了观点深刻分化但论述充分的看法。支持者强调了农村和移动用户（房车旅行者、远程工作者）的实际好处——他们此前没有可靠的互联网选择。批评者提出了三大主要担忧：由于私人拥有轨道空间而导致的天文污染和自然夜空的消失、再入大气层时燃烧卫星材料造成的大气污染，以及对 Starlink 在政府资助的光纤已变得实惠的地区长期必要性的怀疑。一位评论者指出，对于非洲和印度以外的许多市场，光纤可能已经提供了更具竞争力的替代方案。

**标签**: `#Starlink`, `#SpaceX`, `#satellite-internet`, `#infrastructure`, `#space-policy`

---

<a id="item-15"></a>
## [Bethesda 工会员工计划 7 月 15 日因 Xbox 裁员举行罢工抗议](https://www.techpowerup.com/350680/unionized-bethesda-workers-plan-strike-over-xbox-mass-layoffs) ⭐️ 6.5/10

隶属于 CWA 的 OneBGS 工会已宣布将于 7 月 15 日在蒙特利尔、奥斯汀、达拉斯和罗克维尔的 Bethesda 工作室发起名为"拯救我们的开发者"的联合游行，抗议微软/Xbox 大规模裁员浪潮中 Bethesda Game Studios、ZeniMax Online Studios、id Software、ZeniMax QA 及 ZeniMax 公司部门约 440 个工会岗位被裁撤。 这是游戏行业迄今为止规模最大的有组织劳工行动之一，工会员工正利用法律保护的集体谈判权利来抵制企业重组。其结果可能为大型游戏发行商如何处理工会员工裁员树立先例，并影响整个游戏开发行业的劳工运动走向。 此次裁员对 id Software 打击尤为严重，约占其员工总数的 50%，Bethesda Game Studios 约 25%，QA 团队乃至 CTO 和 CSUR 等高级职位均受到影响。由于 OneBGS 是 2024 年获得认证的拥有 241 名成员的全面覆盖型工会，受影响员工享有非工会工作室所不具备的法律保护，包括通知期要求和遣散义务。

rss · TechPowerUp News · 7月11日 00:03

**背景**: ZeniMax Media 是一家控股公司，旗下拥有 Bethesda Softworks 及其子公司工作室；微软于 2021 年 3 月完成对 ZeniMax 高达 81 亿美元的收购，将 Bethesda、id Software 等工作室纳入 Xbox 旗下。美国通信工作者工会（CWA）是美国主要劳工组织，一直积极组织游戏行业员工，OneBGS 于 2024 年 7 月成为微软旗下首个被正式承认的工会。本轮裁员与 Xbox 高管 Asha Sharma 主导的"为期一年的战略重置"有关，全公司范围内裁减约 3,200 个职位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ZeniMax_Media">ZeniMax Media - Wikipedia</a></li>
<li><a href="https://gameluster.com/onebgs-save-our-devs-march-xbox-layoffs/">OneBGS Plans 4-City March Over Xbox Layoffs</a></li>
<li><a href="https://www.gamespot.com/articles/bethesda-game-studios-is-now-unionized-across-the-board-recognized-by-microsoft/1100-6525206/">Bethesda Game Studios Is Now Unionized Across The Board ...</a></li>

</ul>
</details>

**标签**: `#gaming-industry`, `#layoffs`, `#labor-unions`, `#xbox`, `#microsoft`

---

<a id="item-16"></a>
## [微软在 2030 年可持续发展承诺上面临挑战,AI 扩张导致碳排放居高不下——公司首席可持续发展官称目标仍可实现](https://www.tomshardware.com/tech-industry/big-tech/microsoft-struggles-to-fulfill-its-2030-sustainability-promise-amid-carbon-heavy-ai-expansions-the-companys-chief-sustainability-officer-claims-the-target-is-still-feasible) ⭐️ 6.5/10

由于 AI 数据中心扩张,微软 2025 财年碳排放量上升了 25%,尽管在水资源和废弃物管理方面取得进展,但其 2030 年可持续发展目标仍面临挑战。

rss · Tom's Hardware · 7月11日 12:45

**标签**: `#AI`, `#sustainability`, `#Microsoft`, `#data-centers`, `#carbon-emissions`

---

<a id="item-17"></a>
## [SK 海力士与 TetraMem 合作研发面向边缘 AI 的忆阻器存内计算 SoC](https://www.tomshardware.com/tech-industry/artificial-intelligence/sk-hynix-and-tetramem-collaborate-on-experimental-chip-to-bolster-energy-efficiency-for-edge-ai-devices-memristor-based-in-memory-soc-research-leaves-performance-questions-up-in-the-air) ⭐️ 6.5/10

SK 海力士、TetraMem 与南加州大学（USC）联合开发了一款基于忆阻器的存内计算片上系统（SoC），面向低功耗 AI 边缘设备。该实验性芯片在能效方面取得了令人鼓舞的结果，但研究团队尚未证明该架构能够提供具有竞争力的性能表现。 边缘 AI 设备（从智能手机到物联网传感器）受到严格的功耗预算限制，因此能效成为关键的设计优先项。基于忆阻器的存内计算有望通过消除传统冯·诺依曼架构中的数据搬运瓶颈来大幅降低 AI 推理的能耗，这可能会重塑低功耗 AI 硬件的竞争格局。 该合作利用了 TetraMem 的模拟忆阻器交叉阵列技术与 CMOS 工艺的集成方案，此前的相关研究成果已发表于《Nature》杂志。尽管该芯片实现了显著的能效提升，但文章指出其性能基准尚未完整公开，其吞吐量能否匹敌竞品边缘 AI 加速器仍存疑问。

rss · Tom's Hardware · 7月10日 16:58

**背景**: 忆阻器（memristor）是一种非线性二端电子元件，其电阻值会随流过电荷量的变化而改变，并且在断电后仍能保持该电阻状态——本质上将存储与计算功能合二为一。存内计算（In-Memory Computing, IMC）是一种新兴的非冯·诺依曼计算范式，它直接在存储阵列内部执行计算，而无需在独立的处理单元和存储单元之间搬运数据，对于以大向量乘加运算为主的 AI 负载尤其具有吸引力。TetraMem 是从 USC 研究项目中衍生出的初创公司，是模拟忆阻器技术的先驱，此前已展示过可在极端温度（700°C）下工作的忆阻器，凸显了该技术在恶劣环境与太空应用中的潜力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Memristor">Memristor - Wikipedia</a></li>
<li><a href="https://research.ibm.com/projects/in-memory-computing">In-memory computing - IBM Research</a></li>
<li><a href="https://thenextweb.com/news/tetramem-memristor-700c-space-ai-computing">TetraMem memristor survives 700 degrees Celsius as startup moves...</a></li>

</ul>
</details>

**标签**: `#hardware`, `#edge-AI`, `#memristors`, `#in-memory-computing`, `#semiconductors`

---

<a id="item-18"></a>
## [独家 | 智谱创始人唐杰发内部信：「GLM 时刻」之后，什么是更重要的事](https://36kr.com/p/3891132709206784?f=rss) ⭐️ 6.3/10

智谱 AI 创始人唐杰的内部信揭示了公司在 DeepSeek R1 之后对编程与推理能力的战略押注，推动市值增长 10 倍、估值突破万亿港元，开源模型 GLM-5.2 性能比肩 Claude Opus 4.8 和 GPT-5.5。

rss · 36氪 · 7月11日 11:28

**标签**: `#Zhipu-AI`, `#GLM-5.2`, `#AI-Coding`, `#Chinese-AI`, `#Open-Source-LLMs`

---

<a id="item-19"></a>
## [9 点 1 氪丨“国产存储第一股”长鑫科技公布承销团阵容；SK 海力士登陆美股，上市首日大涨近 13%；OpenAI 推出 ChatGPT 智能体](https://36kr.com/p/3890553690192384?f=rss) ⭐️ 6.3/10

Daily tech news roundup highlighting SK Hynix's successful ~$265B US listing, OpenAI's ChatGPT agent launch, and Long Xin Technology's IPO underwriting team announcement as China's domestic storage leader.

rss · 36氪 · 7月11日 01:24

**标签**: `#AI`, `#semiconductors`, `#IPO`, `#OpenAI`, `#Chinese-tech`

---

<a id="item-20"></a>
## [《终结者 2》开创性视觉特效技术的口述历史](https://vfxblog.com/2017/08/23/the-tech-of-terminator-2-an-oral-history/) ⭐️ 6.0/10

VFXBlog 发布了一篇详尽的口述历史，记录了为 1991 年电影《终结者 2：审判日》所开创的视觉特效技术，其中包含对那些发明了如今已成为行业标准技术的工程师和艺术家的采访。 《终结者 2》是一部突破视觉特效边界的里程碑式影片，其开发的技术——包括变形动画、go-motion 动态定格动画以及早期 CGI 角色制作——为现代视觉特效奠定了基础。了解这段历史有助于当代从业者认识到沿用至今的工具和工作流程的起源。 该片的特效由四个核心团队开发：工业光魔（ILM）、斯坦·温斯顿工作室、Fantasy II Film Effects 以及 4-Ward Productions，太平洋数据影像和 Video Images 提供了部分额外特效。T-1000 的液态金属变形依赖于使用 Cyberware 头部与面部扫描仪的变形技术，而 T-800 的定格动画场景则采用了 ILM 与菲尔·蒂皮特共同开发的 go-motion 技术，在每一帧中引入运动模糊效果。

hackernews · markus_zhang · 7月10日 16:48 · [社区讨论](https://news.ycombinator.com/item?id=48862365)

**背景**: 变形（morphing）是一种视觉特效技术，可以将一个图像或形状无缝转变为另一个，自 1990 年代初便取代了传统的溶解过渡方法。Go-motion 是 ILM 与菲尔·蒂皮特共同开发的定格动画变体，在每一帧中加入运动模糊，弥补了传统定格动画那种断断续续、过于锐利的视觉效果。这些技术——连同使用 Softimage 软件制作的早期变形合成——共同塑造了 T-1000 的视觉形象，并持续影响至今的数字角色动画制作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Special_effects_of_Terminator_2:_Judgment_Day">Special effects of Terminator 2: Judgment Day - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Morphing">Morphing - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Go_motion">Go motion - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这篇口述历史是难得的佳作，并对当时几乎所有特效流程都必须从零发明感到惊讶。一些评论补充了宝贵的背景信息，包括 Softimage 在该片制作中的角色、用于液态金属弹孔效果的实用爆炸装置（squibs），以及推荐了关于 ILM 艺术家 Steve 'Spaz' Williams 的纪录片《Jurassic Punk》（2022）。部分读者反思，当代 CGI 是否能像 T2 中的实物特效和早期数字特效那样经得起时间的考验。

**标签**: `#visual-effects`, `#computer-graphics`, `#film-history`, `#technology-history`, `#CGI`

---