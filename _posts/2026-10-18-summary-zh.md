---
layout: default
title: "Horizon Summary: 2026-10-18 (ZH)"
date: 2026-10-18
lang: zh
---

> 从 39 条内容中筛选出 14 条重要资讯。

---

1. [RepRapMicron 实现 1:1000 比例的自复制微制造](#item-1) ⭐️ 9.0/10
2. [NVIDIA 发布 RTX Spark N1X：GB10 芯片组登陆 Windows 平台](#item-2) ⭐️ 8.5/10
3. [独立开发者将完整 NVIDIA DLSS 套件移植至 AMD RDNA 2-4 GPU](#item-3) ⭐️ 7.5/10
4. [F-22 飞行员在模拟战斗中成功指挥 Anduril YFQ-44A 无人机](#item-4) ⭐️ 7.5/10
5. [Official DLSS 5 running on unsupported games delivers up to 90% better performance than the leaked version](#item-5) ⭐️ 7.5/10
6. [Parser Combinators](#item-6) ⭐️ 7.0/10
7. [无掩模 EUV 光刻作为电子束光刻的替代方案](#item-7) ⭐️ 7.0/10
8. [DeepSeek 推出低成本搜索与获取 API](#item-8) ⭐️ 6.0/10
9. [开源自制微操作器实现亚微米级精度](#item-9) ⭐️ 6.0/10
10. [Sphinx 钩子考核开发者对 AI 生成代码的掌握程度](#item-10) ⭐️ 6.0/10
11. [PS6 RAM and Storage Alone Reportedly Cost Sony Over $680, Claims Leaker](#item-11) ⭐️ 5.5/10
12. [科乐美总裁早川英树表示 AI 不会从根本上改变游戏市场](#item-12) ⭐️ 5.5/10
13. [网页版芯片制造工程游戏在台湾爆红](#item-13) ⭐️ 5.5/10
14. [MapQuest 通过新监控层揭示 Flock ALPR 摄像头位置](#item-14) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [RepRapMicron 实现 1:1000 比例的自复制微制造](https://github.com/VikOlliver/RepRapMicron/wiki) ⭐️ 9.0/10

开源项目 RepRapMicron 展示了一台能够制造 1:1000 比例自我复制品 的机器，标志着自复制纳米技术的一项重大里程碑。 这一进展表明，有可能掀起新一轮本地化微制造浪潮，在该浪潮中，设备可以以极高精度复制自身部件。 该项目涉及通过 3D 打印制造机器自身的微型版本，若要完全复制，则需要相当于 1,000,000 分之一比例的公差。

hackernews · RobotToaster · 10月18日 13:48 · [社区讨论](https://news.ycombinator.com/item?id=50141076)

**背景**: RepRap 是一个专注于使用开源硬件和 3D 打印技术构建自复制机器的运动。
在自复制系统中，机器可以制造自身的部件，从而使其能够生产自己的副本。
该概念依赖于高精度制造和目前正在 RepRapMicron 项目中推进的特定材料科学原理。

**社区讨论**: 社区讨论对达到的高度公差及微制造的未来潜力表示高度兴奋，但部分评论对制造 1/1,000,000 比例打印机的实用价值持怀疑态度。

**标签**: `#nanotechnology`, `#manufacturing`, `#self-replication`, `#hardware`, `#3D-printing`

---

<a id="item-2"></a>
## [NVIDIA 发布 RTX Spark N1X：GB10 芯片组登陆 Windows 平台](https://www.servethehome.com/nvidia-rtx-spark-n1x-launch-overview-nvidia-arms-windows/) ⭐️ 8.5/10

NVIDIA 推出了高端的 RTX Spark N1X 平台，首次将 GB10 系统级芯片（SoC）引入 Windows 操作系统。此次发布旨在利用这款强大的、专注于 AI 的处理器重塑笔记本电脑市场。 此举意义重大，因为它标志着 NVIDIA 进军 Windows ARM 笔记本电脑市场，将高性能 AI 能力与主要的操作系统生态系统相结合。它通过挑战传统的 x86 架构并加速边缘设备上的 AI 推理，对更广泛的行业产生了影响。 核心技术是 GB10 芯片组，专门针对 AI 密集型工作负载进行了设计。该硬件配置在 Windows 平台上的可用性是一项新的进展。

rss · ServeTheHome · 10月17日 17:00

**背景**: 系统级芯片（SoC）是一种将计算机系统（如 CPU 和图形处理单元）的各种组件集成到单一芯片上的技术。GB10 是 NVIDIA 开发的一款高端 SoC。Windows ARM 是微软 Windows 操作系统的版本，经过优化以适配 ARM 架构，传统上用于移动设备，但如今正越来越多地应用于高性能笔记本电脑。从历史上看，AI 推理一直是笔记本电脑硬件的主要瓶颈，而集成强大的 AI SoC 使得无需完全依赖云即可在本地设备上进行数据处理。

**标签**: `#NVIDIA`, `#Hardware`, `#AI`, `#Windows ARM`, `#SoC`

---

<a id="item-3"></a>
## [独立开发者将完整 NVIDIA DLSS 套件移植至 AMD RDNA 2-4 GPU](https://www.tomshardware.com/pc-components/gpus/amd-cards-now-run-all-dlss-features-thanks-to-one-developers-project-plans-to-match-native-nvidia-gpu-performance) ⭐️ 7.5/10

一位独立开发者发布了一个模组，使三代 AMD RDNA 游戏 GPU 能够支持 NVIDIA DLSS 的完整功能套件。这包括 DLSS 超级分辨率、光线重建、帧生成和神经渲染。 该模组通过让数百万 AMD 用户访问 NVIDIA 专有的 AI 超分辨率技术，缩小了 AMD 与 NVIDIA 之间的功能差距。这有可能使这些用户在视觉性能和帧速率上媲美原生 NVIDIA GPU。 该模组目前在 RDNA 3 和 RDNA 4 GPU 上支持所有功能，而 RDNA 2 正处于测试阶段，目前仅支持神经渲染。该工具允许 AMD GPU 运行 NVIDIA 的神经渲染模型，尽管在某些情况下性能可能仍较粗糙。

rss · Tom's Hardware · 10月18日 16:03

**背景**: DLSS 是 NVIDIA 专为游戏打造的 AI 技术套件，利用超分辨率、光线重建、帧生成和神经渲染来提升性能和视觉保真度。AMD 的竞争性 GPU 架构基于 RDNA 系列，范围从 RDNA 2 到最新的 RDNA 4。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/danielblnc/DLSS-NR-on-AMD">GitHub - danielblnc/ DLSS -NR- on - AMD : Run DLSS 5 Neural Rendering...</a></li>
<li><a href="https://www.techpowerup.com/352360/modders-get-dlss-5-working-on-amd-graphics-cards-though-performance-is-rough">Modders Get DLSS 5 Working on AMD Graphics... | TechPowerUp</a></li>

</ul>
</details>

**标签**: `#GPU`, `#AMD`, `#NVIDIA`, `#DLSS`, `#Gaming`

---

<a id="item-4"></a>
## [F-22 飞行员在模拟战斗中成功指挥 Anduril YFQ-44A 无人机](https://www.tomshardware.com/tech-industry/drones/f-22-raptor-pilot-successfully-demonstrates-command-of-wingman-fighter-drone-in-simulated-combat-anduril-yfq-44a-fury-test-advances-usafs-program-to-integrate-uncrewed-aircraft-into-fighter-squadrons) ⭐️ 7.5/10

美国空军证实 F-22 猛禽战斗机飞行员在模拟战斗中成功指挥了 Anduril 的 YFQ-44A Fury 无人机，标志着无人机整合进战斗机中队的关键里程碑。 这证明了有人-无人协同的可行性，验证了美国空军向集成可负担、可大规模生产的自主无人机与有人战机协同作战的战略转变，以增强空中优势。 Anduril YFQ-44A 仅用 556 天便实现首飞，利用 Lattice 软件实现自主操作、近战斗机速度性能和模块化任务载荷。

rss · Tom's Hardware · 10月18日 15:02

**背景**: YFQ-44A Fury 是 Anduril 公司开发的自主飞行器，最初由 Blue Force Technologies 作为攻击机平台设计。它是美国空军协同作战飞机计划的一部分，旨在将无人无人机与有人战机配对，以提高出动架次率并降低飞行员风险。'有人-无人协同'概念指的是一名有人机飞行员在战斗场景中指挥多架自主无人机的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anduril.com/news/anduril-yfq-44a-begins-flight-testing-for-the-collaborative-combat-aircraft-program">Anduril’s YFQ-44A Begins Flight Testing for the Collaborative ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anduril_FQ-44_Fury">Anduril FQ-44 Fury - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Military Tech`, `#Drones`, `#USAF`, `#Autonomous Systems`, `#Aerospace`

---

<a id="item-5"></a>
## [Official DLSS 5 running on unsupported games delivers up to 90% better performance than the leaked version](https://www.tomshardware.com/pc-components/gpus/modders-used-the-official-dlss-5-release-on-unsupported-games-and-are-seeing-up-to-90-percent-better-performance-than-the-leaked-dlss-5-nvidia-says-new-nr-model-uses-20-percent-less-vram-and-processes-neural-workloads-up-to-2x-faster) ⭐️ 7.5/10

Modders report that the official DLSS 5 Neural Renderer model, extracted from NBA 2K27, delivers up to 90% better performance than previous versions while reducing VRAM usage by 20% and processing neural workloads twice as fast.

rss · Tom's Hardware · 10月18日 12:45

**标签**: `#NVIDIA`, `#DLSS`, `#GPU Performance`, `#Graphics`, `#Benchmarks`

---

<a id="item-6"></a>
## [Parser Combinators](https://t3.at/blog/2026-10-17-parser-combinators/) ⭐️ 7.0/10

A well-received and visually intuitive explanation of parser combinators, accompanied by community discussion on practical implementation tools and alternative parsing strategies.

hackernews · schindlabua · 10月18日 08:19 · [社区讨论](https://news.ycombinator.com/item?id=50139067)

**标签**: `#compiler-theory`, `#parsing`, `#formal-languages`, `#software-architecture`

---

<a id="item-7"></a>
## [无掩模 EUV 光刻作为电子束光刻的替代方案](https://semiwiki.com/lithography/373583-maskless-euv-lithography-an-alternative-to-e-beam/) ⭐️ 7.0/10

SemiWiki 近期的一篇文章介绍了无掩模极紫外（EUV）光刻技术，作为半导体制造中电子束（E-beam）光刻的一种可行替代方案。这一新方法旨在利用 EUV 技术克服当前电子束系统的固有局限性。 开发无掩模 EUV 光刻意义重大，因为它可能会改善电子束光刻在吞吐量或分辨率之间的权衡，而后者的串行写入机制往往是其主要限制。这对目前受电子束瓶颈制约的先进封装和大批量制造具有重大影响。 传统 EUV 光刻使用 13.5 纳米的光和光掩模，而无掩模 EUV 则不使用掩模来投影图案，这是一种被公认为极具挑战性的技术。文章仅提供了一个引言，提供的文本中没有详细说明焦点和像差控制等具体技术挑战。

rss · SemiWiki · 10月18日 15:00

**背景**: 光刻是将电路图案转移到硅片上的过程，是半导体制造的基石。电子束光刻以极高的分辨率著称，但由于其串行写入图案的特性，速度较慢。EUV 光刻采用速度极快的并行投影方法，传统上需要物理掩模，使得无掩模 EUV 成为高产量、高分辨率应用中一种极具吸引力的混合概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">EUV lithography - Wikipedia</a></li>
<li><a href="https://vixra.org/pdf/2007.0167v2.pdf">Microsoft PowerPoint - EUVL_2020_P22_Johnson_v2_vixra.pptx</a></li>
<li><a href="https://e-ame.caa.cz/en/e-beam-lithography">e - Beam Lithography | Optaglio</a></li>

</ul>
</details>

**标签**: `#Semiconductors`, `#Lithography`, `#EUV`, `#Manufacturing`, `#Hardware`

---

<a id="item-8"></a>
## [DeepSeek 推出低成本搜索与获取 API](https://api-docs.deepseek.com/guides/search/) ⭐️ 6.0/10

DeepSeek 推出了新的网页搜索和内容获取 API，价格为每 1,000 次成功请求 0.75 美元。该服务为支持 LLM 应用提供了获取网络数据的专用方法，且具有极具竞争力的成本。 具有攻击性的定价大幅降低了开发者将实时网络数据集成到 LLM 应用程序的门槛，对 Brave 和 Kagi 等现有提供商构成挑战。这突显了围绕大型语言模型开发者工具领域日益激烈的竞争。 在检索特定页面时，开发者必须考虑该服务如何处理反机器人保护（例如 Cloudflare 勾选框或 Anubis）。其价格明显低于每 1,000 次请求 5.00 美元的 Brave Search API 和每 1,000 次请求 12.00 美元的 Kagi API。

hackernews · fagnerbrack · 10月18日 06:50 · [社区讨论](https://news.ycombinator.com/item?id=50138531)

**背景**: LLM 依赖网页搜索和获取来访问实时数据，这产生了对专用 API 的需求。现有解决方案包括 Brave 和 Kagi 等商业提供商，以及像 SearXNG 这样的自托管替代方案，后者可以在不使用 API 密钥的情况下抓取结果。

**社区讨论**: 社区讨论集中在成本效益上，一些用户主张使用 SearXNG 等免费自托管工具而非付费 API。其他用户提供了与竞争对手的直接价格比较，并提出了关于该 API 绕过反机器人保护机制能力的问题。

**标签**: `#API`, `#Search`, `#Cost-Optimization`, `#DeepSeek`, `#LLM-Tools`

---

<a id="item-9"></a>
## [开源自制微操作器实现亚微米级精度](https://github.com/0x23/MicroManipulatorStepper) ⭐️ 6.0/10

一位创作者发布了一款开源 DIY 三轴运动控制平台，能够在 23x23x23mm³ 的工作体积内实现最小 50 纳米的步进精度。这款低成本设备为昂贵的工业级微操作器提供了实用的替代方案。 该项目大幅降低了高精度任务（如探针台应用和显微拾放）的入门门槛，这些任务通常需要昂贵的专有设备。它证明了使用开源方法和易获取的组件也可以实现亚微米级精度。 该系统支持任意加速度限制的运动路径，并依赖闭环控制来实现相对精度。它与 RepRap 社区密切相关，类似的项目如 RepRapMicron 也在探索开源微操纵。

hackernews · _Microft · 10月18日 11:16 · [社区讨论](https://news.ycombinator.com/item?id=50140001)

**背景**: 微米是百万分之一米，实现亚微米级运动对于需要探针接触微小组件的电子测试和材料科学至关重要。工业级微操作器通常价格昂贵，但开源方法使用步进电机和可 3D 打印的部件，以极低的成本复制了这一功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=MgQbPdiuUTw">An Open Source Motorized XYZ Micro - Manipulator ... - YouTube</a></li>
<li><a href="https://news.ycombinator.com/item?id=50140001">Open MicroManipulator – A sub - micrometer 3 D motion control ...</a></li>

</ul>
</details>

**社区讨论**: 社区对创作者的投入印象深刻，指出他在没有任何商业炒作或宣传的情况下发布了详尽的 YouTube 系列视频。讨论中还将该设备与 Delta 机器人进行了比较，承认虽然 Delta 机器人拥有更大的运动范围，但该设计优先考虑的是针对特定窄应用的高精度。

**标签**: `#robotics`, `#hardware`, `#open-source`, `#precision-engineering`, `#diy`

---

<a id="item-10"></a>
## [Sphinx 钩子考核开发者对 AI 生成代码的掌握程度](https://sphinx-six-theta.vercel.app/) ⭐️ 6.0/10

Sphinx 是一款新的开源软件钩子，它整合到编码代理工作流中，在代码推送至生产环境前测试开发者对代码的理解程度。 它解决了 AI 辅助开发中技能退化和责任缺失的关键问题，确保开发者保持对代码库的控制权，而不是沦为被动的旁观者。 该工具在“推送至生产”事件时触发问卷调查，但社区讨论建议在拉取请求阶段进行拦截可能会避免更多的资源浪费。

hackernews · critiquebrowser · 10月18日 04:33 · [社区讨论](https://news.ycombinator.com/item?id=50137950)

**背景**: 编码代理是能够编写代码的 AI 工具，但开发人员往往难以核实他们是否理解生成的输出。如果没有验证层，未经检查的代码可能会引入漏洞和结构问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.visualstudio.com/docs/agent-customization/hooks">Configure agent hooks in Visual Studio Code (Preview)</a></li>
<li><a href="https://www.sonarsource.com/solutions/ai-code-verification/">AI Code Verification Tools | Verify AI-Generated Code | Sonar</a></li>

</ul>
</details>

**社区讨论**: 评论者认为这个概念很有用，但建议将拦截环节移至拉取请求阶段以节省人力时间。一些用户表示当前的 AI 工作流让他们没有技能增长，凸显了主动学习的必要性。

**标签**: `#AI-Coding`, `#DevTools`, `#Software-Engineering`, `#Workflow`, `#HN`

---

<a id="item-11"></a>
## [PS6 RAM and Storage Alone Reportedly Cost Sony Over $680, Claims Leaker](https://www.techpowerup.com/353834/ps6-ram-and-storage-alone-reportedly-cost-sony-over-usd-680-claims-leaker) ⭐️ 5.5/10

Hardware leaker KeplerL2 claims that RAM and storage components for the PlayStation 6 will cost Sony over $680, suggesting the device's total bill of materials may significantly exceed previous estimates due to the memory crunch.

rss · TechPowerUp News · 10月17日 23:33

**标签**: `#PlayStation`, `#Hardware`, `#Leak`, `#Memory`, `#Gaming`

---

<a id="item-12"></a>
## [科乐美总裁早川英树表示 AI 不会从根本上改变游戏市场](https://www.techpowerup.com/353829/konami-president-says-ai-wont-significantly-change-the-games-market-creators-come-first) ⭐️ 5.5/10

在科乐美集团截至 2026 年 3 月的综合报告中，总裁早川英树表示，由于通用游戏引擎和用户生成内容已经降低了入门门槛，生成式 AI 不会给游戏市场带来重大改变。他同时强调，创造引人入胜且具有创新性的电子游戏，最重要的人依然是人类创作者。 这家大型发行商高管的表态反映了游戏行业更广泛的争论，即虽然 AI 会提高制作效率，但它对市场颠覆的影响可能远没有预测的那么深远。这一观点强调了游戏行业的核心价值仍然依赖于人类的创新与创造，而不仅仅是先进的工具。 早川英树在公司的官方综合报告中发表了这一声明，表明了该企业在技术层面的战略立场。他承认使用 AI 很有可能会提高生产效率，但坚持认为市场格局并不会因此发生剧烈的变动。

rss · TechPowerUp News · 10月17日 20:02

**背景**: 科乐美（Konami）是日本一家著名的游戏发行商，代表作包括《合金装备》、《恶魔城》和《实况足球》（原《胜利十一人》）等。综合报告是一种公司披露文件，详细说明了公司的战略和财务表现。用户生成内容是指玩家而非专业开发者创作的游戏修改包或全新游戏，这已经在很大程度上普及了游戏创作过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://automaton-media.com/en/news/konami-president-hayakawa-believes-ai-wont-bring-a-significant-change-to-the-game-market-humans-and-creators-are-crucial-for-developing/">Konami president Hayakawa believes AI “won’t bring a significant...”</a></li>
<li><a href="https://en.wikipedia.org/wiki/Konami">Konami - Wikipedia</a></li>
<li><a href="https://www.konami.com/ir/en/ir-data/financial_rpt.html">Periodic Financial Reports - KONAMI GROUP CORPORATION</a></li>

</ul>
</details>

**标签**: `#gamedevelopment`, `#ai`, `#konami`, `#industrytrends`

---

<a id="item-13"></a>
## [网页版芯片制造工程游戏在台湾爆红](https://www.tomshardware.com/video-games/pc-gaming/chip-fab-engineering-game-goes-viral-in-taiwan-realistic-and-stressful-simulation-is-basically-a-horror-game-say-some-players) ⭐️ 5.5/10

一款展现半导体晶圆厂员工日常生活的 3D 网页模拟游戏在台湾走红，玩家形容其真实且充满压力的环境犹如恐怖游戏。

rss · Tom's Hardware · 10月18日 12:50

**标签**: `#Semiconductor`, `#Gaming`, `#Engineering`, `#Simulation`, `#Viral`

---

<a id="item-14"></a>
## [MapQuest 通过新监控层揭示 Flock ALPR 摄像头位置](https://www.tomshardware.com/software/maps/flock-camera-locations-revealed-on-mapquests-new-surveillance-layer-users-can-now-see-placement-and-direction-of-known-license-plate-readers-from-multiple-companies) ⭐️ 5.5/10

MapQuest 推出了一个新的监控图层，用于可视化 Flock Safety 自动车牌识别（ALPR）摄像头的具体位置和朝向。该功能允许用户查看其周边部署了哪些车牌读取器。 这一进展通过提供实用的工具来识别并可能避开已知的监控区域，极大地提高了用户的意识。它通过聚合摄像头数据到一个广泛可访问的地图界面中，代表了地理空间隐私工具的一大步。 该地图专门显示已知车牌读取器的放置位置和方向，重点在于 Flock ALPR 摄像头。这些数据使用户能够明智地决定其出行路线，以尽量减少对自动化跟踪系统的暴露。

rss · Tom's Hardware · 10月18日 10:00

**背景**: Flock Safety 是一家主要的技术公司，为执法机构提供基于云的自动车牌识别（ALPR）系统。ALPR 技术捕捉并传输车牌图像和数据以识别车辆用于安全目的，这引发了关于大规模监控和个人隐私的持续辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.findingflock.com/map">Flock & ALPR Camera Map of the United States · Finding Flock</a></li>

</ul>
</details>

**标签**: `#Privacy`, `#Geospatial Data`, `#ALPR`, `#Surveillance`, `#MapQuest`

---