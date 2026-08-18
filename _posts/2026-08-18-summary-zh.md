---
layout: default
title: "Horizon Summary: 2026-08-18 (ZH)"
date: 2026-08-18
lang: zh
---

> 从 85 条内容中筛选出 20 条重要资讯。

---

1. [DuckDB v2.0 预览：Quack 新增客户端/服务器模式](#item-1) ⭐️ 9.0/10
2. [AI 生成的 GitHub Copilot“Autofix”导致 Snowflake 的 Jira 被入侵](#item-2) ⭐️ 8.0/10
3. [HBM 出货转向马来西亚，英特尔 Project Pelican 成 CoWoS 竞争对手](#item-3) ⭐️ 7.5/10
4. [Intel Nova Lake-S 测试曝光，支持 AVX-512 和 APX 指令集](#item-4) ⭐️ 7.5/10
5. [Geekom 在 AMD 迷你电脑中捆绑含恶意软件驱动，已下架处理](#item-5) ⭐️ 7.5/10
6. [DDR5 内存价格 12 个月内暴涨 500%，达历史最低价 10 倍](#item-6) ⭐️ 7.5/10
7. [美国最大电网拟在电力短缺时优先切断新数据中心供电——50 兆瓦以上数据中心须自备发电设施以避免断电](#item-7) ⭐️ 7.5/10
8. [美国一原告在法庭文件中植入针对 LLM 的提示词](#item-8) ⭐️ 7.3/10
9. [AI;DR 运动：读者开始抵制 LLM 生成内容](#item-9) ⭐️ 7.0/10
10. [液冷技术将于 2026 年在高端 AI 服务器中实现 53%渗透率](#item-10) ⭐️ 7.0/10
11. [嵌入式设备中类脑神经形态芯片的安全短板](#item-11) ⭐️ 7.0/10
12. [英伟达预订台积电 1.6nm A16 产能用于 Feynman GPU](#item-12) ⭐️ 7.0/10
13. [数据中心 XPU 与 CPU 的比例正从 10:1 向 1:1 转变](#item-13) ⭐️ 7.0/10
14. [华硕 GPU Tweak III 新增自动关机功能，防止 12V-2×6 接头熔毁](#item-14) ⭐️ 6.5/10
15. [长鑫存储(CXMT)在 AMD 平台突破 DDR5 9,000 MT/s 大关](#item-15) ⭐️ 6.5/10
16. [阿里巴巴以至少 15 亿美元出售其游戏工作室以资助 AI 布局，效仿美光退出消费业务的做法——清空其在灵犀游戏（开发了《三国志：战略版》）的全部股权](#item-16) ⭐️ 6.5/10
17. [切罗基族禁止在其部落土地建设超大规模数据中心](#item-17) ⭐️ 6.5/10
18. [AI 数据中心光互连市场规模到 2030 年将达 1440 亿美元](#item-18) ⭐️ 6.5/10
19. [PC Partner 警告 2026 年下半年显卡涨价及入门级产品缺货](#item-19) ⭐️ 6.5/10
20. [日本维修店推出 25 美元/GB 显存升级服务，打造廉价 AI 工作站](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [DuckDB v2.0 预览：Quack 新增客户端/服务器模式](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 9.0/10

DuckDB v2.0 预览版发布，带来多项重大新特性，其中最引人注目的是「Quack」扩展，它实现了原生客户端/服务器协议，允许 DuckDB 实例通过网络相互通信。v2.0 版本还整合了在不到六个月内累积的大约 10,000 次提交。 Quack 将 DuckDB 从一个纯粹的嵌入式分析引擎转变为混合式客户端/服务器系统，极大地扩展了其部署场景——从单机分析到分布式工作负载——同时不牺牲其标志性的易用性。v2.0 里程碑也标志着对一个已成为现代数据栈基础层工具的持续强力投入，从 dbt 管道到流式处理引擎。 Quack 以扩展（extension）形式交付而非核心改动，这意味着客户端和服务器端都是通过原生协议通信的 DuckDB 实例。DuckDB 团队提到，用户「一直非常坚持地」要求客户端/服务器模式，而团队此前更倾向于嵌入式模型而未予支持。

hackernews · ibotty · 8月17日 13:46 · [社区讨论](https://news.ycombinator.com/item?id=49330781)

**背景**: DuckDB 是一个进程内分析型（OLAP）数据库管理系统，于 2018 年首次发布，旨在直接在应用程序（通常是 Python 或 R）中执行快速的列式分析。与 PostgreSQL 等传统客户端/服务器系统不同，DuckDB 嵌入在宿主进程中运行，类似于 SQLite，但针对分析工作负载进行了优化。它支持磁盘溢出（spill to disk），以处理大于可用内存的数据集，并已在本地数据分析、数据工程管道和嵌入式分析中广受欢迎。OLAP（在线分析处理）是指针对复杂多维查询和报表进行优化的数据库系统，与处理大量小型事务的 OLTP（在线事务处理）形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://duckdb.org/2026/08/17/duckdb-20-highlights">A Preview of DuckDB v2.0 – DuckDB</a></li>
<li><a href="https://duckdb.org/quack/">Quack Remote Protocol – DuckDB</a></li>
<li><a href="https://duckdb.org/">DuckDB – An in-process SQL OLAP database management system</a></li>
<li><a href="https://en.wikipedia.org/wiki/Online_analytical_processing">Online analytical processing - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应极为热烈，实践者们将 DuckDB 描述为 dbt 管道、流式分析引擎（如每秒处理数千事件的 sql-flow）、空间数据工作负载和嵌入式运行时存储的首选工具。多位评论者特别表达了对 Quack 的兴奋之情。一个值得注意的讨论线索质疑不到六个月内的 10,000 次提交是否反映了大量 AI 辅助开发，引发了关于 AI 增强型开源开发速度的更广泛元讨论。

**标签**: `#duckdb`, `#database`, `#analytics`, `#olap`, `#open-source`

---

<a id="item-2"></a>
## [AI 生成的 GitHub Copilot“Autofix”导致 Snowflake 的 Jira 被入侵](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 8.0/10

AI 生成的 GitHub Copilot“Autofix”代码在 Snowflake 的 GitHub Actions 工作流中引入了模板注入漏洞，导致其 Jira 实例遭到入侵。

hackernews · galnagli · 8月17日 14:18 · [社区讨论](https://news.ycombinator.com/item?id=49331423)

**标签**: `#security`, `#ai-generated-code`, `#github-actions`, `#supply-chain`, `#copilot`, `#vulnerability`

---

<a id="item-3"></a>
## [HBM 出货转向马来西亚，英特尔 Project Pelican 成 CoWoS 竞争对手](https://www.techpowerup.com/351658/hbm-shipments-to-malaysia-surge-pointing-to-intels-project-pelican-facility) ⭐️ 7.5/10

根据 SemiAnalysis Chipbook 的出口数据，韩国出口的高带宽内存（HBM）正越来越多地流向马来西亚而非台湾，目前约有 13 亿美元 HBM 发往马来西亚，而发往台湾的不足 30 亿美元——几个月前发往台湾的金额还超过 50 亿美元。分析人士推断，英特尔位于马来西亚的 70 亿美元 Project Pelican 先进封装工厂正在吸收此前由台积电 CoWoS 主导的 HBM 集成工作。 这一转变标志着英特尔正成为先进 HBM 封装领域一个可行的第二来源，有望打破台积电在 CoWoS 技术上的近乎垄断地位，而该技术对 AI 加速器生产至关重要。如今代工客户在 chiplet 集成方面拥有了替代路径，这可能重塑 AI 芯片供应链，并缓解此前制约英伟达及其他 AI GPU 交付的 CoWoS 产能瓶颈。 英特尔的 Project Pelican 支持 EMIB（Embedded Multi-die Interconnect Bridge，嵌入式多芯片互连桥接）和 Foveros 两种封装流程，该工厂目前已完成 99%，预计 2026 年开始运营。推断接收这批 HBM 的是英特尔而非台积电或其他马来西亚小型厂商，其依据在于台积电在马来西亚没有先进封装工厂，且目前只有英特尔的 EMIB/Foveros 技术足够成熟，能够处理大规模 HBM 集成。

rss · TechPowerUp News · 8月17日 17:19

**背景**: 高带宽内存（HBM）是一种 3D 堆叠的 DRAM 技术，可在内存与处理器之间提供极高的数据传输带宽，是英伟达 GPU 等 AI 训练和推理芯片的核心组件。台积电的 CoWoS（Chip-on-Wafer-on-Substrate，芯片-晶圆-基板）以及英特尔的 EMIB 和 Foveros 等先进封装技术，是将 HBM 堆叠与逻辑芯片物理集成在单一封装内所必需的，也是现代 AI 加速器所采用的 chiplet 设计的基础。CoWoS 有多个变体——CoWoS-S、CoWoS-L 和 CoWoS-R——在互连密度和可扩展性方面各有取舍。CoWoS 的需求已远远超过供应，成为 AI 硬件供应链中的重大瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/343545/intel-completes-project-pelican-malaysia-packaging-fab-for-emib-and-foveros">Intel Completes "Project Pelican" Malaysia Packaging Fab for EMIB and Foveros | TechPowerUp</a></li>
<li><a href="https://www.trendforce.com/news/2026/03/18/news-intel-ramps-up-advanced-packaging-malaysia-complex-operational-in-2026-emib-update/">[News] Intel Ramps Up Advanced Packaging: Malaysia Complex Operational in 2026, EMIB Update</a></li>
<li><a href="https://www.ariat-tech.com/blog/CoWoS-Packaging-Explained-CoWoS-S-vs.CoWoS-R-vs.CoWoS-L,HBM,Manufacturing,and-AI-Chips.html">CoWoS Packaging Explained: CoWoS - S vs. CoWoS - R vs....</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#intel`, `#HBM`, `#advanced-packaging`, `#supply-chain`

---

<a id="item-4"></a>
## [Intel Nova Lake-S 测试曝光，支持 AVX-512 和 APX 指令集](https://www.techpowerup.com/351647/intel-nova-lake-s-tested-with-avx-512-and-apx-enabled) ⭐️ 7.5/10

据 InstLatX64 确认，Intel 正在内部测试两款 Nova Lake-S 桌面 CPU 型号——24 核版本（频率 3.4 GHz）和 28 核版本（频率 3.2 GHz），两者均支持 AVX-512 和 APX 指令集。这证实了 512 位向量处理能力在缺席多年后正式回归 Intel 桌面处理器产品线。 AVX-512 回归 Intel 主流桌面平台，弥合了高性能计算、科学计算、机器学习推理以及其他 SIMD 重负载工作负载的重大性能差距——这些任务此前只能依赖 Xeon 或 HEDT 芯片完成。结合 APX 将通用寄存器数量翻倍的特性，Nova Lake-S 缩小了消费级与服务器/专业级产品之间的鸿沟，为开发者和发烧友提供了更强大的通用计算与向量计算平台。 Nova Lake-S 采用 "Coyote Cove" 性能核和 "Arctic Wolf" 能效核，搭配新的 LGA1954 插槽，预计 2026 年晚些时候发布。Alder Lake 和 Raptor Lake 消费级 CPU 曾因混合架构中 P 核与 E 核差异导致软件优化复杂而禁用 AVX-512，此次重新引入意味着 Intel 已解决软硬件共存的难题。

rss · TechPowerUp News · 8月17日 12:46

**背景**: AVX-512 是 Intel 于 2013 年推出、2016 年随 Xeon Phi（Knights Landing）首次量产的 512 位宽 SIMD 指令集扩展，每个时钟周期的浮点运算量是 256 位 AVX2 的两倍，在高性能计算、密码学和机器学习等场景中价值显著。Intel APX（Advanced Performance Extensions，高级性能扩展）将通用寄存器数量从 16 个翻倍至 32 个，并新增其他特性，在不显著增加芯片面积和功耗的前提下提升通用计算性能。Intel 最初在 12 代 Alder Lake 混合架构 CPU 上禁用了 AVX-512，原因是异构核心类型上运行 512 位指令会带来软件优化复杂性，导致需要 AVX-512 的桌面用户只能转向 Xeon 或 HEDT 平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://builders.intel.com/docs/networkbuilders/intel-avx-512-instruction-set-for-packet-processing-technology-guide-1645717553.pdf">Intel ® AVX - 512 - Instruction Set for Packet Processing Technology...</a></li>
<li><a href="https://www.phoronix.com/news/Intel-APX">Intel Details APX - Advanced Performance Extensions - Phoronix</a></li>
<li><a href="https://www.igorslab.de/en/intel-nova-lake-s-when-mainstream-suddenly-smells-like-hedt/">Intel Nova Lake - S : When mainstream suddenly smells like... | igor´sLAB</a></li>

</ul>
</details>

**标签**: `#intel`, `#cpu-architecture`, `#avx-512`, `#nova-lake`, `#hardware`

---

<a id="item-5"></a>
## [Geekom 在 AMD 迷你电脑中捆绑含恶意软件驱动，已下架处理](https://www.tomshardware.com/tech-industry/cyber-security/geekom-admits-to-shipping-malware-laced-network-drivers-for-amd-mini-pcs-company-responds-with-guidance-removes-malicious-package) ⭐️ 7.5/10

Geekom 已确认其网站托管的 A7、A8、AE7、AX7 Pro 和 AX8 Pro 等 AMD 迷你电脑的网络驱动被 Windows 安全中心标记为可执行攻击者命令的木马程序，目前公司已彻底下架受影响的旧版 LAN 驱动下载页面。在官方声明中，Geekom 将问题归因于旧页面上的过期资源，该页面虽已不再从主产品页链接，但此前仍可公开访问。 这是一起典型的供应链安全事件：硬件厂商通过官方下载渠道提供了含有恶意软件的驱动程序，直接损害了消费者对开箱即用设备的信任。该事件凸显了消费者应通过多种扫描工具验证驱动程序下载的重要性，也再次呼吁硬件厂商在软件物料清单方面提高透明度。 该恶意文件经多个独立扫描服务验证确为恶意软件，包括 VirusTotal（使用 70 多个杀毒引擎）、FileScan 和 OPSWAT 的 MetaDefender。Geekom 表示问题仅限于已下架的旧版驱动并已发表致歉声明，但据报道该公司还曾要求撤下关于此事件的报道内容，引发了外界对其透明度的质疑。

rss · Tom's Hardware · 8月17日 17:18

**背景**: 供应链安全是指对软件和硬件交付链中的每个环节进行安全防护，因为攻击者经常利用受信任的供应商渠道来分发恶意软件。当硬件厂商提供含有恶意软件的驱动时，相信其为合法软件而安装的客户可能会在不知情的情况下让攻击者远程执行命令。VirusTotal 和 MetaDefender 等多引擎恶意软件扫描平台允许用户和研究人员通过一次性将可疑文件提交给数十个杀毒引擎和沙箱环境来独立验证文件安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VirusTotal">VirusTotal - Wikipedia</a></li>
<li><a href="https://www.opswat.com/products/metadefender">Advanced Threat Prevention - MetaDefender - OPSWAT</a></li>
<li><a href="https://www.linkedin.com/posts/tekkeez_smbsecurity-supplychain-cybersecurity-activity-7415105351567507456-PMRi">Protect Your Supply Chain from Cyber Risks | TekkEez... | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: Reddit 上 r/MiniPCs 社区的用户对恶意软件发出警告，并分享了来自 VirusTotal、FileScan 和 MetaDefender 的验证结果以确认威胁。社区对 Geekom 的态度非常负面，由于据报道该公司试图通过下架请求来压制原始报道而非首先透明地处理问题，用户的失望情绪进一步加剧。

**标签**: `#cybersecurity`, `#supply-chain-security`, `#malware`, `#hardware`, `#consumer-electronics`

---

<a id="item-6"></a>
## [DDR5 内存价格 12 个月内暴涨 500%，达历史最低价 10 倍](https://www.tomshardware.com/pc-components/ram/memory-prices-climb-500-percent-in-12-months-up-to-10x-the-lowest-ever-tracked-prices-128gb-of-ddr5-now-usd3-399) ⭐️ 7.5/10

据 Tom's Hardware 报道，DDR5 内存价格在过去的 12 个月内暴涨了约 500%，目前已达到历史最低价的 10 倍，一套 128GB 的 DDR5 内存现在售价为 3,399 美元。 这次前所未有的内存价格上涨波及 PC 装机用户、游戏玩家、数据中心和 AI 基础设施项目，可能延缓硬件升级步伐，并推高整个计算行业的系统总成本。 价格上涨的主要驱动力是 AI 服务器需求激增导致内存供应被大量占用；类似的涨价趋势也波及 SSD 及其他存储产品，整个内存市场面临紧张的产能分配。

rss · Tom's Hardware · 8月17日 13:52

**背景**: DDR5 是最新一代的双倍数据速率同步动态随机存取存储器（DRAM），在带宽、功耗和单条容量方面均优于前代 DDR4。当前的内存危机（被称为"RAMpocalypse"）主要归因于 AI 公司大规模建设数据中心，对系统内存（DRAM）和存储（NAND/SSD）产生了巨大需求。内存厂商将产能优先分配给高容量的服务器级产品，消费级 DIMM 供应被挤压，推动零售价格升至历史最高水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcgamer.com/hardware/memory/ram-and-storage-is-ridiculously-expensive-right-now-because-of-drumroll-ai-of-course-and-theres-little-reason-to-think-prices-will-drop-any-time-soon/">Explainer: The RAMpocalypse is making memory , SSDs... | PC Gamer</a></li>
<li><a href="https://en.hwlibre.com/DDR5-memory-price-crisis:-why-have-prices-skyrocketed-and-when-might-they-come-down/">DDR5 memory price crisis : why prices have skyrocketed and when...</a></li>
<li><a href="https://en.wikipedia.org/wiki/DDR_SDRAM">DDR SDRAM - Wikipedia</a></li>

</ul>
</details>

**标签**: `#memory`, `#DDR5`, `#hardware`, `#pricing`, `#PC-components`

---

<a id="item-7"></a>
## [美国最大电网拟在电力短缺时优先切断新数据中心供电——50 兆瓦以上数据中心须自备发电设施以避免断电](https://www.tomshardware.com/tech-industry/data-centers/new-data-centers-on-americas-largest-grid-face-first-in-line-blackouts-unless-they-bring-their-own-power) ⭐️ 7.5/10

PJM 互联公司提议制定联邦规则，在电力短缺期间优先切断新建大型数据中心（50 兆瓦以上）的电力供应，除非这些数据中心自备现场发电设施。

rss · Tom's Hardware · 8月17日 13:11

**标签**: `#data-centers`, `#energy-policy`, `#ai-infrastructure`, `#grid-management`, `#regulation`

---

<a id="item-8"></a>
## [美国一原告在法庭文件中植入针对 LLM 的提示词](https://www.solidot.org/story?sid=85109) ⭐️ 7.3/10

本期简报涵盖：已知首例在美国法庭文件中嵌入 LLM 提示词注入的案件；对亚马逊大规模扫描并销毁书籍以获取 AI 训练数据行为的调查；以及 Qwen 在 Hugging Face 上的下载量突破 30 亿次。

rss · Solidot · 8月17日 07:16

**标签**: `#prompt-injection`, `#AI-security`, `#legal-tech`, `#AI-training-data`, `#Qwen`

---

<a id="item-9"></a>
## [AI;DR 运动：读者开始抵制 LLM 生成内容](https://www.rickmanelius.com/p/aidr-ai-didnt-read) ⭐️ 7.0/10

"AI;DR"（AI; Didn't Read，即"AI 写的，我不读"）这一概念在 Hacker News 上爆火，获得 562 个赞和 353 条评论，反映出人们在网上文章、代码库和工作沟通中对 LLM 生成文本日益强烈的抵触情绪。 这标志着一种成熟的、针对不加批判地使用 AI 的文化反扑：读者开始通过拒绝机器生成的文字来筛选自己的注意力，这可能重塑内容策略、开发者文档实践以及团队在协作工作流中使用 LLM 的方式。讨论中分享的工作场景轶事表明，这种抵触不仅仅是审美层面的，而是具有实际影响的——代码库因为冗长的 AI 文档而变得"不可读"。 Hacker News 上的讨论揭示了具体的痛点：开发者反映 PR 文档被 AI 生成内容淹没，只剩下关于变量命名的"表演性"注释；一些评论者认为，共享原始 prompt 比共享 AI 输出更有价值。这一运动将 AI 生成的文本视为"智识懒惰"的信号，而非真正的专业知识传递。

hackernews · mooreds · 8月17日 19:47 · [社区讨论](https://news.ycombinator.com/item?id=49336573)

**背景**: 自 2022 年末 ChatGPT 公开发布以来，LLM 生成的文本已遍布互联网，从博客文章、产品描述到代码注释和企业文档。研究者开发了使用文体统计学（stylometry，即对写作风格进行统计分析）和机器学习分类器的检测工具来识别 AI 生成的文本，但这些工具在跨领域泛化方面往往表现不佳，且容易被轻微编辑规避。与此同时，随着 AI 的普及，一种文化反弹也在增长，读者和专业人士越来越多地表达对 LLM 输出所伴随的冗长、术语堆砌和缺乏个人特色的不满。"AI;DR"标签是这种更广泛怀疑论的一部分，它借鉴了早期的"TL;DR"缩写，但将其变成了对抗机器写作的一种社交信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thealgorithmicbridge.com/p/its-ai-so-i-didnt-read">It’s AI , so I Didn ’ t Read - by Alberto Romero</a></li>
<li><a href="https://news.ycombinator.com/item?id=49336573">AI ; DR ( AI ; Didn ' t Read ) | Hacker News</a></li>
<li><a href="https://aman.ai/primers/ai/AIDetect/">Aman's AI Journal • NLP • AI Text Detection Techniques</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论帖显示出广泛共识，即未经请求的 AI 生成内容不受欢迎。评论者描述了工作中 AI 文档膨胀代码库、降低可读性的挫败感，批评 AI 文字冗长、缺乏细微差别，一些人还提出了一个颇具挑衅性的建议：与其共享 AI 输出，不如共享生成它的 prompt。一个反复出现的主题是，AI 文本意味着智识上的懒惰，并侵蚀真实的人际交流；不过也有少数人反驳，认为只有一小部分 AI 生成的文字值得一读，而"AI;DR"标签本身就是一种表演行为。

**标签**: `#ai-generated-content`, `#culture`, `#llm`, `#developer-experience`, `#content-quality`

---

<a id="item-10"></a>
## [液冷技术将于 2026 年在高端 AI 服务器中实现 53%渗透率](https://www.dramexchange.com/WeeklyResearch/Post/2/12801.html) ⭐️ 7.0/10

TrendForce 最新的 AI 服务器研究报告显示，受先进 AI 工作负载（如大语言模型训练与推理）不断攀升的散热需求驱动，高端 AI 服务器基础设施中的液冷技术采用率预计将于 2026 年达到 53%。 这一转变标志着数据中心架构的根本性变革，因为传统风冷技术越来越难以应对下一代 AI 加速器产生的热量。超大规模云服务商、托管数据中心运营商以及服务器 OEM 厂商将需要重新设计机房布局、供应链以及运维流程，以大规模部署液冷方案。 液冷相比风冷能效更高，因为它减少了热管理所需的能耗，从而实现更高的服务器密度并降低数据中心整体运营成本。不过原文内容被截断，因此按冷却类型（直接芯片冷却与浸没式冷却）划分的细分数据或厂商层面的具体数字在原文中未能获取。

rss · DRAMeXchange (TrendForce) · 8月17日 03:59

**背景**: 液冷是一种利用液体（通常是水或介电流体）将服务器组件热量带走散热管理方式，与传统的风扇和暖通空调风冷方案不同。TrendForce 是一家总部位于台湾的市场研究机构，在半导体、显示和数据中心等行业以其技术采用率和价格预测而被广泛引用。AI 工作负载——尤其是 GPU 集群上训练大型神经网络——产生的单机架热量远超传统计算任务，使风冷系统逼近极限，推动了行业向液冷方案的转型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trendforce.com/">Global Market Intelligence & Consulting | TrendForce</a></li>
<li><a href="https://www.linkedin.com/pulse/untapped-potential-liquid-cooling-modern-data-centres-tony-lock-eew5e">The Untapped Potential of Liquid Cooling in Modern Data Centres</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#liquid cooling`, `#TrendForce`, `#server hardware`

---

<a id="item-11"></a>
## [嵌入式设备中类脑神经形态芯片的安全短板](https://www.electronicsweekly.com/news/design/eda-and-ip/security-challenges-of-neuromorphic-intelligence-on-embedded-systems-2026-08/) ⭐️ 7.0/10

Electronics Weekly 发表了 Venus Kohli 的分析文章，指出虽然类脑神经形态芯片为嵌入式设备提供了卓越的处理效率，但其在安全性方面的成熟度仍落后于传统的冯·诺依曼处理器。 随着神经形态处理器越来越多地用于边缘 AI 和物联网应用，未解决的安全漏洞可能使资源受限设备中的敏感数据和关键功能面临风险。在这些芯片能够大规模安全部署于汽车、工业和消费类嵌入式系统之前，弥补这一差距至关重要。 文章将神经形态方案（在芯片上集成存储与计算以实现类脑计算）与围绕冯·诺依曼 CPU 几十年发展所形成的完善安全生态进行了比较。已发布的摘要较为简短，未列出具体的攻击向量，但表明神经形态硬件的安全工具、形式化验证和威胁建模仍是不成熟的领域。

rss · Electronics Weekly · 8月17日 11:46

**背景**: 神经形态计算是对传统冯·诺依曼架构（处理单元与内存物理分离）的根本性突破。神经形态芯片采用存内计算和脉冲神经网络（SNN）来模拟生物神经元的运作方式，尤其在事件驱动和感知 AI 任务中具有出色的能效。由于这一范式相对较新，那些经过数十年为 CPU 和 GPU 打磨的安全基础设施——硬件信任根、侧信道防御、加密内存总线以及成熟的验证流程——在神经形态加速器上尚未达到同等水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.ibm.com/blog/what-is-neuromorphic-or-brain-inspired-computing">How neuromorphic computing takes inspiration from our brains</a></li>
<li><a href="https://fiveable.me/advanced-computer-architecture/unit-16/neuromorphic-computing-architectures/study-guide/MH0tY1CQkuItJgKO">Neuromorphic Computing Architectures | Advanced... | Fiveable</a></li>
<li><a href="https://www.researchgate.net/publication/378891450_NEUROSEC_FPGA-Based_Neuromorphic_Audio_Security">(PDF) NEUROSEC: FPGA-Based Neuromorphic Audio Security</a></li>

</ul>
</details>

**标签**: `#neuromorphic-computing`, `#embedded-systems`, `#hardware-security`, `#AI-hardware`, `#edge-AI`

---

<a id="item-12"></a>
## [英伟达预订台积电 1.6nm A16 产能用于 Feynman GPU](https://www.electronicsweekly.com/news/business/nvidia-books-tsmc-1-6nm-process-for-feynman-in-h2-2028-2026-08/) ⭐️ 7.0/10

据报道，英伟达已预订台积电 A16（1.6nm）工艺产能，用于其继 Rubin 之后的'Feynman' GPU 架构，预计 2028 年下半年量产。 这一预订确认了英伟达在 Rubin 之后多年的 GPU 路线图，并验证了台积电 1.6nm A16 节点作为最苛刻 AI 加速器的可行平台，表明 HPC 和 AI 芯片生态对尖端工艺技术的需求持续旺盛。 A16 节点是台积电首个'埃米级'工艺，取代 2nm N2 节点，同时集成 GAA（全环绕栅极）晶体管和背面供电网络（BSPDN），相较 N2 可提供约 10%的性能提升或 20%的功耗降低，最初计划于 2026 年末量产。

rss · Electronics Weekly · 8月17日 05:17

**背景**: 台积电的工艺节点已从传统的纳米级命名（如 5nm、3nm、2nm）进入'埃米时代'，A16（1.6nm）代表下一代芯片制造工艺。A16 节点引入了全环绕栅极（GAA）晶体管，栅极完全包裹沟道以实现更优的静电控制，取代了早期节点使用的 FinFET 设计。此外，背面供电网络（BSPDN）将供电线路移至晶圆背面，可降低 IR 压降并释放正面布线资源。英伟达的 GPU 产品线历来遵循架构代次规律（Hopper、Blackwell、Rubin），'Feynman'延续了这一传统，作为 Rubin 之后的继任者，面向 AI 和 HPC 工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/tsmc-a16-node-promises-speed-boost-power-cut-over-2nm-backside-power-production-q4-2026/">TSMC 's A 16 ' 1 . 6 nm ' Node Promises 10% Speed Boost or 20% Power...</a></li>
<li><a href="https://www.kad8.com/hardware/tsmc-a16-node-explained-backside-power-and-angstrom-era/">TSMC A16 Node Explained: Backside Power and Angstrom Era · KAD</a></li>
<li><a href="https://semiengineering.com/what-designers-need-to-know-about-gaa/">What Designers Need To Know About GAA | Semiconductor Engineering</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#nvidia`, `#tsmc`, `#process-technology`, `#gpu-architecture`

---

<a id="item-13"></a>
## [数据中心 XPU 与 CPU 的比例正从 10:1 向 1:1 转变](https://www.electronicsweekly.com/news/business/xpu-to-cpu-ratio-transitioning-from-101-to-11-2026-08/) ⭐️ 7.0/10

Dell'Oro 报告称，随着推理工作负载的兴起带来了不同于训练的网络需求，数据中心的 XPU 与 CPU 比例正从 10:1 转向 1:1。

rss · Electronics Weekly · 8月17日 05:09

**标签**: `#datacenter`, `#AI infrastructure`, `#inference`, `#hardware trends`, `#networking`

---

<a id="item-14"></a>
## [华硕 GPU Tweak III 新增自动关机功能，防止 12V-2×6 接头熔毁](https://www.techpowerup.com/351662/asus-gpu-tweak-iii-adds-auto-shutdown-to-prevent-12v-2x6-meltdowns) ⭐️ 6.5/10

华硕发布了 GPU Tweak III V2.1.8.0 版本，为搭载 Power Detector+ 硬件的显卡新增自动关机保护功能。当系统通过 12V-2×6 电源接头侦测到持续高电流时，将自动关闭以防止硬件熔毁。 此次更新针对的是一个已被广泛记录的严重安全问题——高端 NVIDIA 显卡上的 12V-2×6 电源接头发生熔毁，导致昂贵的显卡报废。在硬件层面解决方案仍不明朗的情况下，这是行业持续努力中又一个软件层面的渐进式缓解措施。 自动关机功能仅适用于内置 Power Detector+ 传感器（包含分流电阻以监测每个针脚电流）的华硕显卡，具体型号包括 ROG Astral RTX 5090、ROG Astral LC RTX 5090、ROG Astral RTX 5080 和 ROG Matrix RTX 4090。华硕尚未披露触发关机的具体电流阈值和持续时间参数。

rss · TechPowerUp News · 8月17日 18:48

**背景**: 12V-2×6（也称为 12VHPWR）是一种 16 针电源接口标准，专为向高端 GPU 提供最高 600W 电力而设计，随 NVIDIA RTX 4000 系列推出，并在 RTX 5000 系列上继续使用。它取代了笨重的多组 8 针接口，但出现了大量广为报道的熔毁事件，通常由插入不当、针脚间电流分布不均或线缆与接头制造缺陷引起。Power Detector+ 是华硕推出的硬件级监控方案，利用传感器和分流电阻侦测电源接头各个针脚的异常电流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/12VHPWR">12 VHPWR - Wikipedia</a></li>
<li><a href="https://www.guru3d.com/story/asus-power-feature-how-it-prevents-overheating-in-rog-astral-gpus/">ASUS Power Detector+ Feature : How It Prevents Overheating in...</a></li>
<li><a href="https://rog.asus.com/me-en/articles/guides/how-gpu-tweaks-power-detector-alerts-you-to-abnormal-current-on-your-rog-astral-graphics-card/">How GPU Tweak's Power Detector+ alerts you to abnormal current on...</a></li>

</ul>
</details>

**标签**: `#ASUS`, `#GPU`, `#hardware-safety`, `#12V-2x6`, `#NVIDIA`

---

<a id="item-15"></a>
## [长鑫存储(CXMT)在 AMD 平台突破 DDR5 9,000 MT/s 大关](https://www.techpowerup.com/351649/cxmt-breaks-9-000-mt-s-barrier-with-ddr5) ⭐️ 6.5/10

中国 DRAM 制造商长鑫存储(CXMT)已在 AMD 平台上突破了 9,000 MT/s 的门槛，使用 48GB 的 iGame Shadow II 24G×2 内存套条在 Colorful iGame X870E VULCAN W OC 主板上达到了 9,014 MT/s（4,507 MHz）。该公司还在测试 6,000 MT/s 下的 CL30 甚至 CL28 超低延迟配置，标志着其性能已与全球领先 DRAM 厂商持平。 这一里程碑表明，中国最大的 DRAM 生产商长鑫存储正在与三星、SK 海力士和美光等老牌巨头实现具有竞争力的性能，这对全球内存市场竞争和中国的半导体自给自足具有重要意义。高传输速率与紧凑延迟（CL28-30）的结合，使长鑫存储的内存能够应用于高端消费和发烧友市场，而不仅仅是入门级领域。 9,014 MT/s 的数值源于双倍数据速率（DDR）技术，4,507 MHz 有效翻倍即可超过 9,000 MT/s。长鑫存储去年年底才达到 8,000 MT/s，这意味着几个月内速度提升了近 13%；在 AMD 和 Intel 平台上进行的 CL28 延迟测试表明，该公司在带宽和实际响应速度（以首字延迟衡量）两方面都在缩小差距。

rss · TechPowerUp News · 8月17日 13:28

**背景**: DDR5 是继 DDR4 之后的最新一代系统内存，提供现代 CPU、GPU 和 AI 工作负载所需的更高带宽和密度。MT/s（每秒百万次传输）衡量每秒发生的数据传输次数，由于双倍数据速率信号，对于 DDR 内存来说，其数值是 MHz 时钟频率的两倍。CAS 延迟（CL）衡量从发出内存请求到数据可用之间所经过的时钟周期数；与速度结合时，它决定了实际延迟。长鑫存储（CXMT）成立于 2016 年，是中国国产 DRAM 的旗舰企业，对减少中国对国外内存供应商依赖的努力至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.msn.com/en-us/news/technology/explainer-what-is-cxmt-and-how-did-it-become-chinas-dram-champion/ar-AA28L4vy">Explainer - what is CXMT and how did it become China's DRAM ...</a></li>
<li><a href="https://www.electronicshub.org/mhz-vs-mt-s/">MHz vs MT / s RAM: Decoded! (Understanding RAM Speed)</a></li>
<li><a href="https://zombrax.com/ddr5-speeds-and-timings/">DDR 5 Memory Speeds and Timings: What Moves the Needle</a></li>

</ul>
</details>

**标签**: `#DDR5`, `#memory`, `#CXMT`, `#overclocking`, `#hardware`

---

<a id="item-16"></a>
## [阿里巴巴以至少 15 亿美元出售其游戏工作室以资助 AI 布局，效仿美光退出消费业务的做法——清空其在灵犀游戏（开发了《三国志：战略版》）的全部股权](https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-sells-its-gaming-studio-for-at-least-1-5-billion-to-help-fund-ai-buildout) ⭐️ 6.5/10

阿里巴巴以至少 15 亿美元出售其游戏工作室灵犀游戏，以资助 AI 基础设施建设，这反映了整个行业优先投资 AI 的更广泛趋势。

rss · Tom's Hardware · 8月17日 15:39

**标签**: `#AI infrastructure`, `#Alibaba`, `#industry trends`, `#M&A`, `#investment`

---

<a id="item-17"></a>
## [切罗基族禁止在其部落土地建设超大规模数据中心](https://www.tomshardware.com/tech-industry/data-centers/largest-tribe-in-the-us-bans-hyperscale-data-centers-on-its-lands) ⭐️ 6.5/10

全美最大的印第安部落——拥有超过 47.5 万名公民的切罗基族——已正式禁止在其部落所有土地和联邦托管土地上建设超大规模数据中心。该部落以能源和水资源消耗、空气质量、噪音以及文化遗产保护等方面的担忧为由，并表示在未经事先协商的情况下不会支持任何数据中心项目。 这一决定是对当前 AI 基础设施热潮的重大抵制，因为超大规模数据中心主要由亚马逊、谷歌、微软和 Meta 等科技巨头建设，用于支持云计算和 AI 工作负载。它凸显了科技产业快速扩张与当地社区对环境影响和资源消耗担忧之间的紧张关系，并可能为面临类似开发压力的其他印第安部落树立先例。 "超大规模"数据中心指的是通常容纳数万台服务器的巨型设施，由少数主要云服务提供商运营，需要巨额资本投资并消耗大量能源和水资源用于冷却。该禁令专门适用于部落所有土地和联邦托管土地——这些地区由联邦政府持有法定所有权，但部落保留使用受益权和管辖权。

rss · Tom's Hardware · 8月17日 11:27

**背景**: 超大规模数据中心是为高效支持云计算和 AI 的巨大工作负载而设计的巨型设施，通常容纳通过数百英里光纤电缆连接的庞大服务器阵列。它们需要巨额资本投资，主要由亚马逊、谷歌、微软、Meta、苹果和 IBM 等公司运营。美国的部落土地包括保留地土地和联邦托管土地——托管土地由联邦政府持有法定所有权但由部落使用受益，而保留地边界则界定了部落历史管辖范围的外部界限。总部位于俄克拉荷马州的切罗基族是美国最大的联邦承认部落。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacenterdynamics.com/en/analysis/what-is-a-hyperscale-data-center/">What is a hyperscale data center ? - DCD</a></li>
<li><a href="https://en.wikipedia.org/wiki/Indian_reservation">Indian reservation - Wikipedia</a></li>
<li><a href="https://filtron.co/why-your-map-of-united-states-indian-reservations-is-probably-wrong-2dx">Why Your Map of United States Indian Reservations is... - Filtron</a></li>

</ul>
</details>

**标签**: `#data-centers`, `#infrastructure`, `#policy`, `#environmental-impact`, `#AI-infrastructure`

---

<a id="item-18"></a>
## [AI 数据中心光互连市场规模到 2030 年将达 1440 亿美元](https://www.tomshardware.com/tech-industry/photonics/ai-data-center-optical-interconnect-market-to-hit-usd144-billion-by-2030-an-over-ten-fold-increase-from-2024-figures-according-to-new-projections-silicon-photonics-expected-to-account-for-nearly-two-thirds-of-revenue-driven-by-co-packaged-optics) ⭐️ 6.5/10

CIC 预测，数据中心光互连市场规模将从 2024 年的 137 亿美元增长到 2030 年的 1444 亿美元，增长超过十倍。其中硅光子技术预计将占据 63.7%的收入，主要得益于共封装光学（CPO）的采用。 这一庞大的增长预测凸显了 AI 工作负载如何重塑数据中心基础设施，互连带宽和能效正成为关键瓶颈。硅光子和 CPO 的预期主导地位标志着芯片与交换机物理集成方式的根本性转变，将影响超大规模云服务商、半导体公司以及更广泛的供应链。 该预测将硅光子技术的主导地位归因于共封装光学（CPO），该架构通过超短电连接将光学引擎直接集成到交换机 ASIC 上，相比传统可插拔光学模块可降低功耗和延迟。然而，CPO 在本十年仍是一个快速增长但相对较小的细分市场，可插拔模块在现有 AI 数据中心设计中仍被广泛部署。

rss · Tom's Hardware · 8月17日 11:20

**背景**: 硅光子技术是一种将光子（基于光的）组件集成到硅芯片上的技术，相比传统电信号传输，能以更低的功耗实现更快、更高效的数据传输。共封装光学（CPO）是一种将光学引擎直接放置在与交换机 ASIC 同一封装上的架构，使用超短电互连替代可插拔收发模块中较长的连接。随着 AI GPU 和 CPU 处理速度的飙升，现有 I/O 基础设施难以跟上节奏，导致处理器频繁等待数据——这正是光子和共封装方案旨在解决的瓶颈问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.link-pp.com/resources/strategy/cpo-vs-pluggable-800g-architecture/">Co - Packaged Optics (CPO) vs Pluggable : 800G+ Scaling Limits</a></li>
<li><a href="https://www.avnet.com/integrated/resources/article/pluggable-vs-co-packaged-optics-in-ai-data-centers-power-scale-and-design-trade-offs/">Pluggable vs . co - packaged optics in AI data centers : Power, scale...</a></li>
<li><a href="https://www.ansys.com/blog/what-is-co-packaged-optics">What is Co - packaged Optics ?</a></li>

</ul>
</details>

**标签**: `#ai-infrastructure`, `#data-centers`, `#silicon-photonics`, `#market-forecast`, `#co-packaged-optics`

---

<a id="item-19"></a>
## [PC Partner 警告 2026 年下半年显卡涨价及入门级产品缺货](https://www.tomshardware.com/tech-industry/pc-partner-warns-of-rising-gpu-prices-and-budget-card-shortages-analyst-suggests-makers-are-hiking-prices-beyond-memory-costs) ⭐️ 6.5/10

PC Partner Group（旗下品牌包括 ZOTAC、Inno3D 和 Manli）警告称，由于显存成本上涨和供应趋紧，2026 年下半年显卡价格将进一步上涨，入门级显卡将面临最严重的缺货。分析师 Jon Peddie 暗示，厂商的涨价幅度超过了仅由显存成本上涨所支撑的水平。 这条新闻直接影响 PC 装机者和游戏玩家，尤其是依赖低价入门级显卡的用户，因为价格上涨和缺货可能使预算型装机成本大幅增加。它还表明整个 PC 硬件生态系统面临着更广泛的元器件成本压力，波及范围已扩展到 KTC 和 AOC 等品牌的显示器。 PC Partner 的显卡出货量在 2026 年上半年因元器件短缺下降了 18.4%，营收同比下降 9.2%至 44.6 亿港元，但平均售价仍上涨了 10.7%，说明在销量下降的同时厂商仍在提价。KTC 和 AOC 也已通知分销商即将上调显示器价格，原因为面板、电源元器件和制造成本上升。

rss · Tom's Hardware · 8月17日 11:00

**背景**: PC Partner Group 是一家总部位于香港的制造商，自主设计并生产以 ZOTAC、Inno3D 和 Manli 等自有品牌销售的显卡，同时也为其他公司提供 OEM 代工服务。Jon Peddie 是知名行业分析师，担任 Jon Peddie Research（JPR）总裁，该机构追踪 GPU 市场已有超过 35 年的历史。当前的供应紧张源于显存（如 GDDR6/GDDR7）产能受限，而这些产能同时需要满足 AI 和数据中心等领域的高需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/entry-level-gpus-were-gamers-last-hope-but-pc-partner-says-severe-shortages-arrive-in-second-half-of-2026/">Entry-level GPUs Were Gamers' Last Hope, But PC Partner Says...</a></li>
<li><a href="https://www.jonpeddie.com/">Jon Peddie Research – The latest statistics, trends, and reports on...</a></li>
<li><a href="https://www.eetimes.com/whats-the-story-with-gpus/">Addressing the Global GPU Supply Landscape - EE Times</a></li>

</ul>
</details>

**标签**: `#GPU`, `#hardware`, `#pricing`, `#PC-building`, `#industry-analysis`

---

<a id="item-20"></a>
## [日本维修店推出 25 美元/GB 显存升级服务，打造廉价 AI 工作站](https://www.tomshardware.com/pc-components/gpus/japanese-repair-shop-sells-gddr6-vram-upgrades-for-usd25-per-gb-during-memory-crisis-rtx-2080-ti-modded-to-22gb-for-just-usd282-double-the-vram-creates-a-budget-ai-powerhouse) ⭐️ 6.5/10

一家日本维修店开始以每 GB 25 美元的价格商业化提供 GPU GDDR6 显存升级服务，将一块 RTX 2080 Ti 从 11GB 升级到 22GB 仅需 282 美元。在当前内存价格危机期间，该服务能将旧款消费级 GPU 改造为经济实惠的 AI 工作站。 这一点很重要，因为全球内存价格危机使得新 GPU 和 AI 硬件变得极其昂贵，而这项售后服务提供了一种以极低成本将现有硬件重新用于 AI 工作负载的途径。无法负担当前代际大显存 GPU（如 RTX 3090 或数据中心卡）的预算有限的 AI 研究人员、爱好者和小型工作室，现在有了一条实用的路径来在本地运行更大的模型。 该升级需要高级 BGA 焊接技能、专业的返修设备以及对 GPU BIOS 和 strap 配置的了解——这不是一项适合新手的改装操作，存在永久损坏显卡的风险。每 GB 25 美元的定价是在 AI 驱动的内存供应紧缩导致 GDDR6 价格飙升的背景下制定的。

rss · Tom's Hardware · 8月17日 10:30

**背景**: VRAM（显存）是显卡上用于存储纹理、帧缓冲，以及越来越多地用于存储 AI 模型权重和激活值的专用内存。与可以轻松更换的桌面系统 RAM 不同，VRAM 使用 BGA（球栅阵列）芯片直接焊接在 GPU PCB 上，使得升级难度大得多。RTX 2080 Ti 最初搭载 352-bit 位宽的 11GB GDDR6 显存；将其翻倍到 22GB 需要更换所有显存芯片，并修改 GPU 的 BIOS/strap 设置以识别新容量。更大的 VRAM 对 AI 推理和训练至关重要，因为大语言模型和扩散模型通常会超出普通消费级显卡上 8-12GB 的可用容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://maketecheasier.com/what-vram-is-and-increase-vram/">What Is VRAM , How to Check It, and Can You... - Make Tech Easier</a></li>
<li><a href="https://www.youtube.com/watch?v=nJ97nUr1G-g">Can Any GPU Get a VRAM Upgrade ? | RTX 2080 Ti 11GB... - YouTube</a></li>
<li><a href="https://voltground.com/hardware/gddr6x-memory-temperature-guide/">GDDR 6 X Memory Temperature: Why 110 Degrees Is... — VoltGround</a></li>

</ul>
</details>

**标签**: `#GPU`, `#VRAM-upgrade`, `#hardware-mod`, `#AI-hardware`, `#budget-AI`

---