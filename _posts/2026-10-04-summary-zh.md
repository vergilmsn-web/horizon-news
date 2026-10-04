---
layout: default
title: "Horizon Summary: 2026-10-04 (ZH)"
date: 2026-10-04
lang: zh
---

> 从 36 条内容中筛选出 9 条重要资讯。

---

1. [Strata 工具让 125B Qwen 模型在消费级 RTX 4090 上以 124 词/秒运行](#item-1) ⭐️ 8.0/10
2. [Valve 开发者优化旧款 AMD GPU 的 Linux 支持](#item-2) ⭐️ 8.0/10
3. [分析：为什么开发者偏爱库而非原生浏览器 API](#item-3) ⭐️ 7.0/10
4. [加州下令停止人形机器人笼式格斗](#item-4) ⭐️ 6.5/10
5. [数据库专家使用 5900 行代码在 SQL 中运行 DOOM](#item-5) ⭐️ 6.5/10
6. [美军现场组装无人机投掷 3D 打印“Dragoon”炸弹](#item-6) ⭐️ 6.5/10
7. [Iranian national extradited to US over alleged $3.4 billion state-backed hacking campaign in rare legal win for law enforcement](#item-7) ⭐️ 6.5/10
8. [LeCun 对 AI 灭绝担忧不以为然，引发 AGI 与 LLM 辩论](#item-8) ⭐️ 6.0/10
9. [Jagex 宣布新 MMO《RuneScape 4》，基于 Unreal Engine 开发](#item-9) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Strata 工具让 125B Qwen 模型在消费级 RTX 4090 上以 124 词/秒运行](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

名为 Strata 的工具使 125B 参数量的 Qwen 3.8 Flash Next 模型能够以 124 词/秒的吞吐量在消费级 RTX 4090 硬件上运行。这一演示表明，先进的推理优化技术能够推动最先进的大规模 Mixture-of-Experts (MoE) 模型在无需多卡组网的普通消费级硬件上运行。 这大幅降低了运行高端大语言模型的硬件门槛，使个人开发者和爱好者能够用单张消费级 GPU 来测试 125B 级别的 MoE 架构。它证实了精密的量化与缓存技术可以在易于获取的硬件上实现接近数据中心级的性能，从而改变了本地部署大语言模型的成本曲线。 虽然实现了高速运行，但低于 4-bit 的量化运行存在显著的质量下降风险，正如依赖 4-bit 量化进行关键任务的用户所指出的那样。社区也在询问为什么 llama.cpp 等标准推理栈尚未原生集成这种专家缓存机制，暗示了专业工具与标准运行时之间可能存在的技术鸿沟。

hackernews · snehesht · 10月4日 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: Qwen 3.8 Flash Next 是一个具有 1250 亿参数的大规模 Mixture-of-Experts (MoE) 大语言模型。RTX 4090 是一款配备 24GB 显存的高端消费级显卡，在不采用激进优化技术的情况下，通常不足以加载 125B 的模型。量化是指降低模型权重精度（例如从 16-bit 降至 4-bit）以适应有限内存的过程，而专家缓存则是 MoE 模型中用于优化激活专家通路检索的一种技术。

**社区讨论**: 社区成员对于这种高速表现感到兴奋，但同时对低于 4-bit 量化所付出的代价持怀疑态度。一些用户惊讶于其在消费级配置上的出色表现，并质疑为何 llama.cpp 等标准工具尚未采用这种专家缓存技术；还有用户将其与 Dwarfstar 等现有替代方案进行了对比。

**标签**: `#LLM`, `#Inference Optimization`, `#Quantization`, `#Consumer Hardware`, `#Qwen`

---

<a id="item-2"></a>
## [Valve 开发者优化旧款 AMD GPU 的 Linux 支持](https://www.phoronix.com/news/XDC-2026-Valve-Timur-AMDGPU) ⭐️ 8.0/10

Valve 开发者 Timur Kristóf 展示了专门提升 Linux 内核对旧款 AMD GPU 支持的工作，从而极大地改善了其游戏性能和可用性。 这项举措延长了旧硬件的使用寿命，使 Steam Deck 等设备和旧款桌面 GPU 在 Linux 系统上具备更强的性能，并推动了更广泛的开源游戏生态系统。 改进主要针对特定的旧款 RDNA 和早于 RDNA 的架构，在配备这些 GPU 移动版的手持设备上已观察到实际益处，正如 XDC 2026 演示中所强调的那样。

hackernews · speckx · 10月3日 19:14 · [社区讨论](https://news.ycombinator.com/item?id=49946895)

**背景**: AMD 显卡依赖于 Linux 内核中的开源 amdgpu 驱动程序来运行。虽然像 Steam Deck APU 这样的最新芯片会持续获得优先更新，但旧款世代往往缺乏实现最佳性能所需的具体内核级优化。Valve 作为主要的 Linux 游戏倡导者，通常会在上游改进这些驱动程序。

**社区讨论**: 社区对实际益处感到兴奋，用户报告称旧款手持设备和桌面 GPU 在 Linux 上的表现比在 Windows 上更快更流畅，促使一些人考虑将整个主要设备切换到 Linux。

**标签**: `#Linux`, `#AMD`, `#GPU`, `#Valve`, `#Systems`

---

<a id="item-3"></a>
## [分析：为什么开发者偏爱库而非原生浏览器 API](https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/) ⭐️ 7.0/10

一项分析解释了为什么开发者经常更喜欢自行开发方案或使用 React 等框架，而不是使用原生浏览器平台功能。该论点强调，某些功能的原生实现要么繁琐不堪，要么设计不佳，导致理想与开发者实际体验之间存在脱节。 分析指出，平台 API 往往难以可靠使用，迫使开发者依赖提供更好组合性和抽象的框架。具体例子包括 HTML <datalist> 元素的可用性问题以及原生 Web Components 带来的陡峭学习曲线。

hackernews · vinhnx · 10月4日 04:10 · [社区讨论](https://news.ycombinator.com/item?id=49950554)

**背景**: 在 Web 开发中，“平台”或“原生”功能是指由浏览器引擎直接提供的功能，例如 Web 组件或标准 HTML 表单。React 等框架或 Lit 等库是用 JavaScript 编写的，作为抽象层来管理复杂的 UI 状态。开发者经常选择这些工具，因为它们在不同浏览器之间提供了更一致和可组合的 API，弥补了原始 Web 标准和实际应用开发之间的差距。

**社区讨论**: 评论者普遍认同原生浏览器实现往往缺乏实用性，特别引用了 <datalist> 元素的糟糕可用性以及 Web 组件很少在没有 Lit 等包装库的情况下独立使用的事实。这种情绪表明，对许多开发者而言，在熟悉的框架上构建不仅是“更有趣”，而且是确保复杂应用中可靠性和组合性的必要条件。

**标签**: `#web-development`, `#frontend`, `#browser-apis`, `#frameworks`, `#web-components`

---

<a id="item-4"></a>
## [加州下令停止人形机器人笼式格斗](https://www.tomshardware.com/tech-industry/robotics/robotics-startup-has-real-human-vs-robot-cage-match-california-responds-with-cease-and-desist-order-regulator-threatens-misdemeanor-charges-after-youtuber-fights-three-robotic-humanoids) ⭐️ 6.5/10

加州州运动委员会向一家举办了人类与人形机器人公开格斗表演的机器人初创公司发出了停止令。监管机构威胁称，如果该实体不立即停止此类活动，将对负责人提起轻罪指控并处以罚款。 此事件凸显了随着人形机器人智能化提升，监管层面的法律空白。它迫使监管机构重新界定机器人在体育竞赛中的法律地位和安全标准，以确保人类与机器人互动的安全。 停止令是一份法律文件，要求个人或实体立即停止特定行为，通常作为提起正式诉讼前的最后警告。加州州运动委员会是负责监管加州业余和职业拳击及其他体育赛事的监管机构。

rss · Tom's Hardware · 10月4日 14:36

**背景**: 人形机器人近期已从实验室环境逐步过渡到现实应用，部分初创公司开始将其作为劳动力或陪伴机器人推向市场。传统上，运动委员会基于人类生物竞技来制定赛事规则，机器人作为“运动员”缺乏既有的法律保护或标准。监管机构通过将该事件视为未经许可的体育竞技，将现有的安全规范应用于新兴的 AI 技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixed_martial_arts_competition_for_children">Mixed martial arts competition for children - Wikipedia</a></li>
<li><a href="http://bomasasawavi.pbworks.com/f/54340082470.pdf">Cease and desist letter form free</a></li>

</ul>
</details>

**标签**: `#Humanoid Robotics`, `#Regulation`, `#Tech Industry`, `#AI Safety`

---

<a id="item-5"></a>
## [数据库专家使用 5900 行代码在 SQL 中运行 DOOM](https://www.tomshardware.com/video-games/pc-gaming/database-expert-runs-doom-in-sql-with-just-5-900-lines-of-code-1-300-line-graphical-renderer-spans-89-different-tables-full-featured-sqldoom-is-the-sequel-to-embryonic-doomql) ⭐️ 6.5/10

CedarDB 发布了 SQLDoom，这是 DOOMQL 的完整功能续作，使用 5900 行 SQL 代码实现了 1993 年原版游戏的运行。该项目拥有一个跨越 89 个不同表的图形渲染器，并在 CedarDB 数据库引擎内运行。 这项技术演示展示了现代关系型数据库在处理复杂计算负载时的极端灵活性和性能能力。它为数据库工程师提供了一个引人入胜的展示，并突出了数据存储系统在创意计算环境下的边界。 游戏循环以原版 35 FPS 运行，而渲染器在普通笔记本电脑上可以以高达 60 Hz 的速度生成完整的 320x200 帧缓冲区。一个小型 Python 客户端负责输入/输出和计时，而 CedarDB 表则跟踪游戏几何形状和状态。

rss · Tom's Hardware · 10月4日 14:00

**背景**: CedarDB 是一个面向开发者的数据库，以其高性能和现代 SQL 功能著称。前序项目 DOOMQL 是一个思维实验，它完全用 SQL 实现了一个多人 Doom 类射击游戏，为这个更完整的移植版本奠定了基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/cedardb/sqldoom/blob/main/README.md">sqldoom /README.md at main · cedardb/ sqldoom · GitHub</a></li>
<li><a href="https://arstechnica.com/gaming/2026/10/can-it-run-doom-sql-database-edition/">Someone got Doom in an SQL database - Ars Technica</a></li>
<li><a href="https://github.com/cedardb/DOOMQL">GitHub - cedardb/ DOOMQL : A multiplayer DOOM -like in pure SQL</a></li>

</ul>
</details>

**标签**: `#databases`, `#sql`, `#retro-gaming`, `#performance`, `#technical-demo`

---

<a id="item-6"></a>
## [美军现场组装无人机投掷 3D 打印“Dragoon”炸弹](https://www.tomshardware.com/tech-industry/drones/us-army-unit-deploys-drone-assembled-completely-in-house-uses-3d-printed-dragoon-bombs-with-ball-bearing-shrapnel-device-has-a-range-of-up-to-12-miles-and-can-be-configured-for-anti-personnel-and-anti-light-armor-missions) ⭐️ 6.5/10

美军一个部队成功实施了无承包商支持的实弹动能无人机打击，完全依靠自身组装无人机，并使用装有 C-4 炸药和破片的 3D 打印“Dragoon”炸弹。 这一战术转变使步兵部队能够独立具备低成本动能打击能力，极大地降低了对专业支援单位和外部后勤保障的依赖。 无人机具有 12 英里的射程，可配置用于反人员和反轻型装甲任务，3D 打印外壳内装有 250 克 C-4 炸药和 M6 低电压雷管。

rss · Tom's Hardware · 10月4日 13:40

**背景**: 现场可组装无人机是指由普通步兵人员利用易得部件进行现场组装或建造军用的无人飞行器，这一技术将保障责任从专业支援单位转移到了前线。3D 打印弹药（或称“Dragoon”炸弹）是通过增材制造生产的爆炸性武器，旨在减少将成品炸药运入战场所带来的后勤负担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/drones/us-army-unit-deploys-drone-assembled-completely-in-house-uses-3d-printed-dragoon-bombs-with-ball-bearing-shrapnel-device-has-a-range-of-up-to-12-miles-and-can-be-configured-for-anti-personnel-and-anti-light-armor-missions">US Army unit deploys drone assembled completely... | Tom' s Hardware</a></li>
<li><a href="https://www.stripes.com/branches/army/2026-10-01/2nd-cavalry-soldiers-one-way-attack-drone-live-fire-23022168.html">Army unit claims a first with attack drone built and... | Stars and Stripes</a></li>

</ul>
</details>

**标签**: `#Military Technology`, `#3D Printing`, `#Drones`, `#Hardware`, `#Defense`

---

<a id="item-7"></a>
## [Iranian national extradited to US over alleged $3.4 billion state-backed hacking campaign in rare legal win for law enforcement](https://www.tomshardware.com/tech-industry/cyber-security/iranian-national-extradited-to-us-over-alleged-usd3-4-billion-state-backed-hacking-campaign-in-rare-legal-win-for-law-enforcement-operative-helped-steal-31-terabytes-of-data-from-over-300-universities) ⭐️ 6.5/10

An Iranian-Turkish national was extradited to the US for his role in a state-sponsored hacking campaign that exfiltrated 31 TB of data from over 300 universities and government agencies.

rss · Tom's Hardware · 10月4日 12:55

**标签**: `#cybersecurity`, `#state-sponsored-attacks`, `#data-breach`, `#iran`, `#law-enforcement`

---

<a id="item-8"></a>
## [LeCun 对 AI 灭绝担忧不以为然，引发 AGI 与 LLM 辩论](https://fortune.com/2026/10/01/ai-godfather-yann-lecun-has-zero-concerns-about-human-extinction-says-anthropic-ceo-dario-amodei-is-deuded/) ⭐️ 6.0/10

Yann LeCun 公开表示，他对 AI 毁灭人类或发生“失控”事件毫无担忧。这一立场在 Hacker News 上引发了关于大型语言模型局限性及存在性风险叙事有效性的激烈辩论。 作为“AI 教父”之一，LeCun 对存在性风险的忽视与其他行业领袖的警示形成鲜明对比，直接影响公众对 AI 安全的认知。这场辩论凸显了区分当前 LLM 能力与真正的 AGI 的迫切性，以避免盲目自满或不必要的恐慌。 LeCun 认为，仅靠扩大 LLM 规模无法实现 AGI，他指出其缺乏基本的常识物理和世界建模能力。批评者则反驳称，“失控”行为往往只是 LLM 在执行缺乏适当安全约束的明确人类指令，因此人类问责制才是核心问题。

hackernews · Anon84 · 10月3日 17:44 · [社区讨论](https://news.ycombinator.com/item?id=49946228)

**背景**: Yann LeCun 是一位先驱计算机科学家，因其对卷积神经网络的工作而闻名，该工作彻底改变了计算机视觉领域。近年来，AI 社区对当前大型语言模型（LLM）是否通往通用人工智能（AGI）产生了分歧，而“失控 AI”事件通常源于过于宽泛的系统提示或缺乏监督。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lexfridman.com/yann-lecun-3-transcript/">Transcript for Yann Lecun : Meta AI, Open Source, Limits of LLMs, AGI ...</a></li>
<li><a href="https://jamesbachini.com/llm-vs-agi/">LLM vs AGI | Limiting Reality of Language Models in AGI</a></li>
<li><a href="https://www.greaterwrong.com/posts/TpExcpmeHhhfNtXoh/lightning-post-things-people-in-ai-safety-should-stop">Lightning Post: Things people in AI Safety should stop talking about</a></li>

</ul>
</details>

**社区讨论**: 社区评论在支持 LeCun 认为当前 LLM 远未达到 AGI 的观点，以及认为由于人类的疏忽“失控 AI”已是实际威胁的观点之间产生了分歧。一些用户强调，真正的“失控”行为要求开发人员对部署具有危险目标的智能体承担责任，而不是对模型拟人化。

**标签**: `#AI Safety`, `#AGI`, `#Yann LeCun`, `#AI Ethics`, `#LLM Limitations`

---

<a id="item-9"></a>
## [Jagex 宣布新 MMO《RuneScape 4》，基于 Unreal Engine 开发](https://www.techpowerup.com/353372/jagex-announces-runescape-4-a-new-mmo-built-in-unreal-engine) ⭐️ 5.5/10

Jagex 在 RuneFest 2026 活动期间正式宣布了一款名为《RuneScape 4》（RS4）的新 MMORPG。该游戏目前处于早期开发阶段，将使用 Unreal Engine 构建，并在预告片中展示了绿色山谷、浮岛和巨龙骑士的画面。 这一宣布对游戏行业意义重大，标志着 Jagex 时隔多年回归 MMO 数字续作，显示出其对该 IP 的持续投入。同时，采用 Unreal Engine 开发大型 MMO 项目也反映了现代游戏开发流水线中引擎采用的新趋势。 《RuneScape 4》起初是为生存游戏《RuneScape: Dragonwilds》计划的扩展包，但后来演变成了独立项目。游戏故事发生在 Ashenfall 地区，虽然现有作品仍会继续运营，但目前的盈利机制和进度继承方式尚未公布。

rss · TechPowerUp News · 10月4日 00:51

**背景**: RuneScape 是一个历史悠久的大型多人在线角色扮演游戏（MMORPG）系列，最近推出了设定在相同世界观下的独立生存游戏《RuneScape: Dragonwilds》。Unreal Engine 是一款应用广泛的游戏引擎，能够提供先进的图形和物理效果，如今越来越多的开发商将其用于大规模 3D 游戏。自 2013 年推出《RuneScape 3》以来，Jagex 一直未发布过新的数字编号 MMO 作品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RuneScape:_Dragonwilds">RuneScape: Dragonwilds</a></li>

</ul>
</details>

**标签**: `#Gaming`, `#MMO`, `#Unreal Engine`, `#Jagex`, `#Software Development`

---