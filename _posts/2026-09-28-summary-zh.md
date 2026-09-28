---
layout: default
title: "Horizon Summary: 2026-09-28 (ZH)"
date: 2026-09-28
lang: zh
---

> 从 86 条内容中筛选出 20 条重要资讯。

---

1. [Anthropic 发布 Claude Sonnet 5.5，性能提升并增加安全限制](#item-1) ⭐️ 9.0/10
2. [台积电将 2nm 产能提升：2026 年底前增至 120,000 片](#item-2) ⭐️ 8.5/10
3. [谷歌确认 2034 年停止 ChromeOS 以过渡到 Googlebook OS](#item-3) ⭐️ 8.5/10
4. [North Korea named as primary suspect in $387 million Bitget crypto hack](#item-4) ⭐️ 8.5/10
5. [PS5 Emulator SharpEmu Reaches Gameplay In 17 Games, 8 Run at 60 FPS](#item-5) ⭐️ 7.5/10
6. [Synopsys 推出 Autopilot 平台，利用 AI 自主开发芯片](#item-6) ⭐️ 7.5/10
7. [OpenAI 自研 Jalapeno AI 推理 ASIC 仅供内部使用，但为未来更广泛推广留有余地](#item-7) ⭐️ 7.5/10
8. [青少年利用 JWT 漏洞访问海量微软数据库](#item-8) ⭐️ 7.5/10
9. [研究发现 PS5 流媒体传输未加密](#item-9) ⭐️ 7.0/10
10. [Scrimba 推出 HN.watch，可即时生成由 LLM 驱动的解释视频](#item-10) ⭐️ 7.0/10
11. [TEC raises $450m Series C for reusable spacecraft](#item-11) ⭐️ 7.0/10
12. [imec IC-Link 联手台积电，简化先进工艺节点接入流程](#item-12) ⭐️ 7.0/10
13. [玩家用 Armada 项目将安卓掌机改装成迷你 Steam Deck](#item-13) ⭐️ 6.5/10
14. [（公关）VSMC 在圣路易斯庆祝其首个 300 毫米晶圆厂正式启动](#item-14) ⭐️ 6.5/10
15. [两款雷电 5 M.2 存储扩展坞的性能对比](#item-15) ⭐️ 6.5/10
16. [Parley: Federated, decentralised chat that speaks plain IRC](#item-16) ⭐️ 6.0/10
17. [MongoDB CEO resigns to join Meta](#item-17) ⭐️ 6.0/10
18. [美欧合作对全球量子技术领导地位至关重要](#item-18) ⭐️ 6.0/10
19. [Calterah 利用 UWB 无钥匙进入硬件实现舱内传感](#item-19) ⭐️ 6.0/10
20. [Xcena MX1 利用 CXL 和 RISC-V 解决内存瓶颈](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Sonnet 5.5，性能提升并增加安全限制](https://www.anthropic.com/claude-sonnet-5-5) ⭐️ 9.0/10

Anthropic 发布了 Claude Sonnet 5.5，这是其 Sonnet 系列中在高性能和成本效益之间取得新平衡的模型。此次发布立即引发了关于其令牌效率及与更高级别 Opus 5.5 模型基准对比的技术分析。 此次发布意义重大，因为它为需要强大功能但又不想支付 Opus 级别高额费用的开发者提供了高性价比的选择。它还凸显了在原始基准测试分数与令牌使用和计算资源方面的实际效率之间的平衡。 在 Terminal-Bench 测试中，Sonnet 5.5 获得了 70.6 分，超过了 Opus 5.5 的 66.4 分，但较高的得分可能受到 Opus 因安全限制导致 10% 回退模型率（相比之下 Sonnet 仅为 1.5%）的影响。此外，由于网络攻击（cyber）能力大幅提升，该模型还需要类似于 Opus 5.5 的安全限制。

hackernews · D2OQZG8l5BI1S06 · 9月28日 17:58 · [社区讨论](https://news.ycombinator.com/item?id=49881850)

**背景**: Anthropic 的模型层级通常按能力和成本分类，其中 Opus 是最先进且最昂贵的，而 Sonnet 则作为中端选项平衡了性能和价格。在大语言模型（LLM）推理中，令牌效率是一个关键指标，因为需要更多“思考”令牌来解决问题的模型会占用更多的时间和资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude Platform Docs</a></li>
<li><a href="https://www.cosmicjs.com/blog/claude-sonnet-45-vs-opus-45-a-real-world-comparison">Claude Sonnet 4.5 vs Opus 4.5: Which to Use - Cosmic JS</a></li>
<li><a href="https://dev.to/dr_hernani_costa/claude-ai-models-2025-opus-vs-sonnet-vs-haiku-guide-24mn">Claude AI Models 2025: Opus vs Sonnet vs Haiku Guide - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 社区分析聚焦于令牌效率，指出在较高的“思考”努力级别下，模型在完成复杂任务前可能会耗尽 128,000 个思考令牌的限制。评论者也质疑了 Sonnet 在基准测试中超越 Opus 的优势，并指出 Opus 较高的回退率可能扭曲了结果。此外，用户强调了成本问题，一些人指出该模型比竞争对手贵得多。

**标签**: `#LLM`, `#Anthropic`, `#AI-Releases`, `#Benchmarks`, `#Cost-Performance`

---

<a id="item-2"></a>
## [台积电将 2nm 产能提升：2026 年底前增至 120,000 片](https://www.techpowerup.com/353153/tsmc-to-scale-2-nm-production-to-120-000-wafers-per-month-by-the-end-of-2026) ⭐️ 8.5/10

台积电正将 2 纳米 N2 制程的产能扩大 20%，目标在 2026 年底前达到每月 120,000 片晶圆。这相较于八月初设定的 100,000 片目标有所上调，以应对激增的客户订单需求。 产能的大幅增加表明市场对 AI 和高端芯片的领先需求已超出全球供给能力。N2 产能的扩大将有助于稳定苹果、AMD 等主要客户的供应链，并推动更广泛的科技进步。 台积电表示，N2 节点的流片（tape-out）数量是前代 3 纳米 N3 节点的 4 倍。截至 2026 年第二季度，N2 占营收仅 3%，而 3nm 和 5nm 分别占 30%和 33%，但预计至第三季度末，N2 的占比将大幅上升。

rss · TechPowerUp News · 9月28日 11:22

**背景**: 台积电的 2 纳米 N2 制程是一项重大里程碑，它引入了全环绕栅极（GAA）晶体管技术，以取代以往的设计，从而提升性能和能效。所谓“流片（tape-out）”是指芯片设计的最终步骤，即将蓝图发送给代工厂进行生产。代工厂以“每月晶圆片数（wpm）”来衡量产能，这决定了它们满足全球芯片需求的快慢。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.arenasolutions.com/resources/glossary/tape-out/">Tape - Out in Semiconductor Manufacturing: Definition , Process & PLM</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#tsmc`, `#manufacturing`, `#2nm`, `#hardware-supply`

---

<a id="item-3"></a>
## [谷歌确认 2034 年停止 ChromeOS 以过渡到 Googlebook OS](https://www.tomshardware.com/laptops/google-confirms-chromeos-phase-out-in-2034-10-year-support-lifetime-cut-short-for-some-devices-company-says-it-will-support-transition-to-googlebook-os) ⭐️ 8.5/10

谷歌官方确认将于 2034 年逐步停止对 ChromeOS 的更新支持。与此同时，公司正转向新的“Googlebook OS”战略，这将推出新款笔记本电脑，并导致部分现有 Chromebook 型号的支持寿命缩短。 这一行业决策对依赖 ChromeOS 平台的硬件制造商、企业用户和开发者产生重大影响。它标志着在教育和企业领域最主流的操作系统之一发生重大生命周期转变。 一个值得注意的运营细节是，由于此次过渡，部分设备原本 10 年的支持寿命将会缩短。谷歌已声明将支持向新操作系统的过渡过程。

rss · Tom's Hardware · 9月28日 16:38

**背景**: ChromeOS 是谷歌开发的一种操作系统，主要专为 Chromebook 设计，这是一种主要依赖基于 Web 的应用程序的轻量级笔记本电脑。转向“Googlebook OS”代表了该生态系统在市场成熟过程中的重新定位和战略演变。

**标签**: `#ChromeOS`, `#Google`, `#Operating Systems`, `#Hardware Support`, `#Industry News`

---

<a id="item-4"></a>
## [North Korea named as primary suspect in $387 million Bitget crypto hack](https://www.tomshardware.com/tech-industry/cryptocurrency/north-korea-named-as-primary-suspect-in-usd387-million-bitget-crypto-hack-investigators-identify-ip-addresses-tied-to-vpn-infrastructure-previously-used-by-north-korean-hacker-groups-thieves-swapped-stablecoins-for-eth-in-minutes-to-dodge-freezes) ⭐️ 8.5/10

Investigators attribute a $387 million hack on the Bitget exchange to North Korean state-backed actors who exploited VPN infrastructure and rapidly converted stolen stablecoins to Ethereum to avoid asset freezes.

rss · Tom's Hardware · 9月28日 12:00

**标签**: `#cybersecurity`, `#cryptocurrency`, `#state-sponsored-attacker`, `#bitcoin-hack`, `#forensics`

---

<a id="item-5"></a>
## [PS5 Emulator SharpEmu Reaches Gameplay In 17 Games, 8 Run at 60 FPS](https://www.techpowerup.com/353152/ps5-emulator-sharpemu-reaches-gameplay-in-17-games-8-run-at-60-fps) ⭐️ 7.5/10

The experimental PS5 emulator SharpEmu has updated its compatibility list to show 17 games with gameplay capability, including 8 titles running at 60 FPS.

rss · TechPowerUp News · 9月28日 11:07

**标签**: `#PS5 Emulation`, `#SharpEmu`, `#Systems Research`, `#Gaming`, `#Rapid Progress`

---

<a id="item-6"></a>
## [Synopsys 推出 Autopilot 平台，利用 AI 自主开发芯片](https://www.tomshardware.com/tech-industry/semiconductors/synopsys-debuts-autopilot-platform-for-developing-chips-autonomously-using-ai-new-agentengineer-platform-is-poised-for-general-availability-by-the-end-of-2026) ⭐️ 7.5/10

Synopsys 推出了 Autopilot 平台，该平台具备七个 AgentEngineer AI 智能体，旨在实现芯片开发的自动化，预计将于 2026 年底正式可用。

rss · Tom's Hardware · 9月28日 16:35

**标签**: `#EDA`, `#AI Agents`, `#Semiconductors`, `#Synopsys`, `#Chip Design`

---

<a id="item-7"></a>
## [OpenAI 自研 Jalapeno AI 推理 ASIC 仅供内部使用，但为未来更广泛推广留有余地](https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-custom-jalapeno-ai-inference-asic-is-for-openais-internal-use-but-company-leaves-the-door-open-to-broader-rollout-firm-says-it-will-have-its-hands-full-with-jalapeno-for-a-good-long-time) ⭐️ 7.5/10

OpenAI 正优先考虑将自研的 Jalapeño 推理 ASIC 用于内部运营，但仍保留了未来进行更广泛部署的可能性。

rss · Tom's Hardware · 9月28日 15:45

**标签**: `#AI Hardware`, `#Custom ASIC`, `#OpenAI`, `#Inference`, `#Compute Infrastructure`

---

<a id="item-8"></a>
## [青少年利用 JWT 漏洞访问海量微软数据库](https://www.tomshardware.com/tech-industry/cyber-security/teenager-hacks-open-microsoft-database-with-17-trillion-total-rows-and-25-000-user-accounts-custom-ai-bot-and-lack-of-jwt-token-validation-yields-a-fruitful-trove-earns-usd5-000-bug-bounty) ⭐️ 7.5/10

一名青少年发现由于缺乏 JWT 令牌验证而存在的安全漏洞，成功访问了包含 17 万亿行数据和 25,000 个用户账户的微软数据库。该用户利用自定义 AI 机器人利用此漏洞，并获得了 5000 美元的漏洞赏金。 此事件强调了企业系统中适当的 API 安全和身份管理的重要性，表明像缺少令牌验证这样的单一疏忽可能导致海量数据泄露。它为企业组织在需要强化安全测试方面提供了警示。 该漏洞涉及特定方面 JWT 令牌验证的缺失，这导致了未经授权的访问到大量数据集。研究人员使用了自定义 AI 机器人来导航和访问数据库。

rss · Tom's Hardware · 9月28日 11:00

**背景**: JSON Web Token（JWT）是一种紧凑的、可安全用于 URL 的格式，用于在各方之间表示需要传输的声明。在安全的 Web 应用程序中，JWT 用于身份验证，这意味着有效的令牌证明了用户的身份。未能正确验证这些令牌是一个常见但严重的安全错误，可能会导致数据库和敏感系统向未授权访问开放。

**标签**: `#cybersecurity`, `#jwt`, `#vulnerability`, `#microsoft`, `#api-security`

---

<a id="item-9"></a>
## [研究发现 PS5 流媒体传输未加密](https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/) ⭐️ 7.0/10

研究发现 PS5 使用未加密的 RTMP 传输视频数据，存在被拦截的风险。 这突显了硬件流媒体管道中存在的安全漏洞，并引发对 2026 年数据隐私的担忧。 未加密的流允许拦截视频数据，并可能导致凭证被篡改。

hackernews · ibobev · 9月28日 15:35 · [社区讨论](https://news.ycombinator.com/item?id=49879702)

**背景**: RTMP 是一种常用于通过互联网传输实时视频的协议。在未加密的情况下使用（即使用 RTMP 而非 RTMPS），数据将以明文传输，使其容易受到本地或公共网络上的数据包嗅探和中间人攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dacast.com/blog/rtmps-streaming/">What is RTMPS and Why is it Important to Secure Streaming?</a></li>
<li><a href="https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/">Hijacking the PS5's RTMP Stream</a></li>

</ul>
</details>

**社区讨论**: 评论者对 2026 年仍在使用未加密协议表示担忧，并指出了潜在的被利用漏洞。

**标签**: `#security`, `#ps5`, `#rtmp`, `#reverse-engineering`, `#hardware`

---

<a id="item-10"></a>
## [Scrimba 推出 HN.watch，可即时生成由 LLM 驱动的解释视频](https://hn.watch/) ⭐️ 7.0/10

Hacker News 用户正在探索“HN.watch”，这是 Scrimba 开发的一款工具，它利用 LLM 和基于 HTML 的渲染即时生成任何文章的解释视频。该工具在用户首次点击链接时即时处理请求，以生成视频内容。 通过将视频制作从“美元和分钟”转变为“美分和秒”，该工具解锁了自动解释 Pull Request 或将文档转换为视频等新的用例。它表明，与传统扩散模型相比，AI 驱动的 HTML 渲染在快速内容生成方面具有极高的成本效益。 该服务每个视频的成本约为 0.04 美元，如果涉及图像生成，成本会显著增加。它利用了开源编程语言 Imba 和自定义同步引擎，同时依赖 Gemini、GPTs 和 ElevenLabs 等模型来实现 AI 功能。

hackernews · mrborgen · 9月28日 15:16 · [社区讨论](https://news.ycombinator.com/item?id=49879401)

**背景**: 传统的 AI 视频生成通常依赖基于像素的扩散模型，计算成本高且速度慢。Scrimba 的方法使用专为交互式编程教育设计的基于 HTML 的视频格式，将视频视为 LLM 可以编写和执行的代码。该方法以视觉真实感换取极高的速度和低成本，从而允许快速、可编辑的输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scrimbaguide.tech/blog/scrimba-explain-review/">What Is Scrimba Explain ? The AI Explainer, Tested... | Scrimba Guide</a></li>
<li><a href="https://github.com/showlab/Awesome-Video-Diffusion">GitHub - showlab/Awesome-Video-Diffusion: A curated list of ... Video diffusion generation: comprehensive review and open ... DiffusionRenderer [2312.01409] Generative Rendering: Controllable 4D-Guided ... Diffusion Models for Video Generation | Lil'Log - GitHub Pages</a></li>

</ul>
</details>

**社区讨论**: 社区情感褒贬不一，部分用户更偏好文本而非 AI 生成的视频，但也承认其对偏好视频人群的价值。一位评论者强调了用于对齐语音和动画的开源框架“videowright”，另一位则建议将 Opus 5.5 视为该技术的转折点。

**标签**: `#LLM`, `#Video Generation`, `#HTML5`, `#Automation`, `#Open Source`

---

<a id="item-11"></a>
## [TEC raises $450m Series C for reusable spacecraft](https://www.electronicsweekly.com/news/business/finance/tec-raises-450m-series-c-for-reusable-spacecraft-2026-09/) ⭐️ 7.0/10

The Exploration Company (TEC), a European startup focused on reusable spacecraft, has raised $450 million in a Series C funding round.

rss · Electronics Weekly · 9月28日 15:18

**标签**: `#Space Industry`, `#Venture Capital`, `#Reusable Rocketry`, `#Aerospace`

---

<a id="item-12"></a>
## [imec IC-Link 联手台积电，简化先进工艺节点接入流程](https://www.electronicsweekly.com/news/business/ic-link-by-imec-simplifies-access-2026-09/) ⭐️ 7.0/10

imec 的设计服务提供商 IC-Link 正在与台积电合作，简化客户对先进节点半导体设计能力的接入流程。这项合作伙伴关系将 imec 在 ASIC 和硅光子学领域的专业知识与台积电的制造平台相结合。 通过弥合复杂的尖端制造与设计服务之间的差距，此次合作降低了公司开发定制芯片的入门门槛。它加速了先进半导体的开发周期，惠及更广泛的工业和技术提供商。 该计划专门针对 ASIC 和硅光子学领域，利用台积电作为此接入平台的新成员。重点在于简化利用最先进节点能力所需的技术和后勤步骤。

rss · Electronics Weekly · 9月28日 05:11

**背景**: 在半导体行业中，先进节点的接入通常需要直接管理代工厂复杂的工艺套件和严格的流程规范。imec 是一家领先的研究和技术合作伙伴，通常充当基础研究与商业制造之间的桥梁。IC-Link 作为专门管理这些设计流程的分支部门，确保客户能高效地应对代工厂的要求。

**标签**: `#Semiconductor`, `#TSMC`, `#imec`, `#ASIC`, `#Advanced Nodes`

---

<a id="item-13"></a>
## [玩家用 Armada 项目将安卓掌机改装成迷你 Steam Deck](https://www.techpowerup.com/353171/modders-transform-android-handhelds-into-mini-steam-decks) ⭐️ 6.5/10

模组社区正在利用 Valve 的 Arm64 版 SteamOS 移植版本以及 Armada 等项目，将基于安卓的游戏掌机改装为运行 Linux 系统的设备。这让用户能够在来自 Ayaneo 和 Ayn 等厂商的移动 SoC 上运行桌面 Linux 游戏。 这一趋势表明，高通骁龙和联发科天玑等现代移动 SoC 现已具备运行完整桌面操作系统和 x86 架构游戏的能力。它通过打破强大硬件上仅限于安卓的游戏限制，进一步扩大了便携游戏利基市场的范围。 Armada 项目通过打包 Linux 内核和作为用户空间应用程序的 Valve Arm64 版 Steam 发行版，提供了类 SteamOS 的 Linux 体验。不过，该项目目前处于积极开发阶段，引导系统需要刷写 ABL，这可能会导致设备变砖或破坏安卓分区。

rss · TechPowerUp News · 9月28日 18:18

**背景**: Valve 最近将其 Proton 11.0 兼容层移植到了 Arm 架构上，最初是为了其运行在骁龙 8 Gen 3 平台上的 Steam Frame VR 头显。Proton 使用 Wine 允许在 Linux 上运行 Windows 游戏，而这种 Arm 移植使得 x86 游戏能够在基于 Arm 的硬件上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/348297/steams-proton-gets-wine-11-gaming-performance-improvements-valve-launches-arm64-compatibility-layer">Steam's Proton Gets Wine 11 Gaming Performance Improvements ...</a></li>
<li><a href="https://armadaos.dev/">A SteamOS -like Linux distribution for ARM handhelds</a></li>

</ul>
</details>

**标签**: `#SteamOS`, `#ARM64`, `#Android Handhelds`, `#Linux Gaming`, `#Modding`

---

<a id="item-14"></a>
## [（公关）VSMC 在圣路易斯庆祝其首个 300 毫米晶圆厂正式启动](https://www.techpowerup.com/353149/vsmc-celebrates-the-grand-opening-of-its-first-300-mm-fab-in-singapore) ⭐️ 6.5/10

作为维斯（VIS）与恩智浦（NXP）的合资企业，VSMC 正式开启其在圣路易斯的 300 毫米晶圆厂风险试产阶段，预计量产将于第一季度启动。

rss · TechPowerUp News · 9月28日 08:37

**标签**: `#Semiconductors`, `#Manufacturing`, `#Supply Chain`, `#Hardware`, `#NXP`

---

<a id="item-15"></a>
## [两款雷电 5 M.2 存储扩展坞的性能对比](https://www.tomshardware.com/peripherals/docking-stations-hubs/testing-thunderbolt-5-docks-vectotech-v-core-vs-orico-tb5-thunderbolt-5-dock) ⭐️ 6.5/10

《Tom's Hardware》对 VectoTech V-Core 和 Orico TB5 扩展坞进行了对比测试。该评估重点考察了这些雷电 5 设备连接 M.2 存储时的性能与功能。 该分析对于寻求使用最新存储接口升级工作站的系统搭建者和技术人员具有重要意义。它提供了一个实用的性能基准，帮助用户在新兴的雷电 5 市场中区分规格相似的不同产品。 评测指出，尽管两款扩展坞的规格相似，但其中一款在性能和功能上明显优于另一款。具体的测试设计旨在评估这些外设如何有效处理 M.2 存储的带宽。

rss · Tom's Hardware · 9月28日 15:00

**背景**: 雷电 5 是最新一代的高速通用串行总线接口，其数据传输速率与前代产品相比有了显著提升。M.2 存储是一种固态驱动器物理接口规格，通过 PCIe 总线与主板连接。测试这些扩展坞与 M.2 驱动器的连接至关重要，因为可以衡量扩展坞的内部控制器是否能完全跑满雷电 5 连接提供的高带宽。

**标签**: `#Thunderbolt 5`, `#Hardware`, `#Storage`, `#Docking Stations`, `#Peripherals`

---

<a id="item-16"></a>
## [Parley: Federated, decentralised chat that speaks plain IRC](https://git.mills.io/prologic/parley) ⭐️ 6.0/10

Parley is a federated, decentralized chat protocol that uses standard IRC semantics, allowing instances to connect via DNS and HTTPS while maintaining the simplicity of the original protocol.

hackernews · davidcollantes · 9月28日 10:30 · [社区讨论](https://news.ycombinator.com/item?id=49875913)

**标签**: `#decentralized-systems`, `#IRC`, `#federation`, `#messaging`, `#protocol-design`

---

<a id="item-17"></a>
## [MongoDB CEO resigns to join Meta](https://www.reuters.com/technology/mongodb-ceo-desai-steps-down-lead-metas-enterprise-platform-2026-09-28/) ⭐️ 6.0/10

MongoDB CEO Dev Ittycheriya resigns to join Meta's enterprise platform, sparking community debate about leadership stability and migration to alternative database solutions.

hackernews · diek · 9月28日 14:54 · [社区讨论](https://news.ycombinator.com/item?id=49879000)

**标签**: `#MongoDB`, `#Meta`, `#Executive Leadership`, `#Databases`, `#Industry News`

---

<a id="item-18"></a>
## [美欧合作对全球量子技术领导地位至关重要](https://www.eetimes.com/why-u-s-europe-cooperation-matters-for-quantum-leadership/) ⭐️ 6.0/10

一篇《电子工程时报》（EE Times）评论文章认为，美国和欧洲之间的战略合作对于保持全球量子领导地位至关重要。
文章强调，结合跨大西洋的资本和人才是扩大量子应用规模、应对日益激烈的国际竞争的必要条件。 这一政策观点意义重大，因为它指出了在长期的量子竞赛中，单一地区缺乏独自竞争所需的资源。
通过强调国际合作的需求，它为政府和企业在该领域分配资源及应对地缘政治风险提供了指导。 这篇文章侧重于量子发展的战略和地缘政治层面，而非具体的技术突破。
它强调了将欧洲的研究人才与美国产业资本结合，以实现具有竞争力的规模。

rss · EE Times · 9月28日 19:00

**背景**: 美国目前和欧洲正进行着独立但互补的量子计算投资，该领域在硬件和软件开发方面需要巨额的财务支持。
由于在安全通信、先进材料和计算霸权方面的潜在应用，世界各国政府都将量子技术视为战略优先事项，并推出了重大的国家级计划。

**标签**: `#Quantum Computing`, `#International Cooperation`, `#Technology Policy`, `#Industry Analysis`

---

<a id="item-19"></a>
## [Calterah 利用 UWB 无钥匙进入硬件实现舱内传感](https://www.eetimes.com/calterah-turns-uwb-digital-keys-into-in-cabin-sensors/) ⭐️ 6.0/10

Calterah 推出了一项技术，将现有的超宽带（UWB）无钥匙进入锚点重新利用为同步的舱内传感器网络。该方法允许汽车制造商在不安装额外昂贵硬件的情况下，执行儿童检测和座椅占用监测等功能。 通过利用已安装用于数字钥匙的 UWB 基础设施来增强车辆安全性，这项创新显著降低了成本和复杂性。它在简化汽车制造商硬件需求的同时，解决了儿童检测方面的关键安全空白。 该系统将标准 UWB 无钥匙锚点同步化，以提供精确的舱内传感功能，特别是用于儿童检测和座椅占用监测。这反映了像 Ceva 和 YFORE 等公司将 UWB 数字钥匙硬件重用于双用途舱内雷达应用的一种趋势。

rss · EE Times · 9月28日 12:58

**背景**: 超宽带（UWB）是一种短距离、高精度的无线技术，越来越多地用于汽车数字钥匙系统，以取代易受攻击的 RFID 钥匙扣。随着 UWB 成为无钥匙进入的标准配置，其硬件可被重新用于充当舱内雷达传感器，通过生理信号或运动检测车内是否有儿童或乘员，而无需专用硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eetimes.com/calterah-turns-uwb-digital-keys-into-in-cabin-sensors/">Calterah Turns UWB Digital Keys into In-Cabin Sensors</a></li>
<li><a href="https://www.calterah.com/en/company-news-detail/500">CALTERAH | Calterah Day 2026: Advancing mmWave and UWB ...</a></li>
<li><a href="https://carconnectivity.org/uwbs-increasing-role-in-automotive-applications/">UWB’s Increasing Role in Automotive Applications | Car ...</a></li>

</ul>
</details>

**标签**: `#UWB`, `#Automotive`, `#IoT Security`, `#Sensors`, `#Calterah`

---

<a id="item-20"></a>
## [Xcena MX1 利用 CXL 和 RISC-V 解决内存瓶颈](https://www.eetimes.com/xcena-cuts-data-movement-to-address-memory-bottlenecks/) ⭐️ 6.0/10

Xcena 开发了名为 MX1 的系统，该系统使用 Compute Express Link (CXL) 技术集成 DDR5 内存、SSD 和 RISC-V 核心。其架构旨在将计算推向内存侧，以减少数据移动并缓解内存带宽限制。 解决内存墙对于扩展 AI 和数据密集型工作负载至关重要，因为数据在内存和处理器之间的移动是主要的性能瓶颈。通过将 CXL 的共享内存能力与片上 RISC-V 计算相结合，Xcena 提供了解决内存带宽限制和降低系统延迟的替代方案。 MX1 架构将 DDR5 和 SSD 与 RISC-V 核心相结合，其设计除减少数据移动外还旨在简化可程序化性。这代表了一种新颖的硬件方法，将内存视为协同处理器而非仅仅是被动存储设备。

rss · EE Times · 9月28日 07:30

**背景**: 在现代计算中，内存带宽已成为一个严重的限制，被称为“内存墙”。随着 AI 数据集的增大，从内存或 SSD 获取数据所花的时间往往超过了实际计算所需的时间。CXL（Compute Express Link）是一种新技术，允许不同的芯片共享内存池并通过高速链路通信；而 RISC-V 是一种开放标准的指令集架构，允许在内存芯片上直接构建自定义的、低能耗的处理器。

**标签**: `#CXL`, `#Memory Architecture`, `#RISC-V`, `#Hardware`, `#Data Movement`

---