---
layout: default
title: "Horizon Summary: 2026-08-26 (EN)"
date: 2026-08-26
lang: en
---

> From 122 items, 20 important content pieces were selected

---

1. [d-Matrix Raptor: First 3D-Stacked DRAM AI Accelerator Hits 100 TB/s](#item-1) ⭐️ 8.5/10
2. [OpenAI’s 700W Jalapeño ASIC outpaces 1,400W Nvidia flagship GPU — claims up to 1.9x throughput per kilowatt and 3.6x lower latency, co-developed with Broadcom](#item-2) ⭐️ 8.5/10
3. [Intel Details Crescent Island AI Accelerator at Hot Chips 2026](#item-3) ⭐️ 8.5/10
4. [Memory Prices Soar; DRAM and NAND to Drive 68% of CSP CapEx by 2027](#item-4) ⭐️ 7.5/10
5. [(PR) Apple Introduces New Mac Studio with M5 Max and M5 Ultra](#item-5) ⭐️ 7.5/10
6. [Fujitsu Monaka CPU: 144-core Arm server chip with chiplet cache and dual 256-bit SVE2](#item-6) ⭐️ 7.5/10
7. [OXMIQ outlines narrow use cases for High Bandwidth Flash at Hot Chips 2026](#item-7) ⭐️ 7.5/10
8. [Arm Unveils AGI Server CPU: 136 Cores, UCIe Chiplets at Hot Chips](#item-8) ⭐️ 7.5/10
9. [EPA Proposes Removing Public Input on Air Pollution Permits for Data Centers](#item-9) ⭐️ 7.5/10
10. [Samsung Unveils LPDDR5X-PIM with In-Memory Logic at Hot Chips 2026](#item-10) ⭐️ 7.5/10
11. [Intel Wildcat Lake: 18A Budget Chips with UCIe Chiplet Integration](#item-11) ⭐️ 7.5/10
12. [Google Unveils 8th-Gen TPU Family at Hot Chips 2026](#item-12) ⭐️ 7.5/10
13. [Microsoft to Detail Maia 200 AI Accelerator at Hot Chips 2026](#item-13) ⭐️ 7.5/10
14. [Cerebras Talks Going Rack-Scale with Their WSEs at Hot Chips 2026](#item-14) ⭐️ 7.5/10
15. [NVIDIA Integrates Groq 3 LPUs with Vera Rubin for Heterogeneous AI Compute](#item-15) ⭐️ 7.5/10
16. [Global Ocean Surface Temperatures Hit Record High Amid Climate Change](#item-16) ⭐️ 7.3/10
17. [AWS Acquires DuckDB](#item-17) ⭐️ 7.0/10
18. [Qwen3.8-Flash-Next: 176B MoE Preview of Qwen4 Architecture](#item-18) ⭐️ 7.0/10
19. [Fake US thinktank set up and funded by Israel sought to game AI for propaganda](#item-19) ⭐️ 7.0/10
20. [XCancel and Nitter are receiving C&D letters from XCorp](#item-20) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [d-Matrix Raptor: First 3D-Stacked DRAM AI Accelerator Hits 100 TB/s](https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card) ⭐️ 8.5/10

At Hot Chips 2026, d-Matrix unveiled Raptor, the first 3D DRAM AI accelerator for generative inference, which bonds a TSMC 4nm compute die face-to-face at a 36-micron pitch directly on top of a custom DRAM die, delivering 100 TB/s of memory bandwidth per card. This architecture delivers roughly an order-of-magnitude more bandwidth than current HBM-based accelerators like the H100 (~3.35 TB/s) and B200 (~8 TB/s), directly tackling the memory bandwidth wall that bottlenecks large language model inference. By eliminating HBM and interposers, d-Matrix also claims one-sixth the energy per bit of HBM3, which could reshape cost-efficiency metrics for generative AI serving at scale. Raptor uses face-to-face microbump bonding at a 36-micron pitch, which is looser than bleeding-edge hybrid bonding (sub-10 µm) but is described by d-Matrix as a proven, high-yield process. The compute die sits directly atop the DRAM, eliminating the silicon interposer, through-silicon vias, and HBM stacking steps used in conventional designs.

rss · Tom's Hardware · Aug 26, 12:00

**Background**: Modern AI accelerators typically rely on High Bandwidth Memory (HBM), which stacks DRAM dies vertically and connects them to a logic die via a silicon interposer and through-silicon vias. Face-to-face 3D stacking is an alternative integration approach in which two dies are bonded with their active surfaces facing each other, enabling denser interconnect at lower latency and power. Generative AI inference—running models such as LLMs to produce text—is heavily bandwidth-bound, since the model weights must be streamed from memory for every token generated. Hot Chips is a prestigious annual semiconductor conference where companies present cutting-edge chip architectures to the technical community.

<details><summary>References</summary>
<ul>
<li><a href="https://www.servethehome.com/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026/">d-Matrix Raptor 3D-DRAM Accelerator for Generative Inference at Hot Chips 2026 - ServeTheHome</a></li>
<li><a href="https://www.techtimes.com/articles/325300/20260824/d-matrix-raptor-delivers-100-tb-s-stacked-dram-fraction-hbm-energy-cost.htm">d-Matrix Raptor Delivers 100 TB/s From Stacked DRAM at Fraction of HBM Energy Cost</a></li>

</ul>
</details>

**Tags**: `#AI accelerators`, `#3D stacking`, `#DRAM`, `#semiconductors`, `#Hot Chips 2026`

---

<a id="item-2"></a>
## [OpenAI’s 700W Jalapeño ASIC outpaces 1,400W Nvidia flagship GPU — claims up to 1.9x throughput per kilowatt and 3.6x lower latency, co-developed with Broadcom](https://www.tomshardware.com/tech-industry/semiconductors/openai-says-its-jalapeno-chip-beats-nvidias-gb300-in-first-published-benchmarks) ⭐️ 8.5/10

OpenAI unveiled first benchmarks of its Jalapeño ASIC claiming 1.9x throughput per kilowatt and 3.6x lower latency versus Nvidia's GB300, co-developed with Broadcom.

rss · Tom's Hardware · Aug 25, 18:05

**Tags**: `#AI hardware`, `#ASIC`, `#OpenAI`, `#Nvidia`, `#semiconductors`

---

<a id="item-3"></a>
## [Intel Details Crescent Island AI Accelerator at Hot Chips 2026](https://www.tomshardware.com/pc-components/gpus/hot-chips-2026-intel-dives-deep-on-crescent-island-ai-accelerator-larger-caches-and-deeper-xmx-engines-target-maximum-ai-flops-per-watt) ⭐️ 8.5/10

At Hot Chips 2026, Intel unveiled detailed architecture for its Crescent Island AI accelerator, built on the Xe3P architecture with up to 32 Xe cores, deeper XMX matrix engines, larger caches, HBM4 memory support, and liquid cooling, targeting maximum AI FLOPS per watt for data center inference workloads. Crescent Island represents Intel's bid to re-enter the competitive AI accelerator market dominated by NVIDIA and AMD. By stripping out graphics-specific hardware (3D and ray-tracing) and dedicating silicon to AI compute, Intel is signaling a focused, efficiency-first strategy targeting the rapidly growing inference market, particularly agentic AI workloads. Each of Crescent Island's 32 Xe cores contains 8 Vector Engines and 8 XMX Engines, yielding 256 of each across the full GPU; the design removes 3D and ray-tracing units to free silicon for AI. Intel also revealed a 350W PCIe variant and support for up to 480GB of memory, while XMX engines execute DPAS instructions on 2D systolic arrays for matrix multiplication acceleration.

rss · Tom's Hardware · Aug 25, 15:12

**Background**: Hot Chips is a prestigious annual semiconductor conference where companies present deep architectural details of upcoming chips. XMX (Xe Matrix Extensions) are Intel's dedicated AI matrix multiplication engines, analogous to NVIDIA Tensor Cores, executing Dot Product Accumulate Systolic (DPAS) instructions on 2D systolic arrays and offering up to 16x AI inference compute versus traditional GPU paths. HBM4 (High Bandwidth Memory 4) is the next generation of 3D-stacked DRAM that provides significantly higher bandwidth, critical for feeding large AI models. Xe3P is Intel's third-generation Xe architecture, and by removing graphics-only blocks, Intel creates a datacenter-focused variant optimized purely for AI throughput per watt.

<details><summary>References</summary>
<ul>
<li><a href="https://videocardz.com/newz/intel-details-xe3p-gpu-architecture-crescent-island-gets-up-to-480gb-memory-and-350w-pcie-variant">Intel details Xe3P GPU architecture, Crescent Island gets up to 480GB memory and 350W PCIe variant - VideoCardz.com</a></li>
<li><a href="https://wccftech.com/intel-crescent-island-gpus-32-xe3p-cores-for-agentic-ai-low-cost-lpddr5x-up-to-480-gb/">Intel Crescent Island GPUs Pack Up To 32 Xe3P Cores, Optimized For Agentic AI With Low-Cost LPDDR5X That Reaches Up To 480 GB Capacity</a></li>
<li><a href="https://www.intel.com/content/www/us/en/support/articles/000091112/graphics.html">What is Xe Matrix eXtensions (XMX)? - Intel</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#AI accelerator`, `#Hot Chips 2026`, `#GPU`, `#data center`, `#HBM4`

---

<a id="item-4"></a>
## [Memory Prices Soar; DRAM and NAND to Drive 68% of CSP CapEx by 2027](https://www.techpowerup.com/351976/memory-prices-soar-dram-and-nand-flash-to-account-for-68-of-major-csp-capex-in-2027) ⭐️ 7.5/10

TrendForce forecasts that major cloud service providers' total CapEx will surge 98% year-over-year in 2026 and another 50% in 2027, driven by soaring memory prices and AI infrastructure demand. DRAM and NAND Flash combined will account for 47% of CSP CapEx in 2026 and rise to 68% by 2027. This signals a fundamental reshaping of cloud infrastructure economics, where memory—not compute—becomes the dominant cost line item for hyperscalers. The dramatic price increases will affect AI deployment costs, profit margins of cloud providers, and the broader hardware supply chain, potentially squeezing budgets for GPUs and networking gear. Server DRAM contract prices already rose 64% in 2H25 and are projected to jump another ~270% in 2026, while enterprise SSD prices climbed ~35% in 2H25 with a cumulative 235% surge expected in 2026. These figures reflect contract pricing for high-volume procurement, not spot market rates.

rss · TechPowerUp News · Aug 26, 09:21

**Background**: DRAM (Dynamic Random-Access Memory) is the volatile main memory used by CPUs and GPUs for fast data access, while NAND Flash is the non-volatile storage technology behind SSDs and memory cards. Enterprise SSDs are high-endurance, high-performance drives designed for data center workloads, differing from consumer SSDs in reliability and durability requirements. Cloud Service Providers (CSPs) such as AWS, Microsoft Azure, and Google Cloud operate massive data centers and are the largest buyers of server memory. HBM (High Bandwidth Memory), a specialized form of DRAM, is particularly critical for AI accelerator GPUs, which helps explain why memory demand is rising so sharply as AI training and inference workloads scale.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flash_memory">Flash memory - Wikipedia</a></li>
<li><a href="https://www.crucial.com/articles/for-businesses/consumer-ssds-vs-enterprise-ssds">Consumer vs. Enterprise SSDs: What’s the Difference</a></li>
<li><a href="https://medium.com/@junyoungshin0122/the-evolution-toward-high-bandwidth-memory-hbm-601d38ce2917">Why Memory Matters: The Role of DRAM, NAND Flash, and HBM in Modern Computing | by June_0 | Medium</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#NAND Flash`, `#Cloud Infrastructure`, `#AI Hardware`, `#Memory Market`

---

<a id="item-5"></a>
## [(PR) Apple Introduces New Mac Studio with M5 Max and M5 Ultra](https://www.techpowerup.com/351920/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra) ⭐️ 7.5/10

Apple announces new Mac Studio with M5 Max and M5 Ultra chips, featuring up to 512 GB unified memory and claiming 4.3x faster AI performance, enabling on-device execution of large LLMs.

rss · TechPowerUp News · Aug 25, 13:51

**Tags**: `#apple`, `#hardware`, `#M5 Ultra`, `#on-device AI`, `#local LLM inference`

---

<a id="item-6"></a>
## [Fujitsu Monaka CPU: 144-core Arm server chip with chiplet cache and dual 256-bit SVE2](https://www.tomshardware.com/pc-components/cpus/fujitsus-monaka-cpu-stacks-its-entire-cache-on-a-separate-5nm-die-and-narrows-to-256-bit-sve2) ⭐️ 7.5/10

At Hot Chips 2026 on August 24, Fujitsu unveiled detailed specifications of its 144-core Monaka Arm server CPU, confirming it uses dual 256-bit SVE2 vector units—down from the 512-bit SVE in its A64FX predecessor—and places all cache on a separate 5nm die in a chiplet configuration, with 350W and 500W SKUs slated for release in 2027. Monaka represents Fujitsu's first chiplet-based design and signals a strategic move away from the ultra-wide vector approach pioneered by A64FX (which powered the Fugaku supercomputer). The narrower 256-bit SVE2 reflects Arm ecosystem trends toward broader workload coverage, including AI and cloud, beyond pure HPC. The separate 5nm cache die allows Fujitsu to optimize compute and cache dies independently, likely improving yield and flexibility. The reduction from 512-bit SVE to dual 256-bit SVE2 halves per-core peak vector throughput in exchange for better power efficiency and broader application support.

rss · Tom's Hardware · Aug 26, 13:30

**Background**: Fujitsu's A64FX was the first processor to implement Arm's Scalable Vector Extension (SVE), and it powered Japan's Fugaku supercomputer, which topped the TOP500 list from 2020 to 2022. SVE2 is the successor extension that adds broader data-processing instructions including machine learning and DSP workloads. Chiplet design is an increasingly common approach in modern CPUs, where multiple smaller dies are integrated into a single package to improve manufacturing yield, reduce cost, and enable mixing of different process nodes—Monaka's use of a 5nm cache die alongside its compute die is a textbook example of this trade-off.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fujitsu_A64FX">Fujitsu A64FX - Wikipedia</a></li>
<li><a href="https://chipsandcheese.com/p/hot-chips-2026-fujitsus-monaka-cpu">Hot Chips 2026: Fujitsu’s Monaka CPU - by Chester Lam</a></li>
<li><a href="https://anysilicon.com/the-ultimate-guide-to-chiplets/">The Ultimate Guide to Chiplets - AnySilicon</a></li>

</ul>
</details>

**Tags**: `#fujitsu`, `#monaka`, `#hot-chips-2026`, `#arm`, `#server-cpu`, `#chiplet-design`, `#sve2`

---

<a id="item-7"></a>
## [OXMIQ outlines narrow use cases for High Bandwidth Flash at Hot Chips 2026](https://www.tomshardware.com/pc-components/ssds/hot-chips-2026-high-bandwidth-flash-promises-massive-bandwidth-and-capacity-but-its-usability-is-extremely-limited-new-memory-format-strikes-a-balance-between-hbm-and-nand-flash) ⭐️ 7.5/10

At Hot Chips 2026, OXMIQ presented use-case scenarios for High Bandwidth Flash (HBF), a new memory format positioned between HBM and NAND flash, but the presentation dramatically narrowed the circumstances under which HBF actually makes practical sense. HBF represents a potential new tier in the memory hierarchy that could reshape how AI accelerators and high-performance computing systems are designed, especially for AI inference workloads where memory bandwidth is a critical bottleneck. However, OXMIQ's candid assessment of narrow use cases highlights the real challenges of integrating NAND-based storage-class memory into systems traditionally optimized for DRAM-like performance. HBF is built on TSV-stacked NAND (up to 16-high stacks) and connects via UCIe, offering up to 3 TB/s bandwidth and 512 GB capacity per module—far exceeding HBM in capacity but at lower performance and with non-volatility. OXMIQ's presentation focused on identifying the narrow intersection of workloads where HBF's unique bandwidth-versus-capacity tradeoffs justify adoption over either HBM or conventional SSDs.

rss · Tom's Hardware · Aug 26, 13:00

**Background**: The memory hierarchy in modern computing spans from fast, expensive, volatile DRAM—including HBM (High Bandwidth Memory) used in GPUs and AI accelerators—to slower, cheaper, non-volatile NAND flash storage used in SSDs. HBM delivers very high bandwidth by stacking DRAM dies with through-silicon vias (TSVs), but its capacity is limited and cost is high, while NAND flash offers massive capacity at low cost but much lower bandwidth. High Bandwidth Flash (HBF), jointly developed by Sandisk and SK hynix and formally announced in August 2026, attempts to bridge this gap by applying HBM-style TSV stacking to NAND dies. OXMIQ is a startup building licensable AI compute architectures via its OxCore platform and raised $35 million in Series A funding in July 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/ssds/sandisk-and-sk-hynix-unveil-hbf-spec-up-to-16-hi-nand-stacks-3-tb-s-bandwidth-ucie">New HBF spec outlines tech that can give GPUs terabytes of ...</a></li>
<li><a href="https://www.businesswire.com/news/home/20260701241910/en/OXMIQ-Raises-$35-Million-to-Scale-OxCore-Architecture">OXMIQ Raises $35 Million to Scale OxCore™ Architecture</a></li>

</ul>
</details>

**Tags**: `#memory-systems`, `#hardware-architecture`, `#HotChips`, `#HBM`, `#NAND-flash`

---

<a id="item-8"></a>
## [Arm Unveils AGI Server CPU: 136 Cores, UCIe Chiplets at Hot Chips](https://www.tomshardware.com/pc-components/cpus/hot-chips-2026-arm-details-agi-server-cpu-with-two-70-core-n3p-chiplets-touts-2-tb-s-ucie-fabric-link-and-12-channel-memory-controller) ⭐️ 7.5/10

At Hot Chips 2026, Arm disclosed new details about its AGI server CPU, which integrates two 70-core chiplets manufactured on TSMC's N3P process for up to 136 cores total, connected via a 2 TB/s UCIe fabric link and paired with a 12-channel memory controller. However, the company notably withheld any performance benchmarks or metrics. This announcement signals Arm's serious intent to compete in the AI/data-center server CPU market long dominated by x86 players like Intel and AMD, leveraging chiplet-based scalability and an open interconnect standard. The combination of high core counts, massive memory bandwidth, and high-bandwidth die-to-die links is specifically tailored for AI training and inference workloads. The design relies on UCIe, an open industry standard for die-to-die communication that allows chiplets from different vendors to interoperate in a single package. TSMC's N3P is a performance-enhanced variant of its 3nm-class FinFET process that entered high-volume production in late 2024, offering improved power, performance, and area over the base N3 node.

rss · Tom's Hardware · Aug 26, 11:00

**Background**: A chiplet-based architecture splits a processor into multiple smaller dies that are integrated into a single package, rather than building everything on one large monolithic die, which improves yields, lowers costs, and enables more flexible scaling. UCIe (Universal Chiplet Interconnect Express) is the open standard that defines how these chiplets communicate with each other inside a package, and it is now at version 3.0. Arm's AGI (a brand name, not a reference to artificial general intelligence) is a family of server-class CPUs targeted at hyperscale and AI workloads, designed to compete in a space where AMD's EPYC and Intel's Xeon lines have historically dominated.

<details><summary>References</summary>
<ul>
<li><a href="https://www.uciexpress.org/specifications">Specifications | UCIe Consortium</a></li>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_3nm">3nm Technology - Taiwan Semiconductor Manufacturing Company ...</a></li>
<li><a href="https://anysilicon.com/the-ultimate-guide-to-chiplets/">The Ultimate Guide to Chiplets - AnySilicon</a></li>

</ul>
</details>

**Tags**: `#Arm`, `#server CPU`, `#chiplets`, `#UCIe`, `#AI hardware`, `#Hot Chips`

---

<a id="item-9"></a>
## [EPA Proposes Removing Public Input on Air Pollution Permits for Data Centers](https://www.tomshardware.com/tech-industry/data-centers/u-s-govt-moves-to-suppress-pushback-on-data-centers-by-removing-requirements-for-public-input-on-pollution-epa-change-would-allow-air-pollution-permits-without-publicizing-them) ⭐️ 7.5/10

A proposed change to the EPA's regulations would remove the requirement for states to seek public input when issuing air pollution permits, particularly affecting the permitting process for AI data centers and other large industrial facilities. This regulatory shift could significantly accelerate AI data center construction by streamlining permitting, but it would simultaneously limit community oversight of the environmental impact of these energy-intensive facilities. As AI-driven emissions from major tech companies like Google and Microsoft continue to surge, reducing transparency around air quality permits raises concerns about accountability in the intersection of AI expansion and environmental protection. The proposed change targets Title V operating permits under the Clean Air Act, which are required for larger industrial facilities and provide a consolidated set of air quality regulations. Notably, this regulatory shift comes as data center energy and water consumption is rapidly increasing due to AI workloads, and novel cooling technologies like direct-to-chip and immersion cooling are emerging as ways to mitigate resource usage.

rss · Tom's Hardware · Aug 26, 10:00

**Background**: Title V of the Clean Air Act established a federal operating permit program for larger industrial sources of air pollution, consolidating all applicable air quality requirements into a single document and requiring public notice and comment periods when permits are issued or modified. AI data centers, which require enormous amounts of energy to power and cool AI training and inference workloads, are subject to these air quality regulations due to emissions from backup generators and other on-site power infrastructure. Major tech companies have reported rising emissions directly attributed to data center energy consumption driven by AI demand, making the environmental permitting process for these facilities a growing area of public concern.

<details><summary>References</summary>
<ul>
<li><a href="https://www.epa.gov/title-v-operating-permits/basic-information-about-operating-permits">Basic Information about Operating Permits - US EPA</a></li>
<li><a href="https://www.npr.org/2024/07/12/g-s1-9545/ai-brings-soaring-emissions-for-google-and-microsoft-a-major-contributor-to-climate-change">Google and Microsoft report growing emissions as they... : NPR</a></li>
<li><a href="https://www.eesi.org/articles/view/data-centers-and-water-consumption">Data Centers and Water Consumption | Article | EESI</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#EPA regulation`, `#environmental policy`, `#government policy`

---

<a id="item-10"></a>
## [Samsung Unveils LPDDR5X-PIM with In-Memory Logic at Hot Chips 2026](https://www.tomshardware.com/pc-components/dram/hot-chips-2026-samsung-makes-lpddr5x-smart-with-logic-unit-in-memory-lpddr5x-pim-is-3-01x-faster-than-lpddr5x-in-ai-inference-with-8x-the-bandwidth) ⭐️ 7.5/10

Samsung unveiled the industry's first LPDDR5X-PIM at Hot Chips 2026, embedding processing logic directly into low-power memory to accelerate AI inference workloads. The company claims the new memory delivers 3.01x faster AI inference performance and up to 8x the bandwidth of standard LPDDR5X. This marks Samsung's extension of Processing-in-Memory (PIM) technology from high-bandwidth memory (HBM) to the LPDDR5X standard, which is widely used in mobile and edge devices. By tackling the memory bandwidth bottleneck directly, the technology could enable more powerful on-device AI inference for smartphones, laptops, and edge hardware without relying on cloud connectivity. LPDDR5X is a low-power DRAM standard commonly used in smartphones, tablets, and laptops, making PIM at this tier particularly relevant for power-constrained AI workloads. Samsung had previously shipped HBM-PIM for data-center applications, so this represents a migration of the architecture toward mobile and edge platforms, though practical ecosystem support (compilers, runtimes, OS integration) remains to be seen.

rss · Tom's Hardware · Aug 25, 18:31

**Background**: Processing-in-Memory (PIM) is an architectural approach that places compute units near or inside memory arrays to reduce the energy and latency costs of moving data between memory and processors—a problem known as the memory wall. Samsung previously commercialized PIM in HBM stacks for AI accelerators in servers. LPDDR5X is the latest generation of low-power DDR memory, typically used in battery-powered devices where energy efficiency is critical. Bringing PIM to LPDDR5X targets the growing demand for running AI models locally on phones and edge devices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/dram/hot-chips-2026-samsung-makes-lpddr5x-smart-with-logic-unit-in-memory-lpddr5x-pim-is-3-01x-faster-than-lpddr5x-in-ai-inference-with-8x-the-bandwidth">Hot Chips 2026: Samsung makes LPDDR 5 X smart... | Tom's Hardware</a></li>
<li><a href="https://www.servethehome.com/samsung-lpddr5x-pim-at-hot-chips-2026/">Samsung LPDDR 5 X- PIM at Hot Chips 2026 - ServeTheHome</a></li>
<li><a href="https://en.wikipedia.org/wiki/LPDDR">LPDDR - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#memory-architecture`, `#processing-in-memory`, `#samsung`, `#AI-inference`, `#hardware`

---

<a id="item-11"></a>
## [Intel Wildcat Lake: 18A Budget Chips with UCIe Chiplet Integration](https://www.tomshardware.com/pc-components/cpus/hot-chips-2026-intel-details-cutting-edge-tech-in-entry-level-wildcat-lake-value-focused-18a-chips-necessitated-ucie-integration) ⭐️ 7.5/10

At Hot Chips 2026, Intel detailed its Wildcat Lake (branded as Intel Core Series 3) entry-level laptop SoC, which is derived from the Panther Lake-based Core Ultra Series 3 architecture and uses the company's most advanced 18A process node alongside UCIe chiplet interconnect technology to target the budget laptop market. This matters because it demonstrates Intel's commitment to extending its most advanced packaging and process technology into budget-tier products, a segment where cost constraints typically force compromises on cutting-edge features. The use of UCIe in an entry-level chip signals that chiplet-based design is becoming mainstream rather than reserved solely for premium offerings, potentially reshaping competition with AMD and Qualcomm in the value laptop space. Wildcat Lake's design objective prioritizes broad deployment of current-generation CPU, graphics, AI, memory, security, and connectivity features over maximum feature density. The integration of UCIe—a standardized chiplet interconnect—into a budget chip is notable given that 18A is Intel's make-or-break foundry technology aimed at reclaiming manufacturing leadership from TSMC.

rss · Tom's Hardware · Aug 25, 15:45

**Background**: UCIe（Universal Chiplet Interconnect Express，通用芯粒互连 express）是一项开放的行业标准，使来自不同厂商的芯粒能够在同一封装内无缝通信，从而促进模块化芯片设计。英特尔的 18A 工艺节点是该公司最先进的制造技术，采用了 RibbonFET 环栅晶体管和 PowerVia 背面供电技术，被广泛视为英特尔夺回与台积电代工竞争力的关键赌注。基于芯粒的架构将单片芯片拆分为更小的专用裸片，这些裸片可以混合搭配，从而提高良率和灵活性并降低成本——这种设计理念正在整个半导体行业中普及。

<details><summary>References</summary>
<ul>
<li><a href="https://www.uciexpress.org/">Home | UCIe Consortium</a></li>
<li><a href="https://abhs.in/blog/intel-18a-foundry-tsmc-rival-us-chip-independence-2026">Intel 18 A : The Make-or-Break Foundry Bet That Could End...</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#UCIe`, `#18A process node`, `#chiplets`, `#Hot Chips 2026`

---

<a id="item-12"></a>
## [Google Unveils 8th-Gen TPU Family at Hot Chips 2026](https://www.servethehome.com/googles-tpuv8s-for-training-and-inference-at-hot-chips-2026/) ⭐️ 7.5/10

At Hot Chips 2026, Google presented its eighth-generation TPU family, introducing the TPU 8t for training workloads and the TPU 8i for inference, continuing the company's custom AI silicon roadmap. Google remains one of the only hyperscalers designing its own training silicon, so each TPU generation has significant implications for the competitive AI hardware landscape and for Google Cloud's ability to offer differentiated AI infrastructure. Google is splitting the new generation into dedicated training (8t) and inference (8i) variants, reflecting a trend toward workload-specific accelerators, though the ServeTheHome article is a preview and does not yet disclose detailed specs such as process node, HBM capacity, or interconnect bandwidth.

rss · ServeTheHome · Aug 26, 00:15

**Background**: TPUs (Tensor Processing Units) are Google's custom ASICs optimized for the massive matrix multiplications that dominate deep-learning workloads such as CNNs and large language models. Hot Chips is an annual, invite-style symposium held at Stanford (August 23–25, 2026) where chip designers reveal architectural details to a technical audience. Hyperscalers like Google, AWS, and Microsoft Azure operate global-scale data centers and increasingly design their own accelerators to reduce reliance on third-party GPUs from NVIDIA.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hotchips.org/">Hot Chips</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hyperscale_computing">Hyperscale computing - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Google TPU`, `#AI hardware`, `#Hot Chips 2026`, `#machine learning`, `#data center accelerators`

---

<a id="item-13"></a>
## [Microsoft to Detail Maia 200 AI Accelerator at Hot Chips 2026](https://www.servethehome.com/microsofts-maia-200-accelerator-at-hot-chips-2026/) ⭐️ 7.5/10

Microsoft is set to present an in-depth architectural disclosure of its second-generation Maia 200 AI inference accelerator at Hot Chips 2026, building on the chip's January 2026 launch and Azure deployment. This presentation signals Microsoft's serious commitment to proprietary AI silicon as a strategy to reduce dependency on NVIDIA, and Hot Chips is a premier venue where deep microarchitectural details typically emerge, giving competitors and customers a clearer picture of Microsoft's hardware roadmap. Maia 200 is built on TSMC's 3nm process with native FP8/FP4 tensor cores, 216GB of HBM3e memory delivering 7 TB/s bandwidth, 272MB of on-chip SRAM, approximately 10 PFLOPS of FP4 performance at 750W, and Microsoft claims it reduces total cost of ownership by 30% and energy consumption by 15% compared to other accelerators in its fleet.

rss · ServeTheHome · Aug 25, 22:45

**Background**: Maia 200 is Microsoft's first custom-built AI accelerator designed specifically for inference—the production deployment phase of AI models—rather than training. It succeeds the original Maia 100 and represents Microsoft's vertical integration strategy for AI infrastructure. Hot Chips is an annual symposium focused on high-performance chip architectures, where companies traditionally disclose detailed microarchitectural information including pipeline design, memory hierarchy, and interconnect. The conference is well-attended by hardware engineers, researchers, and industry analysts seeking deep technical insight beyond marketing announcements.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/">Maia 200: The AI accelerator built for inference - The ...</a></li>
<li><a href="https://www.hotchips.org/">Hot Chips</a></li>
<li><a href="https://aimagazine.com/news/microsoft-unveils-maia-200-ai-accelerator">Microsoft: How Maia 200 Accelerator Addresses AI Bottlenecks</a></li>

</ul>
</details>

**Tags**: `#AI-hardware`, `#Microsoft`, `#Hot-Chips`, `#AI-accelerators`, `#custom-silicon`

---

<a id="item-14"></a>
## [Cerebras Talks Going Rack-Scale with Their WSEs at Hot Chips 2026](https://www.servethehome.com/cerebras-talks-going-rack-scale-with-their-wses-at-hot-chips-2026/) ⭐️ 7.5/10

Cerebras announced at Hot Chips 2026 that their next-generation wafer-scale engines will go rack-scale via a new Nexus architecture, marking a major step in scaling AI accelerator deployments.

rss · ServeTheHome · Aug 25, 22:15

**Tags**: `#Cerebras`, `#AI hardware`, `#wafer-scale`, `#Hot Chips 2026`, `#rack-scale architecture`

---

<a id="item-15"></a>
## [NVIDIA Integrates Groq 3 LPUs with Vera Rubin for Heterogeneous AI Compute](https://www.servethehome.com/nvidias-groq-3-lpu-accelerators-for-heterogeneous-ai-compute-at-hot-chips-2026/) ⭐️ 7.5/10

At Hot Chips 2026, NVIDIA detailed how it is integrating Groq 3 LPUs into Vera Rubin clusters as part of a heterogeneous compute architecture, specifically targeting lower latency during the decode phase of LLM inference. The LPX system, built around 256 interconnected LPUs and co-designed with the Vera Rubin NVL72 platform, is positioned as a rack-scale inference accelerator for agentic AI workloads. This announcement signals NVIDIA's strategic shift toward heterogeneous AI compute, acknowledging that GPUs alone cannot optimally serve every phase of inference and that specialized accelerators like LPUs are needed for the token-by-token decode phase. It validates the industry trend of disaggregating prefill and decode workloads across different silicon, which could reshape how hyperscalers and enterprises design their AI infrastructure. NVIDIA claims the Groq 3 LPX delivers up to 35x higher inference throughput per megawatt and 10x more revenue opportunity for trillion-parameter models. LPUs differ from GPUs by keeping model weights in on-chip SRAM and using deterministic execution schedules, eliminating the memory-wait stalls that slow GPU-based token generation. The 256-LPU LPX rack works alongside Vera Rubin GPUs rather than replacing them.

rss · ServeTheHome · Aug 25, 21:45

**Background**: LLM inference operates in two distinct phases: the prefill phase, which processes the entire input prompt to build the KV cache and is compute-heavy, and the decode phase, which generates output tokens one at a time and is memory-bandwidth-bound. LPUs (Language Processing Units) are inference-specialized chips designed by Groq that store model weights in on-chip SRAM and use deterministic scheduling to avoid memory latency stalls, making them particularly well-suited for decode workloads. An LPU inference engine is typically used alongside rather than instead of a GPU-based training and prefill system, which is why heterogeneous architectures combining both types of accelerators have gained traction.

<details><summary>References</summary>
<ul>
<li><a href="https://www.servethehome.com/nvidias-groq-3-lpu-accelerators-for-heterogeneous-ai-compute-at-hot-chips-2026/">NVIDIA’s Groq 3 LPU Accelerators for Heterogeneous AI Compute ...</a></li>
<li><a href="https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform">Inside NVIDIA Groq 3 LPX: The Low-Latency Inference ...</a></li>
<li><a href="https://groq.com/blog/the-groq-lpu-explained">What is a Language Processing Unit? | Groq is the premier ...</a></li>
<li><a href="https://redis.io/blog/prefill-vs-decode/">Prefill vs Decode : LLM Inference Phases Explained</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Groq`, `#LPU`, `#Hot Chips 2026`, `#AI inference`, `#heterogeneous compute`, `#Vera Rubin`

---

<a id="item-16"></a>
## [Global Ocean Surface Temperatures Hit Record High Amid Climate Change](https://www.solidot.org/story?sid=85198) ⭐️ 7.3/10

According to the European Copernicus Climate Change Service, the global average sea surface temperature (excluding polar regions) reached 21.1°C on Saturday, slightly exceeding the previous record of 21.09°C set in March 2024. Scientists warn that the current El Niño event has not yet peaked and could become one of the strongest in centuries. Record-breaking ocean temperatures have wide-ranging consequences, including intensifying extreme weather events, accelerating sea level rise, and damaging marine ecosystems. Because oceans absorb the vast majority of excess atmospheric heat, these records serve as a critical indicator of the pace and severity of global climate change. The temperature data is derived from measurements taken 10 meters below the sea surface using buoys, ships, and satellites. The annual peak in global mean sea surface temperature typically occurs in March or April, corresponding to the end of the Southern Hemisphere summer, because the Southern Hemisphere has significantly more ocean area than the Northern Hemisphere.

rss · Solidot · Aug 26, 07:45

**Background**: El Niño is a climate phenomenon characterized by unusually warm ocean waters in the central and eastern equatorial Pacific, driven by weakened trade winds. It typically occurs every two to seven years and is known to disrupt global weather patterns, often causing increased temperatures worldwide. The Copernicus Climate Change Service is the European Union's Earth observation program, which provides authoritative climate data based on satellite observations and in-situ measurements from around the globe.

**Tags**: `#AI-hardware`, `#OpenAI`, `#Nvidia`, `#climate-science`, `#China-AI`

---

<a id="item-17"></a>
## [AWS Acquires DuckDB](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws) ⭐️ 7.0/10

AWS has acquired DuckLabs (the commercial entity behind DuckDB), while the open-source DuckDB project remains under the nonprofit DuckDB Foundation's control.

hackernews · onderkalaci · Aug 26, 12:59 · [Discussion](https://news.ycombinator.com/item?id=49448321)

**Tags**: `#aws`, `#duckdb`, `#acquisition`, `#open-source`, `#databases`

---

<a id="item-18"></a>
## [Qwen3.8-Flash-Next: 176B MoE Preview of Qwen4 Architecture](https://qwen.ai/blog?id=qwen3.8-flash-next) ⭐️ 7.0/10

Qwen has released Qwen3.8-Flash-Next, an experimental preview of the Qwen4 architecture: a multimodal ultra-sparse Mixture-of-Experts model with 176B total parameters (including a 51B N-gram embedding table) that activates only 6B parameters per token, reportedly outperforming the previous 27B model while fitting on 128GB hardware at roughly 73GB in quantized form. This release suggests that ultra-sparse MoE combined with a hybrid GDN + QSA attention design can deliver 100B+-class quality at small-model compute costs, potentially reshaping the economics of self-hosted AI and making high-end inference accessible on prosumer hardware like Mac Studio and AMD Strix Halo. The model ships in FP8 with day-0 vLLM and SGLang support and is already integrated into Unsloth Desktop. Its 6B active-parameter count sidesteps the memory-bandwidth bottleneck that throttles dense 27B-class models on consumer GPUs, enabling Q3/Q4 quantized inference with reasonable context length even on a single 128GB host.

hackernews · tosh · Aug 26, 12:52 · [Discussion](https://news.ycombinator.com/item?id=49448210)

**Background**: Mixture-of-Experts (MoE) models partition their weights into many 'expert' sub-networks and use a learned router to activate only a small subset per token, dramatically reducing compute while keeping memory proportional to total parameters; prior sparse designs such as Mixtral 8x7B already showed that this pattern can beat much larger dense models. The architecture described here also replaces pure softmax attention with a hybrid Gated DeltaNet (GDN) + QSA mechanism to further cut memory and compute at long context. Qwen describes Qwen3.8-Flash-Next as the experimental foundation that will underpin the next-generation Qwen4 model family.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next-FP8">Qwen/ Qwen 3 .8- Flash -Next-FP8 · Hugging Face</a></li>
<li><a href="https://recipes.vllm.ai/Qwen/Qwen3.8-Flash-Next">Qwen/ Qwen 3 .8- Flash -Next | vLLM Recipes</a></li>
<li><a href="https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next">Qwen 3 .8- Flash -Next - SGLang Documentation</a></li>

</ul>
</details>

**Discussion**: The community reacts with strong enthusiasm, particularly around self-hosting on Strix Halo and 128GB Macs, since the ~73GB quantized size is feasible on such hardware. Users are curious whether the model matches the reasoning depth of larger Qwen3.8 variants, and several ask whether it inherits the verbosity and cumulative input-token cost issues seen with Qwen3.8-27B and GLM 5.2. Overall sentiment is optimistic but cautiously awaiting real-world benchmarks on production workloads.

**Tags**: `#qwen`, `#llm`, `#model-release`, `#cost-efficiency`, `#self-hosting`

---

<a id="item-19"></a>
## [Fake US thinktank set up and funded by Israel sought to game AI for propaganda](https://www.theguardian.com/world/2026/aug/26/fake-thinktank-israel-ai-propaganda) ⭐️ 7.0/10

A fake US think tank funded by Israel was used to attempt to influence AI systems for propaganda purposes, as disclosed by OpenAI's anti-abuse efforts.

hackernews · n1b0m · Aug 26, 12:11 · [Discussion](https://news.ycombinator.com/item?id=49447600)

**Tags**: `#AI safety`, `#disinformation`, `#state-sponsored-actors`, `#propaganda`, `#AI ethics`

---

<a id="item-20"></a>
## [XCancel and Nitter are receiving C&D letters from XCorp](https://news.ycombinator.com/item?id=49446210) ⭐️ 7.0/10

X Corp has issued cease and desist letters to Nitter and XCancel, shutting down both alternative front-ends that enabled login-free, privacy-respecting access to Twitter/X content.

hackernews · mobilio · Aug 26, 09:34

**Tags**: `#twitter`, `#nitter`, `#open-web`, `#platform-policy`, `#decentralization`

---