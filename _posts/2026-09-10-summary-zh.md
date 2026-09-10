---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> 从 88 条内容中筛选出 20 条重要资讯。

---

1. [OpenAI 在 Hot Chip 大会发布首款定制 AI 推理芯片 Jalapeño](#item-1) ⭐️ 8.0/10
2. [Isar Aerospace 实现欧洲大陆首次轨道发射](#item-2) ⭐️ 8.0/10
3. [MOD 开发者为 RTX 30 系列显卡解锁 DLSS 多帧生成功能](#item-3) ⭐️ 7.5/10
4. [OpenAI 考虑将下一代芯片交由三星代工，暗示算力需求巨大](#item-4) ⭐️ 7.5/10
5. [安全研究员逆向重建 Stuxnet 源代码并发布在 GitHub](#item-5) ⭐️ 7.5/10
6. [可折叠 iPhone 正式亮相：Apple 新品发布会回顾](#item-6) ⭐️ 7.3/10
7. [Shopify 收购 Tailwind CSS，AI 冲击开发者工具商业模式](#item-7) ⭐️ 7.0/10
8. [GPT-6 Astra、循环 Transformer 与隐藏推理机制](#item-8) ⭐️ 7.0/10
9. [Qwen 3.8 沿用了 GPT-5.5 Pro 的推理预填充模式](#item-9) ⭐️ 7.0/10
10. [GNU Radio 通过 WebAssembly 移植到浏览器](#item-10) ⭐️ 7.0/10
11. [安全研究员揭露恶意软件广告绕过 Google Ads 审核流程](#item-11) ⭐️ 7.0/10
12. [LED 实现 5 米距离更安全的室内无线供电](#item-12) ⭐️ 7.0/10
13. [苹果全线 iPhone 涨价 100 美元，DRAM 短缺推高成本](#item-13) ⭐️ 6.5/10
14. [1900 名暴雪员工签署工会合同，涉及生成式 AI、裁员及远程办公](#item-14) ⭐️ 6.5/10
15. [苹果发布 iPhone 18 Pro 和 Pro Max，搭载可变光圈](#item-15) ⭐️ 6.5/10
16. [HP 推出搭载 NVIDIA GB300 和 Red Hat 的 ZGX Fury AI 工作站](#item-16) ⭐️ 6.5/10
17. [CXMT HBM3E 良率仅 25%，TSV 技术不成熟为主因](#item-17) ⭐️ 6.5/10
18. [LG 强烈否认涉及 2.16 亿台电视的间谍指控](#item-18) ⭐️ 6.5/10
19. [OpenAI 称 GPT‑6 Astra 具类 AGI 能力但仍有常见弱点](#item-19) ⭐️ 6.5/10
20. [Arm 发布 Neoverse CSS N4，面向下一代 CPU 与 DPU](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [OpenAI 在 Hot Chip 大会发布首款定制 AI 推理芯片 Jalapeño](https://semiwiki.com/semiconductor-manufacturers/373394-jalapeno-hot-chip-cool-power-bill-openai-turns-up-the-heat-on-ai-inference/) ⭐️ 8.0/10

OpenAI 在 Hot Chip 大会上发布了与 Broadcom 联合开发的定制推理加速器'Jalapeño'。该芯片专为支撑交互式和智能体 AI 系统的低延迟、多芯片工作负载而优化，摒弃了传统上以峰值 FLOPS 和内存带宽为核心的基准测试思路。 这标志着 OpenAI 正式进入定制芯片赛道，与 Google TPU 和 AWS Trainium 并列为开发自研推理硬件的主要 AI 实验室。该芯片转向优化智能体和多步骤推理工作负载，反映出业界日益认识到真实场景下的 AI 性能不仅仅取决于原始算力吞吐。 Jalapeño 是一款专为 LLM 推理（非训练）设计的 ASIC，其设计理念优先考虑端到端延迟和能效，而非吸睛的峰值规格。文章内容被截断，未提供具体每秒 token 数或详细功耗测量等深度技术基准数据。

rss · SemiWiki · 9月9日 21:00

**背景**: Hot Chips 是自 1989 年起举办的顶级高性能微处理器和集成电路年度研讨会，在半导体行业专业人士中享有盛誉。定制 AI 芯片已成为超大规模云厂商的战略重点，因为通用 GPU 虽然用途广泛，但在大型语言模型推理等特定工作负载上可能无法充分释放性能和效率。智能体 AI 工作负载不同于传统的单次推理，因为智能体会执行由多次顺序模型调用、工具使用和推理步骤组成的执行轨迹（trace），此时关键指标是整个流水线的延迟，而非单次调用的吞吐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/jalapeno-first-results/">Jalapeño's first results show industry-leading speed and ... - OpenAI</a></li>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip</a></li>
<li><a href="https://www.getimpala.ai/blog/inference-for-agentic-workloads-is-different-heres-what-that-means-for-your-stack">Inference for Agentic Workloads Is Different. Here's What That...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI Hardware`, `#Custom Silicon`, `#AI Inference`, `#Hot Chip`

---

<a id="item-2"></a>
## [Isar Aerospace 实现欧洲大陆首次轨道发射](https://www.electronicsweekly.com/news/andoya-isar-aerospace-achieve-first-european-orbital-launch-2026-09/) ⭐️ 8.0/10

德国 Isar Aerospace 从挪威安道亚航天发射场成功发射了 Spectrum 火箭，实现了欧洲大陆的首次轨道发射。据 2026 年 9 月报道，此次任务标志着欧洲太空进入能力的一个历史性里程碑，摆脱了对海外发射场的依赖。 这一成就使欧洲拥有了从本土进行的自主轨道发射能力，减少了对外国发射服务商的依赖，并缓解了拥挤的欧洲发射排期压力。它将 Isar Aerospace 定位为小型运载火箭市场中的关键参与者，并验证了安道亚作为欧洲大陆轨道发射门户的战略。 Spectrum 是一款两级小型轨道运载火箭，高 28 米、直径 2 米，使用液氧和丙烷推进剂以获得更清洁的燃烧效果。Isar Aerospace 于 2018 年在慕尼黑附近的奥托布伦成立，已通过 15 轮融资筹集超过 9.56 亿美元，其中包括 2026 年 6 月的一笔 3.1163 亿美元 D 轮融资。

rss · Electronics Weekly · 9月9日 11:16

**背景**: 安道亚太空（前身为安道亚火箭靶场）位于挪威韦斯特龙群岛最北端的安道亚岛上，纬度为北纬 69 度，非常适合极地轨道和太阳同步轨道发射。Isar Aerospace 是欧洲几家追求小型运载火箭能力的初创公司之一，旨在服务不断增长的小卫星市场。该公司此前曾在安道亚经历过一次失败的试飞，因此这次成功的轨道发射任务标志着其重大回归，也验证了其在运载火箭设计与制造方面采用垂直整合策略的正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Spectrum_(rocket)">Spectrum ( rocket ) - Wikipedia</a></li>
<li><a href="https://isaraerospace.com/spectrum">Spectrum - Isar Aerospace</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isar_Aerospace">Isar Aerospace - Wikipedia</a></li>

</ul>
</details>

**标签**: `#space-launch`, `#european-space`, `#isar-aerospace`, `#orbital-rocketry`, `#milestone`

---

<a id="item-3"></a>
## [MOD 开发者为 RTX 30 系列显卡解锁 DLSS 多帧生成功能](https://www.techpowerup.com/352508/modders-unlock-dlss-multi-frame-generation-for-rtx-30-series-ampere-gpus) ⭐️ 7.5/10

一款名为 DLSSG SM86 的新 MOD 让 GeForce RTX 30 系列（Ampere 架构）显卡支持 DLSS 多帧生成的 2X 和 4X 模式，而该功能此前被 NVIDIA 官方限定于 RTX 50 系列（Blackwell 架构）。与以往用 AMD FSR 帧生成替换的方案不同，该 MOD 使用代理后端保留了 NVIDIA 原生的 DLSS 模型，并将帧生成调用重定向到捆绑的 DLSSG 310.1 运行时，且无需修改游戏文件。 该 MOD 通过将新一代旗舰功能带到老一代显卡上，延长了 RTX 30 系列硬件的使用寿命，可能减轻玩家升级到 RTX 50 系列的压力。同时也表明 NVIDIA 在技术上完全可以在旧显卡上启用该功能，引发了关于人为硬件分层的讨论。 该 MOD 在搭载驱动 591.86 的 RTX 3080 Ti 上进行了测试（Windows 系统、D3D12 接口），《黑神话：悟空》在 4X 模式下帧率从 50 FPS 提升至 150 FPS，《赛博朋克 2077》开启路径追踪后从 35 FPS 提升至 100 FPS。另一项在 RTX 3080 上的 YouTube 测试显示，《赛博朋克 2077》帧率从约 42 FPS 提升至 74 FPS（2X）和 120 FPS（4X），但开发者承认尚未完成正式的帧时间、延迟和长时间稳定性测试。

rss · TechPowerUp News · 9月9日 13:09

**背景**: DLSS（深度学习超采样）是 NVIDIA 推出的 AI 驱动超采样与帧生成技术。帧生成通过在传统渲染帧之间插入 AI 生成的中间帧来提升观感流畅度，而多帧生成可以在每个渲染帧之间插入多达三个额外帧，配合 DLSS 超采样可实现最高 8 倍的帧率提升。DLSS 多帧生成重度依赖 RTX 50 系列 GPU 中新一代 Tensor Core，此前被视为 Blackwell 架构的独占功能。RTX 30 系列采用 SM86（Ampere）架构，缺少新一代专用硬件加速器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/352508/modders-unlock-dlss-multi-frame-generation-for-rtx-30-series-ampere-gpus">Modders Unlock DLSS Multi Frame Generation For RTX 30-Series "Ampere" GPUs | TechPowerUp</a></li>
<li><a href="https://videocardz.com/newz/nvidia-keeps-dlss-multi-frame-gen-locked-to-rtx-50-modders-just-got-it-working-on-rtx-30-with-dlss5-included">NVIDIA keeps DLSS Multi Frame Gen locked to RTX 50, modders just got it working on RTX 30 with DLSS5 included - VideoCardz.com</a></li>
<li><a href="https://www.nvidia.com/en-us/geforce/news/dlss4-multi-frame-generation-ai-innovations/">NVIDIA DLSS 4 Introduces Multi Frame Generation & Enhancements For All DLSS Technologies | GeForce News | NVIDIA</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，赞扬了 MOD 社区的技术成就，以及为老硬件注入新活力的前景。部分评论指出，NVIDIA 显然有能力在旧显卡上启用该技术，只是为了保持 RTX 50 系列的升级吸引力而选择不这么做。

**标签**: `#DLSS`, `#RTX 30-series`, `#frame-generation`, `#GPU-modding`, `#NVIDIA`

---

<a id="item-4"></a>
## [OpenAI 考虑将下一代芯片交由三星代工，暗示算力需求巨大](https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-says-its-next-generation-processors-could-be-made-at-samsung-double-sourcing-with-tsmc-hints-at-massive-volume-requirements) ⭐️ 7.5/10

OpenAI 正在深化与三星的芯片合作，并据报道准备将自研 AI ASIC 同时交由三星和台积电双源代工，这表明其对自研芯片的需求已远超单一代工厂的供应能力。此举意味着 OpenAI 正在向大规模量产其定制 AI 加速器迈进。 同时向全球两大最先进的代工厂双源采购，是一个强烈的信号，表明 OpenAI 的算力需求已进入需要数百亿美元硅片采购的量级，正在重塑 AI 基础设施的经济格局和供应链动态。这同时也降低了 OpenAI 对任何单一代工厂的依赖，缓解了地缘政治和产能风险，并加剧了与 NVIDIA GPU 主导地位的竞争。 这并非 OpenAI 首次涉足自研芯片——其首款代号为 Jalapeño 的自研芯片由博通代工，标志着多代际芯片平台的起步。转向由三星和台积电代工的大规模 ASIC 生产，意味着其需求量远远超出了一代芯片那种有限、依赖合作伙伴的早期量产规模。

rss · Tom's Hardware · 9月9日 14:30

**背景**: AI ASIC（专用集成电路）是专为特定 AI 工作负载定制设计的芯片，相比通用 GPU 在性能和功耗效率上更优，但牺牲了灵活性。台积电和三星等晶圆代工厂负责制造由其他公司设计的芯片，双源采购（在两家代工厂之间分配生产）是确保产能、降低风险并获得定价优势的经典供应链策略。OpenAI 此前与博通合作的 Jalapeño 芯片是其首个公开讨论的第一方自研芯片，如今扩展到双代工厂生产，标志着该项目正在成熟为一个完整的硬件平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/">OpenAI unveils its first custom chip, built by Broadcom</a></li>
<li><a href="https://openai.com/index/jalapeno-first-results/">Jalapeño's first results show industry-leading speed and ... - OpenAI</a></li>
<li><a href="https://ai-stack.ai/en/asic-vs-gpu">What are ASIC Chips? A Detailed Comparison with GPUs and Application Scenarios - INFINITIX | AI-Stack</a></li>

</ul>
</details>

**标签**: `#AI`, `#semiconductors`, `#OpenAI`, `#hardware`, `#supply-chain`

---

<a id="item-5"></a>
## [安全研究员逆向重建 Stuxnet 源代码并发布在 GitHub](https://www.tomshardware.com/tech-industry/cyber-security/researcher-reconstructs-infamous-stuxnet-malware-source-code-attack-targeted-iranian-nuclear-facilities-and-was-the-first-software-of-its-type-to-cause-physical-damage) ⭐️ 7.5/10

一位匿名安全研究员逆向重建了 Stuxnet 蠕虫的源代码，并将其发布在 GitHub 上。Stuxnet 最初是在布什和奥巴马政府期间被开发出来，用于暗中干扰伊朗的铀浓缩活动。 Stuxnet 是已知首个造成物理破坏的网络武器，是网络战历史上的标志性事件。公开逆向重建的源代码为安全防御人员提供了宝贵的研究资料，但也引发了关于网络武器知识扩散的双重用途担忧。 Stuxnet 专门针对用于操作工业离心机的西门子可编程逻辑控制器（PLC），改变其旋转速度以造成物理损坏，同时向操作员屏蔽正常的读数。该恶意软件通过可移动驱动器传播，并利用了多个零日漏洞，是一款极为精密的国家级代码。

rss · Tom's Hardware · 9月9日 10:30

**背景**: Stuxnet 于 2010 年被发现，被广泛认为是一次针对伊朗核计划的美国-以色列联合行动。它通过操控控制铀浓缩离心机的西门子 PLC 工作，使其以破坏性的速度旋转，同时向操作员报告正常读数。该蠕虫通过 USB 驱动器传播，并利用了四个零日 Windows 漏洞，这在当时是前所未有的数量。对如此复杂的恶意软件进行逆向工程通常需要使用 JEB 或 dnSpy 等反编译器、反汇编器以及十六进制编辑器，从编译后的二进制文件中重建源代码级别的逻辑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.avast.com/c-stuxnet">What is Stuxnet , Who Created it & How Does it Work ?</a></li>
<li><a href="https://medium.com/@2019se70082/stuxnet-the-worm-that-changed-the-world-8c868687a859">Stuxnet , the Worm that Changed The World | by Seth Balgas | Medium</a></li>
<li><a href="https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/malware-reverse-engineering/">Malware Reverse Engineering for Beginners Explained</a></li>

</ul>
</details>

**标签**: `#stuxnet`, `#malware-analysis`, `#cyberwarfare`, `#reverse-engineering`, `#security-research`

---

<a id="item-6"></a>
## [可折叠 iPhone 正式亮相：Apple 新品发布会回顾](https://sspai.com/post/114392) ⭐️ 7.3/10

Apple 于 9 月 10 日凌晨召开新品发布会，正式推出了新一代 iPhone 18 Pro 系列、Apple Watch Series 12、Apple Watch Ultra 4 以及 AirPods 5 系列。 如果 Apple 真的推出可折叠 iPhone，这将是 iPhone 产品形态与产品线策略的重大变化，可能加剧与现有折叠屏厂商的竞争，并重塑高端智能手机市场的格局。 现有摘要缺少关于可折叠设备的关键技术细节，例如铰链设计、屏幕规格、上市日期和定价信息；该文章仅为发布会简要回顾，并未提供详细的产品技术解析。

rss · 少数派 · 9月9日 21:21

**背景**: 自三星于 2019 年推出 Galaxy Fold 以来，折叠屏智能手机已成为一个不断增长的品类，华为、Google 和小米等竞争对手也相继推出了各自的折叠设备。Apple 长期以来一直被传言正在研发可折叠 iPhone，但此前并未正式进入这一领域。9 月的产品发布会传统上是 Apple 一年一度的 iPhone 发布会，公司通常会在此期间推出旗舰智能手机以及可穿戴和音频产品线的更新。

**标签**: `#Apple`, `#iPhone`, `#可折叠设备`, `#智能手表`, `#发布会`

---

<a id="item-7"></a>
## [Shopify 收购 Tailwind CSS，AI 冲击开发者工具商业模式](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 7.0/10

Shopify 收购了最广泛使用的 utility-first CSS 框架之一 Tailwind CSS。在此之前，Tailwind Labs 因 AI 导致文档流量下降（较 2023 年初减少约 40%）而经历了大规模裁员，工程团队 75%的成员失业。 这次收购揭示了 AI 如何颠覆传统的开发者工具商业模式——尤其是依赖文档流量和模板销售变现的公司，因为大语言模型可以直接生成用户过去需要搜索文档才能获得的代码。它预示着一种潜在的整合趋势：开源 DevTools 如果缺乏托管等规模化服务，将越来越难以维持商业运营。 Tailwind Labs 一直在其开源框架的基础上销售 UI 模板和商业产品，但 AI 按需生成样式化组件的能力削弱了这些收入。Shopify 主要收购的是团队和品牌，创始人 Adam Wathan 此前已公开承认 AI 对业务的影响。

hackernews · EdwinHoksberg · 9月9日 13:27 · [社区讨论](https://news.ycombinator.com/item?id=49626190)

**背景**: Tailwind CSS 是一个 utility-first CSS 框架，允许开发者通过在 HTML 中直接组合小型、单一用途的类（如`bg-blue-600`或`p-4`）来为应用程序添加样式，而无需编写自定义 CSS。自推出以来，它已成为最受欢迎的 CSS 框架之一，与传统方法和 Bootstrap 等组件库竞争。该框架的文档站点历史上是开发者学习和查阅类的主要流量来源。如今，AI 编程助手通常已熟记 Tailwind 的类名，减少了开发者查阅官方文档的需求——这一转变在整个文档和开发者工具生态系统中已产生可衡量的商业影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tailwindlabs/tailwindcss">GitHub - tailwindlabs/tailwindcss: A utility-first CSS ... Styling with utility classes - Core concepts - Tailwind CSS Tailwind CSS: Utility-First Styling for Rapid UI Development Tailwind CSS - A Utility-First CSS Framework for Rapidly ... Tailwind CSS: The Utility-First Framework Explained What is Tailwind CSS? Utility-First Framework Guide 2026</a></li>
<li><a href="https://tailwindcss.com/docs/utility-first">Styling with utility classes - Core concepts - Tailwind CSS</a></li>
<li><a href="https://www.mintlify.com/blog/state-of-ai">The state of agent traffic in documentation (March 2026)</a></li>

</ul>
</details>

**社区讨论**: 社区讨论非常活跃（910 个赞，361 条评论），涉及多个角度。像 fg137 这样的评论者质疑，鉴于现代原生 CSS 特性的发展，Tailwind 是否仍然必要；而 pil0u 则认为它是帮助其提升工程能力的教育工具。讨论的主导主题是 AI 对开发者工具的影响：simonw 和 jedberg 强调，随着大语言模型取代文档查阅和模板购买，运营兼具开源和商业组件的 DevTools 公司正变得越来越困难，表明托管等规模化服务正成为生存的关键。

**标签**: `#tailwind`, `#shopify`, `#acquisition`, `#ai-impact`, `#developer-tools`, `#css`

---

<a id="item-8"></a>
## [GPT-6 Astra、循环 Transformer 与隐藏推理机制](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) ⭐️ 7.0/10

Sebastian Raschka 分析了新兴的人工智能趋势，包括关于 GPT-6 "Astra" 的传闻、循环 Transformer 架构，以及大语言模型中的隐藏推理机制。

hackernews · ModelForge · 9月9日 14:37 · [社区讨论](https://news.ycombinator.com/item?id=49627370)

**标签**: `#transformers`, `#LLM-architecture`, `#hidden-reasoning`, `#GPT-6`, `#AI-research`

---

<a id="item-9"></a>
## [Qwen 3.8 沿用了 GPT-5.5 Pro 的推理预填充模式](https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3) ⭐️ 7.0/10

技术分析显示 Qwen 3.8 遵循了 GPT-5.5 Pro 的推理预填充模式，暗示其可能从 OpenAI 的专有模型中进行了知识蒸馏。

hackernews · wsxiaoys · 9月9日 17:24 · [社区讨论](https://news.ycombinator.com/item?id=49630026)

**标签**: `#AI`, `#model-distillation`, `#Qwen`, `#OpenAI`, `#LLM-evaluation`

---

<a id="item-10"></a>
## [GNU Radio 通过 WebAssembly 移植到浏览器](https://gnuradioworld.com/) ⭐️ 7.0/10

GNU Radio 这一流行的开源软件定义无线电（SDR）框架已通过 WebAssembly（WASM）移植到网页浏览器中，无需本地安装即可进行信号处理工作流。 这大幅降低了 SDR 实验和学习的门槛，让任何拥有浏览器的人都能探索信号处理。结合用于硬件访问的 WebUSB 技术，它可以实现一个完整的 SDR 开发环境，在易用性方面有望媲美传统的桌面设置。 浏览器版本支持通过 WebUSB 连接到 USRP B200 等 SDR 硬件，并保留了 GNU Radio 熟悉的图形化流图界面用于构建信号处理流水线。社区项目展示了实际应用案例，包括宽带射频扫描、AX.25 分组无线电解码和 FM 接收，全部在浏览器中运行。

hackernews · kristianpaul · 9月9日 15:53 · [社区讨论](https://news.ycombinator.com/item?id=49628576)

**背景**: GNU Radio 是一个免费软件开发工具包，提供用于实现软件定义无线电的信号处理模块，传统上通过 Python 或 C++ 配合图形化流图编辑器使用。软件定义无线电（SDR）用软件取代传统的模拟无线电硬件电路，使通用计算机能够处理无线电信号。WebAssembly（WASM）是一种二进制指令格式，能在网页浏览器中实现接近原生的代码执行速度，使得 GNU Radio 等复杂应用程序无需安装即可运行。WebUSB 是一种浏览器 API，允许网页与 USB 设备通信，使基于浏览器的 SDR 工具能够直接与物理无线电硬件连接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GNU_Radio">GNU Radio - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software-defined radio - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly/Guides/Concepts">WebAssembly concepts - WebAssembly | MDN</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体上非常热情，用户展示了他们自己的基于浏览器的 SDR 项目，包括使用 WebUSB 连接 USRP B200 的宽带射频扫描仪、AX.25 分组解码器以及 FM 接收器。一位评论者将其与 MaxMSP 相提并论，并回忆起了信号处理课程，另一位则表示有兴趣重新尝试 GNU Radio，因为过去觉得它难以理解。一些批评意见指出着陆页的用户体验可以改进，可读性差且缺乏音频输出，使得新手初次体验时感到困惑。

**标签**: `#sdr`, `#gnuradio`, `#webassembly`, `#signal-processing`, `#browser`

---

<a id="item-11"></a>
## [安全研究员揭露恶意软件广告绕过 Google Ads 审核流程](https://xlii.space/eng/malicious-software-on-google-ads/) ⭐️ 7.0/10

一位安全研究员发布了一篇详细调查报告，记录了他们如何成功通过 Google Ads 投放恶意软件广告，证明了该平台的自动化审核和监管系统无法识别明显的恶意内容。在公开曝光并通过 Hacker News 获得关注后，该研究者的账户最终被恢复。 这一案例研究揭示了全球最大广告平台之一的实际弱点，在该平台上恶意广告可以直接危及信任 Google 品牌的终端用户。它引发了关于平台责任、过度依赖自动化审核以及在大型科技公司中难以挑战不透明算法决策的更广泛担忧。 Google Ads 使用包含自动化 AI 检查和可选人工审核的多阶段审核流程，但研究者的案例表明，明显恶意的广告在公共舆论迫使平台采取行动之前已被批准并投放。报告此问题的作者账户最初被封停，仅在该调查报告广泛传播后才得以恢复。

hackernews · xlii · 9月9日 11:43 · [社区讨论](https://news.ycombinator.com/item?id=49624856)

**背景**: 恶意广告（Malvertising）是“恶意软件”（malware）和“广告”（advertising）的合成词，指利用在线广告分发恶意软件或将用户引向有害网站的行为，即便用户不点击也可能感染系统。Google Ads 通过自动化 AI 检查和人工审核相结合的方式，对每条广告按照其广告政策进行审核，大多数广告由系统自动处理。本案揭示了一个反复出现的矛盾：平台通过自动化扩展内容审核规模，但恶意行为者——以及有时探测漏洞的合法研究者——可以在触发人工审核之前利用审核缺口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Malvertising">Malvertising - Wikipedia</a></li>
<li><a href="https://www.fortinet.com/resources/cyberglossary/malvertising">What is Malvertising and how to prevent it? | Fortinet</a></li>
<li><a href="https://support.google.com/google-ads/answer/1722120?hl=en">About the ad review process - Google Ads Help</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Google 的自动化流程表达了广泛的挫败感，并引用了与之无关的经历，例如合法的 Tesla 超级充电站提交被拒绝，以及 YouTube 上充斥大量诈骗广告。多位用户认为大型公司躲在自动化系统背后逃避责任，并呼吁通过监管要求企业设立人工联系渠道，以及建立更清晰的自动化决策申诉流程。研究者在评论中指出，仅有借助 Hacker News 放大的公开投诉才促使问题得到解决，进一步凸显了社区对缺乏有效反馈机制的担忧。

**标签**: `#security`, `#malvertising`, `#google-ads`, `#infosec`, `#platform-security`

---

<a id="item-12"></a>
## [LED 实现 5 米距离更安全的室内无线供电](https://www.eetimes.com/leds-push-wireless-power-further/) ⭐️ 7.0/10

东京科学大学的研究人员展示了一种基于 LED 的无线电力传输系统，该系统利用自适应光学和人工智能波束控制技术，可在 5 米距离内向室内物联网设备供电。这种方法为基于激光的光学无线电力传输方式提供了一种替代方案。 这项研究具有重要意义，因为基于 LED 的光学无线供电在室内使用上本质上比基于激光的系统更安全——LED 产生的是扩散的、较低强度的光束，对人眼和皮肤的危害较小。在室内实现 5 米的实用充电距离，可以显著扩大无电池物联网传感器、智能家居设备以及其他目前需要电池或有线连接的低功耗电子设备的部署场景。 该系统将自适应光学（通常用于天文学中通过可变形镜或液晶阵列校正大气畸变）与人工智能驱动的波束控制相结合，以将 LED 光线精确导向接收器。虽然基于激光的系统已展示更长的传输距离（接近 100 英尺），但在室内使用时存在安全隐患；LED 方法在功率密度和传输距离上有所牺牲，以换取更好的人体安全性。

rss · EE Times · 9月9日 20:00

**背景**: 光学无线电力传输（OWPT）使用定向光源（通常是激光二极管）向远程设备输送能量，在某些应用场景中比基于射频的无线充电具有优势。激光可以高效地长距离传输电力，但存在眼睛安全风险，这限制了它们在室内环境中的使用。自适应光学最初是为天文望远镜开发的，可以实时测量和补偿波前畸变，现在正被重新用于维护激光和 LED 电力传输系统的光束质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eetimes.com/leds-push-wireless-power-further/">LEDs Push Wireless Power Further - EE Times</a></li>
<li><a href="https://en.wikipedia.org/wiki/Adaptive_optics">Adaptive optics - Wikipedia</a></li>
<li><a href="https://www.allaboutcircuits.com/news/researchers-achieve-wireless-power-transfer-nearly-100-feet-using-laser/">Researchers Achieve Wireless Power Transfer Nearly 100 Feet Using...</a></li>

</ul>
</details>

**标签**: `#wireless-power`, `#IoT`, `#LED`, `#beam-steering`, `#energy-harvesting`

---

<a id="item-13"></a>
## [苹果全线 iPhone 涨价 100 美元，DRAM 短缺推高成本](https://www.techpowerup.com/352538/apple-raises-prices-across-the-iphone-lineup-as-dram-costs-catch-up) ⭐️ 6.5/10

苹果在 9 月 9 日发布 iPhone 18 Pro 之际，将其全系 iPhone 价格上调了 100 美元，包括 iPhone 18 Pro 起售价 1,199 美元、iPhone 18 Pro Max 起售价 1,299 美元、iPhone 16 起售价 799 美元、iPhone 17e 起售价 699 美元、iPhone 17 起售价 899 美元以及 iPhone Air 起售价 1,099 美元，老款机型并未获得任何硬件升级。 这一定价决定表明，由 AI 驱动的内存短缺已开始直接影响全球市值最高的智能手机厂商的消费电子产品定价，说明即使是苹果也无法让消费者免受不断上涨的 DRAM 成本影响。此举与华硕等 PC OEM 厂商已面临的 DRAM 和 SSD 涨价潮如出一辙，反映出 AI 基础设施需求正在重塑消费硬件可负担性这一更广泛的行业趋势。 苹果 CEO 蒂姆·库克将内存短缺比作"百年一遇的洪水"，并表示苹果已无法像以前那样消化不断上涨的内存和存储成本；值得注意的是，价格上涨统一适用于所有老款机型，而这些机型并未获得任何相应的硬件升级。

rss · TechPowerUp News · 9月9日 23:41

**背景**: DRAM（动态随机存取内存）是智能手机和电脑中用于临时数据处理的核心组件。当前的全球短缺主要由 AI 数据中心需求驱动——训练集群中的每个 GPU 节点可能消耗数百 GB 的 DRAM，而超大规模数据中心园区部署着数万台此类服务器。随着内存供应商将晶圆和封装产能转向面向 AI 应用的高带宽内存（HBM）和服务器 DRAM，可用于消费级内存的产能减少，推高了整个行业的价格。行业分析师警告称，这一短缺可能持续到 2027 年甚至更久。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/storage/perfect-storm-of-demand-and-supply-driving-up-storage-costs">AI data centers are swallowing the world's memory and storage supply, setting the stage for a pricing apocalypse that could last a decade | Tom's Hardware</a></li>
<li><a href="https://aitocore.com/en/news/global-ai-memory-shortage-hbm-dram-crisis">Global HBM and DRAM Shortage Due to AI Demand - AitoCore</a></li>
<li><a href="https://www.ramexchange.net/blog/ram-demand-surge-due-to-ai">RAM Demand Surge Due to AI: How Data Centers Are Reshaping Global Memory Markets — Ram Exchange</a></li>

</ul>
</details>

**标签**: `#Apple`, `#iPhone`, `#DRAM`, `#semiconductor-shortage`, `#AI-infrastructure`

---

<a id="item-14"></a>
## [1900 名暴雪员工签署工会合同，涉及生成式 AI、裁员及远程办公](https://www.techpowerup.com/352519/1-900-blizzard-workers-secure-union-contract-covering-gen-ai-layoffs-and-remote-work) ⭐️ 6.5/10

美国通信工人工会批准了一项新的工会合同，覆盖近 1900 名暴雪员工，涉及生成式 AI、裁员和混合远程办公等方面的保障措施。

rss · TechPowerUp News · 9月9日 18:00

**标签**: `#labor-unions`, `#gaming-industry`, `#gen-ai-policy`, `#blizzard`, `#workplace-rights`

---

<a id="item-15"></a>
## [苹果发布 iPhone 18 Pro 和 Pro Max，搭载可变光圈](https://www.techpowerup.com/352523/apple-debuts-iphone-18-pro-and-iphone-18-pro-max) ⭐️ 6.5/10

苹果正式发布 iPhone 18 Pro 和 iPhone 18 Pro Max，配备 4800 万像素可变光圈 Fusion 主摄、全新 A20 Pro 芯片、新一代蒸汽腔散热系统，以及搭载 Apple Intelligence 的 iOS 27。预购将于 9 月 12 日（周六）开启，9 月 18 日（周五）正式上市。 此次发布表明苹果在持续推进专业级移动影像的同时，通过蒸汽腔散热技术解决了长期存在的散热和续航瓶颈。可变光圈则打破了多年来智能手机行业普遍采用固定光圈的设计格局，是一个重要的技术转折点。 iPhone 18 Pro Max 宣称实现了 iPhone 史上最大幅度的电池续航提升，新增酒红色配色，与黑色、银色、冰川色共同构成四种配色方案。可变光圈支持对进光量和景深的物理控制，而蒸汽腔散热则旨在实现苹果迄今为止最高的持续性能输出。

rss · TechPowerUp News · 9月9日 17:55

**背景**: 可变光圈摄像头通过物理方式调节进入镜头的光量，让摄影师可以手动控制曝光和景深——这一功能长期以来仅限于传统相机，直至近年才被华为 Mate 50 Pro、三星 Galaxy S9 等少数智能手机采用。蒸汽腔散热的原理是利用密封腔体内的液体蒸发与凝结，将处理器产生的热量均匀扩散出去，从而实现更高的持续性能而不会触发降频。Dynamic Island 是苹果自 iPhone 14 Pro 开始用以取代刘海屏的药丸形交互显示区域，可展示通知和实时活动（Live Activities）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://refurbo.in/blogs/variable-aperture-smartphone-cameras-marketing-gimmick-or-useful-feature">Variable Aperture Smartphone Cameras Guide</a></li>
<li><a href="https://tonecooling.com/vapor-chamber-on-phones/3/">Vapor Chamber on Phones : Cooling Technology for Smartphones</a></li>
<li><a href="https://www.macrumors.com/how-to/use-dynamic-island-iphone-14-pro/">What iPhone's Dynamic Island Does and How to Use It 9 Surprisingly Useful Things the iPhone's Dynamic Island Can ... View Live Activities in the Dynamic Island on iPhone iPhone 18 Pro’s New Dynamic Island Tracks 3 Activities at ... Dynamic Island on iPhone: Everything You Need to Know ... Everything You Need to Know About Dynamic Island - MacRumors How to Use Dynamic Island on iPhone - SimplyMac</a></li>

</ul>
</details>

**标签**: `#Apple`, `#iPhone`, `#mobile hardware`, `#product launch`, `#smartphones`

---

<a id="item-16"></a>
## [HP 推出搭载 NVIDIA GB300 和 Red Hat 的 ZGX Fury AI 工作站](https://www.techpowerup.com/352521/hp-launches-zgx-fury-ai-station-powered-by-nvidia-gb300-grace-blackwell-and-red-hat) ⭐️ 6.5/10

惠普（HP）宣布推出 ZGX Fury AI 工作站，这是一款与 Red Hat 联合开发、搭载 NVIDIA GB300 Grace Blackwell 芯片的企业级 AI 平台，可为本地推理工作负载提供高达 20 PFLOPS 的 FP4 AI 性能。 此次发布将 NVIDIA 下一代 Blackwell Ultra 架构引入预集成的惠普企业工作站，并搭配 Red Hat 的混合云软件栈，为企业提供了一条开箱即用的本地 AI 推理路径，减少对云端 GPU 的依赖。 该工作站以 Red Hat Enterprise Linux 和 Red Hat OpenShift 为基础，通过优化的 CUDA 库和多 GPU 工作负载编排来最大化 GPU 利用率；FP4（特别是 NVIDIA 的 NVFP4 变体）可在保持精度的同时实现大规模超低精度推理。

rss · TechPowerUp News · 9月9日 17:28

**背景**: NVIDIA GB300 属于 Blackwell Ultra 一代，取代 GB200，提供包括原生 FP4 吞吐量在内的增强 Tensor Core 性能。FP4（4 位浮点）是深度学习中主流使用的最小浮点格式，相比 FP16 或 FP8 可大幅降低内存和计算需求。Red Hat AI Factory with NVIDIA 是一个联合工程平台，将 Red Hat AI Enterprise 与 NVIDIA AI Enterprise 软件相结合，基于 RHEL 和 OpenShift 构建，旨在跨混合云环境标准化 AI 工作负载部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gpusmith.com/hardware/systems/nvidia-gb300-nvl72">NVIDIA GB 300 NVL72 Specs & Procurement | GPU Smith</a></li>
<li><a href="https://www.nvidia.com/en-us/solutions/ai-factories/red-hat/">Red Hat AI Factory with NVIDIA for the Hybrid Cloud | NVIDIA</a></li>
<li><a href="https://aiwiki.ai/wiki/fp4">FP4 (4-bit floating point) - AI Wiki</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#NVIDIA Blackwell`, `#HP`, `#Red Hat`, `#enterprise AI`

---

<a id="item-17"></a>
## [CXMT HBM3E 良率仅 25%，TSV 技术不成熟为主因](https://www.techpowerup.com/352511/cxmt-reportedly-struggles-with-hbm3e-yields-are-only-25) ⭐️ 6.5/10

据报道，中国存储芯片制造商长鑫存储（CXMT）的 HBM3E 风险量产良率仅为 25%，即每四个堆叠中有三个存在缺陷。低良率归因于不成熟的硅通孔（TSV）技术——CXMT 每层仅使用约 3,000 个 TSV，而 SK 海力士在 HBM3 中每层使用超过 8,000 个。 这则报道凸显了中国在先进存储封装技术方面持续落后的现状，而这些技术对 AI 加速器和高性能 GPU 至关重要。CXMT 仍落后于三星、SK 海力士和美光两代，后者已在送样 HBM4E，这可能制约中国本土 AI 硬件的发展，并加深其对国外 HBM 供应的依赖。 CXMT 的前端制造良率约为 30%，后端封装在此基础上再产出约 70%的良率，两者叠加后形成总体 25%的良率。该公司目前瞄准标准的 8-Hi HBM3E 配置，即 8 层堆叠、每层 3,000 个 TSV，短期内不太可能转向 12-Hi 堆叠，因为仍需解决工程难题。

rss · TechPowerUp News · 9月9日 14:59

**背景**: HBM3E（高带宽存储器第三代扩展版）是最新一代堆叠 DRAM 内存，主要用于 AI 加速器和高性能计算。它采用硅通孔（TSV）技术——穿过硅裸片的垂直电气连接——来堆叠多层 DRAM，每一代通常需要更多 TSV 以提供更高带宽。风险量产是一种小批量制造阶段，在此阶段制造完整晶圆的单芯片设计以验证性能并优化良率，随后才进入大规模量产。三星、SK 海力士和美光主导全球 HBM 市场，且已在推进 HBM4E 送样，使 CXMT 在这一关键的 AI 供应链环节大幅落后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Through-silicon_via">Through - silicon via - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Risk_production_semiconductors">Risk production (semiconductors) — Grokipedia</a></li>

</ul>
</details>

**标签**: `#HBM3E`, `#CXMT`, `#semiconductor manufacturing`, `#AI hardware`, `#memory technology`

---

<a id="item-18"></a>
## [LG 强烈否认涉及 2.16 亿台电视的间谍指控](https://www.tomshardware.com/tech-industry/big-tech/lg-strongly-denies-tv-security-claims-says-tracking-and-snooping-concerns-not-true-online-investigation-claims-216-000-000-spy-tvs-record-audio) ⭐️ 6.5/10

LG 对其智能电视存在隐蔽跟踪和录音行为的安全与隐私指控发表了强烈否认，称这些说法"不属实"。此次否认是对一项网络调查的回应，该调查声称多达 2.16 亿台 LG 电视在未充分告知用户的情况下窃取隐私并捕获音频。 这场争议凸显了智能电视制造商与消费者隐私倡导者之间持续的紧张关系，尤其是在观看数据被收集的程度以及用户是否被适当告知方面。如果这些指控属实，可能会影响数亿家庭，并引发多个司法管辖区对物联网隐私的监管审查。 智能电视通常使用自动内容识别（ACR）技术，这是一种类似 Shazam 的指纹识别方法，定期捕获屏幕显示内容以分析用户观看习惯，用于精准广告投放。据报道，该调查的 2.16 亿台电视数据基于汇总的遥测数据，而 LG 已公开质疑该统计方法及其对自身数据实践的定性。

rss · Tom's Hardware · 9月9日 11:50

**背景**: 自动内容识别（ACR）是一种嵌入在大多数现代智能电视中的跟踪技术，通过定期采样屏幕上显示的内容并与内容数据库进行比对来确定用户观看的内容。这些数据随后被用于构建详细的观众画像，以进行精准广告投放和跨平台测量。智能电视和其他物联网消费设备是众所周知的隐私问题领域，因为它们往往缺乏自动安全更新、可能向多个第三方传输数据，并且其隐私设置通常难以被普通用户找到和配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_content_recognition">Automatic content recognition - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2409.06203v1">Watching TV with the Second-Party: A First Look at Automatic Content Recognition Tracking in Smart TVs</a></li>
<li><a href="https://www.cyber.nj.gov/guidance-and-best-practices/device-security/iot-device-security-and-privacy">IoT Device Security and Privacy | NJCCIC - NJ.gov</a></li>

</ul>
</details>

**标签**: `#privacy`, `#smart-tv`, `#lg`, `#iot-security`, `#consumer-electronics`

---

<a id="item-19"></a>
## [OpenAI 称 GPT‑6 Astra 具类 AGI 能力但仍有常见弱点](https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-claims-gpt-6-astra-is-an-ethereal-alien-mind-with-agi-like-qualities-company-warns-of-alignment-challenges-as-new-frontier-leader-emerges) ⭐️ 6.5/10

OpenAI 发布了 GPT‑6 Astra，并称其为目前最智能、最对齐的模型，在计算机操作、编程、网络安全和科学领域具备领先能力。报道援引的基准测试同时显示，该模型仍存在大语言模型的常见弱点，OpenAI 也承认对齐挑战尚未解决。 所提供的信息没有列出具体基准测试分数、失败类型、价格或访问权限，因此难以量化 GPT‑6 Astra 声称提升的实际幅度。OpenAI 将其宣传为能力最强且最对齐的系统，但报道强调其仍存在典型缺陷，说明更强的通用能力并不能消除可靠性与安全问题。

rss · Tom's Hardware · 9月9日 11:20

**背景**: 大语言模型是经过训练后能够处理和生成语言的模型，而基准测试使用标准化指标评估其能力、安全性与可靠性。“类 AGI 能力”描述的是看似接近广泛通用智能的行为，但这一说法本身不能证明系统已经实现 AGI。AI 对齐旨在确保模型遵循设计者和用户的意图与价值观，常用评估方法包括人工反馈、对抗测试、红队测试和宪法式方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://arxiv.org/abs/2507.19672">[2507.19672] Alignment and Safety in Large Language Models ... AI Alignment Challenges in Large Language Models: Technical ... Evaluating alignment in large language models: a review of ... Evaluating alignment in large language models: a review of ... Increasing alignment of large language models with language ... Alignment and Safety in Large Language Models: Safety ...</a></li>
<li><a href="https://www.databricks.com/blog/best-practices-and-methods-llm-evaluation">Best Practices and Methods for LLM Evaluation - Databricks</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#AGI`, `#AI-alignment`, `#LLM-benchmarks`

---

<a id="item-20"></a>
## [Arm 发布 Neoverse CSS N4，面向下一代 CPU 与 DPU](https://www.servethehome.com/arm-neoverse-css-n4-launched-for-next-gen-cpus-and-dpus/) ⭐️ 6.5/10

Arm 正式发布全新的 Neoverse CSS N4 计算子系统 IP，这是一款预集成、可配置的数据中心 CPU 平台，每颗裸片支持 8 至 128 个核心，并兼容 LPDDR6 内存与 PCIe Gen 7 I/O，使合作伙伴能够快速构建面向 AI、云和网路负载的自定义 CPU 与 DPU。 Arm 提供的并非原始 IP 核，而是一套经过预验证的子系统，这大幅缩短了超大规模云厂商和芯片厂商推出定制 Arm 数据中心芯片所需的开发周期与工程投入，从而在 AI 服务器与 DPU 领域进一步加剧了与 x86 阵营的竞争。 CSS N4 支持最大 256 MB 共享 L3 缓存与 128 GT/s 的 PCIe 7.0（该规范已于 2025 年 6 月由 PCI-SIG 正式发布），并且该平台原生面向定制 Agentic AI 与 DPU 芯片，而非仅限于通用服务器 CPU。

rss · ServeTheHome · 9月9日 17:10

**背景**: Arm Neoverse 是 Arm 面向数据中心、网络与基础设施负载的 CPU IP 产品线。Compute Subsystem（CSS）将 CPU 核、互连、内存控制器与 I/O 整合为一个经过预验证的整体，使客户无需从零开始重新设计这些模块即可构建定制芯片。DPU（数据处理单元）是一类专用处理器，用于将网络、存储和安全任务从主 CPU 上卸载。PCIe 7.0 是外围组件互连标准的最新一代，相较 PCIe 6.0 带宽翻倍，达到 128 GT/s。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://convergedigest.com/arm-neoverse-css-n4-custom-ai-silicon/">Arm Pushes Custom AI Silicon Forward with Neoverse CSS N 4</a></li>
<li><a href="https://www.phoronix.com/news/PCI-Express-7.0-PCIe-7.0">PCI Express 7.0 Final Specification Published ... - Phoronix</a></li>
<li><a href="https://www.techtarget.com/searchdatacenter/tip/How-do-CPU-GPU-and-DPU-differ-from-one-another">How do CPU, GPU and DPU differ from one another? - TechTarget</a></li>

</ul>
</details>

**标签**: `#Arm`, `#Neoverse`, `#data-center`, `#semiconductor`, `#PCIe-Gen7`

---