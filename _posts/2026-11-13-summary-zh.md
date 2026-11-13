---
layout: default
title: "Horizon Summary: 2026-11-13 (ZH)"
date: 2026-11-13
lang: zh
---

> 从 94 条内容中筛选出 20 条重要资讯。

---

1. [英伟达首席执行官黄仁勋因出口及不当行为指控辞职](#item-1) ⭐️ 10.0/10
2. [Rust 1.100 发布，带来自定义分配器和 never 类型稳定化](#item-2) ⭐️ 9.0/10
3. [苹果发布用于 iOS 本地大语言模型的基础模型框架](#item-3) ⭐️ 8.0/10
4. [Apex Compute 推出神经渲染技术挑战 NVIDIA DLSS](#item-4) ⭐️ 7.5/10
5. [Google reworks TPU silicon into specialized systems for agents and security](#item-5) ⭐️ 7.5/10
6. [Gemini 4 Hydrogen and Orchestrator](#item-6) ⭐️ 7.0/10
7. [Edge0-145B: Frontier AI Capabilities on Your Own Computer](#item-7) ⭐️ 7.0/10
8. [Show HN: My $300 embroidery machine needed a subscription, so I built my own app](#item-8) ⭐️ 7.0/10
9. [英伟达员工请愿要求黄仁昭复出](#item-9) ⭐️ 7.0/10
10. [开源项目实现在内存不足 1GB 的设备上运行 16B 大模型](#item-10) ⭐️ 7.0/10
11. [高光谱成像技术促进大豆病害早期检测](#item-11) ⭐️ 7.0/10
12. [Vicinity Technologies 利用 SDR 将 AI 连接至物理世界](#item-12) ⭐️ 7.0/10
13. [Keychron 宣布针对磁轴键盘的开源 MKF 固件](#item-13) ⭐️ 6.5/10
14. [AMD 据报将中国游戏显卡供应量削减高达 50%](#item-14) ⭐️ 6.5/10
15. [Techie uses voltage glitching hack to turn $2,500 Nvidia 8GB cryptomining GPU into a full-fat $20,000 A100 with 80GB of VRAM](#item-15) ⭐️ 6.5/10
16. [Hobbyist turns $45 USB-C hub into a working Nintendo Switch 2 dock by patching its firmware](#item-16) ⭐️ 6.5/10
17. [Service degradation on Microsoft 365](#item-17) ⭐️ 6.0/10
18. [Design Smarter – Energy Harvesting for Battery-Free and Low-Maintenance Devices in Safety & Security applications](#item-18) ⭐️ 6.0/10
19. [AMD Siren Halo APU 被曝将采用混合 GDDR7 与 LPDDR 内存架构](#item-19) ⭐️ 5.5/10
20. [Noctua 发布适用于 AM5 的 Carbice 碳纳米管导热垫](#item-20) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [英伟达首席执行官黄仁勋因出口及不当行为指控辞职](https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f) ⭐️ 10.0/10

英伟达首席执行官黄仁勋已宣布辞职，此前有报道称其存在个人不当行为，并被指控规避美国出口管制。这一公告将引发全球领先的人工智能芯片制造商的重大领导层更迭。 黄仁勋是当前人工智能热潮的核心人物，他的离开可能会严重破坏半导体行业的发展轨迹。关于违反出口管制的指控对美国的地缘政治和国家安全构成了重大关切。 据报道，辞职的原因包括规避出口禁令的指控（这是一项国家安全问题）以及涉及与中国政府官员关系的不当个人行为。在官方声明发布前，具体的细节和官方理由仍部分不明确。

hackernews · lldb · 11月12日 13:52 · [社区讨论](https://news.ycombinator.com/item?id=50467087)

**背景**: 黄仁勋执掌英伟达数十年，推动其转变为领先的 AI 加速器供应商。美国出口限制规定限制向中国销售先进的 AI 芯片，这使得英伟达成为地缘政治争端的焦点。

**社区讨论**: 社区讨论存在分歧，有人认为辞职的真正原因是规避出口禁令，而非个人私事。另有理论认为，辞职是竞争对手采取的预防性举措，或是一场旨在让特定群体获益的公关表演。

**标签**: `#NVIDIA`, `#Jensen Huang`, `#AI Industry`, `#Geopolitics`, `#Leadership`

---

<a id="item-2"></a>
## [Rust 1.100 发布，带来自定义分配器和 never 类型稳定化](https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/) ⭐️ 9.0/10

Rust 1.100.0 是一个里程碑版本，稳定了 never 类型并引入了稳定的自定义分配器。该版本还包含增强 Cargo 功能，如依赖管理的最小发布时间配置和未使用依赖项的警告。 此版本对 Rust 生态系统意义重大，因为它最终实现了长期未决的架构特性，极大地扩展了该语言在复杂系统编程和 AI 工作负载中的实用性。通过更严格的依赖项管理和工具更新，它提高了供应链安全性和代码健康度。 Cargo 默认报告未使用的依赖项，最小发布时间特性（RFC 3923）允许解析器忽略最近发布的版本，以防止依赖项冷却期攻击。此外，像 bool::toggle()和 Box::map()等次要的稳定 API 新增内容也被包含在内，但未在主要博客文章中提及。

hackernews · mbStavola · 11月12日 18:39 · [社区讨论](https://news.ycombinator.com/item?id=50472038)

**背景**: Rust 是一种以内存安全和性能著称的系统级编程语言。“never 类型”(!)代表永远不会完成的计算，而“自定义分配器”允许开发人员控制内存分配，超越默认的全局分配器。这些特性解决了在编写高性能和特定领域内存管理应用中的核心局限性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/">Announcing Rust 1.100.0 | Rust Blog</a></li>
<li><a href="https://doc.rust-lang.org/std/primitive.never.html">never - Rust</a></li>
<li><a href="https://iifx.dev/en/articles/457134612/from-c-pmr-to-rust-s-generics-understanding-custom-memory-management">From C++ PMR to Rust 's Generics: Understanding Custom Memory...</a></li>

</ul>
</details>

**社区讨论**: 社区反响非常积极，核心团队史蒂夫·克拉布尼克将其称为“纪念性”发布。用户将 never 类型和依赖项冷却期列为个人最爱，同时也注意到该版本对 AI 代码生成的影响。然而，一些用户指出官方博客文章中未提及一些有用的新标准库函数。

**标签**: `#Rust`, `#Programming Language`, `#Release`, `#Cargo`, `#Systems Programming`

---

<a id="item-3"></a>
## [苹果发布用于 iOS 本地大语言模型的基础模型框架](https://developer.apple.com/foundation-models-framework/) ⭐️ 8.0/10

苹果正式发布了其基础模型框架，为开发人员提供 Swift API，以便在 iOS 应用程序中集成本地大语言模型。该框架支持由 Apple Intelligence 驱动本地 AI 处理，且无需调用云 API。 此次发布是移动 AI 领域的一个重要里程碑，使开发者能够创建注重隐私的应用，确保数据永不离开用户设备。它通过降低本地 AI 集成的门槛，巩固了苹果在本地计算领域的领先地位。 该框架专门针对驱动 Apple Intelligence 的本地模型，该模型运行于 Apple Neural Engine，适用于 iOS 26 及更高版本。此外，加入特定项目的开发者可以零额外成本访问 Private Cloud Compute 功能。

hackernews · kermatt · 11月12日 21:13 · [社区讨论](https://news.ycombinator.com/item?id=50474361)

**背景**: 本地 AI 指的是直接在用户硬件（如智能手机）上运行机器学习模型，而不是将数据发送到外部服务器。Apple Intelligence 是苹果集成的 AI 系统，利用本地模型在 iOS 生态系统内进行语言理解和任务执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/documentation/foundationmodels">Foundation Models | Apple Developer Documentation</a></li>
<li><a href="https://medium.com/@yenatlij/getting-started-with-apples-foundation-models-framework-22255113de24">Getting Started with Apple ’s Foundation Models Framework | Medium</a></li>
<li><a href="https://ztabs.co/blog/on-device-llms-mobile-2026">On - Device LLMs for Mobile (2026): Apple Intelligence... | ZTABS</a></li>

</ul>
</details>

**社区讨论**: 社区成员强调了几项相关进展，指出苹果的 CoreAI 项目正在将开放权重模型适配为原生 Swift 运行。用户还分享了低内存 Mac 上本地 AI 的实际案例，并提及了 Anthropic 的 Claude App Attest 对 iOS 的支持。

**标签**: `#Apple`, `#On-Device AI`, `#LLM`, `#iOS Development`, `#Privacy`

---

<a id="item-4"></a>
## [Apex Compute 推出神经渲染技术挑战 NVIDIA DLSS](https://www.techpowerup.com/354727/apex-neural-rendering-beats-nvidia-dlss-in-both-image-quality-and-performance) ⭐️ 7.5/10

Apex Compute 推出了 Apex 神经渲染（ANR），这是一款声称在延迟和 GPU 内存效率上优于 NVIDIA DLSS 的新框架。在 RTX 5090 上，其帧生成延迟为 1.01 毫秒，内存占用仅为 214 MB，而 DLSS 的延迟为 1.26 毫秒，内存占用则高达 562 MB。 由于 ANR 实现了比业界领先的 DLSS 更低的延迟和显著减少的内存消耗，它为实时 AI 加速渲染提供了更高效的选择。这一突破对于寻求优化高端游戏硬件的玩家和开发者而言极具价值。 ANR 目前是一个 Beta 版注入器，依赖于 NVIDIA OptiScaler，使其能够在任何支持 NVIDIA DLSS 帧生成的游戏中无缝运行。其神经网络权重极其高效，仅需 0.17 MB 的空间。

rss · TechPowerUp News · 11月12日 09:19

**背景**: NVIDIA DLSS 是一种广泛应用于 PC 游戏的、基于 AI 的超分辨率与帧生成技术，它对 GPU 性能有重大影响。Apex 神经渲染（ANR）在概念层面上与其相似，但采用了不同的软件实现方式以达到同等甚至更优的效果。由于该技术以注入器（injector）形式运行于 OptiScaler 之上，开发者无需在游戏中明确添加 ANR 支持即可实现兼容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apexcompute.com/neural-rendering">ANR: Apex Neural Rendering | Apex Compute</a></li>
<li><a href="https://www.gamingonlinux.com/2026/11/apex-compute-revealed-apex-neural-rendering-anr-their-cross-platform-answer-to-nvidia-dlss/">Apex Compute revealed Apex Neural Rendering ... | GamingOnLinux</a></li>
<li><a href="https://github.com/apex-compute/ANR">GitHub - apex - compute /ANR: Apex Neural Rendering (ANR) by...</a></li>

</ul>
</details>

**标签**: `#neural-rendering`, `#DLSS`, `#GPU-optimization`, `#computer-graphics`, `#AI-acceleration`

---

<a id="item-5"></a>
## [Google reworks TPU silicon into specialized systems for agents and security](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-adds-two-new-specialized-chips-for-ai-agents-and-security-to-8th-gen-tpu-lineup-tpu-8i-max-puts-two-chips-on-one-package-for-long-context-work-tpu-8tx-swaps-arm-hosts-for-amd-epyc) ⭐️ 7.5/10

Google has introduced two new specialized TPU systems, TPU 8i Max for long-context agent workloads and TPU 8tx for confidential inference using AMD EPYC hosts.

rss · Tom's Hardware · 11月12日 11:00

**标签**: `#Google TPU`, `#AI Hardware`, `#AI Agents`, `#Silicon Design`, `#Inference Security`

---

<a id="item-6"></a>
## [Gemini 4 Hydrogen and Orchestrator](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/) ⭐️ 7.0/10

Google Antigravity announces Gemini 4 Hydrogen and an Orchestrator mode, which community members discuss in terms of performance comparisons to existing models and the technical implications of multi-model pipeline caching.

hackernews · jonbaer · 11月12日 18:52 · [社区讨论](https://news.ycombinator.com/item?id=50472260)

**标签**: `#Gemini`, `#LLM`, `#Model Orchestration`, `#Google AI`, `#Developer Tools`

---

<a id="item-7"></a>
## [Edge0-145B: Frontier AI Capabilities on Your Own Computer](https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer) ⭐️ 7.0/10

Edge0-145B is introduced as a 145B-parameter AI model designed for local inference on consumer hardware, achieving low memory footprints through expert matrix sharing and demonstrating advanced tool-use capabilities.

hackernews · sroussey · 11月12日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50475713)

**标签**: `#AI/ML`, `#Edge Computing`, `#Large Language Models`, `#Model Compression`, `#Local Inference`

---

<a id="item-8"></a>
## [Show HN: My $300 embroidery machine needed a subscription, so I built my own app](https://github.com/simpsoka/zigzag) ⭐️ 7.0/10

A developer built a custom app for their $300 embroidery machine to avoid a subscription fee, showcasing the practical use of LLMs in automating niche hardware.

hackernews · simpsoka · 11月12日 17:02 · [社区讨论](https://news.ycombinator.com/item?id=50470488)

**标签**: `#hardware`, `#AI-Tools`, `#IOT`, `#OpenSource`, `#HackerNews`

---

<a id="item-9"></a>
## [英伟达员工请愿要求黄仁昭复出](https://www.wired.com/story/nvidia-employees-petition-for-jensen-huangs-return/) ⭐️ 7.0/10

英伟达员工发起了一项内部请愿，呼吁重新任命前首席执行官黄仁昭。此举在企业界及网络社区引发了关于其道德瑕疵的强烈争议。 此事件暴露了严重的公司治理危机，凸显了领导者运营成功与在严格的国际出口管制法律下的合规失误之间的摩擦。它引发了关于董事会问责制和风险管理的关键问题。 批评者指出，黄仁昭的涉嫌行为超出了普通的个人失误，涉及与试图规避 ITAR（国际武器贸易条例）限制的外国实体的关系，属于系统性的行为模式。支持者则主张其卓越的领导力以及给予第二次机会的权利。

hackernews · lavendermon · 11月13日 02:16 · [社区讨论](https://news.ycombinator.com/item?id=50477231)

**背景**: 黄仁昭最近卸任了英伟达的首席执行官，有关此事的公众细节仍在逐步披露中。ITAR（国际武器贸易条例）是美国联邦法规，严格限制国防相关物品的出口，协助外国实体规避该条例将面临严重的法律后果。

**社区讨论**: 社区观点严重分歧；部分人基于其过往成就为黄仁昭辩护，但另一些人则认为其与规避出口管制的实体交往表明其存在鲁莽的行为模式。许多人表达了对公司潜在漏洞及董事会未能解决这些风险的担忧。

**标签**: `#Nvidia`, `#Corporate Governance`, `#Jensen Huang`, `#Ethics`, `#Tech Leadership`

---

<a id="item-10"></a>
## [开源项目实现在内存不足 1GB 的设备上运行 16B 大模型](https://github.com/hyperionaidev/smolmaxxing/) ⭐️ 7.0/10

一项开源倡议成功让 16B 参数的大语言模型在内存不足 1GB 的极限受限设备上运行，例如第一代 iPad Air 和小米电视盒子。该项目通过优化的推理内核、模型修改以及在 Hugging Face 上共享资源来实现这一目标。 这一突破大幅提升了大语言模型在老旧及低功耗硬件上的可访问性，证明了边缘 AI 不需要高端资源。它符合行业缩小推理引擎计算足迹的更广泛趋势，促进了更加包容和分布式的 AI 生态系统。 该项目依赖自定义开发的内核和修改后的模型权重来绕过传统内存瓶颈。尽管受硬件限制只能达到“尚可”的速度，部署此类系统的主要挑战在于物理硬件的获取，而非计算逻辑本身，因为推理引擎本质上只是乘法等基础运算。

hackernews · mrashad74 · 11月12日 15:23 · [社区讨论](https://news.ycombinator.com/item?id=50468888)

**背景**: 大语言模型在推理时通常需要将模型参数存储在内存中，这需要大量的内存（通常以 GB 为单位）。要在内存小于 1GB 的设备上运行它们，需要采用激进的模型量化技术（降低权重的数值精度）以及优化的 CPU 内存访问自定义推理内核。这些修改使全部计算能够适应传统移动和电视硬件受限的内存极限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cast.ai/blog/demystifying-quantizations-llms/">LLM Quantization Methods: GPTQ, AWQ, GGUF - Cast AI</a></li>
<li><a href="https://www.linkedin.com/posts/martinuke0_optimizing-local-inference-a-guide-to-running-activity-7459953891997249536-cg5R">Optimizing 100B Parameter Models on Edge Hardware | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 社区成员对该项目表现出极大热情，并分享了类似的成就，例如通过 Windows CE 在复古 Dreamcast 硬件上运行 LLM。讨论指出，现代推理引擎主要受限于内存和基础计算，使得硬件的获取而非算法复杂度成为了新的入门门槛。

**标签**: `#LLM`, `#Edge AI`, `#Hardware Optimization`, `#Open Source`, `#Inference`

---

<a id="item-11"></a>
## [高光谱成像技术促进大豆病害早期检测](https://www.eetimes.com/can-machines-see-a-sick-plant-before-a-farmer-can/) ⭐️ 7.0/10

大豆病害研究突出了高光谱成像在早期检测植物疾病方面的应用。半导体技术的进步使芯片级光谱传感系统变得经济实惠，从而能够在大范围农业中使用。 早期检测作物疾病可以显著减少产量损失并优化农业资源使用。使该技术变得经济实惠对于普及精准农业和改善全球粮食安全至关重要。 高光谱传感器在田间和温室等精准农业环境中的实际应用仍是一个挑战。新兴技术侧重于低成本、CMOS 集成的多光谱和偏振传感。

rss · EE Times · 11月12日 13:00

**背景**: 高光谱成像通过捕获许多窄波段内的详细光谱数据，使其能够检测到人眼不可见的细微植物健康变化。机器学习算法处理这些数据以早期识别特定的疾病症状。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iis.fraunhofer.de/en/ff/sse/sensor-solutions/optnanostruktcmos.html">nanoSPECTRAL: Multispectral and Polarization Sensors</a></li>
<li><a href="https://www.mdpi.com/2073-4395/12/6/1451">Hyperspectral Sensing of Plant Diseases: Principle and Methods</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8983301/">A review of hyperspectral image analysis techniques for plant ...</a></li>

</ul>
</details>

**标签**: `#Hyperspectral Imaging`, `#Precision Agriculture`, `#Sensors`, `#Semiconductors`

---

<a id="item-12"></a>
## [Vicinity Technologies 利用 SDR 将 AI 连接至物理世界](https://www.eetimes.com/connecting-ai-to-the-physical-world/) ⭐️ 7.0/10

一篇由 Vicinity Technologies 首席执行官撰写的文章认为，专用无线设备和 SDR IP 对于将人工智能连接到物理世界至关重要。文章强调，这些组件对于下一代智能机器不可或缺。 这一观点之所以重要，是因为它弥合了数字人工智能与现实物理世界之间的鸿沟，指出了专用硬件作为智能系统必要通道的地位。它凸显了在部署高级物联网和自主系统时的一个关键依赖项。 文章作者代表 Vicinity Technologies 公司，表明该内容带有特定商业角度的思想领导力或行业分析性质。分析重点在于 SDR 软件 IP 的作用，而不仅仅是硬件，并强调了软件定义的灵活性。

rss · EE Times · 11月12日 10:20

**背景**: 软件定义无线电（SDR）使用嵌入式系统上的软件取代传统的模拟硬件组件，从而实现可编程和灵活的无线电通信。通过将人工智能与 SDR 结合，机器可以动态地感知、分析和响应物理频谱环境，这对现代物联网环境至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software-defined radio - Wikipedia</a></li>
<li><a href="https://ieeexplore.ieee.org/abstract/document/11456026">Artificial Intelligence in Software Defined Radio: A Survey</a></li>

</ul>
</details>

**标签**: `#AI`, `#IoT`, `#SDR`, `#Hardware`, `#Wireless`

---

<a id="item-13"></a>
## [Keychron 宣布针对磁轴键盘的开源 MKF 固件](https://www.techpowerup.com/354759/keychron-launches-open-source-magnetic-keyboard-firmware) ⭐️ 6.5/10

Keychron 宣布了 MKF，这是一款面向 TMR 和霍尔效应游戏键盘的开源固件项目，其功能概述包括 8kHz 轮询、快速触发和控制器模拟。该项目目前仅有一个落地页，尚无公开的代码贡献。 开源磁轴键盘固件顺应了更广泛的开源硬件运动，允许发烧友定制自定义响应曲线和 PDO 等特性。它提供了一个由社区驱动的基础，有可能在高端游戏外设领域与闭源固件相媲美。 初期计划仅支持有线连接，但固件将包括如 PDO 等高级特性，该特性会根据按键按下的深度发送更多按键信号。该项目明确欢迎社区为非竞技游戏用途的功能做出贡献。

rss · TechPowerUp News · 11月12日 21:34

**背景**: 磁轴键盘使用 TMR 或霍尔效应传感器来检测开关位置，从而实现可调触发和快速触发。快速触发在按键释放时重置按键，而 SOCD（同时相反基本方向）有助于解决同时按下相反方向时的冲突。这些特性对于竞技 FPS 游戏至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unikeyboards.com/blogs/weekeebpedia/tmr-vs-hall-effect">TMR vs Hall Effect: Which Magnetic Keyboard Technology Is ...</a></li>
<li><a href="https://gameperipherals.com/blogs/all-posts/rapid-trigger-adjustable-actuation-and-socd-explained">Rapid Trigger, Adjustable Actuation and SOCD Explained</a></li>

</ul>
</details>

**标签**: `#hardware`, `#firmware`, `#open-source`, `#keyboards`, `#input-devices`

---

<a id="item-14"></a>
## [AMD 据报将中国游戏显卡供应量削减高达 50%](https://www.techpowerup.com/354757/amd-reportedly-cuts-gaming-gpu-supply-in-china-by-up-to-50) ⭐️ 6.5/10

据报道，自第四季度初以来，AMD 将中国市场的游戏显卡供应量减少了 20% 至 50%，导致 Radeon 显卡的分配更紧张且价格上涨。由于供应链持续缩减，这种情况预计将持续到 1 月。 这种供应缩减通过增加获得负担得起的 Radeon 显卡的难度，对中国玩家和 PC 组装者造成了显著影响。价格上涨和货源紧张反映了全球硬件行业在内存和 GPU 成本方面的广泛压力。 预计 AMD 将继续提高 GPU 和 GDDR6 套件的价格，而竞争对手如 NVIDIA 的高端型号也面临供应限制。市场显示显卡的平均售价比 MSRP 高出 44%，这使得新发布的显卡对消费者而言价格更加昂贵。

rss · TechPowerUp News · 11月12日 21:14

**背景**: 显卡制造商与加入板卡合作伙伴（AIB）合作生产零售产品，供应量的波动会直接影响这些分销商。GDDR6 是现代 GPU 中使用的一种内存，其成本是游戏硬件最终零售价格的重要因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hwbusters.com/news/amd-reportedly-plans-another-radeon-price-increase-for-november-as-gddr6-keeps-climbing/">AMD Reportedly Plans Another Radeon Price Increase for November...</a></li>
<li><a href="https://grokipedia.com/page/Add-in_board">Add-in board — Grokipedia</a></li>
<li><a href="https://pcbstore.com.bd/glossary/aib-partner-card">What is AIB Partner Card? Custom GPU Basics Explained</a></li>

</ul>
</details>

**标签**: `#Hardware`, `#Supply Chain`, `#AMD`, `#GPU`, `#China`

---

<a id="item-15"></a>
## [Techie uses voltage glitching hack to turn $2,500 Nvidia 8GB cryptomining GPU into a full-fat $20,000 A100 with 80GB of VRAM](https://www.tomshardware.com/pc-components/gpus/techie-turns-usd2-500-cmp-170hx-8gb-mining-card-into-a-full-fat-a100-80gb-with-voltage-glitching-carefully-blowing-onboard-fuses-to-unlock-entire-vram-and-shader-modules) ⭐️ 6.5/10

A technician used voltage glitching techniques to disable fuses on an Nvidia CMP-170HX mining card, effectively unlocking its full 80GB VRAM and shader capabilities to create a high-performance equivalent of an A100 GPU.

rss · Tom's Hardware · 11月12日 10:30

**标签**: `#GPU`, `#Hardware Mod`, `#AI Hardware`, `#Nvidia`, `#Cryptocurrency Mining`

---

<a id="item-16"></a>
## [Hobbyist turns $45 USB-C hub into a working Nintendo Switch 2 dock by patching its firmware](https://www.tomshardware.com/video-games/nintendo/hobbyist-turns-usd45-usb-c-hub-into-a-working-nintendo-switch-2-dock-by-patching-its-firmware-consoles-proprietary-handshake-needs-about-540-bytes-of-code-to-answer) ⭐️ 6.5/10

A hobbyist successfully patched the firmware of a $45 USB-C hub to function as a Nintendo Switch 2 dock, enabling TV mode and HDR support by emulating the proprietary handshake.

rss · Tom's Hardware · 11月12日 09:00

**标签**: `#Hardware Hacking`, `#Nintendo Switch`, `#Firmware`, `#Reverse Engineering`, `#USB-C`

---

<a id="item-17"></a>
## [Service degradation on Microsoft 365](https://status.cloud.microsoft/) ⭐️ 6.0/10

A major service degradation affecting Microsoft 365 worldwide, with community members sharing real-time updates on status page issues, mitigation steps, and the impact on enterprise email and communication tools.

hackernews · dkpk · 11月12日 18:20 · [社区讨论](https://news.ycombinator.com/item?id=50471731)

**标签**: `#Microsoft 365`, `#Outage`, `#IT Operations`, `#Cloud Services`, `#Reliability`

---

<a id="item-18"></a>
## [Design Smarter – Energy Harvesting for Battery-Free and Low-Maintenance Devices in Safety & Security applications](https://www.eetimes.com/design-smarter-energy-harvesting-for-battery-free-and-low-maintenance-devices-in-safety-security-applications/) ⭐️ 6.0/10

A design guide explaining how to implement energy harvesting in safety and security devices to eliminate the need for manual battery maintenance.

rss · EE Times · 11月12日 15:00

**标签**: `#Energy Harvesting`, `#Hardware Design`, `#IoT`, `#Embedded Systems`, `#Power Management`

---

<a id="item-19"></a>
## [AMD Siren Halo APU 被曝将采用混合 GDDR7 与 LPDDR 内存架构](https://www.techpowerup.com/354765/amd-siren-halo-apu-rumored-to-pair-dedicated-gddr7-with-lpddr-memory) ⭐️ 5.5/10

来自 X 平台的泄露消息称，AMD 下一代'Siren Halo' APU 将采用混合内存架构，结合专用 GDDR7 显存与标准 LPDDR 系统内存。泄露者还声称 Siren Halo 将继 Medusa Halo 之后推出，且 Siren Point 基本只是 Medusa 的刷新版本。 该混合设计将标志着 AMD 当前统一内存 APU 的重大转变，有望通过提供更高内存带宽来提升 iGPU 的游戏性能，同时保留独立系统内存用于 AI 和通用工作负载。这表明 AMD 在高性能集成显卡方面的持续演进。 此次泄露未披露 Siren Halo 具体的内存容量、位宽或上市时间等详细信息。据传该 APU 与 AMD 的 Project Magnus 项目相关，该项目又与微软 Project Helix 主机硬件有关。

rss · TechPowerUp News · 11月13日 00:37

**背景**: AMD 当前的高端 APU（如 Strix Halo）使用共享的 LPDDR5X 内存池为 CPU 和 iGPU 供电，该设计因本地运行大语言模型（LLM）而备受青睐。GDDR7 是较新的高带宽内存标准，近期已被独立显卡采用，且 AMD 已提前在其驱动中加入 GDDR7 支持，为 RDNA 5 GPU 架构做好准备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/354765/amd-siren-halo-apu-rumored-to-pair-dedicated-gddr7-with-lpddr-memory">AMD "Siren Halo" APU Rumored to Pair Dedicated GDDR7 With ...</a></li>

</ul>
</details>

**标签**: `#AMD`, `#APU`, `#GDDR7`, `#Hardware Rumor`, `#GPU Architecture`

---

<a id="item-20"></a>
## [Noctua 发布适用于 AM5 的 Carbice 碳纳米管导热垫](https://www.techpowerup.com/354729/noctua-introduces-nt-cp1-carbice-carbon-nanotube-thermal-pad-for-am5) ⭐️ 5.5/10

Noctua 发布了专为 AMD AM5 和 AM4 处理器设计的高端碳纳米管导热垫 NT-CP1。该导热垫采用 Carbice 技术，声称在经历数百次至数千次热循环后，其传热性能不仅不会像传统导热硅脂那样衰减，反而会逐步提升。 该产品通过消除重新涂抹导热硅脂的维护环节，解决了高性能计算中的一个关键可靠性问题。它为发烧友提供了一种耐用且“一次安装长期有效”的解决方案，防止因泵出效应和脱层导致的性能下降。 NT-CP1 采用坚固的铝制背板和相变聚合物涂层，确保了安装的便捷性以及接触面的电气绝缘性。在初始激活阶段贴合表面微观结构完成后，该导热垫可在数年内保持性能稳定。

rss · TechPowerUp News · 11月12日 10:25

**背景**: 导热垫是一种固态导热界面材料，用于填补处理器集成散热顶盖（IHS）与散热器之间的间隙。传统导热硅脂常受“泵出”效应影响，即在热循环作用下，流体材料会从界面迁移出来，导致热阻增加。碳纳米管技术正日益被采用，以创造更稳定、使用寿命更长的导热界面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.noctua.at/en/news/noctua-introduces-nt-cp1-carbon-nanotube-thermal-pad-for-am5">Noctua introduces NT-CP1 Carbice ® carbon nanotube thermal pad ...</a></li>
<li><a href="https://carbice.com/technology/how-it-works">How Carbice Works | Carbice</a></li>
<li><a href="https://www.lenecold.com/resources/thermal-pad-pump-out.html">What Is TIM Pump-Out? Why Thermal Grease Fails in Cycling ...</a></li>

</ul>
</details>

**标签**: `#Hardware`, `#Thermal Management`, `#AMD`, `#PC Cooling`, `#Product Release`

---