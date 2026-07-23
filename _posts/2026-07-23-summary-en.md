---
layout: default
title: "Horizon Summary: 2026-07-23 (EN)"
date: 2026-07-23
lang: en
---

> From 103 items, 20 important content pieces were selected

---

1. [AMD to Supply Anthropic with 2GW of MI450 GPUs, Invests Up to $5B](#item-1) ⭐️ 9.5/10
2. [Codeberg Bans Vibe-Coded Projects Amid AI Resource Concerns](#item-2) ⭐️ 8.3/10
3. [Terence Tao's ChatGPT conversation about the Jacobian Conjecture counterexample](#item-3) ⭐️ 8.0/10
4. [GigaToken: ~1000x faster Language model tokenization](#item-4) ⭐️ 8.0/10
5. [Etched Raises $300M, $1B in Pre-Orders for Transformer ASIC](#item-5) ⭐️ 8.0/10
6. [Wistron Opens First U.S. AI Smart Factory for NVIDIA GB300 Production](#item-6) ⭐️ 7.5/10
7. [Bipartisan US Bill Proposes Kill Switches for Powerful AI Models](#item-7) ⭐️ 7.5/10
8. [Inside optical and the battle for scale – how the AI industry is racing to integrate photonic interconnects](#item-8) ⭐️ 7.5/10
9. [Intel and AMD lock in long-term server CPU deals with China at 40%+ price hikes](#item-9) ⭐️ 7.5/10
10. [Everyone Should Know SIMD: A Practical Guide to Vectorized Programming](#item-10) ⭐️ 7.0/10
11. [Alphabet's cash burn raises alarm for Big Tech as AI spending climbs](#item-11) ⭐️ 7.0/10
12. [Bento: A Single HTML File PowerPoint Alternative with Editing and Live Collaboration](#item-12) ⭐️ 7.0/10
13. [Are AI labs pelicanmaxxing?](#item-13) ⭐️ 7.0/10
14. [Protecting our FLOSS commons from LLMs](#item-14) ⭐️ 7.0/10
15. [DAC 2026: Chip Giants Build DIY AI Design Tools, Bypassing EDA Vendors](#item-15) ⭐️ 7.0/10
16. [Framework Teases Desktop with Ryzen AI Max+ PRO 495 and 192GB Memory](#item-16) ⭐️ 6.5/10
17. [CachyOS Proton Fork Adds NVIDIA Reflex Support via vkd3d-low-latency](#item-17) ⭐️ 6.5/10
18. [Developer Gets NVIDIA RTX 4060 Working on Windows-on-Arm Desktop](#item-18) ⭐️ 6.5/10
19. [Jensen Huang argues American companies should be allowed to use Chinese AI models — Nvidia CEO says backdoors connected to China are misconceptions](#item-19) ⭐️ 6.5/10
20. [Fortinet becomes Intel Foundry's first Intel 4 customer with SP6 ASIC](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [AMD to Supply Anthropic with 2GW of MI450 GPUs, Invests Up to $5B](https://www.tomshardware.com/tech-industry/amd-to-supply-anthropic-with-2-gigawatts-of-instinct-mi450-gpus) ⭐️ 9.5/10

AMD announced it will supply Anthropic with 2 gigawatts of next-generation Instinct MI450 GPUs, deployed in AMD Helios rack-scale systems starting with the first gigawatt coming online in the first half of 2027. Concurrently, AMD will invest up to $5 billion into Anthropic, expanding an existing partnership in which Anthropic is already deploying MI355X GPUs. This deal represents AMD's largest single-customer commitment to date and a significant competitive win against NVIDIA in the AI accelerator market, as one of the leading frontier AI labs diversifies away from an NVIDIA-dominated supply chain. The combined hardware supply and equity investment tightly align AMD's roadmap with Anthropic's compute needs, potentially accelerating the adoption of CDNA 5 and the open UALink networking ecosystem. The MI450 is built on AMD's CDNA 5 architecture using TSMC's 2nm N2 compute chiplets paired with N3P I/O dies, packing 432 GB of HBM4 memory and up to 40 PFLOPS of compute. The Helios platform integrates MI450 GPUs with AMD's 'Vulcano' networking based on the UALink standard, and is built on Meta's 2025 Open Compute Project rack design.

rss · Tom's Hardware · Jul 22, 15:38

**Background**: AMD Instinct is AMD's data center GPU brand, originally launched in 2016 as a successor to FirePro S, and is purpose-built for deep learning, neural network training, and high-performance computing workloads as a competitor to NVIDIA's data center GPUs. Anthropic is the AI research company behind the Claude family of large language models, and it has historically relied heavily on NVIDIA hardware for training and inference. Rack-scale systems like AMD Helios are an emerging architectural pattern in which compute, memory, networking, and power are co-designed at the entire rack level to maximize efficiency for AI workloads, contrasting with traditional approaches where individual servers are assembled from commodity components.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AMD_Instinct">AMD Instinct - Wikipedia</a></li>
<li><a href="https://awesomeagents.ai/hardware/amd-mi450/">AMD Instinct MI450 - 2nm, 432 GB HBM4, 40 PFLOPS</a></li>
<li><a href="https://www.amd.com/en/blogs/2025/amd-helios-ai-rack-built-on-metas-2025-ocp-design.html">AMD Helios - AI Rack Built on Meta’s 2025 OCP Design</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#Anthropic`, `#AI Hardware`, `#GPU`, `#Data Center Infrastructure`

---

<a id="item-2"></a>
## [Codeberg Bans Vibe-Coded Projects Amid AI Resource Concerns](https://www.solidot.org/story?sid=84906) ⭐️ 8.3/10

German non-profit open-source hosting platform Codeberg announced a major policy shift following a member vote (358 in favor, 144 against), pledging not to use user data for LLM training and banning vibe-coded projects from its platform. The organization cited ballooning hardware costs, energy consumption, AI crawler traffic, and unresolved licensing issues around LLM-generated code as key reasons for the decision. As one of the largest non-commercial open-source hosting alternatives, Codeberg's stance signals a growing open-source community pushback against the unchecked proliferation of AI-generated code and the hidden costs it imposes on shared infrastructure. The decision could set a precedent for other platforms and reshape how open-source communities view contributions made via LLMs. Codeberg reported that identical SSDs that cost €700 a few years ago now cost €3,700 and are frequently out of stock, directly linking price inflation to AI industry demand. The platform clarified that occasional LLM-assisted coding or projects where maintainers unknowingly receive LLM-generated contributions will not be targeted, and only dedicated vibe-coded projects will be removed.

rss · Solidot · Jul 23, 10:44

**Background**: Vibe coding is a term coined by OpenAI co-founder Andrej Karpathy in February 2025, describing a software development approach where programmers guide and test LLM-generated code rather than writing it manually. Codeberg is a non-profit, community-run Git hosting platform built on Forgejo, hosted in Germany, and dedicated to supporting free and open-source software. It operates as a charitable organization (Codeberg e.V.) that does not monetize through premium tiers or data collection, positioning itself as a privacy- and ethics-focused alternative to commercial platforms like GitHub.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>
<li><a href="https://codeberg.org/">Codeberg .org</a></li>
<li><a href="https://www.cloudflare.com/learning/ai/ai-vibe-coding/">What is vibe coding?</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#Codeberg`, `#LLM`, `#AI-ethics`, `#policy`

---

<a id="item-3"></a>
## [Terence Tao's ChatGPT conversation about the Jacobian Conjecture counterexample](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56) ⭐️ 8.0/10

Terence Tao's ChatGPT conversation analyzing a claimed counterexample to the Jacobian Conjecture, demonstrating how frontier mathematicians are leveraging LLMs as research tools for exploring open problems.

hackernews · gmays · Jul 22, 17:30 · [Discussion](https://news.ycombinator.com/item?id=49010345)

**Tags**: `#AI-assisted mathematics`, `#Terence Tao`, `#Jacobian Conjecture`, `#ChatGPT`, `#LLM applications`

---

<a id="item-4"></a>
## [GigaToken: ~1000x faster Language model tokenization](https://github.com/marcelroed/gigatoken/) ⭐️ 8.0/10

GigaToken achieves ~1000x faster language model tokenization through SIMD-optimized pretokenization, branch minimization, and aggressive caching.

hackernews · syrusakbary · Jul 22, 17:20 · [Discussion](https://news.ycombinator.com/item?id=49010167)

**Tags**: `#tokenization`, `#performance-optimization`, `#SIMD`, `#LLM`, `#systems-engineering`

---

<a id="item-5"></a>
## [Etched Raises $300M, $1B in Pre-Orders for Transformer ASIC](https://www.eetimes.com/etched-raises-300m-with-1b-in-pre-orders/) ⭐️ 8.0/10

AI chip startup Etched has raised $300 million in funding and secured $1 billion in pre-orders for its Sohu transformer ASIC, with first racks slated to ship in summer 2026. The company previously exited stealth on June 30, 2026, at a reported $5 billion valuation. The massive pre-order volume signals strong industry appetite for alternatives to NVIDIA's general-purpose GPUs in the LLM inference market, where cost and efficiency are critical. Etched's bet on a transformer-only ASIC—if it delivers on performance claims—could reshape the economics of running large language models at scale. Sohu is an application-specific integrated circuit (ASIC) purpose-built for transformer inference, implementing attention as fixed-function silicon rather than programmable matrix-multiply instructions, which Etched claims enables unmatched throughput. No independent benchmarks exist yet, and the product is not currently available for purchase or rent.

rss · EE Times · Jul 23, 15:00

**Background**: Most AI accelerators today, including NVIDIA's GPUs, are general-purpose processors that can run many types of AI workloads. An ASIC (Application-Specific Integrated Circuit) is a chip custom-designed for one particular task—in Etched's case, running transformer models like those behind ChatGPT. Transformer inference (generating tokens from a trained model) is the dominant workload for deployed AI services, and by stripping out everything unrelated to it, an ASIC can theoretically achieve far higher performance and efficiency. Etched has reportedly recruited over 400 engineers from NVIDIA, TSMC, and other firms to co-design chips, racks, and software together.

<details><summary>References</summary>
<ul>
<li><a href="https://www.spheron.network/blog/etched-ai-sohu-vs-nvidia-transformer-asic-inference/">Etched AI Sohu vs NVIDIA: Transformer ASIC vs General-Purpose GPU for LLM Inference (2026) | Spheron Blog</a></li>
<li><a href="https://www.techtimes.com/articles/319393/20260630/transformer-chip-startup-etched-exits-stealth-800m-raised-1b-contracts.htm">Transformer Chip Startup Etched Exits Stealth: $800M Raised, $1B in Contracts</a></li>
<li><a href="https://wccftech.com/etched-pulls-400-engineers-nvidia-tsmc-build-new-frontier-inference-cluster-for-ai/">Etched Pulls 400+ Engineers From NVIDIA, TSMC & More to Build a New Frontier Inference Cluster For AI Which Is Already Worth $1B in Demand</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#startup funding`, `#semiconductors`, `#AI chips`, `#venture capital`

---

<a id="item-6"></a>
## [Wistron Opens First U.S. AI Smart Factory for NVIDIA GB300 Production](https://www.techpowerup.com/350985/wistron-celebrates-grand-opening-of-first-u-s-smart-factory) ⭐️ 7.5/10

Wistron officially opened its D1 AI smart facility in Fort Worth, Texas — a $700 million, 324,000-square-foot plant that is the first U.S. site to mass-produce NVIDIA's GB300 Grace Blackwell Ultra Superchips. The ceremony was led by Wistron Chairman Simon Lin and NVIDIA CEO Jensen Huang, with Wistron announcing plans to also produce the next-generation NVIDIA Vera Rubin Superchip at the same location. This is a significant milestone for U.S.-based AI infrastructure manufacturing, reducing reliance on overseas production for NVIDIA's most advanced accelerators and strengthening the domestic AI supply chain. The presence of Jensen Huang signals NVIDIA's strategic commitment to expanding U.S. production capacity for its flagship AI silicon amid surging global demand. The factory runs on NVIDIA accelerated computing and integrates NVIDIA's Nemotron and Cosmos open frontier models along with Omniverse and Metropolis libraries, using digital twin technology to optimize factory design and workflows. The GB300 NVL72 platform itself integrates 72 Blackwell Ultra GPUs and 36 Grace CPUs per rack-scale system, with 288 GB HBM3e per GPU and up to 1,400 PFLOPS FP4 inference performance.

rss · TechPowerUp News · Jul 22, 18:30

**Background**: Wistron is a Taiwanese original design manufacturer (ODM) long known as a key assembly partner for major tech brands, and it has increasingly pivoted toward AI server and accelerator manufacturing. NVIDIA's Grace Blackwell Ultra (GB300) Superchip is the successor to the GB200, pairing a Grace Arm-based CPU with a Blackwell Ultra GPU on a single board, designed to deliver massive performance gains for AI training and inference. The Vera Rubin Superchip, mentioned by Wistron as a future product at this facility, is NVIDIA's next-generation AI platform expected to follow Blackwell. NVIDIA Nemotron is a family of open multimodal foundation models for agentic AI, while NVIDIA Cosmos provides world foundation models for physical AI applications — both being used here to power the factory's own AI-driven operations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/gb300-nvl72/">Designed for AI Reasoning Performance & Efficiency | NVIDIA GB300 NVL72</a></li>
<li><a href="https://www.nvidia.com/en-us/ai/cosmos/">Physical AI with World Foundation Models | NVIDIA Cosmos</a></li>
<li><a href="https://www.nvidia.com/en-eu/ai-data-science/foundation-models/nemotron/">Build Agentic AI with Multimodal Foundation Models | NVIDIA Nemotron</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#AI infrastructure`, `#semiconductor manufacturing`, `#GB300`, `#Wistron`

---

<a id="item-7"></a>
## [Bipartisan US Bill Proposes Kill Switches for Powerful AI Models](https://www.tomshardware.com/tech-industry/artificial-intelligence/bipartisan-bill-would-require-kill-switches-on-the-most-powerful-ai-models) ⭐️ 7.5/10

A bipartisan US bill has been proposed that would require kill switches on the most powerful AI models, empowering the Department of Homeland Security (DHS) to throttle or fully shut down these systems. The bill targets companies with at least $500 million in annual AI revenue whose models were trained with compute costs exceeding $100 million, with non-compliance fines reaching $20 million per day. This proposal signals serious bipartisan momentum toward regulating frontier AI, potentially reshaping how the largest AI companies develop and deploy their most capable models. If enacted, it would mark one of the most aggressive US federal interventions into AI operations, affecting major players such as OpenAI, Google, Anthropic, and Meta. The bill uses specific quantitative thresholds ($500M annual AI revenue and $100M training compute) to define covered models, focusing regulatory power on the most resource-intensive frontier systems rather than broadly applied rules. It amends the Homeland Security Act, placing AI oversight under DHS rather than creating a new dedicated agency, and includes tiered enforcement actions from throttling to full shutdown.

rss · Tom's Hardware · Jul 23, 15:02

**Background**: Frontier AI models refer to the most capable, cutting-edge AI systems, typically large language models trained with enormous computational resources measured in floating-point operations (FLOPs). Training compute costs have grown exponentially over the past decade, with leading models now requiring tens or hundreds of millions of dollars in compute alone. Kill switches are emergency mechanisms designed to halt or throttle AI systems in scenarios where they pose risks, such as autonomous behavior, cybersecurity threats, or misuse. Earlier regulatory discussions around frontier AI have focused on licensing, risk assessment, auditing, and post-deployment monitoring, making this kill-switch proposal a notable escalation of the US approach.

<details><summary>References</summary>
<ul>
<li><a href="https://80000hours.org/podcast/episodes/markus-anderljung-regulating-cutting-edge-ai/">Markus Anderljung on how to regulate cutting-edge AI models</a></li>
<li><a href="https://futuretech.mit.edu/news/what-drives-progress-in-ai-trends-in-compute">What drives progress in AI ? Trends in Compute</a></li>
<li><a href="https://datahub.io/blog/the-trillion-fold-rise-how-ai-training-compute-exploded">The Trillion-Fold Rise: How AI Training Compute Exploded</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#regulation`, `#bipartisan bill`, `#AI safety`, `#frontier AI`

---

<a id="item-8"></a>
## [Inside optical and the battle for scale – how the AI industry is racing to integrate photonic interconnects](https://www.tomshardware.com/tech-industry/inside-optical-and-the-battle-for-scale-how-the-ai-industry-is-racing-to-integrate-photonic-interconnects) ⭐️ 7.5/10

Analysis of the AI industry's shift from copper to photonic interconnects for scaling data centers, featuring expert insights on emerging standards and the role of companies like Lightmatter.

rss · Tom's Hardware · Jul 23, 14:22

**Tags**: `#AI infrastructure`, `#photonic interconnects`, `#data centers`, `#hardware`, `#Lightmatter`

---

<a id="item-9"></a>
## [Intel and AMD lock in long-term server CPU deals with China at 40%+ price hikes](https://www.tomshardware.com/pc-components/cpus/intel-and-amd-sign-long-term-server-cpu-deals-with-chinese-customers-as-prices-jump-over-40-percent) ⭐️ 7.5/10

Intel and AMD have reportedly signed long-term server CPU supply agreements with Chinese customers, with prices jumping more than 40% and some deals extending two years or longer, according to Reuters via Tom's Hardware. The move signals a significant supply-and-pricing power shift in the server CPU market amid tightening US-China tech restrictions, with Chinese hyperscalers and cloud buyers apparently willing to absorb sharp price increases to lock in allocation. It also reflects how export-control pressure can translate directly into higher revenues for the two dominant x86 server vendors. The agreements reportedly guarantee purchase volumes for roughly one year without fixing prices, giving both sides flexibility as market conditions change. Some customers have discussed multi-year commitments, suggesting they are hedging against further supply tightening or additional US restrictions.

rss · Tom's Hardware · Jul 23, 13:49

**Background**: Server CPUs such as Intel Xeon and AMD EPYC differ fundamentally from consumer chips — they offer far higher core counts (EPYC 9004 series reaches up to 128 cores), support multi-socket configurations, and prioritize reliability, parallel request handling, and virtualization for data center workloads. Since October 7, 2022, the United States has imposed sweeping export controls targeting China's ability to access advanced computing and semiconductor manufacturing items, restricting American firms from selling cutting-edge chips and seeking to prevent circumvention through third countries. These restrictions have tightened global supply of high-end server silicon, creating conditions where Chinese customers feel pressure to commit early. The deal structure resembles long-term agreements (LTAs) used in other commodity semiconductor supply chains, where buyers secure guaranteed volume while pricing floats with the market.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_New_Export_Controls_on_Advanced_Computing_and_Semiconductors_to_China">United States New Export Controls on Advanced ... - Wikipedia</a></li>
<li><a href="https://www.nortonrosefulbright.com/en/knowledge/publications/5a936192/us-expands-export-restrictions-on-advanced-semiconductors">US expands export restrictions on advanced semiconductors</a></li>
<li><a href="https://www.flytronics-group.com/articledetail/913.html">Samsung reportedly in talks with Google, Microsoft on long - term ...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#Intel`, `#AMD`, `#server-hardware`, `#geopolitics`

---

<a id="item-10"></a>
## [Everyone Should Know SIMD: A Practical Guide to Vectorized Programming](https://mitchellh.com/writing/everyone-should-know-simd) ⭐️ 7.0/10

Mitchell Hashimoto published an introductory guide to SIMD (Single Instruction, Multiple Data) programming, explaining how vectorized operations can dramatically accelerate performance-critical code. The article walks through concrete examples of replacing scalar loops with SIMD intrinsics to achieve significant speedups. As CPU clock speeds plateau, performance gains increasingly depend on parallelism at the data level, making SIMD knowledge essential for systems programmers, game developers, and anyone working on performance-critical code. The article received 549 upvotes and 200 substantive comments, indicating strong community interest in low-level optimization techniques. Community discussion highlighted that SWAR (SIMD Within A Register) can serve as a simpler stepping stone using standard 64-bit registers, and that array programming provides a useful mindset that compilers can more easily auto-vectorize. A practitioner reported achieving 5x speedups in a bioinformatics project using AVX-512 fused kernels with the Rust 'wide' crate.

hackernews · WadeGrimridge · Jul 22, 17:48 · [Discussion](https://news.ycombinator.com/item?id=49010648)

**Background**: SIMD is a parallel computing paradigm where a single instruction operates on multiple data elements simultaneously, available on modern CPUs through instruction sets like SSE, AVX, AVX-512 (x86) and NEON (ARM). Unlike multi-threading, SIMD achieves parallelism within a single CPU instruction by packing multiple values into wide registers (e.g., 256-bit or 512-bit). SIMD Within A Register (SWAR) is a software technique that simulates SIMD-like parallelism using ordinary integer registers, offering a hardware-independent way to explore these patterns. Array programming, used in languages like APL and NumPy, expresses operations over entire arrays rather than individual elements, which naturally aligns with SIMD execution and aids compiler auto-vectorization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SWAR">SWAR - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Array_programming">Array programming - Wikipedia</a></li>
<li><a href="https://sunsite.icm.edu.pl/Linux/Documentation/HOWTO/Parallel-Processing-HOWTO-4.html">Linux Parallel Processing HOWTO: SIMD Within A Register ...</a></li>

</ul>
</details>

**Discussion**: The community response was largely positive and technically substantive. Commenters expanded the discussion beyond the article: one recommended starting with SWAR for hardware-independent exploration, another argued that array programming is an even more fundamental skill since it aids compiler auto-vectorization, and a bioinformatics practitioner shared real-world AVX-512 experience with 5x speedups. A common theme was that modern compilers auto-vectorize well until edge cases break them, making manual SIMD knowledge important for diagnosing unexpected performance cliffs.

**Tags**: `#SIMD`, `#performance-optimization`, `#low-level-programming`, `#computer-architecture`, `#parallel-computing`

---

<a id="item-11"></a>
## [Alphabet's cash burn raises alarm for Big Tech as AI spending climbs](https://www.reuters.com/business/retail-consumer/alphabets-cash-burn-raises-alarm-big-tech-ai-spending-climbs-2026-07-23/) ⭐️ 7.0/10

Analysis of Alphabet's massive cash burn from AI infrastructure spending, raising concerns about whether Big Tech's unprecedented AI capex commitments (~$3T total) can generate sufficient returns to justify investment.

hackernews · 1vuio0pswjnm7 · Jul 23, 13:10 · [Discussion](https://news.ycombinator.com/item?id=49021006)

**Tags**: `#AI economics`, `#Big Tech`, `#Alphabet`, `#capital expenditure`, `#industry analysis`

---

<a id="item-12"></a>
## [Bento: A Single HTML File PowerPoint Alternative with Editing and Live Collaboration](https://bento.page/slides/) ⭐️ 7.0/10

Bento is a new open-source presentation tool that packages an entire PowerPoint-style application—editing, animations, sharing, and live collaboration—into a single ~560 KB HTML file that works fully offline. The file stores slide data as plain JSON near the top and contains the app logic as a base64-encoded blob that decompresses in the browser via the DecompressionStream API. It exemplifies a growing trend of single-file web apps and local-first software, removing the need for installs, cloud accounts, or external fetches. It also integrates naturally with AI coding assistants like Claude Code, letting users describe edits in natural language rather than manually editing code, which could reshape how presentations and lightweight tools are built and shared. Collaboration is achieved through an encrypted blind relay that never sees plaintext, making it end-to-end secure. The project is MIT-licensed on GitHub, built on reveal.js plus several other libraries, and the slide JSON near the top is designed to be readable, greppable, and directly addressable by AI coding harnesses.

hackernews · starfallg · Jul 22, 15:19 · [Discussion](https://news.ycombinator.com/item?id=49008211)

**Background**: Single-file web apps are standalone HTML documents that bundle all logic, styles, and data so the file itself is the entire application—no build step, server, or backend needed. Local-first software is a design philosophy, coined by the Ink & Switch lab in its 2019 manifesto, where the user's device holds the primary copy of the data and cloud sync is secondary, enabling fast, offline-capable experiences. AI coding harnesses like Anthropic's Claude Code are agentic terminal tools that can read, edit, and run code across an entire repository based on natural-language instructions.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.powersync.com/resources/local-first-software">Understand the local - first software architecture pattern and how...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://dev.to/iamjephter/building-a-blind-relay-in-rust-with-tauri-at-the-edge-57gp">Architecting a Blind Relay : E2EE Clipboard Sync... - DEV Community</a></li>

</ul>
</details>

**Discussion**: The HN thread was strongly positive (939 upvotes, 214 comments), with many commenters echoing the sentiment that single-file web apps and local-first tools represent an important emerging pattern, not just a novelty. Several users highlighted that the economic incentive to ship truly local software has only recently arrived, while others pointed to alternatives like Slidev and Typst for AI-generated slides. The creator added technical detail about the JSON-plus-base64 architecture and how AI harnesses can directly target the slide data.

**Tags**: `#single-file-apps`, `#local-first`, `#web-development`, `#presentations`, `#ai-assisted-coding`

---

<a id="item-13"></a>
## [Are AI labs pelicanmaxxing?](https://dylancastillo.co/posts/pelicanmaxxing.html) ⭐️ 7.0/10

A systematic analysis of 1008 AI-generated images testing whether AI labs are specifically optimizing for the 'pelican on a bicycle' benchmark, with sound methodology that goes beyond casual spot-checking.

hackernews · dcastm · Jul 22, 17:17 · [Discussion](https://news.ycombinator.com/item?id=49010129)

**Tags**: `#AI evaluation`, `#benchmark integrity`, `#image generation`, `#AI labs`, `#methodology`

---

<a id="item-14"></a>
## [Protecting our FLOSS commons from LLMs](https://blog.codeberg.org/protecting-our-floss-commons-from-llms.html) ⭐️ 7.0/10

Codeberg announces measures to protect FLOSS projects hosted on their platform from being scraped and used as LLM training data, sparking debate about open source identity and AI ethics.

hackernews · acmnrs · Jul 23, 01:14 · [Discussion](https://news.ycombinator.com/item?id=49015635)

**Tags**: `#open-source`, `#LLM`, `#Codeberg`, `#FLOSS`, `#policy`

---

<a id="item-15"></a>
## [DAC 2026: Chip Giants Build DIY AI Design Tools, Bypassing EDA Vendors](https://www.eetimes.com/dac-2026-users-are-not-waiting-diy-ai-is-now-in-vogue/) ⭐️ 7.0/10

At DAC 2026, EE Times reports that major chip companies are no longer waiting for traditional EDA vendors to deliver AI-powered design tools and are instead building their own AI-driven design capabilities in-house. This shift signals a potential disruption to the long-standing EDA oligopoly dominated by Synopsys, Cadence, and Siemens EDA, and could reshape how AI is integrated into semiconductor design workflows across the industry. The available content is limited to a brief teaser paragraph; specific chip companies, tool names, and technical capabilities discussed at DAC 2026 are not detailed in the source material provided.

rss · EE Times · Jul 23, 07:45

**Background**: The Design Automation Conference (DAC) is the premier annual event for the electronic design automation (EDA) industry, combining a technical conference with a trade show focused on semiconductor and electronic system design. EDA tools are specialized software used to design, simulate, verify, and manufacture semiconductor chips, spanning the full IC workflow from design to packaging and testing. The EDA market has long been dominated by three major vendors—Synopsys, Cadence Design Systems, and Siemens EDA (formerly Mentor Graphics)—which have historically grown through both internal R&D and acquisitions of startups. AI's growing role in chip design has been a rising theme in recent years, with traditional EDA vendors racing to incorporate AI features into their offerings.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Design_Automation_Conference">Design Automation Conference - Wikipedia</a></li>
<li><a href="https://semiengineering.com/knowledge_centers/eda-design/definitions/electronic-design-automation/">Electronic Design Automation ( EDA ) - Semiconductor Engineering</a></li>
<li><a href="https://en.wikipedia.org/wiki/Comparison_of_EDA_software">Comparison of EDA software - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#EDA`, `#semiconductor`, `#AI`, `#DAC2026`, `#chip-design`

---

<a id="item-16"></a>
## [Framework Teases Desktop with Ryzen AI Max+ PRO 495 and 192GB Memory](https://www.techpowerup.com/350997/framework-teases-desktop-with-ryzen-ai-max-pro-495-and-192gb-memory) ⭐️ 6.5/10

Framework teases its first mini-PC powered by AMD Ryzen AI Max+ PRO 495 with 192GB LPDDR5X unified memory, enabling local AI inference for models up to 300 billion parameters.

rss · TechPowerUp News · Jul 23, 08:30

**Tags**: `#AMD`, `#Framework`, `#AI hardware`, `#local inference`, `#Ryzen AI`

---

<a id="item-17"></a>
## [CachyOS Proton Fork Adds NVIDIA Reflex Support via vkd3d-low-latency](https://www.techpowerup.com/350984/linux-gets-nvidia-reflex-support-in-new-cachyos-proton-translation-layer) ⭐️ 6.5/10

The latest build of proton-cachyos (cachyos-11.0-20260703-slr) now includes NVIDIA Reflex latency reduction support through the vkd3d-low-latency DX12-to-Vulkan translation layer, a feature that was previously absent from vkd3d-proton, which only supported AMD's Anti-Lag. This fills a long-standing gap in Linux gaming where DirectX 12 titles lacked access to NVIDIA Reflex's low-latency optimizations, and the implementation works across both NVIDIA and AMD GPUs, benefiting a broader audience of Linux gamers who previously had to rely on vendor-specific solutions. The Reflex implementation natively executes within the translation layer rather than converting to the VK_NV_low_latency2 Vulkan extension, enabling hardware-agnostic frame pacing. However, it does not work on Intel GPUs and still requires individual games to expose in-game Reflex toggles to function.

rss · TechPowerUp News · Jul 22, 22:45

**Background**: Proton is Valve's open-source compatibility layer, built on Wine and components like DXVK (for Direct3D 9-11) and vkd3d-proton (for Direct3D 12), that allows Windows games to run on Linux; its success on the Steam Deck catalyzed the rise of numerous Linux gaming distributions. CachyOS is one such Arch-based distribution that maintains its own Proton fork, often integrating experimental fixes before they reach upstream. NVIDIA Reflex is a vendor SDK that synchronizes CPU and GPU work to reduce render and input latency, roughly analogous to AMD's Anti-Lag and Intel's latency-reduction technologies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gamingonlinux.com/2026/07/proton-cachyos-adds-support-for-vkd3d-low-latency-upgrades-d7vk-and-more/">Proton-CachyOS adds support for vkd 3 d - low - latency , upgrades d7vk...</a></li>
<li><a href="https://github.com/netborg-afps/vkd3d-low-latency/releases">Releases · netborg-afps/ vkd 3 d - low - latency · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/DXVK">DXVK - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#linux-gaming`, `#proton`, `#nvidia-reflex`, `#vkd3d`, `#cachyos`

---

<a id="item-18"></a>
## [Developer Gets NVIDIA RTX 4060 Working on Windows-on-Arm Desktop](https://www.techpowerup.com/350967/nvidia-rtx-4060-running-on-arm-desktop-shows-promise-for-gaming-on-windows-on-arm) ⭐️ 6.5/10

A Chinese developer known as VoidTech extracted NVIDIA's ARM64 driver from the RTX Spark toolkit and successfully ran an NVIDIA RTX 4060 GPU on a Huawei Qingyun Arm desktop powered by a Kunpeng 920 CPU. While the GPU is recognized by both NVIDIA's driver and GPU-Z and can accelerate graphics tasks, there is no video output, making the setup currently suitable only for streaming. This is an important early milestone for Windows-on-Arm gaming, as it demonstrates that the ecosystem is maturing beyond simple productivity workloads toward supporting discrete gaming GPUs. If NVIDIA eventually releases official ARM64 drivers for its consumer GeForce lineup, it could unlock a new frontier for Arm-based desktops and laptops capable of running modern games. The GPU-Z utility properly recognizes the RTX 4060, confirming the driver is functional at a hardware level, but the absence of video output means the system can only accelerate rendering tasks for remote display or streaming rather than driving a local monitor. There is also still no native Windows-on-Arm CUDA toolkit outside of WSL, so CUDA-based applications like Blender still run as x64 builds under emulation.

rss · TechPowerUp News · Jul 22, 17:05

**Background**: Windows-on-Arm refers to Microsoft's effort to run Windows on processors built on the Arm architecture, which traditionally powers smartphones and is now expanding into laptops and desktops. A key historical limitation has been software compatibility, especially for x86-native applications and drivers, though Microsoft has added x86-to-Arm emulation to bridge the gap. NVIDIA's RTX Spark is an Arm-based Windows platform that recently received its first native ARM64 CUDA toolkit, but its drivers were originally intended for the platform's own GPUs rather than consumer GeForce cards. The Huawei Kunpeng 920 is an Arm-based server CPU with up to 64 cores, which is now also appearing in desktop form factors like the Qingyun system used in this experiment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/350891/nvidia-paves-the-way-for-windows-on-arm-gaming-with-rtx-spark-toolkit">NVIDIA Paves the Way for Windows - on - Arm Gaming With RTX ...</a></li>
<li><a href="https://wccftech.com/developer-forces-nvidia-rtx-4060-onto-windows-11-arm-by-hacking-drivers-never-meant-for-it/">Developer Forces NVIDIA RTX 4060 Onto Windows 11 Arm By...</a></li>
<li><a href="https://www.servethehome.com/huawei-kunpeng-920-64-core-arm-server-cpu/">Huawei Kunpeng 920 64-Core Arm Server CPU... - ServeTheHome</a></li>

</ul>
</details>

**Tags**: `#Windows-on-Arm`, `#NVIDIA`, `#RTX-4060`, `#Arm-desktop`, `#gaming`

---

<a id="item-19"></a>
## [Jensen Huang argues American companies should be allowed to use Chinese AI models — Nvidia CEO says backdoors connected to China are misconceptions](https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-argues-american-companies-should-be-allowed-to-use-chinese-ai-models-nvidia-ceo-says-backdoors-connected-to-china-are-misconceptions) ⭐️ 6.5/10

Nvidia CEO Jensen Huang urges that American companies should be allowed to use Chinese AI models and argues that backdoor concerns are misconceptions, advocating for open AI models.

rss · Tom's Hardware · Jul 22, 17:55

**Tags**: `#AI policy`, `#Nvidia`, `#US-China relations`, `#open source AI`, `#Jensen Huang`

---

<a id="item-20"></a>
## [Fortinet becomes Intel Foundry's first Intel 4 customer with SP6 ASIC](https://www.tomshardware.com/tech-industry/semiconductors/intel-4-gets-its-first-foundry-customer-in-fortinet-three-years-after-intel-scoped-the-node-to-meteor-lake) ⭐️ 6.5/10

Fortinet has become the first foundry customer for Intel's Intel 4 process node, with Intel set to design, package, and fabricate Fortinet's sixth-generation Security Processor (SP6) for its FortiGate firewalls. This marks the first external customer win for Intel 4, which was originally scoped primarily for Intel's own Meteor Lake processors three years ago. This is a notable milestone for Intel's foundry business, which has been struggling with significant financial losses and is central to the company's strategic pivot under CEO Lip-Bu Tan. While the deal is on a mature node rather than Intel's leading-edge 18A, it provides meaningful validation of Intel Foundry Services with a credible networking and security customer. Intel 4 was Intel's first process node to use EUV lithography and was designed to deliver roughly 20% higher performance at double the transistor density versus its predecessor. The SP6 is a custom firewall ASIC (Application-Specific Integrated Circuit) — a specialized chip optimized for deep-packet inspection and security workloads rather than general-purpose computing.

rss · Tom's Hardware · Jul 22, 16:17

**Background**: Intel Foundry is Intel's contract manufacturing arm, designed to fabricate chips designed by other companies — a business model pioneered by TSMC. Under CEO Lip-Bu Tan, Intel has aggressively pursued external foundry customers as part of a strategic restructuring. Intel 4 is a relatively mature node (roughly comparable to TSMC's N4/N5 in capability terms) that entered high-volume production around 2023. ASIC-based firewall processors, like Fortinet's SP-series, are custom silicon that offloads security functions from general-purpose CPUs for higher throughput and lower power consumption in enterprise firewalls.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/intel-to-co-develop-and-manufacture-fortinets-next-gen-firewall-asic">Intel to co-develop and manufacture Fortinet's next-gen firewall ASIC ...</a></li>
<li><a href="https://www.techpowerup.com/295809/intel-4-process-node-detailed-doubling-density-with-20-higher-performance">Intel 4 Process Node Detailed, Doubling Density with... | TechPowerUp</a></li>
<li><a href="https://www.remio.ai/post/intel-s-recovery-hinges-on-its-high-stakes-foundry-business">Intel 's Recovery Hinges on Its High-Stakes Foundry Business</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#semiconductors`, `#foundry`, `#Fortinet`, `#Intel-4`

---