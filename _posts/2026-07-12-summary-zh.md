---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 48 条内容中筛选出 11 条重要资讯。

---

1. [Nvidia RTX 5070 Ti 因导热硅脂涂抹不当导致 107°C 过热降频，隐藏的热点传感器被曝光](#item-1) ⭐️ 7.5/10
2. [中国具身数据赛道爆发：97 家玩家、一年融资 44.7 亿](#item-2) ⭐️ 7.3/10
3. [AI 热潮太费电，燃气轮机价格 3 年涨了 300%](#item-3) ⭐️ 7.3/10
4. [Mindwalk：在 3D 代码库地图上回放 AI 编程代理会话](#item-4) ⭐️ 7.0/10
5. [RISCBoy 是一款从零开始设计的开源便携式游戏机](#item-5) ⭐️ 7.0/10
6. [美国联邦通信委员会批准轨道空间镜项目，首批测试卫星将于今年发射——大型航天器可将阳光反射至地球表面，用于建筑工地照明、搜救照明等用途](#item-6) ⭐️ 6.5/10
7. [苹果起诉 OpenAI，指控前员工窃取商业机密](#item-7) ⭐️ 6.3/10
8. [陶哲轩谈使用现代编程代理构建应用](#item-8) ⭐️ 6.0/10
9. [Mesh LLM：基于 iroh 的分布式 AI 计算](#item-9) ⭐️ 6.0/10
10. [英伟达、CoreWeave 与 Nebius：GPU 热潮循环融资内幕](#item-10) ⭐️ 6.0/10
11. [AIC 推出 32 盘位 E3 SSD JBOF，瞄准 AI 键值缓存](#item-11) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Nvidia RTX 5070 Ti 因导热硅脂涂抹不当导致 107°C 过热降频，隐藏的热点传感器被曝光](https://www.tomshardware.com/pc-components/gpus/hotspot-temperature-sensor-on-nvidias-blackwell-gaming-gpus-is-still-accessible-if-you-have-access-to-nvidias-internal-mods-tool-nvidia-rtx-5070-ti-caught-throttling-at-107-c-over-poor-tim-application) ⭐️ 7.5/10

通过使用 Nvidia 内部诊断工具 MODS（模块化诊断软件）进行测试发现，RTX 5070 Ti 显卡因导热界面材料（TIM）涂抹不当，热点温度高达 107°C 并出现降频。Nvidia 在 RTX 50 系列上有意对消费者隐藏了热点温度传感器，但该内部诊断工具仍可读取，暴露了严重的散热问题。 这一消息引发了人们对 Nvidia Blackwell 游戏显卡质量管控的担忧，并暗示消费者可能一直被蒙在鼓里，不知道存在过热降频问题。RTX 5070 Ti 的购买者可能正在经历性能下降却毫不知情，这可能需要发起保修或 RMA 退换货申请。 Nvidia 的 MODS 是一款不对外公开的内部诊断工具套件，且无法在 Windows 上运行，因为操作系统会拦截硬件监控 API 调用。热点（结温）温度测量的是 GPU 芯片上最热的单个点，而非平均核心温度，通常热点与边缘温度之间的差值才能真正反映散热问题。

rss · Tom's Hardware · 7月11日 16:18

**背景**: MODS（模块化诊断软件）是 Nvidia 内部用于在出货前或 RMA 过程中测试显卡的工具，可检测从显存芯片到 GPU 核心的各项指标。GPU 热点温度与核心温度不同：核心温度代表整个芯片硅片的平均热量，而热点温度是数十个内部传感器中单个最热点的读数。导热界面材料（TIM），即常见的导热硅脂，填充在处理器与散热器之间以传导热量，涂抹不当会大幅降低散热效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/hotspot-temperature-sensor-on-nvidias-blackwell-gaming-gpus-is-still-accessible-if-you-have-access-to-nvidias-internal-mods-tool-nvidia-rtx-5070-ti-caught-throttling-at-107-c-over-poor-tim-application">Hotspot temperature sensor on Nvidia 's Blackwell gaming GPUs is still...</a></li>
<li><a href="https://rkblog.dev/posts/pc-hardware/nvidia-modular-diagnostic-software-mods/">Nvidia Modular diagnostic software - MODS</a></li>
<li><a href="https://www.darkflash.com/article/gpu-junction+temperature-explained">Understanding GPU Junction Temp vs . Core Temp: Is Your Hotspot ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#RTX 5070 Ti`, `#GPU thermal issues`, `#Blackwell architecture`, `#hardware review`

---

<a id="item-2"></a>
## [中国具身数据赛道爆发：97 家玩家、一年融资 44.7 亿](https://36kr.com/p/3892027841362694?f=rss) ⭐️ 7.3/10

36 氪/量子位调研统计了国内 97 家具身数据行业玩家，其中 70 家做数据采集、27 家做数据基础设施。过去一年（2025 年 7 月至 2026 年 7 月），15 家「不做本体、不做模型、只做数据」的独立具身数据服务商共融资约 44.7 亿元。数据采集方式花样百出：湖南郴州一家中国移动营业厅挂牌「具身数据采集 5S 店」，普通顾客穿戴夹爪、手套和头戴相机边做家务边采集数据。 具身智能——让机器人在物理世界中交互——长期受困于高质量、多样化训练数据的匮乏，数据采集本身正催生一个百亿级市场。44.7 亿元在一年内流向纯数据厂商，标志着数据正在成为机器人技术栈中的独立层级，正如标注数据集曾助推大语言模型革命一样。 目前主流采集路线分为四类：真机遥操（22 家单独押注，数量最多）、无本体采集（15 家）、仿真合成（仅剩 2 家单独押注）、互联网视频蒸馏（1 家，号称成本可压至行业平均的千分之五）。值得注意的是，43%的采集公司同时走多条路线，反映行业共识——单一数据源无法满足训练需求。仿真赛道萎缩，主因是 sim2real 差距仍未解决，难以高保真还原真实世界中的摩擦、形变与触觉反馈。

rss · 36氪 · 7月12日 02:16

**背景**: 具身智能（Embodied Intelligence）是指 AI 系统通过机器人本体与物理世界交互来完成学习，将感知、行动与认知深度融合。与基于文本的大语言模型不同，具身模型需要感知运动数据——关节力矩、夹爪力觉、第一视角视频、触觉信号——这类数据的采集成本和时间远高于抓取网页文本。特斯拉 Optimus 等人形机器人项目已从依赖遥操转向大规模视频数据采集，以突破动作捕捉服的限制；开源数据集如 Bridge 和 RT-1 则成为训练和评估通用机器人策略的标准基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7486670839923359796">什 么 是 具 身 智 能 ？ 具 身 智 能 （ Embodied Intelligence...</a></li>
<li><a href="https://news.pedaily.cn/202606/565591.shtml">具身数据采集产业链调查：被机器人采集的人_投资界</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1905656875946612379">万字长文详解：五家主流具身智能开源数据集核心内容 - 知乎</a></li>

</ul>
</details>

**标签**: `#embodied-AI`, `#robotics`, `#data-collection`, `#industry-analysis`, `#China-tech`

---

<a id="item-3"></a>
## [AI 热潮太费电，燃气轮机价格 3 年涨了 300%](https://36kr.com/newsflashes/3892556678543880?f=rss) ⭐️ 7.3/10

人工智能热潮带来的巨大电力需求推动燃气轮机价格在三年内上涨约 300%。微软以超过 17.5 亿美元从 GE Vernova 采购的大额订单凸显了数据中心扩张面临的严峻能源基础设施瓶颈。

rss · 36氪 · 7月12日 11:37

**标签**: `#AI infrastructure`, `#energy`, `#data centers`, `#GE Vernova`, `#AI economics`

---

<a id="item-4"></a>
## [Mindwalk：在 3D 代码库地图上回放 AI 编程代理会话](https://github.com/cosmtrek/mindwalk) ⭐️ 7.0/10

开发者 cosmtrek 开源了 Mindwalk，这是一款将 AI 编程代理（如 Claude Code）的会话记录并渲染为可导航的代码库 3D 地图的工具，让用户可以空间化地探索代理读取、编辑或写入过的文件。 随着 Claude Code 等 AI 编程代理逐渐成为主流，开发者需要超越平面终端日志的方式来审计、调试和理解代理行为。空间化可视化范式有望从根本上改变人类与自主编程代理的交互和信任方式。 该工具捕获代理会话中的读取、编辑和写入操作，并将其投射到代码库的 3D 地形/树状视图上，同时配有时间轴。据反馈，如果原始项目已不在用户本地驱动器上，树状/地形视图可能无法正常渲染。

hackernews · cosmtrek · 7月12日 05:51 · [社区讨论](https://news.ycombinator.com/item?id=48878682)

**背景**: Claude Code 是 Anthropic 于 2025 年 2 月发布的代理式命令行工具，允许开发者通过自然语言提示委派编程任务，并于 2025 年 5 月与 Claude 4 模型一同正式上线。由于代理的工作以非线性方式横跨多个文件，在终端滚动输出中跟踪其活动十分困难。AI 代理可观测性工具和会话回放工具是一个新兴类别，旨在让这些工作流更加透明和可审计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://github.com/es617/claude-replay">GitHub - es617/claude-replay: Convert AI coding agent sessions (Claude Code, Cursor, Codex, Gemini, OpenCode) into self-contained, embeddable HTML replays · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区反响热烈且具有前瞻性。评论者提出了引人入胜的未来用例，例如比较不同模型如何遍历同一代码库，或衡量同一模型多次运行之间的差异；一位开发者提议将自己项目（glyph3d.dev）中的字形级文件渲染集成进来；还有人将该项目比作 Xerox PARC 时代对新 UI 隐喻的探索。同时也有用户报告了一个实际问题：当源项目已不在本地时，地形视图会显示为空。

**标签**: `#ai-agents`, `#developer-tools`, `#visualization`, `#claude-code`, `#show-hn`

---

<a id="item-5"></a>
## [RISCBoy 是一款从零开始设计的开源便携式游戏机](https://github.com/Wren6991/RISCBoy) ⭐️ 7.0/10

这是一款围绕自研 RISC-V SoC 从零打造的开源便携式游戏机,由树莓派 ASIC 工程师 Luke Wren 设计,是 Gameboy Advance 的现代重塑之作。

hackernews · mariuz · 7月11日 21:58 · [社区讨论](https://news.ycombinator.com/item?id=48876245)

**标签**: `#RISC-V`, `#open-source-hardware`, `#ASIC-design`, `#embedded-systems`, `#retro-gaming`

---

<a id="item-6"></a>
## [美国联邦通信委员会批准轨道空间镜项目，首批测试卫星将于今年发射——大型航天器可将阳光反射至地球表面，用于建筑工地照明、搜救照明等用途](https://www.tomshardware.com/tech-industry/fcc-approves-orbital-space-mirrors-first-test-satellites-will-launch-this-year-large-spacecraft-reflects-sunlight-to-earths-surface-for-construction-sites-search-and-rescue-lighting-and-more) ⭐️ 6.5/10

美国联邦通信委员会已批准一家初创公司的实验性轨道镜面卫星，该卫星可将阳光反射至地球。尽管天文学家对此表示担忧，首批测试卫星仍计划于今年发射。

rss · Tom's Hardware · 7月12日 12:20

**标签**: `#space-technology`, `#FCC`, `#satellites`, `#orbital-mirrors`, `#commercial-space`

---

<a id="item-7"></a>
## [苹果起诉 OpenAI，指控前员工窃取商业机密](https://www.solidot.org/story?sid=84806) ⭐️ 6.3/10

苹果已对 OpenAI 提起诉讼，指控包括 OpenAI 首席硬件官 Tang Tan 和工程师 Chang Liu 在内的前苹果员工窃取了与未发布硬件产品相关的商业机密。诉讼指控称，Tan 指导新入职 OpenAI 的前苹果员工规避苹果针对离职员工的安全流程，而 Liu 下载了数十份有关工程演示、技术规格和私有项目数据的机密文件，通过同事的笔记本电脑利用认证漏洞访问内部网络，并在漏洞被发现后在同事的笔记本上留言'LOL'。 这起诉讼凸显了 AI 时代日益激烈的人才争夺战和商业机密之争，各大科技公司在员工向 AI 公司流动的同时竞相保护其专有硬件设计。该案可能为竞业限制和商业机密保护如何适用于快速发展的 AI 硬件领域树立先例。 诉讼指控 Liu 未归还苹果配发的笔记本电脑。在另一则新闻中，布朗大学经济学教授 Roberto Serrano 在期中考试成绩异常后将期末考试改为线下进行，结果期末平均分骤降至 48.6%——创下该班级历史最低纪录，18 名学生选择退课。JAXA 也在 7 月 11 日宣布其可回收火箭原型 RV-X 完成了 40 秒的测试飞行，达到 11 米高度，完成了升空、悬停、水平移动和垂直着陆四个动作。

rss · Solidot · 7月11日 16:40

**背景**: OpenAI 一直在积极从苹果的设计团队中招募硬件人才，以推进其自身的硬件业务，这一背景有助于理解此案中的具体指控。布朗大学的故事反映了教师群体对生成式 AI 工具在远程考试中助长学术不端行为的日益担忧。JAXA 的 RV-X 正作为不可回收的 H-3 火箭的继任者进行开发，旨在降低发射成本，法国和德国也参与了该研发合作，不过日本在可回收火箭领域被普遍认为落后于中国。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aa.com.tr/en/asia-pacific/japan-tests-prototype-reusable-rocket/3994840">Anadolu Ajansı: Japan tests prototype reusable rocket</a></li>
<li><a href="https://en.wikipedia.org/wiki/Japanese_space_program">Japanese space program - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Apple`, `#OpenAI`, `#AI-cheating`, `#education`, `#JAXA`, `#reusable-rockets`, `#trade-secrets`

---

<a id="item-8"></a>
## [陶哲轩谈使用现代编程代理构建应用](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/) ⭐️ 6.0/10

菲尔兹奖得主陶哲轩发表博客文章，分享了他使用现代 LLM 编程代理构建应用程序（尤其是为其数学论文制作交互式可视化工具）的经验。他得出的结论是，这些工具非常适合非关键性的补充用途，因为此类场景的下行风险是可接受的。 鉴于陶哲轩在数学界的重要地位，他的观点具有举足轻重的分量，他对编程代理在特定场景下的务实认可，有助于为领域专家采用 AI 辅助开发正名。他以区分关键任务与辅助用途为核心的平衡视角，为 AI 编程工具在专业工作流中定位的广泛讨论贡献了理性的声音。 陶哲轩明确围绕风险容忍度来构建他的决策框架，他写道：对论文核心发现并非关键的补充材料，使用 LLM 生成代码的下行风险是可接受的。文章的重点在于交互式教学和可视化辅助工具，而非用于核心数学推理或证明验证的工具。

hackernews · subset · 7月12日 11:09 · [社区讨论](https://news.ycombinator.com/item?id=48880170)

**背景**: AI 编程代理超越了简单的代码补全工具（如早期的 GitHub Copilot），能够自主规划、执行并迭代多步骤编码任务。与自动补全式助手不同，代理可以根据自然语言描述构建完整的功能或小型应用程序，不过其准确性会因任务复杂度和编程语言的不同而有显著差异。陶哲轩是加州大学洛杉矶分校教授，被广泛认为是最伟大的在世数学家之一，于 2006 年获得菲尔兹奖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codegen.com/guides/what-are-ai-coding-agents/">What Are AI Coding Agents ? A Beginner's Guide</a></li>
<li><a href="https://calmops.com/ai/ai-coding-agents-devin-2026-complete-guide/">AI Coding Agents and Devin 2026: The Complete Guide - Calmops</a></li>

</ul>
</details>

**社区讨论**: 社区的回应总体上积极赞赏陶哲轩的平衡观点。一位计算机科学教授分享了类似的经验，使用 Claude 构建教学可视化工具（包括一个简化的 8 位计算机模拟器），而其他人则幽默地指出，即使是菲尔兹奖得主也会遇到与所有人相同的调试难题。一些评论者提出质疑，认为这些例子始终是业余爱好或辅助性项目，而非关键任务工作，由此引发了关于 AI 辅助编程局限性的讨论。

**标签**: `#LLM-coding`, `#AI-assisted-development`, `#Terry Tao`, `#mathematics`, `#coding-agents`

---

<a id="item-9"></a>
## [Mesh LLM：基于 iroh 的分布式 AI 计算](https://www.iroh.computer/blog/mesh-llm) ⭐️ 6.0/10

Mesh LLM 基于 iroh，可聚合分布式消费设备（笔记本、台式机、服务器）的显存来协作运行大型语言模型，但性能受网络带宽限制。

hackernews · tionis · 7月11日 22:38 · [社区讨论](https://news.ycombinator.com/item?id=48876505)

**标签**: `#distributed-systems`, `#LLM-inference`, `#P2P`, `#iroh`, `#open-source`

---

<a id="item-10"></a>
## [英伟达、CoreWeave 与 Nebius：GPU 热潮循环融资内幕](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) ⭐️ 6.0/10

分析英伟达与 CoreWeave、Nebius 等 AI 云服务商之间所谓的循环融资现象，社区讨论大多质疑该前提，并指向更实质性的 GPU 经济问题。

hackernews · adletbalzhanov · 7月11日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48873836)

**标签**: `#ai-infrastructure`, `#nvidia`, `#gpu-economics`, `#coreweave`, `#investment-analysis`

---

<a id="item-11"></a>
## [AIC 推出 32 盘位 E3 SSD JBOF，瞄准 AI 键值缓存](https://www.servethehome.com/aic-gets-flashy-with-32-ssd-bay-jbof-server-for-key-value-caching/) ⭐️ 5.5/10

AIC 发布了 F2032-01-G6，这是一款 2U JBOF 存储系统，可容纳多达 32 块 EDSFF E3 SSD。该机箱专为搭配 NVIDIA BlueField-4 DPU 使用而设计，定位为面向 Rubin/Vera 时代 AI 基础设施的键值缓存设备。 键值缓存对于通过存储注意力计算来加速大语言模型推理、减少重复计算至关重要，由 DPU 管理的专用存储层可能有效缓解 GPU 显存压力。这款产品表明，存储行业正朝着与 DPU 紧密耦合的解耦化、无计算闪存机箱方向演进，以服务新兴 AI 工作负载。 F2032-01-G6 采用 EDSFF E3.S 形态规格，相比传统的 2.5 英寸 U.2 硬盘具有更高的密度和更好的散热性能。作为一款真正的 JBOF，它本身不配备存储控制器——卸载、网络和缓存管理完全由外部连接的 BlueField-4 DPU 处理。

rss · ServeTheHome · 7月11日 17:00

**背景**: JBOF（"Just a Bunch of Flash"，即"一堆闪存"）是一种存储架构，将大量 NVMe SSD 聚合到单个机箱中，通过高速网络对外提供服务，不包含传统存储控制器，计算能力由外部提供。EDSFF E3.S 是一种较新的 SSD 形态规格，专为高密度、散热高效的服务器和存储部署而设计，正在 AI 系统中逐步取代 2.5 英寸和 M.2 硬盘。NVIDIA BlueField DPU 最初由 Mellanox 开发，NVIDIA 于 2019 年将其收购，可从主机 CPU 卸载网络、存储和安全功能。键值（KV）缓存在 Transformer 推理过程中存储中间注意力计算结果以避免重复计算，NVIDIA 已将 BlueField-4 定位为在 AI 数据中心中启用专用 KV 缓存新内存层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ntchosting.com/encyclopedia/hosting/jbof/">JBOF Explained: High-Speed NVMe Flash Storage</a></li>
<li><a href="https://www.aewin.com/tech-blog-detail/230/">Introduction to NVMe SSD : Enhancing Server Performance and...</a></li>
<li><a href="https://learn-more.supermicro.com/data-center-stories/storage-technology-ai-inference-with-nvidia-bluefield-4">Supermicro New Storage Technology with NVIDIA BlueField ®- 4</a></li>

</ul>
</details>

**标签**: `#storage`, `#JBOF`, `#SSD`, `#DPU`, `#AI-infrastructure`

---