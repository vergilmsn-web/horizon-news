---
layout: default
title: "Horizon Summary: 2026-09-27 (ZH)"
date: 2026-09-27
lang: zh
---

> 从 33 条内容中筛选出 12 条重要资讯。

---

1. [解封文件揭露 OpenAI 对 LibGen 盗版风险的知情](#item-1) ⭐️ 9.0/10
2. [SharpEmu PS5 模拟器在六款游戏中实现 60 FPS](#item-2) ⭐️ 8.5/10
3. [AI 辅助编译器优化预计将 Linux 内核构建时间缩短至 10 秒](#item-3) ⭐️ 8.5/10
4. [历史性时刻：美英海军从机器人潜艇发射重型鱼雷](#item-4) ⭐️ 7.5/10
5. [AI 辅助开发导致难以复现的软件故障常态化](#item-5) ⭐️ 7.0/10
6. [Neovim 升级删除 Vim 持久撤销文件](#item-6) ⭐️ 7.0/10
7. [DLSS-NR-on-AMD 模组 24 小时内性能提升 74%](#item-7) ⭐️ 6.5/10
8. [TypeSafe AI 的 Jev 模型在一周内通关《宝可梦红》](#item-8) ⭐️ 6.5/10
9. [Sony Patents Tap-to-Pay Technology for PlayStation Controllers](#item-9) ⭐️ 5.5/10
10. [GTA 2 借助 RTX Remix 模组支持路径追踪](#item-10) ⭐️ 5.5/10
11. [Gigabyte 1000GM PG5 1000W power supply review: Impressive Platinum-level efficiency with T-Guard thermal protection](#item-11) ⭐️ 5.5/10
12. [Flock seeks to have security researchers' map of Flock cameras taken down](#item-12) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [解封文件揭露 OpenAI 对 LibGen 盗版风险的知情](https://authorsguild.org/news/ag-v-openai-top-execs-knew-mass-book-piracy-was-illegal/) ⭐️ 9.0/10

在作者协会起诉微软和 OpenAI 的案件中，新解封的法院文件显示，OpenAI 的高管和员工明知从 LibGen 使用盗版书籍数据会带来极高的法律风险。 这些文件通过展示内部对侵犯版权的知情，有力削弱了 OpenAI 的“善意”和“干净训练”抗辩理由，从而改变了 AI 模型训练的法律格局。 员工 Ryan Lowe 的具体评估估计有超过 80%的概率因数据来源受到质疑，团队成员还明确担心在 Hacker News 上引发“不利观感”。

hackernews · papergirl · 9月27日 06:19 · [社区讨论](https://news.ycombinator.com/item?id=49863864)

**背景**: Library Genesis（LibGen）是一个具有争议的影子图书馆，提供有版权保护的科学和普通书籍的免费访问，常被企业描述为“可疑”来源。作者协会代表美国专业作家，在 AI 时代为其版权保护倡导，此时训练大型语言模型使用未授权文本已成为核心法律战场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LibGen">LibGen</a></li>
<li><a href="https://en.wikipedia.org/wiki/Authors_Guild">Authors Guild</a></li>

</ul>
</details>

**社区讨论**: 用户强调内部文件证明高管明白大规模书籍盗版会导致作家失业，并特别担心在 Hacker News 等平台上产生负面公众形象。人们还对 OpenAI 内部认为先进 AI 可以替代类型小说写家的观点表示兴趣，这对合理使用论点具有法律意义。

**标签**: `#AI`, `#Legal`, `#Copyright`, `#OpenAI`, `#HackerNews`

---

<a id="item-2"></a>
## [SharpEmu PS5 模拟器在六款游戏中实现 60 FPS](https://www.tomshardware.com/desktops/gaming-pcs/ps5-emulator-successfully-runs-six-titles-at-a-playable-60-fps-ps5-emulation-continues-to-gather-momentum-as-developers-improve-shader-translation-and-vulkan-support) ⭐️ 8.5/10

SharpEmu PS5 模拟器在六款特定游戏中实现了可玩的 60 FPS 性能，目前 55 款受测游戏中有 12 款已达到游戏可运行状态。这一进展得益于着色器转换和 Vulkan API 支持的持续改进。 在 PS5 游戏中实现稳定的 60 FPS 标志着系统模拟的一个重要技术里程碑，表明该软件正从基本功能向实际可玩性迈进。这降低了用户对专有主机 GPU 的依赖，使最新的控制台体验在 PC 硬件上更加易于获取。 该模拟器目前有 55 款受测游戏中的 12 款达到了游戏可运行状态，而达到 60 FPS 的六款游戏代表了高性能基准。开发重点仍在于完善着色器转换，以将主机特定的图形代码准确映射到现代 PC 图形 API 上。

rss · Tom's Hardware · 9月27日 12:40

**背景**: PS5 模拟极具挑战性，因为主机的 GPU 使用专有编程语言，必须将其翻译成 PC 硬件能理解的格式（如 Vulkan 或 DirectX）。Vulkan 是一种低开销的图形 API，能够实现与 GPU 的高效通信，对于模拟器维持流畅的帧率且避免瓶颈至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xenia-emulator.com/knowledge-base/gpu-emulation/">GPU Emulation – Translating Xbox 360 Graphics to Vulkan & Direct3D 12</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vulkan">Vulkan - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Emulation`, `#PS5`, `#Vulkan`, `#GPU`, `#Systems Research`

---

<a id="item-3"></a>
## [AI 辅助编译器优化预计将 Linux 内核构建时间缩短至 10 秒](https://www.tomshardware.com/software/linux/linux-enthusiasts-see-10-second-kernel-compilation-times-on-the-horizon-ai-assisted-patches-cut-build-times-by-nearly-a-third-without-a-ramdisk) ⭐️ 8.5/10

PC 硬件的进步和 AI 辅助的编译器优化预计将 Linux 内核的干净构建时间缩短至大约 10 秒。这种新方法专门针对构建基础设施，旨在大幅提高开发者的迭代速度，且不依赖于传统的 ramdisk 等变通方法。 将内核编译时间缩短至 10 秒将通过更快的回归测试和代码二分查找迭代周期，显著提升 Linux 开发者的效率。这一突破标志着 AI 在传统系统编程基础设施应用方面的重大转变，可能会影响所有大规模软件项目。 预计 10 秒的构建时间是通过结合尖端处理器进步和机器学习驱动的编译器启发式算法实现的。与 ccache 等传统加速技术不同，该方法通过成比例地减少构建时间，即使对于非尖端系统上的干净构建也能提供显著的性能提升。

rss · Tom's Hardware · 9月27日 12:20

**背景**: 从头开始构建 Linux 内核通常需要几分钟到几个小时，这会拖慢开发工作流程和回归错误排查。ccache 等传统加速工具通过重用之前编译的文件来节省时间，但对于缓存为空的干净构建，其效果较差。基于 AI 的编译器优化是一个新兴领域，它使用机器学习自动预测并应用最佳的编译标志和优化路径，从而取代了手动调优。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/review/near-10-sec-kernel-build">Approaching A 10 Second Linux Kernel Build - Phoronix</a></li>
<li><a href="https://nickdesaulniers.github.io/blog/2018/06/02/speeding-up-linux-kernel-builds-with-ccache/">Speeding Up Linux Kernel Builds With ccache</a></li>
<li><a href="https://github.com/shrutisaxena51/Artificial-Intelligence-in-Compiler-Optimization">Artificial-Intelligence-in-Compiler-Optimization - GitHub (PDF) Advancements in AI-Based Compiler Optimization ... 5.1. Overview of AI Compilers — Machine Learning Systems ... AI Powered Compiler Techniques for DL Code Optimization GitHub - zwang4/awesome-machine-learning-in-compilers: Must ... Fan Yang - AI compiler</a></li>

</ul>
</details>

**标签**: `#Linux Kernel`, `#Compilers`, `#AI`, `#Build Optimization`, `#Performance`

---

<a id="item-4"></a>
## [历史性时刻：美英海军从机器人潜艇发射重型鱼雷](https://www.tomshardware.com/tech-industry/u-s-and-uk-navies-successfully-launch-3-700-pound-submarine-sinking-torpedo-from-robotic-drone-submarine-in-historic-first-project-broadsword-proves-weapon-interchangeability-in-just-seven-months) ⭐️ 7.5/10

美国海军和英国皇家海军成功从英国无人的“XV Excalibur”潜艇中发射了一枚重 3700 磅的 Mk 48 重型鱼雷。这是该常规武器首次被整合进自主水下航行器并从中发射。 这一里程碑证明了重型常规海军武器与无人平台互换的可行性，减少了高风险环境中对载人潜艇的需求。它大幅提升了自主系统在水下战争执行致命打击任务的能力。 该测试在仅七个月内将鱼雷适配到无人平台，证实了武器的互换性。Mk 48 鱼雷是一种精密的 21 英寸武器，具备反潜和反水面战双重角色。

rss · Tom's Hardware · 9月27日 10:30

**背景**: Mk 48 是一种高度复杂的单组分推进剂鱼雷，是美国海军潜艇的主要重型武器，通常由有人船只发射。“XV Excalibur”是英国“塞图斯计划”（Project Cetus）的一部分，旨在开发能够执行长时间水下任务的超大无人水下航行器。自主水下航行器（AUV）通常设计用于情报收集和检查，但目前正在向作战角色转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Cetus">Project Cetus - Wikipedia</a></li>
<li><a href="https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2167907/mk-48-heavyweight-torpedo/">MK 48 - Heavyweight Torpedo - United States Navy</a></li>

</ul>
</details>

**标签**: `#Defense Tech`, `#Autonomous Systems`, `#Robotics`, `#Naval Warfare`, `#Engineering`

---

<a id="item-5"></a>
## [AI 辅助开发导致难以复现的软件故障常态化](https://www.ihatethefuture.com/2026/09/the-normalization-of-inexplicable.html) ⭐️ 7.0/10

一篇新的评论文章指出，LLM 和智能体工具在软件开发中的广泛集成正在导致非确定性和难以复现的故障常态化。这种转变引发了业内关于这种“足够好”的可靠性标准是否适用于关键基础设施和库的激烈争论。 这一点之所以重要，是因为它揭示了 AI 辅助编码带来的效率提升与下游系统所需的稳定性之间的根本矛盾。如果非确定性故障在库和基础设施中成为新常态，可能会波及整个技术栈的可靠性。 讨论中的一个重要细节是，“足够好”的可靠性对于孤立的用户端应用可能是可以接受的，但如果它成为基础库、基础设施或编译器的标准，则极具问题。难以解释的故障常态化也伴随着调试过程中责任缺失的常态化。

hackernews · pxx · 9月27日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=49867486)

**背景**: 确定性软件系统是指在相同的输入和环境条件下产生完全相同输出的系统，这对可靠的测试、调试和基础设施至关重要。而 LLM 和智能体开发工具本质上是非确定性的，会产生变化的输出，这使得传统的软件测试和类似 Nix 的可复现构建流程变得更加困难。该争论的核心在于，AI 生成代码的“幻觉”或不可预测性是否会损害软件工程的基石。

**社区讨论**: 社区的回应分为接受“足够好”结果的实用主义 AI 用户和严格的确定性与可复现性倡导者。评论者表达了强烈的担忧，认为在共享库和基础设施中让难以解释的故障常态化，会导致整体可靠性不断下降，最终拖慢整个行业的发展。

**标签**: `#AI-assisted development`, `#Software reliability`, `#Reproducibility`, `#LLM engineering`, `#DevOps culture`

---

<a id="item-6"></a>
## [Neovim 升级删除 Vim 持久撤销文件](https://unsung.aresluna.org/they-had-no-concept-of-a-duty-of-care-to-their-users/) ⭐️ 7.0/10

Neovim 的一次更新更改了持久撤销文件的格式，导致 Neovim 删除了来自原版 Vim 安装的不兼容撤销文件。 该事件揭示了一个严重的软件维护缺陷，其中破坏性变更导致在相关联但不同的工具之间发生数据丢失。 自 2021 年 3 月的 0.4.4 版本起，Neovim 使用了与 Vim 不同的撤销文件格式，这意味着文件无法互换使用。

hackernews · jandeboevrie · 9月27日 14:45 · [社区讨论](https://news.ycombinator.com/item?id=49867067)

**背景**: 持久撤销是 Vim 中的一项功能，它可将撤销历史保存到磁盘，允许用户在不同会话和重启之间撤销更改。Vim 通常将这些文件存储在 ~/.vim/undodir 目录中，而 Neovim 则使用不同的结构。当 Neovim 打开文件时，它发现了一个旧格式的撤销文件，由于无法读取，便将其删除。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vi.stackexchange.com/questions/46731/can-neovim-understand-vim-undo-files">Can Neovim understand Vim undo files? - Vi and Vim Stack Exchange</a></li>
<li><a href="https://stackoverflow.com/questions/5700389/using-vims-persistent-undo">Using Vim 's persistent undo ? - Stack Overflow</a></li>

</ul>
</details>

**社区讨论**: 用户们非常震惊，因为他们可能在 Neovim 升级后在不知情的情况下丢失了撤销历史。一些资深 Vim 用户表示庆幸自己一直没有切换，而一名评论者则指出该博文缺乏支持作者具体说法的参考资料。

**标签**: `#Neovim`, `#Data Safety`, `#Open Source`, `#Technical Writing`, `#Community Discussion`

---

<a id="item-7"></a>
## [DLSS-NR-on-AMD 模组 24 小时内性能提升 74%](https://www.techpowerup.com/353131/modder-squeezes-74-more-performance-out-of-dlss-5-on-amd-radeon-in-one-day) ⭐️ 6.5/10

DLSS-NR-on-AMD 模组的开发者在 24 小时内发布了两个更新，使 Radeon GPU 的性能提升了大约 74%。 这一性能提升使 NVIDIA 的 DLSS 5 技术在 AMD 硬件上更加可用，为游戏玩家提供了一种利用先进神经渲染的新方式。 该模组通过将 NVIDIA 的 DLSS 5 DLL 路由到 AMD 硬件上工作，最新更新还增加了图形化安装程序和设置编辑器。

rss · TechPowerUp News · 9月27日 12:09

**背景**: DLSS 5 神经渲染是 NVIDIA 的最新技术，它使用 3D 引导的神经渲染来生成最终的视觉细节，通常需要特定的硬件支持。DLSS-NR-on-AMD 项目是一个社区制作的模组，通过利用 AMD Radeon 显卡对特定数学运算的支持，使该技术能够在兼容的 AMD 显卡上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/danielblnc/DLSS-NR-on-AMD">GitHub - danielblnc/DLSS-NR-on-AMD: Run DLSS 5 Neural ...</a></li>
<li><a href="https://research.nvidia.com/labs/adlr/DLSS5/">DLSS 5: Generative Neural Rendering - NVIDIA ADLR</a></li>

</ul>
</details>

**标签**: `#DLSS`, `#AMD Radeon`, `#Graphics`, `#Game Performance`, `#Modding`

---

<a id="item-8"></a>
## [TypeSafe AI 的 Jev 模型在一周内通关《宝可梦红》](https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-says-jev-decision-model-beat-pokemon-red-in-under-a-week-non-llm-engine-succeeds-where-traditional-chatbots-stalled-for-months-but-claude-opus-5-coached-the-model-through-its-dead-ends) ⭐️ 6.5/10

TypeSafe AI 开发了一款名为 Jev 的非 LLM 决策模型，该模型成功在不到一周内通关了《宝可梦红》。这与之前在此任务上停滞数月的传统聊天机器人方法形成了鲜明对比。 这一成就表明非 LLM 架构可以在特定游戏环境中优于传统的生成式 AI 方法。它为评估不同 AI 模型在强化学习基准测试中的效率和有效性提供了重要的参考数据。 Jev 是一款专门的非 LLM 决策模型，在开发和训练过程中，它得到了 Claude Opus 5 的协助以绕过死胡同。最终结果是该模型成功进入了宝可梦名人堂。

rss · Tom's Hardware · 9月27日 11:30

**背景**: 强化学习（RL）是一种机器学习方法，代理通过在环境中采取行动以最大化累积奖励来学习如何做决策。在电子游戏背景下，这意味着 AI 模型控制角色完成关卡、击败 Boss 并最终通关。传统的大语言模型（LLM）经常被用于此类任务，但在封闭回路的游戏交互中往往效率低下或容易出现停滞。

**标签**: `#AI`, `#Reinforcement Learning`, `#Game AI`, `#Non-LLM Models`, `#Benchmarks`

---

<a id="item-9"></a>
## [Sony Patents Tap-to-Pay Technology for PlayStation Controllers](https://www.techpowerup.com/353132/sony-patents-tap-to-pay-technology-for-playstation-controllers) ⭐️ 5.5/10

Sony has patented technology enabling PlayStation controllers to read payment credentials via NFC or Bluetooth to simplify in-game transactions.

rss · TechPowerUp News · 9月27日 13:32

**标签**: `#Sony`, `#PlayStation`, `#Payment`, `#Hardware`, `#Patent`

---

<a id="item-10"></a>
## [GTA 2 借助 RTX Remix 模组支持路径追踪](https://www.techpowerup.com/353119/modder-brings-path-tracing-and-frame-generation-to-grand-theft-auto-2-via-rtx-remix) ⭐️ 5.5/10

模组开发者 gebdag 发布了开源的 GTA2 RTX Remix 模组，为 1999 年的经典游戏《侠盗猎车手 2》引入了完整的路径追踪和帧生成技术。该模组使用自定义 DLL 封装器将过时的 DirectDraw 调用转换为现代渲染格式。 该模组通过自定义封装器克服了传统图形 API 的兼容性问题，进一步拓展了 NVIDIA RTX Remix 平台的强大功能。它证明了使用尖端的射线追踪技术对经典非 3D 游戏进行现代化改造仍然是可行的。 该模组需要 64 位 Windows 10 或 11 系统，支持 16:9 宽屏比例，并具备动态昼夜光照效果。它最高可生成 60 FPS 的帧率，并且爆炸和汽车火灾等效果也具备实时路径追踪光照。

rss · TechPowerUp News · 9月26日 18:46

**背景**: RTX Remix 是 NVIDIA 推出的一款工具，允许玩家使用现代实时路径追踪技术重新渲染经典 3D 游戏。《侠盗猎车手 2》是一款 1999 年发布的高人气俯视视角动作游戏，最初使用 DirectDraw（一种过时的 2D API）处理图形，缺乏现代 3D 功能，这使得该模组使用的自定义转换层尤为具有挑战性且令人印象深刻。

**标签**: `#Game Development`, `#RTX Remix`, `#Path Tracing`, `#Legacy Systems`, `#Modding`

---

<a id="item-11"></a>
## [Gigabyte 1000GM PG5 1000W power supply review: Impressive Platinum-level efficiency with T-Guard thermal protection](https://www.tomshardware.com/pc-components/power-supplies/gigabyte-1000gm-pg5-1000w-power-supply-review) ⭐️ 5.5/10

Gigabyte's 1000GM PG5 1000W power supply features Platinum efficiency, Japanese capacitors, and T-Guard thermal protection for the 12V-2x6 connector.

rss · Tom's Hardware · 9月27日 13:00

**标签**: `#Power Supply`, `#PC Hardware`, `#Review`, `#Gigabyte`, `#PSU`

---

<a id="item-12"></a>
## [Flock seeks to have security researchers' map of Flock cameras taken down](https://www.tomshardware.com/tech-industry/cyber-security/flock-seeks-to-have-security-researchers-map-of-flock-cameras-taken-down-unauthenticated-flaw-exposed-335-701-camera-locations-nationwide) ⭐️ 5.5/10

Flock is attempting to suppress a security researcher's discovery that an unauthenticated API flaw exposed the locations of over 335,000 cameras, including those securing sensitive government facilities.

rss · Tom's Hardware · 9月27日 12:00

**标签**: `#Security`, `#Vulnerability`, `#IoT`, `#Surveillance`, `#Privacy`

---