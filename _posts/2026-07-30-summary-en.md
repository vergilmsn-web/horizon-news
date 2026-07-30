---
layout: default
title: "Horizon Summary: 2026-07-30 (EN)"
date: 2026-07-30
lang: en
---

> From 117 items, 20 important content pieces were selected

---

1. [Linux Kernel Patches Cut Steam Deck Game Stuttering by 31%](#item-1) ⭐️ 8.5/10
2. [Moonshot AI Reportedly Used Banned Nvidia Blackwell Chips to Train Kimi K3](#item-2) ⭐️ 8.5/10
3. [Document-borne AI worms can self-propagate through Copilot for Word](#item-3) ⭐️ 8.0/10
4. [Research: Long Policy Documents Fail to Govern AI Agents](#item-4) ⭐️ 8.0/10
5. [TSMC Fab 20 running 20k 2nm wpm](#item-5) ⭐️ 8.0/10
6. [HRL Demonstrates Self-Controlling Silicon Quantum Processor](#item-6) ⭐️ 7.5/10
7. [GlobalFoundries Gets $300M CHIPS Act Funding, U.S. Takes 1% Equity Stake](#item-7) ⭐️ 7.5/10
8. [Kioxia Announces UFS 5.0 Embedded Flash Memory Devices](#item-8) ⭐️ 7.5/10
9. [Seagate to start qualifying record-setting 50TB HDDs in 2027 — most drives are sold out through 2028](#item-9) ⭐️ 7.5/10
10. [DRAM Supply to Module Makers May Drop 70%+ by 2027, Apacer CEO Warns](#item-10) ⭐️ 7.5/10
11. [Intel Closes RAMP-C Defense Program Validating 18A Foundry Process](#item-11) ⭐️ 7.5/10
12. [Moonshot AI Kimi Closes $3.5B+ Series F at $35B Valuation](#item-12) ⭐️ 7.3/10
13. [微软新增数据中心租约超1300亿美元](#item-13) ⭐️ 7.3/10
14. [AI's Top Startups Are Increasingly Not Publishing Research](#item-14) ⭐️ 7.0/10
15. [The coolest use for the Vision Pro](#item-15) ⭐️ 7.0/10
16. [Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac](#item-16) ⭐️ 7.0/10
17. [Superlogical](#item-17) ⭐️ 7.0/10
18. [Dynamic AI Demands Drive Memory Diversity](#item-18) ⭐️ 7.0/10
19. [Photonics Shifts From Rack-Scale to Chiplet-Level Integration](#item-19) ⭐️ 7.0/10
20. [Synopsys demos autonomous design verification agents with Nvidia](#item-20) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Linux Kernel Patches Cut Steam Deck Game Stuttering by 31%](https://www.techpowerup.com/351189/linux-cpu-driver-patches-massively-reduce-game-stuttering-on-steam-deck) ⭐️ 8.5/10

Linux kernel developer David Vernet (of Meta) has submitted a new set of patches to the AMD P-State driver introducing an 'epp_boost' feature that implements per-core Energy Performance Preference (EPP) boosting for busy CPU cores. Early benchmarks show the patch can improve 1% low frame rates on AMD CPUs by as much as 31.8%, substantially reducing perceived game stuttering on Steam Deck and similar Linux gaming systems. 1% low frame rates are the primary indicator of perceived stutter and smoothness in games, and a ~31% improvement represents a massive quality-of-life gain for Steam Deck users and the broader Linux gaming community without requiring any hardware change. This kind of kernel-level optimization demonstrates how open-source driver work continues to close the gap between Linux and Windows gaming performance, directly benefiting Valve's SteamOS-based handheld. When epp_boost is enabled, a hook samples each core's C0 residency (delta MPERF over delta TSC) at most every 10 ms; if a core is at least 50% busy, its EPP field in MSR_AMD_CPPC_REQ is set to 'performance' (0) and held there until 300 ms pass without another busy sample. The patch is currently a proposed set on the linux-pm mailing list and has not yet been merged into the mainline kernel, meaning Steam Deck users would need to run a custom kernel or wait for upstream integration.

rss · TechPowerUp News · Jul 29, 15:44

**Background**: AMD P-State is the modern CPU frequency scaling driver for AMD processors on Linux, replacing the older acpi-cpufreq driver and offering more precise control over performance and energy states. The EPP (Energy Performance Preference) hint tells the processor how aggressively to trade power efficiency for performance; a lower EPP value favors performance, while a higher value favors efficiency. The 1% low metric refers to the average frame rate of the slowest 1% of frames, and is widely used as a proxy for stutter and smoothness rather than average FPS. Steam Deck, Valve's handheld gaming PC, runs SteamOS (a Linux distribution) on a custom AMD APU, making kernel-level AMD optimizations especially impactful for its user base.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/AMD-P-State-Better-1p-Lows">AMD P-State Linux Driver Patches Can Boost 1%-Low FPS Gaming Performance By 31% - Phoronix</a></li>
<li><a href="https://www.pcgamer.com/hardware/handheld-gaming-pcs/linux-kernel-patch-can-boost-the-steam-decks-1-percent-low-frame-rate-by-as-much-as-31-percent-in-early-testing/">Linux kernel patch can boost the Steam Deck's 1% low frame rate by as much as 31% in early testing | PC Gamer</a></li>
<li><a href="https://www.xda-developers.com/this-linux-kernel-patch-could-give-steamdeck-surprising-performance-boost/">This Linux kernel patch could give the Steam Deck a surprising performance boost</a></li>

</ul>
</details>

**Discussion**: Across coverage from Phoronix, PC Gamer, and XDA Developers, the reaction has been overwhelmingly positive, with commentators highlighting that a software-only ~31% 1% low improvement on existing hardware is exceptional and rare. Some technically-oriented readers have asked about potential power consumption and battery life trade-offs on the Steam Deck, noting that per-core EPP boosting could increase energy use during sustained loads, which matters more on a handheld than a desktop.

**Tags**: `#Linux`, `#AMD`, `#Steam Deck`, `#kernel`, `#performance`

---

<a id="item-2"></a>
## [Moonshot AI Reportedly Used Banned Nvidia Blackwell Chips to Train Kimi K3](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-moonshot-ai-reportedly-used-nvidia-blackwell-chips-for-training-kimi-k3-company-circumvented-both-u-s-export-and-chinese-import-controls-to-acquire-compute) ⭐️ 8.5/10

Moonshot AI reportedly used Nvidia Blackwell chips to train its Kimi K3 model, circumventing both U.S. export controls and Chinese import regulations. The company allegedly acquired restricted compute that should not have been legally accessible to Chinese AI labs. This story exposes significant gaps in the effectiveness of U.S. export controls designed to slow China's AI development, as Blackwell chips represent the most advanced AI training hardware currently in production. It also raises questions about Chinese enforcement of its own import restrictions and highlights the intensifying compute arms race between U.S. and Chinese frontier AI labs. Kimi K3 is a 2.8 trillion parameter open-weight multimodal reasoning model with a context window exceeding one million tokens. Nvidia Blackwell B100/B200 accelerators are built on TSMC's 3nm process node and have been a primary target of U.S. export restrictions to China since their unveiling.

rss · Tom's Hardware · Jul 29, 10:00

**Background**: The U.S. implemented sweeping semiconductor export controls on China in October 2022, subsequently expanded in 2023 and 2024, targeting advanced AI chips including Nvidia's H100 and Blackwell series, while coordinating with allies such as Japan and the Netherlands. Moonshot AI is one of China's leading AI startups, known for its Kimi chatbot and competitive open-weight large language models. The fact that Chinese companies allegedly circumvent domestic import restrictions as well reflects the dual pressures of U.S. containment efforts and Beijing's parallel push for semiconductor self-sufficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_New_Export_Controls_on_Advanced_Computing_and_Semiconductors_to_China">United States New Export Controls on Advanced Computing and Semiconductors to China - Wikipedia</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K3 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.congress.gov/crs-product/R48642">U.S. Export Controls and China: Advanced Semiconductors | Congress.gov | Library of Congress</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Nvidia`, `#ExportControls`, `#China`, `#Geopolitics`

---

<a id="item-3"></a>
## [Document-borne AI worms can self-propagate through Copilot for Word](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/) ⭐️ 8.0/10

Security researchers demonstrate how AI worms can self-propagate through Microsoft Copilot for Word via prompt injection embedded in shared documents, exploiting the conflation of instructions and data.

hackernews · Canopy9560 · Jul 29, 11:44 · [Discussion](https://news.ycombinator.com/item?id=49096188)

**Tags**: `#ai-security`, `#prompt-injection`, `#microsoft-copilot`, `#vulnerability-research`, `#llm-attacks`

---

<a id="item-4"></a>
## [Research: Long Policy Documents Fail to Govern AI Agents](https://arxiv.org/abs/2607.25398) ⭐️ 8.0/10

A new study titled 'Handbook.md' empirically demonstrates that long policy documents such as CLAUDE.md, AGENTS.md, and similar instruction files do not reliably govern the behavior of AI agents during real tasks. The paper benchmarks how well agents adhere to lengthy written policies and finds significant, systematic failure modes even when the policy is technically within the model's context window. This finding directly challenges a growing practice of teams relying on persistent instruction files to steer AI coding agents like Claude Code, Cursor, and Copilot in production workflows. If agents cannot reliably follow these documents, organizations may need to rethink governance strategies for AI-assisted software development, potentially shifting from declarative policy files toward runtime enforcement, smaller scoped instructions, or tool-based constraints. The paper frames instruction following as a benchmark problem where achieving superhuman adherence would imply superhuman cognitive capabilities, drawing a parallel to humans' own well-documented limits with long policy documents. Technical factors cited by the community include extreme KV-cache quantization in long contexts, aggressive sampler behavior in deployed inference stacks, and the fact that the relevant attention signal gets diluted as system prompts grow.

hackernews · spIrr · Jul 29, 13:01 · [Discussion](https://news.ycombinator.com/item?id=49096969)

**Background**: AI coding agents such as Claude Code, Codex, and Cursor are typically configured via plain-text instruction files placed in the project root (e.g., CLAUDE.md, AGENTS.md, .cursorrules, .github/copilot-instructions.md) that are prepended to the model's context on every turn. Developers treat these files as persistent project memory, encoding coding conventions, preferred libraries, and behavioral rules. The paper 'Handbook.md' tests the assumption that simply placing rules in such a file guarantees they will be followed, and finds that adherence degrades substantially as the policy grows longer and as the conversation proceeds. Related work has similarly shown that LLM instruction-following rates can drop by up to 61% with minor prompt perturbations and that instructions buried mid-prompt receive less attention than those at the beginning or end.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/data-science-collective/the-complete-guide-to-ai-agent-memory-files-claude-md-agents-md-and-beyond-49ea0df5c5a9">The Complete Guide to AI Agent Memory Files (CLAUDE.md, AGENTS.md, and Beyond)</a></li>
<li><a href="https://siliconopera.com/why-a-longer-system-prompt-usually-makes-llms-worse/">Why a Longer System Prompt Usually Makes LLMs... — Silicon Opera</a></li>
<li><a href="https://artoftruth.org/llm-instruction-following-compliance-gap/">LLM instruction following drops 61%: devastating AI crisis</a></li>

</ul>
</details>

**Discussion**: The discussion is largely convergent with the paper's findings. Top commenters attribute failures to engineering-level causes — extreme KV-cache quantization, lossy samplers, and long-context dilution — with one noting that local inference engines tend to preserve adherence much better than hosted APIs. A prominent practitioner reports that Claude follows CLAUDE.md instructions well for roughly ten minutes before bypassing them, while the same instructions delivered inline in the active prompt are obeyed reliably. Another commenter frames 'agentic AI' itself as a synthetic capability bolted on through post-training RL on curated datasets, arguing that any policy the lab did not specifically train for will be ignored by default.

**Tags**: `#AI-agents`, `#LLM-evaluation`, `#system-prompts`, `#context-windows`, `#alignment`

---

<a id="item-5"></a>
## [TSMC Fab 20 running 20k 2nm wpm](https://www.electronicsweekly.com/news/business/tsmc-fab-20-running-20k-2nm-wpm-2026-07/) ⭐️ 8.0/10

TSMC's Fab 20 has reached a production milestone of 20,000 wafers per month on its 2nm process, signaling ramp-up of leading-edge manufacturing capacity.

rss · Electronics Weekly · Jul 29, 05:38

**Tags**: `#TSMC`, `#semiconductors`, `#2nm`, `#fabrication`, `#manufacturing`

---

<a id="item-6"></a>
## [HRL Demonstrates Self-Controlling Silicon Quantum Processor](https://www.techpowerup.com/351204/hrl-demonstrates-a-silicon-quantum-processor-that-runs-itself) ⭐️ 7.5/10

HRL Laboratories published a paper in Nature demonstrating a silicon quantum processor integrated with custom cryogenic CMOS control chips that autonomously run quantum error correction routines, replacing racks of external control electronics with a chip placed next to the qubits in extreme cold. This addresses one of the central scalability obstacles in quantum computing: the unmanageable tangle of wiring and room-temperature electronics required to control the enormous number of qubits needed for useful machines. Integrating control electronics directly with the qubits is considered a critical step toward fault-tolerant quantum computing. The control chip operates at 3 K using CMOS technology compatible with silicon qubit fabrication, while the qubits themselves operate at ~20 mK. By placing the controller in the cryogenic environment next to the qubits, HRL eliminated the need for thousands of signal lines running between room temperature and the dilution refrigerator, and the system executed error correction autonomously without external intervention.

rss · TechPowerUp News · Jul 29, 19:44

**Background**: Quantum error correction is essential for building useful quantum computers because qubits are highly susceptible to noise and decoherence. Surface codes are a leading topological approach that encodes a single logical qubit across many physical qubits—for example, correcting any single-qubit error requires at least five physical qubits. Silicon spin qubits encode quantum information in the spin state of single electrons trapped in silicon nanostructures, and they are attractive because they can leverage the same CMOS fabrication ecosystem used in modern transistors. However, traditional control schemes rely on racks of room-temperature instruments connected to qubits via coaxial cabling, and this wiring complexity becomes a major bottleneck as qubit counts scale toward the thousands or millions needed for fault-tolerant operation. Cryogenic CMOS control chips, first demonstrated for simple qubit manipulation in 2021, aim to move that control hardware into the dilution refrigerator itself.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-021-03469-4">CMOS-based cryogenic control of silicon quantum circuits | Nature</a></li>
<li><a href="https://link.aps.org/doi/10.1103/PRXQuantum.5.010326">Using Cryogenic CMOS Control Electronics to Enable a Two-Qubit Cross-Resonance Gate | PRX Quantum</a></li>
<li><a href="https://en.wikipedia.org/wiki/Surface_code">Surface code - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#quantum-computing`, `#hardware`, `#silicon-photonics`, `#error-correction`, `#research-breakthrough`

---

<a id="item-7"></a>
## [GlobalFoundries Gets $300M CHIPS Act Funding, U.S. Takes 1% Equity Stake](https://www.techpowerup.com/351199/globalfoundries-receives-usd-300m-for-silicon-photonics-u-s-government-acquires-1-stake) ⭐️ 7.5/10

The U.S. Department of Commerce signed a letter of intent with GlobalFoundries under the Trump administration, awarding the company $300 million in CHIPS Act funding and acquiring approximately a 1% equity stake to advance next-generation silicon photonics technologies. This represents a notable policy shift as the U.S. government is taking direct equity stakes in semiconductor companies, while the investment signals the strategic importance of silicon photonics for AI infrastructure, where traditional electrical interconnects are becoming a bottleneck. The funding targets near-packaged optics (NPO), co-packaged optics (CPO), 3D hybrid bonding, and novel material development at GlobalFoundries' Malta, New York and Burlington, Vermont facilities. The company's SCALE (Silicon Photonics Co-Packaged Advanced Light Engine) platform already supports 400 Gb/s package transfers with high energy efficiency.

rss · TechPowerUp News · Jul 29, 17:30

**Background**: Silicon photonics is a technology that uses silicon as an optical medium to transmit data using light rather than electrical signals, enabling faster and more energy-efficient data transfer. Co-Packaged Optics (CPO) integrates optical engines directly adjacent to switch ASICs and accelerators, collapsing electrical distances from inches to millimeters to address the energy demands of AI workloads. GlobalFoundries notably exited leading-edge node research during the industry's transition to 7nm, but has since pivoted to silicon photonics and advanced packaging as growth areas driven by AI expansion.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Silicon_photonics">Silicon photonics - Wikipedia</a></li>
<li><a href="https://www.ansys.com/blog/what-is-co-packaged-optics">What is Co-packaged Optics?</a></li>
<li><a href="https://blogs.sw.siemens.com/semiconductor-packaging/2026/02/05/five-key-trends-of-co-packaged-optics-cpo-in-2026/">Five Key Trends of Co-Packaged Optics (CPO) in 2026 - Semiconductor Packaging</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#CHIPS-Act`, `#silicon-photonics`, `#GlobalFoundries`, `#AI-infrastructure`

---

<a id="item-8"></a>
## [Kioxia Announces UFS 5.0 Embedded Flash Memory Devices](https://www.techpowerup.com/351183/kioxia-announces-ufs-5-0-embedded-flash-memory-devices) ⭐️ 7.5/10

Kioxia announced its UFS 5.0 embedded flash memory solutions built on the JEDEC UFS 5.0 standard, offering 1 TB and 512 GB commercial samples with theoretical interface speeds up to 46.6 Gb/s per lane and approximately 10.8 GB/s effective dual-lane read/write performance. Mass production is planned by the end of 2026, and the devices will be demonstrated at FMS (the Future of Memory and Storage). As large language models, multimodal AI, and real-time inference move on-device, storage read performance has become a critical bottleneck for mobile and edge AI workloads. UFS 5.0 removes this bottleneck by roughly doubling the bandwidth of UFS 4.1, enabling faster model loading and greater responsiveness for next-generation smartphones and AI-enabled edge devices. The devices leverage MIPI M-PHY v6.0 physical layer and UniPro v3.0 protocol with HS-Gear6 operation, and use a serial interface that supports full-duplex concurrent read/write. The 10.8 GB/s figure represents effective throughput across dual lanes, a significant leap that directly addresses the data-movement demands of on-device LLMs and advanced imaging pipelines.

rss · TechPowerUp News · Jul 29, 08:39

**Background**: Universal Flash Storage (UFS) is a JEDEC-standard flash storage specification designed as a replacement for eMMC and SD cards in mobile phones, cameras, and consumer electronics, using a serial interface for full-duplex communication. UFS relies on layered protocols: the MIPI M-PHY physical layer handles high-speed signal transmission, while the MIPI UniPro protocol stack (structured similarly to OSI layers 1–4) manages data unit processing between the host and the storage device. The jump from UFS 4.1 to UFS 5.0 brings a new generation of M-PHY (v6.0) and UniPro (v3.0), enabling the much higher bandwidth required to feed data-hungry on-device AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/351183/kioxia-announces-ufs-5-0-embedded-flash-memory-devices">Kioxia Announces UFS 5 . 0 Embedded Flash Memory... | TechPowerUp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_Flash_Storage">Universal Flash Storage - Wikipedia</a></li>
<li><a href="https://www.mipi.org/specifications/unipro-specifications">MIPI UniPro | MIPI</a></li>

</ul>
</details>

**Tags**: `#storage`, `#UFS 5.0`, `#flash memory`, `#edge AI`, `#mobile hardware`

---

<a id="item-9"></a>
## [Seagate to start qualifying record-setting 50TB HDDs in 2027 — most drives are sold out through 2028](https://www.tomshardware.com/pc-components/hdds/seagate-to-start-qualifying-record-setting-50tb-hdds-in-2027-most-drives-are-sold-out-through-2028) ⭐️ 7.5/10

Seagate will begin qualifying 50TB HAMR hard drives in late 2027 with shipments in 2028, as AI-driven demand keeps production largely sold out through 2028.

rss · Tom's Hardware · Jul 29, 16:40

**Tags**: `#storage`, `#HAMR`, `#Seagate`, `#hard-drives`, `#AI-infrastructure`

---

<a id="item-10"></a>
## [DRAM Supply to Module Makers May Drop 70%+ by 2027, Apacer CEO Warns](https://www.tomshardware.com/pc-components/ram/dram-chip-supply-to-module-makers-could-drop-by-more-than-70-percent-year-on-year-in-2027-says-apacer-ceo-demand-for-hbm-and-server-ram-continues-to-devour-manufacturing-capacity) ⭐️ 7.5/10

Apacer CEO C.K. Chang warned that DRAM chip allocations to independent module makers could fall to just 30% of 2026 levels by 2027, representing a year-on-year drop of more than 70%. The shortage is driven by surging AI-driven demand for High Bandwidth Memory (HBM) and server RAM, which is consuming the lion's share of wafer capacity at major DRAM manufacturers. If this forecast materializes, it would severely constrain supply for consumer-facing memory products such as SSDs, DDR4/DDR5 modules, and mobile DRAM, likely pushing prices sharply higher for end users and PC builders. The shift underscores how AI infrastructure demand is reshaping the entire memory supply chain, with downstream non-AI customers bearing the cost of capacity reallocation. The warning specifically targets independent module makers, which buy DRAM chips from giants like Samsung, SK Hynix, and Micron, rather than memory divisions within those IDMs. HBM production uses 3D-stacked DRAM dies via through-silicon vias, meaning each HBM unit consumes far more wafer area than conventional DDR chips, amplifying the capacity squeeze on standard DRAM.

rss · Tom's Hardware · Jul 29, 10:30

**Background**: DRAM (Dynamic Random-Access Memory) is the primary volatile memory used in computers, servers, and mobile devices. High Bandwidth Memory (HBM) is a specialized 3D-stacked variant that delivers vastly higher bandwidth at lower power, making it essential for AI GPUs and accelerators from companies like NVIDIA and AMD. Major DRAM manufacturers — Samsung, SK Hynix, and Micron — allocate their wafer fabrication capacity across product lines, and growing HBM orders are progressively diverting capacity away from conventional DDR4, DDR5, and LPDDR products. Independent module makers such as Apacer purchase DRAM chips from these fabs to assemble retail memory modules and SSDs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.msn.com/en-gb/money/other/dram-chip-supply-to-memory-module-makers-could-drop-by-more-than-70-in-2027-says-apacer-ceo/ar-AA28YDsr">DRAM chip supply to memory module makers could drop by more...</a></li>
<li><a href="https://supplyics.com/insights/market-intelligence/2026-hbm-dram-memory-supply-chain-analysis/">2026 HBM and DRAM Supply Chain Analysis: Navigating... - SupplyICs</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#HBM`, `#AI infrastructure`, `#supply chain`, `#memory pricing`

---

<a id="item-11"></a>
## [Intel Closes RAMP-C Defense Program Validating 18A Foundry Process](https://www.tomshardware.com/tech-industry/intel-closes-out-the-defense-program-that-paid-nvidia-and-others-to-run-test-chips-on-18a) ⭐️ 7.5/10

Intel Foundry announced it has completed RAMP-C, a U.S. defense program originally awarded to the company in 2021, which paid external partners including Nvidia to run test chips on Intel's 18A process node. The program was designed to establish a domestic leading-edge chip manufacturing ecosystem for secure national-security applications. RAMP-C's completion is a credibility milestone for Intel's foundry ambitions, demonstrating that major chip designers like Nvidia validated Intel's 18A process. It also advances the U.S. strategic goal of reducing reliance on Asian foundries like TSMC for leading-edge defense and commercial silicon. Intel 18A is a 1.8nm-class process that introduces RibbonFET (gate-all-around) transistors and PowerVia backside power delivery, technologies aimed at returning Intel to the forefront of semiconductor manufacturing. The program specifically targeted secure domestic production on advanced processes rather than purely commercial volume.

rss · Tom's Hardware · Jul 29, 09:30

**Background**: The RAMP-C program was created as part of U.S. efforts to ensure domestic access to leading-edge chip manufacturing for defense and national-security workloads, amid concerns about supply-chain concentration in Taiwan and South Korea. Intel's 18A node represents the company's most advanced manufacturing process, competing with TSMC's N2 and Samsung's 2nm offerings in the 1.8nm-class generation. Foundry services, where a chip designer pays a third party to manufacture its designs, have become a strategic battleground as Intel attempts to compete with the dominant TSMC.

<details><summary>References</summary>
<ul>
<li><a href="https://www.globalsmt.net/advanced-packaging/intel-reaches-3nm-milestone/">Intel reaches 3nm milestone - Electronics Manufacturing News</a></li>
<li><a href="https://wccftech.com/tsmc-wins-intel-order-for-two-3nm-cpus-to-regain-market-share-lost-to-amd/">TSMC Wins Intel Order For Two 3nm CPUs To Regain Market Share...</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#semiconductors`, `#RAMP-C`, `#chip-manufacturing`, `#national-security`

---

<a id="item-12"></a>
## [Moonshot AI Kimi Closes $3.5B+ Series F at $35B Valuation](https://36kr.com/p/3916547493965442?f=rss) ⭐️ 7.3/10

Moonshot AI has completed a Series F funding round exceeding $3.5 billion, bringing its post-money valuation to $35 billion, with the round closed early after being oversubscribed by more than 3x. The originally planned August Series G (Pre-IPO) has also been pulled forward, with its pre-money valuation rising to $50 billion. Separately, Alibaba's enterprise service arm Lingyang launched four 'AI employee' agents via its AgentOne platform, and UMC announced a new Tainan fab to meet AI chip demand. This is one of the largest AI funding rounds globally and signals overwhelming investor confidence in Chinese large language model companies, with Moonshot accelerating its IPO timeline. The Lingyang AgentOne deployment and UMC's new fab illustrate the broader commercialization of AI agents and the hardware build-out supporting AI demand across China's tech ecosystem. Moonshot AI is one of China's six 'AI Tigers,' founded in Beijing to compete with U.S. frontier AI labs. Lingyang's AgentOne uses Forward Deployment Engineers (FDEs) — a Palantir-style role where engineers embed with customers to build custom solutions — to help enterprises create tailored 'X-employees' alongside the four out-of-the-box agents for sales, customer service, operations, and marketing.

rss · 36氪 · Jul 29, 11:04

**Background**: Moonshot AI is a Beijing-based AI startup and one of China's six 'AI Tigers,' the group of well-funded Chinese AI labs competing to build frontier models comparable to OpenAI or Anthropic. Its Kimi model line has gained attention for its long-context capabilities. The FDE (Forward Deployment Engineer) role originated at Palantir and involves engineers embedding directly with enterprise customers to build tailored software, rather than selling or consulting. Lingyang is Alibaba Cloud's enterprise data and AI service brand, positioning AgentOne as a platform for deploying AI 'digital employees' into real business workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://www.aibase.com/news/21570">Alibaba Lingyang Launches AgentOne Platform to Promote...</a></li>
<li><a href="https://www.futureventures.ca/insights/understanding-the-forward-deployed-engineering-model">Understanding the Forward Deployed Engineering ( FDE ) Model</a></li>

</ul>
</details>

**Tags**: `#AI funding`, `#Moonshot AI`, `#semiconductor`, `#Chinese tech`, `#AI agents`

---

<a id="item-13"></a>
## [微软新增数据中心租约超1300亿美元](https://36kr.com/newsflashes/3917435911007621?f=rss) ⭐️ 7.3/10

Microsoft disclosed over $130 billion in new unfulfilled data center lease commitments in Q4, bringing total lease commitments to $329.1 billion, signaling accelerating AI compute infrastructure expansion.

rss · 36氪 · Jul 30, 01:01

**Tags**: `#Microsoft`, `#AI Infrastructure`, `#Data Centers`, `#Cloud Computing`, `#AI Investment`

---

<a id="item-14"></a>
## [AI's Top Startups Are Increasingly Not Publishing Research](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research) ⭐️ 7.0/10

A Science magazine analysis reveals that leading AI startups are publishing significantly less research than in previous years, with competitive pressures and intellectual property protection cited as primary reasons. The underlying study uses citation counts as a proxy for measuring research output among AI unicorn companies. This trend widens the gap between industry and academic AI research, potentially slowing the broader scientific community's access to breakthrough methods and making it harder for independent researchers to verify or build upon cutting-edge work. It also signals a fundamental shift away from the open-research ethos that originally defined the AI field. The underlying study measures publications through citation counts rather than direct paper counts, with OpenAI topping the list followed by MEGVII, Hugging Face, Waymo, Momenta, Preferred Networks, Anthropic, Owkin, Databricks, and Aibee. Google is notably excluded because it is not classified as a unicorn company, and the authors acknowledge that citations serve as an imperfect proxy for research significance.

hackernews · YeGoblynQueenne · Jul 29, 21:25 · [Discussion](https://news.ycombinator.com/item?id=49103285)

**Background**: AI research transparency has traditionally been a hallmark of the field, with organizations like OpenAI originally founded on principles of open research. The shift toward closed research practices has accelerated as competition between AI companies intensified, particularly after the launch of large language models like GPT-3 and GPT-4. Startups face a strategic dilemma: publishing innovations can attract talent and credibility but also exposes proprietary methods to competitors who may rapidly replicate them. The use of citations as a research output proxy has inherent limitations, as citations can be inflated by self-citations, media hype, or reviewer networks rather than purely reflecting scientific significance.

**Discussion**: Commenters with direct startup experience strongly validated the article's thesis, with one person explaining their current startup no longer publishes because of prior publishing friction and fear of having six months of work copied by OpenAI or Anthropic. Another commenter highlighted a founder who proactively published research on recursive self-improvement before YC selection, while broader concerns were raised about the 'blogification' of AI research and claims backed by numbers from potentially gamified experimental environments. One helpful commenter clarified the underlying paper's methodology, explaining which companies were included and why Google was excluded.

**Tags**: `#AI research`, `#industry-vs-academia`, `#transparency`, `#AI startups`, `#research publishing`

---

<a id="item-15"></a>
## [The coolest use for the Vision Pro](https://christianselig.com/2026/07/vision-pro-house/) ⭐️ 7.0/10

A practical showcase of using Vision Pro to walk through a fully-designed home in VR before construction, with community discussion confirming widespread adoption of similar workflows in architectural design firms.

hackernews · robbiet480 · Jul 29, 20:39 · [Discussion](https://news.ycombinator.com/item?id=49102774)

**Tags**: `#vision-pro`, `#vr-ar`, `#architecture`, `#design-tools`, `#spatial-computing`

---

<a id="item-16"></a>
## [Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac](https://github.com/drumih/turbo-fieldfare) ⭐️ 7.0/10

An open-source Swift/Metal inference engine called TurboFieldfare that runs Gemma 4 26B (MoE) on any M-series Mac using only 2GB RAM by streaming only the required routed experts from SSD while keeping shared weights and KV cache resident.

hackernews · gitpusher42 · Jul 29, 15:05 · [Discussion](https://news.ycombinator.com/item?id=49098510)

**Tags**: `#ai-inference`, `#apple-silicon`, `#mixture-of-experts`, `#edge-ai`, `#open-source`

---

<a id="item-17"></a>
## [Superlogical](https://www.superlogical.com/) ⭐️ 7.0/10

Mitchell Hashimoto launches Superlogical, a new company that builds on the open-source Ghostty terminal emulator (donated to a non-profit) as a terminal infrastructure platform.

hackernews · yan · Jul 29, 15:41 · [Discussion](https://news.ycombinator.com/item?id=49098965)

**Tags**: `#open-source`, `#ghostty`, `#mitchell-hashimoto`, `#terminal`, `#startup`

---

<a id="item-18"></a>
## [Dynamic AI Demands Drive Memory Diversity](https://www.eetimes.com/dynamic-ai-demands-drive-memory-diversity/) ⭐️ 7.0/10

EE Times analysis on how AI workloads are sharpening memory trade-offs between capacity, latency, and power rather than creating entirely new memory categories.

rss · EE Times · Jul 29, 18:00

**Tags**: `#AI infrastructure`, `#memory architecture`, `#hardware`, `#data center`, `#semiconductors`

---

<a id="item-19"></a>
## [Photonics Shifts From Rack-Scale to Chiplet-Level Integration](https://www.eetimes.com/from-co-packaged-optics-to-nanolasers-photonics-moves-inward/) ⭐️ 7.0/10

CEA-Leti, Scintil Photonics, and NcodiN are each advancing optical interconnect technology from data center rack scale toward co-packaged optics and chiplet-level communication, with NcodiN demonstrating silicon photonic chips integrating nanolasers that achieve energy efficiency below 0.1 pJ/bit. As AI workloads drive exponential growth in chip-to-chip bandwidth, traditional electrical interconnects are becoming bottlenecks; moving photonics inward to the package and chiplet level promises dramatic improvements in energy efficiency, bandwidth density, and latency, directly impacting the scalability of next-generation AI accelerators and data center architectures. Co-packaged optics integrates lasers, photonic engines, and fiber connectors directly alongside ASICs or switches within the same package, while optical I/O takes this further as a chiplet-based interconnect packaged into a single IC; NcodiN's approach combines an FPGA controller with on-chip nanolasers, achieving sub-0.1 pJ/bit energy efficiency.

rss · EE Times · Jul 29, 08:02

**Background**: Co-Packaged Optics (CPO) is an advanced packaging technology that places optical components such as lasers, modulators, and fiber connectors directly next to electronic chips (e.g., switches or ASICs) within a single package, as opposed to traditional pluggable optical modules that sit at the board level. A chiplet is a small integrated circuit die designed to be combined with other chiplets in a package to form a larger system, enabling modular scaling. Optical I/O extends this concept by packaging chiplet-based optical interconnects into a single IC, supporting standardized interfaces like UCIe Optical. Nanolasers are extremely small semiconductor lasers that can be integrated directly on silicon photonic chips, potentially enabling fully on-chip light generation for communication. Together, these technologies represent a push to bring optical signaling as close to the compute as possible to overcome the limitations of copper interconnects in high-bandwidth AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://chiplet-marketplace.com/wiki/co-packaged-optics">Co - Packaged Optics - Semi IP Hub Wiki</a></li>
<li><a href="https://picmagazine.net/article/124637/Ncodin’s_nanolasers_eye_AI_infrastructure">Ncodin’s nanolasers eye AI infrastructure - Photonic Integrated ...</a></li>
<li><a href="https://ayarlabs.com/blog/demystifying-optical-i-o-12-key-terms-to-know/">Demystifying Optical I/O: 12 Key Terms to Know | Ayar Labs</a></li>

</ul>
</details>

**Tags**: `#photonics`, `#co-packaged-optics`, `#chiplets`, `#semiconductors`, `#optical-interconnects`

---

<a id="item-20"></a>
## [Synopsys demos autonomous design verification agents with Nvidia](https://www.electronicsweekly.com/news/business/synopsys-unveils-autonomous-workflows-agents-2026-07/) ⭐️ 7.0/10

On the first anniversary of its Ansys acquisition, Synopsys demonstrated autonomous design verification agents for EDA and CAE workflows, developed in partnership with Nvidia using the NVIDIA Agent Toolkit and CUDA-X libraries. This marks one of the first production-grade deployments of agentic AI in the chip design and simulation pipeline, potentially reshaping how engineers perform verification, thermal analysis, and multi-physics simulation. It also validates the strategic logic of the multi-billion-dollar Ansys acquisition by tying simulation directly into an AI-driven design loop. The agents target a fully autonomous CAE workflow for electronics thermal analysis, leveraging Nvidia's GPU-accelerated compute stack. The announcement lands alongside broader industry momentum — including Siemens' competing agentic platform at DAC 2026 — indicating agentic AI is rapidly moving from demo to deployment in EDA.

rss · Electronics Weekly · Jul 29, 15:28

**Background**: EDA (Electronic Design Automation) refers to the software tools used to design and verify semiconductors, while CAE (Computer-Aided Engineering) covers broader simulation of physical phenomena such as thermal, structural, and electromagnetic behavior — historically Ansys's stronghold. Synopsys completed its roughly $35 billion acquisition of Ansys in mid-2025 to merge chip-design tooling with multi-physics simulation. Agentic AI refers to autonomous AI systems that can plan, invoke tools, and execute multi-step engineering tasks with minimal human supervision, as opposed to traditional chatbots that only respond to prompts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.engineering.com/synopsys-and-nvidia-advance-agentic-ai-for-chip-design/">Synopsys and NVIDIA advance agentic AI for chip design</a></li>
<li><a href="https://www.forbes.com/sites/marcochiappetta/2025/07/18/synopsys-finalizes-ansys-acquisition-to-enable-leading-simulation-enhanced-design/">Synopsys Ansys Acquisition Enables Leading Simulation Enhanced...</a></li>
<li><a href="https://www.techtimes.com/articles/321690/20260727/dac-2026-live-ai-chip-design-agents-hit-production-nobel-laureate-joins-debate.htm">DAC 2026 Live: AI Chip Design Agents Hit Production as Nobel...</a></li>

</ul>
</details>

**Tags**: `#EDA`, `#Synopsys`, `#Nvidia`, `#autonomous-agents`, `#chip-design`

---