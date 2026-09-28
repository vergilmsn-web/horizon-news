---
layout: default
title: "Horizon Summary: 2026-09-28 (ZH)"
date: 2026-09-28
lang: zh
---

> 从 39 条内容中筛选出 8 条重要资讯。

---

1. [SharpEmu PS5 模拟器成功以 60 帧运行六款游戏](#item-1) ⭐️ 8.5/10
2. [Fireworks AI 发布首个自研开源权重模型 Ember-1](#item-2) ⭐️ 8.0/10
3. [ProsperoEden 将任天堂 Switch 模拟器移植到越狱 PS5](#item-3) ⭐️ 7.5/10
4. [Linux 内核编译即将迈入十秒时代](#item-4) ⭐️ 7.5/10
5. [Go 开发者热议将代码与 GitHub 解耦](#item-5) ⭐️ 7.0/10
6. [Flock seeks to have security researchers' map of Flock cameras taken down](#item-6) ⭐️ 6.5/10
7. [Developer says AI decision model Jev beat Pokémon Red in under a week](#item-7) ⭐️ 6.5/10
8. [英国无人潜艇成功发射重型鱼雷，创造历史性首次](#item-8) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [SharpEmu PS5 模拟器成功以 60 帧运行六款游戏](https://www.tomshardware.com/desktops/gaming-pcs/ps5-emulator-successfully-runs-six-titles-at-a-playable-60-fps-ps5-emulation-continues-to-gather-momentum-as-developers-improve-shader-translation-and-vulkan-support) ⭐️ 8.5/10

SharpEmu PS5 模拟器发布了一项更新，使其能够以稳定的 60 帧运行六款特定的测试游戏。此外，该模拟器目前已成功在 55 款测试游戏中的 12 款达到可玩状态。 在现代主机电源上实现稳定的 60 帧对于模拟爱好者和系统研究人员来说是一个重要的技术里程碑。它证明了将复杂的下一代图形 API 翻译到开源后端的可能性。 性能的提升主要得益于着色器翻译流水线的改进以及 Vulkan 后端支持的集成。在 55 款游戏中有 12 款达到可玩状态，表明该项目的兼容性呈现出强劲的增长势头。

rss · Tom's Hardware · 9月27日 12:40

**背景**: PS5 模拟需要将 PlayStation 5 的专有图形和计算 API 转换为在通用 PC 硬件上运行的 Vulkan 等标准格式。着色器翻译是这一过程中的关键瓶颈，因为它涉及将高级图形代码转换为与消费级显卡兼容的高效 GPU 指令。

**标签**: `#Game Emulation`, `#Vulkan`, `#PS5`, `#Graphics Programming`, `#Hardware`

---

<a id="item-2"></a>
## [Fireworks AI 发布首个自研开源权重模型 Ember-1](https://fireworks.ai/blog/ember-1) ⭐️ 8.0/10

作为主要的 AI 基础设施提供商，Fireworks AI 发布了其首个自研模型 Ember-1，标志着其战略重心从单纯托管第三方模型向开展基础模型研究的转变。 此举模糊了推理基础设施提供商与模型开发者之间的界限，可能加速这两个领域的融合，并在成本效率和开源创新方面推动行业竞争。 此次发布以效率和开源权重模型开发为特点，与大型科技公司的专有方法形成对比。社区关注点在于这种自研开发如何影响 Fireworks 作为其他开源模型 API 提供商的中立性。

hackernews · gmays · 9月27日 17:31 · [社区讨论](https://news.ycombinator.com/item?id=49868830)

**背景**: Fireworks AI 是一家主要提供优化 GPU 上的 AI 模型运行推理基础设施的公司。在当前的 AI 领域，“开放权重”模型是指其参数可公开下载的模型，但这与包括对训练数据和代码完全访问权限的“开源”AI 不同。大多数基础设施提供商传统上托管由外部研究机构或大型科技公司开发的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fireworks_AI">Fireworks AI - Wikipedia</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一，一方面有人庆祝模型训练和微调工作流的易得性，另一方面，既然 Fireworks 现在与其曾托管的开源模型存在竞争，部分用户对 Fireworks 的潜在利益冲突表示担忧。一些用户还围绕新发布的背景，就其他模型（如 Sol 和 Kimi K3）的性价比展开了对比讨论。

**标签**: `#LLM`, `#Model-Release`, `#Fireworks-AI`, `#Open-Source-AI`, `#Fine-Tuning`

---

<a id="item-3"></a>
## [ProsperoEden 将任天堂 Switch 模拟器移植到越狱 PS5](https://www.techpowerup.com/353135/experimental-emulator-brings-nintendo-switch-games-to-jailbroken-ps5-consoles) ⭐️ 7.5/10

开发者 BlackBearReloaded 发布了 ProsperoEden，这是 Eden 任天堂 Switch 模拟器的一款实验性自研移植项目，可直接在越狱 PS5 主机上运行。v1.000.010 版本实现了可玩的帧率，例如《Cuphead》达到 60 帧，《马里奥赛车 8 豪华版》也已能进入游戏画面。 该项目展示了越狱 PS5 主机的强大性能，证明了其在跨系统模拟和系统研究方面的潜力。同时，它也凸显了自研社区如何快速利用新的固件漏洞，将主机功能扩展至官方支持范围之外。 该移植版本目前仅支持 OpenGL 后端，未为 PS5 端构建 Vulkan 渲染器。该项目仍处于测试阶段，需要用户手动提供密钥、固件和游戏文件，且像《宝可梦传说 Z-A》等游戏依然运行缓慢并伴随崩溃。

rss · TechPowerUp News · 9月27日 19:03

**背景**: 任天堂曾于 2024 年成功叫停了著名的 Switch 模拟器 Yuzu，促使了 Eden 等后续分支项目的诞生。自 2024 年以来，PS5 越狱社区发展迅速，新工具与自研软件的出现使得该主机能够运行未经授权的应用程序和 Linux 等操作系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yuzu_(emulator)">Yuzu (emulator) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#PS5 Jailbreak`, `#Emulation`, `#Nintendo Switch`, `#Homebrew`, `#Reverse Engineering`

---

<a id="item-4"></a>
## [Linux 内核编译即将迈入十秒时代](https://www.tomshardware.com/software/linux/linux-enthusiasts-see-10-second-kernel-compilation-times-on-the-horizon-ai-assisted-patches-cut-build-times-by-nearly-a-third-without-a-ramdisk) ⭐️ 7.5/10

Phoronix 报道称，全新的 Linux 内核编译时间正逼近 10 秒，而 AI 辅助的编译器补丁使编译时间减少了近三分之一。这一里程碑是通过现代多核硬件（例如在基准测试中表现最快的 AMD EPYC 9575F 2P 系统）实现的。 将内核编译时间缩短至 10 秒以内极大地加速了开发者工作流和 CI/CD 管道。这一里程碑使 Linux 开发者能够以近乎即时的反馈速度迭代复杂的系统级更改。 AMD EPYC 9575F 2P 系统在 x86_64 defconfig 构建上的基准测试时间约为 20 秒。这一速度是在不使用 ramdisk（RAM 磁盘）的情况下实现的，凸显了硬件进步和优化编译器启发式算法的影响。

rss · Tom's Hardware · 9月27日 12:20

**背景**: 编译 Linux 内核是一个资源密集型过程，传统上在消费级硬件上需要数分钟到数小时。来自 AMD 和 Intel 的多核处理器大幅缩短了这些时间，使得 10 秒大关成为社区极力追求的重要里程碑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/review/near-10-sec-kernel-build">Approaching A 10 Second Linux Kernel Build - Phoronix</a></li>
<li><a href="https://www.tomshardware.com/software/linux/linux-enthusiasts-see-10-second-kernel-compilation-times-on-the-horizon-ai-assisted-patches-cut-build-times-by-nearly-a-third-without-a-ramdisk">Linux enthusiasts see 10-second kernel compilation times on ...</a></li>

</ul>
</details>

**标签**: `#Linux`, `#Compiler Optimization`, `#AI`, `#Build Systems`, `#Performance`

---

<a id="item-5"></a>
## [Go 开发者热议将代码与 GitHub 解耦](https://iain.rocks/blog/dont-couple-your-go-code-to-github) ⭐️ 7.0/10

一篇技术文章及随后的 Hacker News 讨论建议，使用自定义域名而非 GitHub URL 来命名空间 Go 包。作者主张将代码与特定的 git 托管商解耦，以简化未来的迁移并提升长期可移植性。 Go 的模块系统将导入路径作为命名空间，因此域名选择对企业稳定性和云服务商中立性至关重要。此问题直接影响大型团队如何管理依赖风险并规划长期基础设施迁移。 批评者指出，使用自定义域名会引入新的运维开销，例如需要维护 Git 服务器或配置自定义 Git 托管服务。此外，go.mod 中的'replace'指令提供了一种标准的、原生的解决方案，可在不修改代码库的情况下实现依赖迁移。

hackernews · birdculture · 9月27日 16:50 · [社区讨论](https://news.ycombinator.com/item?id=49868404)

**背景**: 在 Go 模块中，导入路径是决定包从哪里获取的唯一事实来源，并被直接嵌入代码中。虽然这确保了命名的唯一性，但它将代码严格绑定到特定的 Git 托管服务商（如 GitHub）。go.mod 文件和'vendor'目录是管理或覆盖这些外部依赖的主要机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://go.dev/ref/mod">Go Modules Reference - The Go Programming Language</a></li>
<li><a href="https://arslan.io/2019/08/02/why-you-should-use-a-go-module-proxy/">Why you should use a Go module proxy - Fatih Arslan</a></li>

</ul>
</details>

**社区讨论**: 讨论分歧明显：部分开发者认为自定义域名提供长期安全保障，但也有人反驳称由于 GitHub 的统治地位，这种优化为时过早。此外，讨论还转向了自定义域名的可靠性，有人指出域名注册商可能会单方面注销账户，且 go.mod 的'replace'指令使得手动重构代码变得多余。

**标签**: `#Go`, `#Software Engineering`, `#Dependency Management`, `#Best Practices`, `#Cloud Infrastructure`

---

<a id="item-6"></a>
## [Flock seeks to have security researchers' map of Flock cameras taken down](https://www.tomshardware.com/tech-industry/cyber-security/flock-seeks-to-have-security-researchers-map-of-flock-cameras-taken-down-unauthenticated-flaw-exposed-335-701-camera-locations-nationwide) ⭐️ 6.5/10

Flock is attempting to have security researchers' maps of its 335,701 camera locations removed after an unauthenticated vulnerability exposed data enabling tracking of personnel at sensitive government sites.

rss · Tom's Hardware · 9月27日 12:00

**标签**: `#Cybersecurity`, `#Surveillance`, `#Vulnerability`, `#Data Privacy`, `#IoT`

---

<a id="item-7"></a>
## [Developer says AI decision model Jev beat Pokémon Red in under a week](https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-says-jev-decision-model-beat-pokemon-red-in-under-a-week-non-llm-engine-succeeds-where-traditional-chatbots-stalled-for-months-but-claude-opus-5-coached-the-model-through-its-dead-ends) ⭐️ 6.5/10

TypeSafe AI's non-LLM model Jev successfully beat Pokémon Red in under a week, demonstrating that specialized decision models can outperform general-purpose LLMs in specific gaming environments.

rss · Tom's Hardware · 9月27日 11:30

**标签**: `#Artificial Intelligence`, `#Reinforcement Learning`, `#Gaming`, `#LLM vs Non-LLM`, `#Automation`

---

<a id="item-8"></a>
## [英国无人潜艇成功发射重型鱼雷，创造历史性首次](https://www.tomshardware.com/tech-industry/u-s-and-uk-navies-successfully-launch-3-700-pound-submarine-sinking-torpedo-from-robotic-drone-submarine-in-historic-first-project-broadsword-proves-weapon-interchangeability-in-just-seven-months) ⭐️ 6.5/10

美国海军和英国皇家海军成功从英国的无人员驾驶的 XV Excalibur 潜艇上发射了一枚重达 3,700 磅的 Mk 48 鱼雷。这标志着自主水下无人载具首次发射此类重型武器。 这一里程碑证明了跨平台武器兼容性和互操作性，展示了自主系统在高利害风险的国防领域的实用价值。它极大地缩短了将重型武器整合到无人机平台中的开发周期。 所使用的武器是 Mk 48 重型鱼雷，而无人载具是英国的 XV Excalibur 潜艇。这一成就是在“广剑”计划（Project Broadsword）下实现的，该计划在短短七个月内就证明了武器的互换性。

rss · Tom's Hardware · 9月27日 10:30

**背景**: Mk 48 鱼雷是世界上最广泛使用的反潜武器之一，通常由载人核潜艇或常规潜艇发射。无人水下载具（UUV）正越来越多地被用于扩展海军的打击范围，但让无人载具携带并发射重型鱼雷在历史上一直是一个重大的技术障碍。互操作性是指为某一类舰艇设计的武器可以应用于另一类舰艇。

**标签**: `#Autonomous Systems`, `#Defense Technology`, `#Robotics`, `#Interoperability`, `#Maritime`

---