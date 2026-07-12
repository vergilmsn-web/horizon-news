---
layout: default
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 48 items, 11 important content pieces were selected

---

1. [Nvidia RTX 5070 Ti Throttles at 107°C Due to Poor TIM, Hidden Hotspot Sensor Exposed](#item-1) ⭐️ 7.5/10
2. [China's Embodied Data Boom: 97 Players, 4.47B RMB Raised](#item-2) ⭐️ 7.3/10
3. [AI热潮太费电，燃气轮机价格3年涨了300%](#item-3) ⭐️ 7.3/10
4. [Mindwalk: 3D Codebase Map for Replaying AI Coding Agent Sessions](#item-4) ⭐️ 7.0/10
5. [RISCBoy is an open-source portable games console, designed from scratch](#item-5) ⭐️ 7.0/10
6. [FCC approves orbital space mirrors, first test satellites will launch this year — large spacecraft reflects sunlight to Earth’s surface for construction sites, search-and-rescue lighting, and more](#item-6) ⭐️ 6.5/10
7. [Apple Sues OpenAI Over Alleged Trade Secret Theft by Former Employees](#item-7) ⭐️ 6.3/10
8. [Terry Tao on Building Apps with Modern Coding Agents](#item-8) ⭐️ 6.0/10
9. [Mesh LLM: distributed AI computing on iroh](#item-9) ⭐️ 6.0/10
10. [Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom](#item-10) ⭐️ 6.0/10
11. [AIC Unveils 32-Bay E3 SSD JBOF for AI Key-Value Caching](#item-11) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Nvidia RTX 5070 Ti Throttles at 107°C Due to Poor TIM, Hidden Hotspot Sensor Exposed](https://www.tomshardware.com/pc-components/gpus/hotspot-temperature-sensor-on-nvidias-blackwell-gaming-gpus-is-still-accessible-if-you-have-access-to-nvidias-internal-mods-tool-nvidia-rtx-5070-ti-caught-throttling-at-107-c-over-poor-tim-application) ⭐️ 7.5/10

Testing via Nvidia's internal Modular Diagnostics Software (MODS) tool has revealed that RTX 5070 Ti GPUs are hitting hotspot temperatures of 107°C and throttling due to poor thermal interface material (TIM) application. Nvidia deliberately hid the hotspot temperature sensor from consumers on the RTX 50 series, but the internal diagnostic tool can still read it, exposing significant thermal issues. This news raises concerns about quality control in Nvidia's Blackwell gaming GPUs and suggests that consumers may have been kept in the dark about thermal throttling issues. Buyers of the RTX 5070 Ti could be experiencing performance degradation without knowing it, potentially warranting warranty claims or RMA requests. Nvidia's MODS tool is an internal diagnostic suite not available to the public and does not function on Windows because the OS intercepts hardware monitoring API calls. Hotspot (junction) temperature measures the single hottest point on the GPU die rather than the average core temperature, and it is the gap between hotspot and edge temperatures that typically signals a real thermal problem.

rss · Tom's Hardware · Jul 11, 16:18

**Background**: MODS (Modular Diagnostics Software) is an internal Nvidia tool used to test GPUs before shipment or during the RMA process; it checks everything from VRAM chips to GPU core specifics. GPU hotspot temperature differs from core temperature: core temperature represents the average heat across the silicon die, while hotspot temperature is the reading from the hottest single point among dozens of internal sensors. Thermal Interface Material (TIM), commonly known as thermal paste, sits between the processor and cooler to facilitate heat transfer, and poor application can dramatically reduce cooling efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/hotspot-temperature-sensor-on-nvidias-blackwell-gaming-gpus-is-still-accessible-if-you-have-access-to-nvidias-internal-mods-tool-nvidia-rtx-5070-ti-caught-throttling-at-107-c-over-poor-tim-application">Hotspot temperature sensor on Nvidia 's Blackwell gaming GPUs is still...</a></li>
<li><a href="https://rkblog.dev/posts/pc-hardware/nvidia-modular-diagnostic-software-mods/">Nvidia Modular diagnostic software - MODS</a></li>
<li><a href="https://www.darkflash.com/article/gpu-junction+temperature-explained">Understanding GPU Junction Temp vs . Core Temp: Is Your Hotspot ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#RTX 5070 Ti`, `#GPU thermal issues`, `#Blackwell architecture`, `#hardware review`

---

<a id="item-2"></a>
## [China's Embodied Data Boom: 97 Players, 4.47B RMB Raised](https://36kr.com/p/3892027841362694?f=rss) ⭐️ 7.3/10

A 36Kr/QbitAI survey identified 97 players in China's embodied data industry, of which 70 focus on data collection and 27 on data infrastructure. In the past year (July 2025–July 2026), 15 independent data service companies—those building neither robot hardware nor AI models—raised a combined 4.47 billion RMB, while creative collection methods are emerging, including a China Mobile store in Chenzhou operating as an 'embodied data 5S shop' where ordinary customers collect training data while doing household chores. Embodied AI—training robots to interact with the physical world—has been starved for high-quality, diverse training data, making data collection itself a billion-RMB business opportunity. The fact that 4.47B RMB flowed to pure data vendors in a single year signals that data is maturing into an independent layer of the robotics stack, comparable to how labeled datasets fueled the LLM revolution. Four main collection routes exist: real-robot teleoperation (22 standalone players, the most), bodyless collection via wearables/mocap (15), simulation synthesis (only 2 standalones left as costs drop), and internet video distillation (1 player claiming costs at 0.5% of industry average). Notably, 43% of collection companies pursue multiple routes simultaneously, reflecting the industry's view that no single data source alone can satisfy training needs. The simulation route is shrinking due to the persistent sim2real gap in reproducing friction, deformation, and tactile feedback.

rss · 36氪 · Jul 12, 02:16

**Background**: Embodied Intelligence (具身智能) refers to AI systems that learn by interacting with the physical world through a robot body, integrating perception, action, and cognition. Unlike text-based LLMs, embodied models need sensorimotor data—joint torques, gripper forces, first-person video, tactile signals—which is far more expensive and time-consuming to collect than scraping web text. Companies like Tesla with Optimus have shifted from teleoperation toward large-scale video data collection to escape the limits of motion-capture suits, while open datasets such as Bridge and RT-1 have become standard benchmarks for training and evaluating generalist robot policies.

<details><summary>References</summary>
<ul>
<li><a href="https://juejin.cn/post/7486670839923359796">什 么 是 具 身 智 能 ？ 具 身 智 能 （ Embodied Intelligence...</a></li>
<li><a href="https://news.pedaily.cn/202606/565591.shtml">具身数据采集产业链调查：被机器人采集的人_投资界</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1905656875946612379">万字长文详解：五家主流具身智能开源数据集核心内容 - 知乎</a></li>

</ul>
</details>

**Tags**: `#embodied-AI`, `#robotics`, `#data-collection`, `#industry-analysis`, `#China-tech`

---

<a id="item-3"></a>
## [AI热潮太费电，燃气轮机价格3年涨了300%](https://36kr.com/newsflashes/3892556678543880?f=rss) ⭐️ 7.3/10

The AI boom's massive electricity demand has driven gas turbine prices up approximately 300% over three years, with major deals like Microsoft's $1.75B+ purchase from GE Vernova illustrating the severe energy infrastructure bottleneck facing data center expansion.

rss · 36氪 · Jul 12, 11:37

**Tags**: `#AI infrastructure`, `#energy`, `#data centers`, `#GE Vernova`, `#AI economics`

---

<a id="item-4"></a>
## [Mindwalk: 3D Codebase Map for Replaying AI Coding Agent Sessions](https://github.com/cosmtrek/mindwalk) ⭐️ 7.0/10

Developer cosmtrek has open-sourced Mindwalk, a tool that records AI coding agent sessions (such as Claude Code) and renders them as navigable 3D maps of a codebase, letting users spatially explore which files the agent read, edited, or wrote. As AI coding agents like Claude Code become mainstream, developers need better ways to audit, debug, and understand agent behavior beyond flat terminal logs. A spatial visualization paradigm could fundamentally reshape how humans interact with and trust autonomous coding agents. The tool captures reads, edits, and writes from agent sessions and projects them onto a 3D terrain/tree view of the codebase alongside a timeline. One reported limitation is that the tree/terrain view may not render when the original project is no longer present on the user's local drive.

hackernews · cosmtrek · Jul 12, 05:51 · [Discussion](https://news.ycombinator.com/item?id=48878682)

**Background**: Claude Code, released by Anthropic in February 2025, is an agentic command-line tool that lets developers delegate coding tasks via natural language prompts; it was made generally available in May 2025 alongside the Claude 4 model. Because the agent's work unfolds across many files in a non-linear fashion, following its activity in a terminal scrollback can be difficult. AI agent observability tools and session replay utilities are an emerging category aimed at making these workflows more transparent and auditable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://github.com/es617/claude-replay">GitHub - es617/claude-replay: Convert AI coding agent sessions (Claude Code, Cursor, Codex, Gemini, OpenCode) into self-contained, embeddable HTML replays · GitHub</a></li>

</ul>
</details>

**Discussion**: The community response is enthusiastic and forward-looking. Commenters suggest compelling future use cases such as comparing how different models traverse the same codebase or measuring run-to-run variance for the same model, one builder offered to integrate glyph-level file rendering from their own project (glyph3d.dev), and another likened the project to Xerox PARC-era explorations of new UI metaphors. A practical bug was also flagged: the terrain view appears empty when the source project no longer exists locally.

**Tags**: `#ai-agents`, `#developer-tools`, `#visualization`, `#claude-code`, `#show-hn`

---

<a id="item-5"></a>
## [RISCBoy is an open-source portable games console, designed from scratch](https://github.com/Wren6991/RISCBoy) ⭐️ 7.0/10

An open-source portable games console built from scratch around a custom RISC-V SoC, designed by Raspberry Pi ASIC engineer Luke Wren as a modern reimagining of the Gameboy Advance.

hackernews · mariuz · Jul 11, 21:58 · [Discussion](https://news.ycombinator.com/item?id=48876245)

**Tags**: `#RISC-V`, `#open-source-hardware`, `#ASIC-design`, `#embedded-systems`, `#retro-gaming`

---

<a id="item-6"></a>
## [FCC approves orbital space mirrors, first test satellites will launch this year — large spacecraft reflects sunlight to Earth’s surface for construction sites, search-and-rescue lighting, and more](https://www.tomshardware.com/tech-industry/fcc-approves-orbital-space-mirrors-first-test-satellites-will-launch-this-year-large-spacecraft-reflects-sunlight-to-earths-surface-for-construction-sites-search-and-rescue-lighting-and-more) ⭐️ 6.5/10

The FCC has approved a startup's experimental orbital mirror satellites that reflect sunlight to Earth, with first test launches planned for this year despite concerns from astronomers.

rss · Tom's Hardware · Jul 12, 12:20

**Tags**: `#space-technology`, `#FCC`, `#satellites`, `#orbital-mirrors`, `#commercial-space`

---

<a id="item-7"></a>
## [Apple Sues OpenAI Over Alleged Trade Secret Theft by Former Employees](https://www.solidot.org/story?sid=84806) ⭐️ 6.3/10

Apple has filed a lawsuit against OpenAI alleging that former employees, including OpenAI's Chief Hardware Officer Tang Tan and engineer Chang Liu, stole trade secrets related to unreleased hardware products. The complaint alleges that Tan coached new OpenAI hires on circumventing Apple's security protocols for departing employees, while Liu downloaded dozens of confidential files about engineering demonstrations, technical specifications, and private project data, exploited authentication vulnerabilities via colleagues' laptops, and left a 'LOL' message after the breach was discovered. The lawsuit highlights the intensifying talent war and trade secret battles in the AI era, as major tech companies race to protect proprietary hardware designs while employees migrate to AI-focused firms. It could set precedents for how non-compete and trade secret protections apply in the fast-moving AI hardware space. The complaint alleges Liu failed to return an Apple-issued laptop. In a separate story, Brown University economics professor Roberto Serrano moved finals to in-person after suspicious midterm results, only to see the final exam average plummet to 48.6%—a class historical low—with 18 students dropping the course. JAXA also announced on July 11 that its reusable rocket prototype RV-X completed a 40-second test flight reaching 11 meters altitude, performing liftoff, hovering, lateral movement, and vertical landing.

rss · Solidot · Jul 11, 16:40

**Background**: OpenAI has aggressively recruited hardware talent from Apple's design teams as it pursues its own hardware ambitions, a context that explains the specific allegations in this case. The Brown University anecdote reflects growing faculty concerns about generative AI tools enabling academic dishonesty in remote assessments. JAXA's RV-X is being developed as a successor to the expendable H-3 rocket to lower launch costs, with France and Germany joining the R&D collaboration, though Japan is widely seen as lagging behind China in reusable rocket development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aa.com.tr/en/asia-pacific/japan-tests-prototype-reusable-rocket/3994840">Anadolu Ajansı: Japan tests prototype reusable rocket</a></li>
<li><a href="https://en.wikipedia.org/wiki/Japanese_space_program">Japanese space program - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#OpenAI`, `#AI-cheating`, `#education`, `#JAXA`, `#reusable-rockets`, `#trade-secrets`

---

<a id="item-8"></a>
## [Terry Tao on Building Apps with Modern Coding Agents](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/) ⭐️ 6.0/10

Fields Medalist Terence Tao published a blog post sharing his experience using modern LLM-based coding agents to build applications, particularly interactive visualizations to supplement his mathematical papers. He concludes that these tools work well for non-mission-critical supplements where downside risk is acceptable. Tao's perspective carries significant weight given his stature in mathematics, and his pragmatic endorsement of coding agents for specific use cases helps legitimize AI-assisted development among domain experts. His balanced framing — distinguishing mission-critical from supplemental uses — adds a thoughtful voice to the broader debate about where AI coding tools fit in professional workflows. Tao explicitly frames his decision around risk tolerance, writing that supplements not mission-critical to a paper's core findings have acceptable downside risk for LLM-generated code. The focus is on interactive teaching and visualization aids rather than tools for core mathematical reasoning or proof verification.

hackernews · subset · Jul 12, 11:09 · [Discussion](https://news.ycombinator.com/item?id=48880170)

**Background**: AI coding agents are tools that go beyond simple code completion (such as early GitHub Copilot) by autonomously planning, executing, and iterating on multi-step coding tasks. Unlike autocomplete-style assistants, agents can build entire features or small applications from natural language descriptions, though accuracy varies significantly by task complexity and programming language. Terence Tao, a professor at UCLA, is widely regarded as one of the greatest living mathematicians and received the Fields Medal in 2006.

<details><summary>References</summary>
<ul>
<li><a href="https://codegen.com/guides/what-are-ai-coding-agents/">What Are AI Coding Agents ? A Beginner's Guide</a></li>
<li><a href="https://calmops.com/ai/ai-coding-agents-devin-2026-complete-guide/">AI Coding Agents and Devin 2026: The Complete Guide - Calmops</a></li>

</ul>
</details>

**Discussion**: The community response is largely positive and appreciative of Tao's balanced perspective. A CS professor shares parallel experiences using Claude to build teaching visualizations (including a simplified 8-bit computer), while others humorously note that even a Fields Medalist faces the same debugging frustrations as everyone else. Some commenters push back, observing that these examples are always hobby or supplemental projects rather than mission-critical work, prompting discussion about the limits of AI-assisted coding.

**Tags**: `#LLM-coding`, `#AI-assisted-development`, `#Terry Tao`, `#mathematics`, `#coding-agents`

---

<a id="item-9"></a>
## [Mesh LLM: distributed AI computing on iroh](https://www.iroh.computer/blog/mesh-llm) ⭐️ 6.0/10

Mesh LLM on iroh enables pooling VRAM across distributed consumer devices (laptops, desktops, servers) to collaboratively run large language models, though performance is limited by network bandwidth.

hackernews · tionis · Jul 11, 22:38 · [Discussion](https://news.ycombinator.com/item?id=48876505)

**Tags**: `#distributed-systems`, `#LLM-inference`, `#P2P`, `#iroh`, `#open-source`

---

<a id="item-10"></a>
## [Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) ⭐️ 6.0/10

Analysis of alleged circular financing between Nvidia and AI cloud providers like CoreWeave and Nebius, with community discussion largely challenging the premise and pointing to more substantive questions about GPU economics.

hackernews · adletbalzhanov · Jul 11, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48873836)

**Tags**: `#ai-infrastructure`, `#nvidia`, `#gpu-economics`, `#coreweave`, `#investment-analysis`

---

<a id="item-11"></a>
## [AIC Unveils 32-Bay E3 SSD JBOF for AI Key-Value Caching](https://www.servethehome.com/aic-gets-flashy-with-32-ssd-bay-jbof-server-for-key-value-caching/) ⭐️ 5.5/10

AIC has unveiled its F2032-01-G6, a 2U JBOF storage system that can house up to 32 EDSFF E3 SSDs. The enclosure is purpose-built to be paired with NVIDIA BlueField-4 DPUs, positioning it as a key-value caching appliance for AI infrastructure in the Rubin/Vera era. Key-value caching is essential for accelerating LLM inference by storing attention computations and reducing redundant recalculation, and dedicated DPU-managed storage tiers could meaningfully alleviate GPU memory pressure. This product signals how the storage industry is evolving toward disaggregated, compute-less flash enclosures tightly coupled with DPUs to serve emerging AI workloads. The F2032-01-G6 uses the EDSFF E3.S form factor, which delivers higher density and better thermal performance than legacy 2.5" U.2 drives. As a true JBOF, it has no onboard storage controller—offload, networking, and caching management are handled entirely by the externally attached BlueField-4 DPUs.

rss · ServeTheHome · Jul 11, 17:00

**Background**: A JBOF ('Just a Bunch of Flash') is a storage architecture that aggregates many NVMe SSDs into a single enclosure exposed over a high-speed fabric, without a traditional storage controller; compute is supplied externally. EDSFF E3.S is a newer SSD form factor designed for high-density, thermally efficient server and storage deployments, increasingly replacing 2.5" and M.2 drives in AI systems. NVIDIA BlueField DPUs—originally developed by Mellanox, acquired by NVIDIA in 2019—offload networking, storage, and security functions from host CPUs. Key-value (KV) caching stores intermediate attention computations during transformer inference to avoid redundant recomputation, and NVIDIA has positioned BlueField-4 as enabling a new memory tier dedicated to KV cache in AI data centers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ntchosting.com/encyclopedia/hosting/jbof/">JBOF Explained: High-Speed NVMe Flash Storage</a></li>
<li><a href="https://www.aewin.com/tech-blog-detail/230/">Introduction to NVMe SSD : Enhancing Server Performance and...</a></li>
<li><a href="https://learn-more.supermicro.com/data-center-stories/storage-technology-ai-inference-with-nvidia-bluefield-4">Supermicro New Storage Technology with NVIDIA BlueField ®- 4</a></li>

</ul>
</details>

**Tags**: `#storage`, `#JBOF`, `#SSD`, `#DPU`, `#AI-infrastructure`

---