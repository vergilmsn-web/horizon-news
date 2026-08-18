---
layout: default
title: "Horizon Summary: 2026-08-18 (EN)"
date: 2026-08-18
lang: en
---

> From 85 items, 20 important content pieces were selected

---

1. [DuckDB v2.0 Preview: Quack Adds Client/Server Mode](#item-1) ⭐️ 9.0/10
2. [AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](#item-2) ⭐️ 8.0/10
3. [HBM Shipments Shift to Malaysia, Intel's Project Pelican Emerges as CoWoS Competitor](#item-3) ⭐️ 7.5/10
4. [Intel Nova Lake-S Tested with AVX-512 and APX Support](#item-4) ⭐️ 7.5/10
5. [Geekom ships malware-laced drivers in AMD mini PCs, then removes them](#item-5) ⭐️ 7.5/10
6. [DDR5 Memory Prices Surge 500% in 12 Months, Hitting 10x Historical Lows](#item-6) ⭐️ 7.5/10
7. [America's largest grid wants to cut power to new data centers first during shortages — 50MW-plus data centers must bring their own electricity generation to avoid shutoffs](#item-7) ⭐️ 7.5/10
8. [美国一原告在法庭文件中植入针对 LLM 的提示词](#item-8) ⭐️ 7.3/10
9. [AI;DR Movement: Readers Push Back Against LLM-Generated Content](#item-9) ⭐️ 7.0/10
10. [Liquid Cooling Set to Reach 53% Penetration in High-End AI Servers by 2026](#item-10) ⭐️ 7.0/10
11. [Security Gaps in Brain-Inspired Neuromorphic Chips for Embedded Devices](#item-11) ⭐️ 7.0/10
12. [Nvidia Books TSMC 1.6nm A16 Capacity for Feynman GPU](#item-12) ⭐️ 7.0/10
13. [XPU to CPU ratio in datacentres transitioning from 10:1 to 1:1](#item-13) ⭐️ 7.0/10
14. [ASUS GPU Tweak III Adds Auto-Shutdown to Prevent 12V-2×6 Meltdowns](#item-14) ⭐️ 6.5/10
15. [CXMT Breaks 9,000 MT/s DDR5 Barrier on AMD Platform](#item-15) ⭐️ 6.5/10
16. [Alibaba is selling its gaming studio for at least $1.5 billion to help fund AI buildout, mirroring Micron's exit from consumer business — dumps entire stake in Lingxi Games, which made 'Three Kingdoms: Strategy Edition'](#item-16) ⭐️ 6.5/10
17. [Cherokee Nation bans hyperscale data centers on tribal lands](#item-17) ⭐️ 6.5/10
18. [AI Data Center Optical Interconnect Market to Reach $144 Billion by 2030](#item-18) ⭐️ 6.5/10
19. [PC Partner Warns of H2 2026 GPU Price Hikes and Budget Card Shortages](#item-19) ⭐️ 6.5/10
20. [Japanese Shop Offers $25/GB GPU VRAM Upgrades for Budget AI](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [DuckDB v2.0 Preview: Quack Adds Client/Server Mode](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 9.0/10

DuckDB v2.0 was previewed with major new features, most notably the 'Quack' extension, which implements a native client/server protocol allowing DuckDB instances to communicate over a network. The v2.0 release also incorporates approximately 10,000 commits accumulated in under six months. Quack transforms DuckDB from a purely embedded analytics engine into a hybrid client/server system, dramatically expanding its deployment scenarios — from single-machine analytics to distributed workloads — without sacrificing its signature ease of use. The v2.0 milestone also signals continued strong investment in a tool that has become a foundational layer in modern data stacks, from dbt pipelines to streaming engines. Quack is delivered as an extension rather than a core change, meaning both client and server are DuckDB instances communicating via a native protocol. The DuckDB project noted that users had 'very persistently' requested client/server mode, which the team had previously resisted in favor of the embedded model.

hackernews · ibotty · Aug 17, 13:46 · [Discussion](https://news.ycombinator.com/item?id=49330781)

**Background**: DuckDB is an in-process analytical (OLAP) database management system, first released in 2018, designed for fast columnar analytics directly within applications (commonly Python or R). Unlike traditional client-server systems such as PostgreSQL, DuckDB runs embedded inside the host process, similar to SQLite but optimized for analytical workloads. It supports spilling to disk to handle datasets larger than available memory, and has become popular for local data analysis, data engineering pipelines, and embedded analytics. OLAP (Online Analytical Processing) refers to database systems optimized for complex multi-dimensional queries and reporting, as opposed to OLTP (Online Transaction Processing) which handles many small transactions.

<details><summary>References</summary>
<ul>
<li><a href="https://duckdb.org/2026/08/17/duckdb-20-highlights">A Preview of DuckDB v2.0 – DuckDB</a></li>
<li><a href="https://duckdb.org/quack/">Quack Remote Protocol – DuckDB</a></li>
<li><a href="https://duckdb.org/">DuckDB – An in-process SQL OLAP database management system</a></li>
<li><a href="https://en.wikipedia.org/wiki/Online_analytical_processing">Online analytical processing - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community response is overwhelmingly enthusiastic, with practitioners describing DuckDB as a go-to tool for dbt pipelines, streaming analytics engines (like sql-flow processing thousands of events per second), spatial workloads, and embedded runtime storage. Several commenters expressed excitement specifically about Quack. One notable thread questioned whether the 10,000 commits in under six months reflect significant AI-assisted development, raising a broader meta-discussion about the pace of AI-augmented open-source development.

**Tags**: `#duckdb`, `#database`, `#analytics`, `#olap`, `#open-source`

---

<a id="item-2"></a>
## [AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 8.0/10

AI-generated GitHub Copilot 'Autofix' code introduced a template injection vulnerability in Snowflake's GitHub Actions workflow, enabling compromise of their Jira instance.

hackernews · galnagli · Aug 17, 14:18 · [Discussion](https://news.ycombinator.com/item?id=49331423)

**Tags**: `#security`, `#ai-generated-code`, `#github-actions`, `#supply-chain`, `#copilot`, `#vulnerability`

---

<a id="item-3"></a>
## [HBM Shipments Shift to Malaysia, Intel's Project Pelican Emerges as CoWoS Competitor](https://www.techpowerup.com/351658/hbm-shipments-to-malaysia-surge-pointing-to-intels-project-pelican-facility) ⭐️ 7.5/10

According to SemiAnalysis Chipbook export data, high-bandwidth memory (HBM) shipments from South Korea are increasingly heading to Malaysia rather than Taiwan, with approximately $1.3 billion in HBM now going to Malaysia versus less than $3 billion to Taiwan—down from over $5 billion to Taiwan just months ago. Analysts infer that Intel's $7 billion Project Pelican advanced packaging facility in Malaysia is absorbing HBM integration work that was previously TSMC's CoWoS domain. This shift signals the emergence of Intel as a viable second source for advanced HBM packaging, potentially breaking TSMC's near-monopoly on CoWoS technology that is critical for AI accelerator production. Foundry customers now have an alternative path for chiplet integration, which could reshape the AI chip supply chain and ease the severe CoWoS capacity bottleneck that has constrained NVIDIA and other AI GPU deliveries. Intel's Project Pelican supports both EMIB (Embedded Multi-die Interconnect Bridge) and Foveros packaging flows, and the facility is 99% complete with operations expected to begin in 2026. The inference that Intel—not TSMC or other smaller Malaysian players—is the recipient of this HBM volume is based on the fact that TSMC has no advanced packaging fab in Malaysia and only Intel's EMIB/Foveros technologies are mature enough to handle large-scale HBM integration.

rss · TechPowerUp News · Aug 17, 17:19

**Background**: High-Bandwidth Memory (HBM) is a 3D-stacked DRAM technology that provides extremely high data throughput between memory and processors, making it essential for AI training and inference chips such as NVIDIA GPUs. Advanced packaging technologies like TSMC's CoWoS (Chip-on-Wafer-on-Substrate) and Intel's EMIB and Foveros are required to physically integrate HBM stacks with logic dies in a single package, enabling the chiplet-based designs that power modern AI accelerators. CoWoS comes in several variants—CoWoS-S, CoWoS-L, and CoWoS-R—each offering different trade-offs in interconnect density and scalability. Demand for CoWoS has far outstripped supply, creating a major bottleneck in the AI hardware supply chain.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/343545/intel-completes-project-pelican-malaysia-packaging-fab-for-emib-and-foveros">Intel Completes "Project Pelican" Malaysia Packaging Fab for EMIB and Foveros | TechPowerUp</a></li>
<li><a href="https://www.trendforce.com/news/2026/03/18/news-intel-ramps-up-advanced-packaging-malaysia-complex-operational-in-2026-emib-update/">[News] Intel Ramps Up Advanced Packaging: Malaysia Complex Operational in 2026, EMIB Update</a></li>
<li><a href="https://www.ariat-tech.com/blog/CoWoS-Packaging-Explained-CoWoS-S-vs.CoWoS-R-vs.CoWoS-L,HBM,Manufacturing,and-AI-Chips.html">CoWoS Packaging Explained: CoWoS - S vs. CoWoS - R vs....</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#intel`, `#HBM`, `#advanced-packaging`, `#supply-chain`

---

<a id="item-4"></a>
## [Intel Nova Lake-S Tested with AVX-512 and APX Support](https://www.techpowerup.com/351647/intel-nova-lake-s-tested-with-avx-512-and-apx-enabled) ⭐️ 7.5/10

Intel has been internally testing two Nova Lake-S desktop CPU SKUs — a 24-core variant at 3.4 GHz and a 28-core variant at 3.2 GHz — both featuring AVX-512 and APX instruction sets, as confirmed by InstLatX64. This confirms that 512-bit vector processing is returning to Intel's desktop lineup after being absent since the 11th generation. The return of AVX-512 to Intel's mainstream desktop platform closes a significant performance gap for HPC, scientific computing, machine learning inference, and other SIMD-heavy workloads that previously required Xeon or HEDT chips. Combined with APX's doubled register count, Nova Lake-S narrows the divide between consumer and server/professional tiers, giving developers and enthusiasts a much more capable general-purpose and vector platform. Nova Lake-S uses 'Coyote Cove' P-cores and 'Arctic Wolf' E-cores, sits on the new LGA1954 socket, and is expected to launch later in 2026. AVX-512 was disabled on Alder Lake and Raptor Lake client CPUs because the hybrid P-core/E-core design complicated software optimization, so its reintroduction here signals that Intel has resolved those software/hardware coexistence issues.

rss · TechPowerUp News · Aug 17, 12:46

**Background**: AVX-512 is a 512-bit-wide SIMD instruction set extension introduced by Intel in 2013 (first shipped on Xeon Phi Knights Landing in 2016) that doubles the floating-point operations per clock compared to 256-bit AVX2, making it valuable for HPC, cryptography, and ML workloads. Intel APX (Advanced Performance Extensions) doubles the number of general-purpose registers from 16 to 32 and adds other features to enhance general-purpose CPU performance without significantly increasing silicon area or power consumption. Intel originally disabled AVX-512 on its 12th-gen Alder Lake hybrid CPUs due to the complexity of running 512-bit instructions on heterogeneous core types, effectively pushing desktop users needing AVX-512 toward Xeon or HEDT platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://builders.intel.com/docs/networkbuilders/intel-avx-512-instruction-set-for-packet-processing-technology-guide-1645717553.pdf">Intel ® AVX - 512 - Instruction Set for Packet Processing Technology...</a></li>
<li><a href="https://www.phoronix.com/news/Intel-APX">Intel Details APX - Advanced Performance Extensions - Phoronix</a></li>
<li><a href="https://www.igorslab.de/en/intel-nova-lake-s-when-mainstream-suddenly-smells-like-hedt/">Intel Nova Lake - S : When mainstream suddenly smells like... | igor´sLAB</a></li>

</ul>
</details>

**Tags**: `#intel`, `#cpu-architecture`, `#avx-512`, `#nova-lake`, `#hardware`

---

<a id="item-5"></a>
## [Geekom ships malware-laced drivers in AMD mini PCs, then removes them](https://www.tomshardware.com/tech-industry/cyber-security/geekom-admits-to-shipping-malware-laced-network-drivers-for-amd-mini-pcs-company-responds-with-guidance-removes-malicious-package) ⭐️ 7.5/10

Geekom has confirmed that network drivers hosted on its website for its AMD-based A7, A8, AE7, AX7 Pro, and AX8 Pro mini PCs were flagged by Windows Security as trojans capable of executing attacker commands, and the company has since removed the affected legacy LAN driver download page entirely. In an official statement, Geekom attributed the issue to an outdated resource on an older page that was publicly accessible but no longer linked from the main product page. This is a textbook supply chain security incident: a hardware vendor shipped software containing malware from an official download channel, directly undermining trust in out-of-the-box devices. It highlights the importance of consumers verifying driver downloads via multiple scanning tools and reinforces calls for greater transparency from hardware vendors regarding software bill of materials. The malicious file was verified as malware by multiple independent scanning services, including VirusTotal (which uses over 70 antivirus engines), FileScan, and OPSWAT's MetaDefender. Geekom stated the issue is confined to the now-removed legacy drivers and issued an apology, though the company reportedly also requested a takedown of reporting on the incident, raising concerns about transparency.

rss · Tom's Hardware · Aug 17, 17:18

**Background**: Supply chain security refers to the practice of securing every link in the software and hardware delivery chain, from development through to the end user, since attackers often exploit trusted vendor channels to distribute malware. When a hardware vendor ships infected drivers, customers who install them believing them to be legitimate can unknowingly grant attackers remote command execution on their systems. Multi-engine malware scanning platforms like VirusTotal and MetaDefender allow users and researchers to independently verify suspicious files by submitting them to dozens of antivirus engines and sandbox environments at once.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VirusTotal">VirusTotal - Wikipedia</a></li>
<li><a href="https://www.opswat.com/products/metadefender">Advanced Threat Prevention - MetaDefender - OPSWAT</a></li>
<li><a href="https://www.linkedin.com/posts/tekkeez_smbsecurity-supplychain-cybersecurity-activity-7415105351567507456-PMRi">Protect Your Supply Chain from Cyber Risks | TekkEez... | LinkedIn</a></li>

</ul>
</details>

**Discussion**: Community discussion on Reddit's r/MiniPCs raised alarms about the malware, with users sharing verification results from VirusTotal, FileScan, and MetaDefender to confirm the threat. Sentiment was strongly negative toward Geekom, with frustration compounded by reports that the company attempted to suppress the original reporting via a takedown request rather than addressing the issue transparently first.

**Tags**: `#cybersecurity`, `#supply-chain-security`, `#malware`, `#hardware`, `#consumer-electronics`

---

<a id="item-6"></a>
## [DDR5 Memory Prices Surge 500% in 12 Months, Hitting 10x Historical Lows](https://www.tomshardware.com/pc-components/ram/memory-prices-climb-500-percent-in-12-months-up-to-10x-the-lowest-ever-tracked-prices-128gb-of-ddr5-now-usd3-399) ⭐️ 7.5/10

Tom's Hardware reports that DDR5 memory prices have climbed approximately 500% over the past 12 months and now reach up to 10x the lowest prices ever tracked, with a 128GB DDR5 kit now priced at $3,399. This unprecedented memory price surge affects PC builders, gamers, data centers, and AI infrastructure projects, potentially slowing hardware upgrades and increasing the total cost of computing systems across the industry. The price increases are primarily driven by surging AI server demand, which is consuming memory supply; similar trends are affecting SSDs and other storage products as the broader memory market faces tight capacity allocation.

rss · Tom's Hardware · Aug 17, 13:52

**Background**: DDR5 is the latest generation of Double Data Rate Synchronous DRAM, succeeding DDR4 with higher bandwidth, lower power consumption, and greater density per module. The current memory crisis, sometimes dubbed the 'RAMpocalypse,' is largely attributed to AI companies building massive data centers that require enormous quantities of both system memory (DRAM) and storage (NAND/SSD). Memory manufacturers are prioritizing high-capacity server-grade products over consumer DIMMs, creating a supply squeeze that has pushed retail prices to record highs across the consumer market.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pcgamer.com/hardware/memory/ram-and-storage-is-ridiculously-expensive-right-now-because-of-drumroll-ai-of-course-and-theres-little-reason-to-think-prices-will-drop-any-time-soon/">Explainer: The RAMpocalypse is making memory , SSDs... | PC Gamer</a></li>
<li><a href="https://en.hwlibre.com/DDR5-memory-price-crisis:-why-have-prices-skyrocketed-and-when-might-they-come-down/">DDR5 memory price crisis : why prices have skyrocketed and when...</a></li>
<li><a href="https://en.wikipedia.org/wiki/DDR_SDRAM">DDR SDRAM - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#memory`, `#DDR5`, `#hardware`, `#pricing`, `#PC-components`

---

<a id="item-7"></a>
## [America's largest grid wants to cut power to new data centers first during shortages — 50MW-plus data centers must bring their own electricity generation to avoid shutoffs](https://www.tomshardware.com/tech-industry/data-centers/new-data-centers-on-americas-largest-grid-face-first-in-line-blackouts-unless-they-bring-their-own-power) ⭐️ 7.5/10

PJM Interconnection proposes federal rules to prioritize power shutoffs to new large data centers (50MW+) during shortages unless they provide their own on-site generation.

rss · Tom's Hardware · Aug 17, 13:11

**Tags**: `#data-centers`, `#energy-policy`, `#ai-infrastructure`, `#grid-management`, `#regulation`

---

<a id="item-8"></a>
## [美国一原告在法庭文件中植入针对 LLM 的提示词](https://www.solidot.org/story?sid=85109) ⭐️ 7.3/10

A digest covering the first known case of LLM prompt injection embedded in US court filings, an investigation into Amazon's mass book-scanning-and-destruction operation for AI training data, and Qwen surpassing 3 billion downloads on Hugging Face.

rss · Solidot · Aug 17, 07:16

**Tags**: `#prompt-injection`, `#AI-security`, `#legal-tech`, `#AI-training-data`, `#Qwen`

---

<a id="item-9"></a>
## [AI;DR Movement: Readers Push Back Against LLM-Generated Content](https://www.rickmanelius.com/p/aidr-ai-didnt-read) ⭐️ 7.0/10

A concept coined 'AI;DR' (AI; Didn't Read) — a declaration that the reader skipped a piece because it appeared to be AI-generated — went viral on Hacker News with 562 upvotes and 353 comments, reflecting growing cultural resistance to LLM-generated text across online writing, codebases, and workplace communication. This signals a maturing cultural pushback against uncritical AI adoption: readers are beginning to curate their attention by rejecting machine-generated prose, which could reshape content strategy, developer documentation practices, and how teams use LLMs in collaborative workflows. The workplace anecdotes shared in the discussion suggest the backlash is not merely aesthetic but operational, with codebases becoming 'post-readable' due to verbose AI documentation. The Hacker News discussion surfaced specific pain points: developers report drowning in AI-generated PR documentation with 'performative' comments about variable names, and some commenters argue that sharing the original prompt is more valuable than sharing the AI output. The movement treats AI-generated text as a signal of 'intellectual laziness' rather than genuine expertise transfer.

hackernews · mooreds · Aug 17, 19:47 · [Discussion](https://news.ycombinator.com/item?id=49336573)

**Background**: Since the public release of ChatGPT in late 2022, LLM-generated text has proliferated across the internet, from blog posts and product descriptions to code comments and corporate documentation. Detectors using stylometry — statistical analysis of writing style — and machine learning classifiers have been developed to identify AI-generated text, but they often struggle with generalization across domains and can be evaded by light editing. Meanwhile, a cultural backlash has grown alongside adoption, with readers and professionals increasingly vocal about the verbosity, jargon-heavy phrasing, and lack of personal voice they associate with LLM output. The 'AI;DR' label is part of this broader skepticism, functioning as a social signal that mirrors earlier 'TL;DR' shorthand but weaponizes it against machine authorship.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thealgorithmicbridge.com/p/its-ai-so-i-didnt-read">It’s AI , so I Didn ’ t Read - by Alberto Romero</a></li>
<li><a href="https://news.ycombinator.com/item?id=49336573">AI ; DR ( AI ; Didn ' t Read ) | Hacker News</a></li>
<li><a href="https://aman.ai/primers/ai/AIDetect/">Aman's AI Journal • NLP • AI Text Detection Techniques</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread shows broad consensus that unsolicited AI-generated content is unwelcome. Commenters described workplace frustration with AI documentation bloating codebases and degrading readability, criticized AI prose as verbose and lacking nuance, and some made the provocative suggestion that sharing the prompt would be more useful than sharing the AI output. A recurring theme is that AI text signals intellectual laziness and erodes authentic human communication, though a minority pushed back, arguing that only a small fraction of AI-generated writing is actually worth reading and that the 'AI;DR' label itself is performative.

**Tags**: `#ai-generated-content`, `#culture`, `#llm`, `#developer-experience`, `#content-quality`

---

<a id="item-10"></a>
## [Liquid Cooling Set to Reach 53% Penetration in High-End AI Servers by 2026](https://www.dramexchange.com/WeeklyResearch/Post/2/12801.html) ⭐️ 7.0/10

TrendForce's latest AI server research indicates that liquid cooling adoption in high-end AI server infrastructure is projected to reach 53% penetration by 2026, driven by escalating thermal demands from advanced AI workloads such as large language model training and inference. This shift signals a fundamental change in data center architecture, as traditional air cooling struggles to handle the thermal output of next-generation AI accelerators. Hyperscalers, colocation providers, and server OEMs will need to redesign facility layouts, supply chains, and maintenance workflows to accommodate liquid cooling at scale. Liquid cooling is more energy-efficient than air cooling because it reduces the energy needed for thermal management, enabling higher server density and lower overall data center operating costs. However, the article content was truncated, so specific breakdowns by cooling type (direct-to-chip vs. immersion) or vendor-level data were not available in the source.

rss · DRAMeXchange (TrendForce) · Aug 17, 03:59

**Background**: Liquid cooling is a thermal management approach that uses liquid—typically water or a dielectric fluid—to transfer heat away from server components, as opposed to traditional air cooling with fans and HVAC systems. TrendForce is a Taiwan-based market intelligence firm widely cited in the semiconductor, display, and data center industries for forecasts on technology adoption and pricing. AI workloads, particularly training large neural networks on GPU clusters, generate significantly more heat per rack than conventional computing tasks, pushing cooling systems to their limits and motivating the industry shift toward liquid-based solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.trendforce.com/">Global Market Intelligence & Consulting | TrendForce</a></li>
<li><a href="https://www.linkedin.com/pulse/untapped-potential-liquid-cooling-modern-data-centres-tony-lock-eew5e">The Untapped Potential of Liquid Cooling in Modern Data Centres</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#liquid cooling`, `#TrendForce`, `#server hardware`

---

<a id="item-11"></a>
## [Security Gaps in Brain-Inspired Neuromorphic Chips for Embedded Devices](https://www.electronicsweekly.com/news/design/eda-and-ip/security-challenges-of-neuromorphic-intelligence-on-embedded-systems-2026-08/) ⭐️ 7.0/10

Electronics Weekly has published an analysis by Venus Kohli highlighting that while brain-inspired neuromorphic chips offer impressive processing efficiency for embedded devices, their security maturity still lags behind that of conventional von Neumann processors. As neuromorphic processors increasingly power edge AI and IoT applications, unresolved security vulnerabilities could expose sensitive data and critical functions in resource-constrained devices. Closing this gap is essential before these chips can be safely deployed at scale in automotive, industrial, and consumer embedded systems. The article contrasts the neuromorphic approach—which integrates memory and processing on-chip for brain-like computation—against the well-established security ecosystems built around decades of von Neumann CPU development. The published excerpt is brief and does not enumerate specific attack vectors, but signals that security tooling, formal verification, and threat modeling for neuromorphic hardware are still immature areas.

rss · Electronics Weekly · Aug 17, 11:46

**Background**: Neuromorphic computing is a radical departure from the traditional von Neumann architecture, where processing and memory are physically separated. Neuromorphic chips instead use in-memory computing and spiking neural networks (SNNs) to mimic how biological neurons operate, yielding high energy efficiency especially for event-driven and sensory AI tasks. Because this paradigm is relatively new, the security infrastructure—hardware root-of-trust, side-channel mitigations, encrypted memory buses, and established verification flows—that has been refined over decades for CPUs and GPUs does not yet exist at the same level for neuromorphic accelerators.

<details><summary>References</summary>
<ul>
<li><a href="https://research.ibm.com/blog/what-is-neuromorphic-or-brain-inspired-computing">How neuromorphic computing takes inspiration from our brains</a></li>
<li><a href="https://fiveable.me/advanced-computer-architecture/unit-16/neuromorphic-computing-architectures/study-guide/MH0tY1CQkuItJgKO">Neuromorphic Computing Architectures | Advanced... | Fiveable</a></li>
<li><a href="https://www.researchgate.net/publication/378891450_NEUROSEC_FPGA-Based_Neuromorphic_Audio_Security">(PDF) NEUROSEC: FPGA-Based Neuromorphic Audio Security</a></li>

</ul>
</details>

**Tags**: `#neuromorphic-computing`, `#embedded-systems`, `#hardware-security`, `#AI-hardware`, `#edge-AI`

---

<a id="item-12"></a>
## [Nvidia Books TSMC 1.6nm A16 Capacity for Feynman GPU](https://www.electronicsweekly.com/news/business/nvidia-books-tsmc-1-6nm-process-for-feynman-in-h2-2028-2026-08/) ⭐️ 7.0/10

Nvidia has reportedly booked TSMC's A16 (1.6nm) process capacity for its 'Feynman' GPU architecture, which succeeds the Rubin generation and is targeted for production in the second half of 2028. This booking confirms Nvidia's multi-year GPU roadmap beyond the Rubin generation and validates TSMC's 1.6nm A16 node as a viable platform for the most demanding AI accelerators, signaling sustained demand for cutting-edge process technology across the HPC and AI chip ecosystem. The A16 node is TSMC's first 'angstrom-class' process, succeeding the 2nm N2 node and incorporating both GAA (gate-all-around) transistors and backside power delivery network (BSPDN), offering roughly 10% performance gains or 20% power reduction compared to N2, with mass production originally slated for late 2026.

rss · Electronics Weekly · Aug 17, 05:17

**Background**: TSMC's process nodes have progressed from traditional nanometer-scale naming (e.g., 5nm, 3nm, 2nm) into the 'angstrom era,' where A16 (1.6nm) represents the next generation of chip manufacturing. The A16 node introduces gate-all-around (GAA) transistors, in which the gate wraps entirely around the channel for superior electrostatic control, replacing the FinFET design used in earlier nodes. Additionally, backside power delivery (BSPDN) relocates power routing to the back of the wafer, reducing IR drop and freeing up front-side routing resources. Nvidia's GPU lineup has historically followed an architecture cadence (Hopper, Blackwell, Rubin), with 'Feynman' continuing this tradition as the post-Rubin successor aimed at AI and HPC workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/tsmc-a16-node-promises-speed-boost-power-cut-over-2nm-backside-power-production-q4-2026/">TSMC 's A 16 ' 1 . 6 nm ' Node Promises 10% Speed Boost or 20% Power...</a></li>
<li><a href="https://www.kad8.com/hardware/tsmc-a16-node-explained-backside-power-and-angstrom-era/">TSMC A16 Node Explained: Backside Power and Angstrom Era · KAD</a></li>
<li><a href="https://semiengineering.com/what-designers-need-to-know-about-gaa/">What Designers Need To Know About GAA | Semiconductor Engineering</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#nvidia`, `#tsmc`, `#process-technology`, `#gpu-architecture`

---

<a id="item-13"></a>
## [XPU to CPU ratio in datacentres transitioning from 10:1 to 1:1](https://www.electronicsweekly.com/news/business/xpu-to-cpu-ratio-transitioning-from-101-to-11-2026-08/) ⭐️ 7.0/10

Dell'Oro reports datacenter XPU-to-CPU ratios are shifting from 10:1 to 1:1 as the rise of inference workloads introduces networking requirements distinct from training.

rss · Electronics Weekly · Aug 17, 05:09

**Tags**: `#datacenter`, `#AI infrastructure`, `#inference`, `#hardware trends`, `#networking`

---

<a id="item-14"></a>
## [ASUS GPU Tweak III Adds Auto-Shutdown to Prevent 12V-2×6 Meltdowns](https://www.techpowerup.com/351662/asus-gpu-tweak-iii-adds-auto-shutdown-to-prevent-12v-2x6-meltdowns) ⭐️ 6.5/10

ASUS has released GPU Tweak III V2.1.8.0, which adds auto-shutdown protection for GPUs equipped with Power Detector+ hardware. The system will power off automatically when persistently high current is detected through the 12V-2×6 power connector. This update addresses a well-documented safety issue where 12V-2×6 power connectors on high-end NVIDIA GPUs have melted, destroying expensive graphics cards. It represents another incremental software-level mitigation in an ongoing industry-wide effort to protect GPUs while hardware-level fixes remain elusive. The auto-shutdown feature only works on ASUS GPUs with built-in Power Detector+ sensors, which include shunt resistors to monitor per-pin current: the ROG Astral RTX 5090, ROG Astral LC RTX 5090, ROG Astral RTX 5080, and ROG Matrix RTX 4090. ASUS has not disclosed the exact current thresholds or duration parameters that trigger the shutdown.

rss · TechPowerUp News · Aug 17, 18:48

**Background**: The 12V-2×6 (also known as 12VHPWR) connector is a 16-pin standard designed to deliver up to 600W to high-end GPUs, introduced with NVIDIA's RTX 4000 series and continued with the RTX 5000 series. It replaced bulky multiple 8-pin connectors but has suffered from widely reported melting incidents, often caused by improper insertion, uneven current distribution across pins, or manufacturing defects in cables and connectors. Power Detector+ is ASUS's hardware-level monitoring solution using sensors and shunt resistors to detect abnormal current draw on individual pins of the power connector.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/12VHPWR">12 VHPWR - Wikipedia</a></li>
<li><a href="https://www.guru3d.com/story/asus-power-feature-how-it-prevents-overheating-in-rog-astral-gpus/">ASUS Power Detector+ Feature : How It Prevents Overheating in...</a></li>
<li><a href="https://rog.asus.com/me-en/articles/guides/how-gpu-tweaks-power-detector-alerts-you-to-abnormal-current-on-your-rog-astral-graphics-card/">How GPU Tweak's Power Detector+ alerts you to abnormal current on...</a></li>

</ul>
</details>

**Tags**: `#ASUS`, `#GPU`, `#hardware-safety`, `#12V-2x6`, `#NVIDIA`

---

<a id="item-15"></a>
## [CXMT Breaks 9,000 MT/s DDR5 Barrier on AMD Platform](https://www.techpowerup.com/351649/cxmt-breaks-9-000-mt-s-barrier-with-ddr5) ⭐️ 6.5/10

Chinese DRAM manufacturer CXMT has surpassed the 9,000 MT/s threshold on an AMD platform, achieving 9,014 MT/s (4,507 MHz) with a 48 GB iGame Shadow II 24G×2 kit on a Colorful iGame X870E VULCAN W OC motherboard. The company is also testing ultra-low latency configurations at CL30 and even CL28 at 6,000 MT/s, signaling performance parity with leading global DRAM makers. This milestone demonstrates that CXMT, China's largest DRAM producer, is achieving competitive performance with established giants like Samsung, SK hynix, and Micron, which has significant implications for global memory market competition and China's semiconductor self-sufficiency. The combination of high transfer rates and tight latencies (CL28-30) makes CXMT memory viable for high-end consumer and enthusiast applications rather than just budget segments. The 9,014 MT/s figure derives from double data rate technology, where 4,507 MHz effectively doubles to exceed 9,000 MT/s. CXMT reached 8,000 MT/s only late last year, making this nearly 13% speed improvement in months; latency tests at CL28 on AMD and Intel platforms suggest the company is closing the gap not just in bandwidth but in real-world responsiveness measured by First Word Latency.

rss · TechPowerUp News · Aug 17, 13:28

**Background**: DDR5 is the latest generation of system memory, succeeding DDR4, and offers higher bandwidth and density required by modern CPUs, GPUs, and AI workloads. MT/s (MegaTransfers per second) measures how many data transfers occur per second, which for DDR memory is double the clock frequency in MHz due to double data rate signaling. CAS Latency (CL) measures the number of clock cycles between a memory request and the data being available; when combined with speed, it determines real-world latency. CXMT (ChangXin Memory Technologies) was founded in 2016 and is China's flagship domestic DRAM producer, critical to the country's efforts to reduce reliance on foreign memory suppliers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.msn.com/en-us/news/technology/explainer-what-is-cxmt-and-how-did-it-become-chinas-dram-champion/ar-AA28L4vy">Explainer - what is CXMT and how did it become China's DRAM ...</a></li>
<li><a href="https://www.electronicshub.org/mhz-vs-mt-s/">MHz vs MT / s RAM: Decoded! (Understanding RAM Speed)</a></li>
<li><a href="https://zombrax.com/ddr5-speeds-and-timings/">DDR 5 Memory Speeds and Timings: What Moves the Needle</a></li>

</ul>
</details>

**Tags**: `#DDR5`, `#memory`, `#CXMT`, `#overclocking`, `#hardware`

---

<a id="item-16"></a>
## [Alibaba is selling its gaming studio for at least $1.5 billion to help fund AI buildout, mirroring Micron's exit from consumer business — dumps entire stake in Lingxi Games, which made 'Three Kingdoms: Strategy Edition'](https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-sells-its-gaming-studio-for-at-least-1-5-billion-to-help-fund-ai-buildout) ⭐️ 6.5/10

Alibaba is selling its gaming studio Lingxi Games for at least $1.5 billion to fund AI infrastructure buildout, reflecting the broader industry trend of prioritizing AI investments.

rss · Tom's Hardware · Aug 17, 15:39

**Tags**: `#AI infrastructure`, `#Alibaba`, `#industry trends`, `#M&A`, `#investment`

---

<a id="item-17"></a>
## [Cherokee Nation bans hyperscale data centers on tribal lands](https://www.tomshardware.com/tech-industry/data-centers/largest-tribe-in-the-us-bans-hyperscale-data-centers-on-its-lands) ⭐️ 6.5/10

The Cherokee Nation, the largest tribe in the US with over 475,000 citizens, has officially banned hyperscale data center development on its tribally owned and trust lands. The tribe cited concerns including energy and water consumption, air quality, noise, and cultural resource protection, and stated it will not support any data center projects without prior consultation. This decision represents a significant pushback against the current AI infrastructure boom, as hyperscale data centers are primarily built by tech giants like Amazon, Google, Microsoft, and Meta to support cloud computing and AI workloads. It highlights growing tensions between rapid tech industry expansion and local community concerns about environmental impact and resource consumption, and could set a precedent for other tribal nations facing similar development pressures. "Hyperscale" refers to massive facilities typically housing tens of thousands of servers, operated by a handful of major cloud providers and requiring enormous capital investment and significant energy and water for cooling. The ban specifically covers tribally owned land and trust land—areas where the federal government holds legal title but the tribe retains beneficial use and jurisdiction.

rss · Tom's Hardware · Aug 17, 11:27

**Background**: Hyperscale data centers are enormous facilities designed to efficiently support the massive workloads of cloud computing and AI, typically housing enormous server arrays connected by hundreds of miles of fiber optic cable. They require massive capital investments and are primarily operated by companies like Amazon, Google, Microsoft, Meta, Apple, and IBM. Tribal lands in the US include both reservation land and trust land—trust land is held in legal title by the federal government but used beneficially by the tribe, while reservation boundaries define the outer limits of a tribe's historical jurisdiction. The Cherokee Nation, headquartered in Oklahoma, is the largest federally recognized tribe in the United States.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datacenterdynamics.com/en/analysis/what-is-a-hyperscale-data-center/">What is a hyperscale data center ? - DCD</a></li>
<li><a href="https://en.wikipedia.org/wiki/Indian_reservation">Indian reservation - Wikipedia</a></li>
<li><a href="https://filtron.co/why-your-map-of-united-states-indian-reservations-is-probably-wrong-2dx">Why Your Map of United States Indian Reservations is... - Filtron</a></li>

</ul>
</details>

**Tags**: `#data-centers`, `#infrastructure`, `#policy`, `#environmental-impact`, `#AI-infrastructure`

---

<a id="item-18"></a>
## [AI Data Center Optical Interconnect Market to Reach $144 Billion by 2030](https://www.tomshardware.com/tech-industry/photonics/ai-data-center-optical-interconnect-market-to-hit-usd144-billion-by-2030-an-over-ten-fold-increase-from-2024-figures-according-to-new-projections-silicon-photonics-expected-to-account-for-nearly-two-thirds-of-revenue-driven-by-co-packaged-optics) ⭐️ 6.5/10

CIC forecasts that the data center optical interconnect market will grow from $13.7 billion in 2024 to $144.4 billion by 2030, a more than tenfold increase. Silicon photonics is projected to capture 63.7% of that revenue, driven largely by the adoption of co-packaged optics (CPO). This massive projected growth underscores how AI workloads are reshaping data center infrastructure, with interconnect bandwidth and energy efficiency becoming critical bottlenecks. The projected dominance of silicon photonics and CPO signals a fundamental shift in how chips and switches are physically integrated, affecting hyperscalers, semiconductor companies, and the broader supply chain. The forecast attributes silicon photonics' dominance to co-packaged optics, which integrates optical engines directly with switch ASICs via ultra-short electrical connections, reducing power consumption and latency versus traditional pluggable optics. However, CPO remains a rapidly growing but still relatively small segment this decade, with pluggable modules still widely deployed in existing AI data center designs.

rss · Tom's Hardware · Aug 17, 11:20

**Background**: Silicon photonics is a technology that integrates photonic (light-based) components onto silicon chips, enabling faster, more efficient data transmission with lower power consumption than traditional electrical signaling. Co-packaged optics (CPO) is an architecture where optical engines are placed directly on the same package as the switch ASIC, using ultra-short electrical traces instead of the longer connections used by pluggable transceiver modules. As AI GPU and CPU processing speeds surge, the existing I/O infrastructure struggles to keep pace, causing processing units to frequently wait for data — a bottleneck that optical and co-packaged solutions are designed to address.

<details><summary>References</summary>
<ul>
<li><a href="https://www.link-pp.com/resources/strategy/cpo-vs-pluggable-800g-architecture/">Co - Packaged Optics (CPO) vs Pluggable : 800G+ Scaling Limits</a></li>
<li><a href="https://www.avnet.com/integrated/resources/article/pluggable-vs-co-packaged-optics-in-ai-data-centers-power-scale-and-design-trade-offs/">Pluggable vs . co - packaged optics in AI data centers : Power, scale...</a></li>
<li><a href="https://www.ansys.com/blog/what-is-co-packaged-optics">What is Co - packaged Optics ?</a></li>

</ul>
</details>

**Tags**: `#ai-infrastructure`, `#data-centers`, `#silicon-photonics`, `#market-forecast`, `#co-packaged-optics`

---

<a id="item-19"></a>
## [PC Partner Warns of H2 2026 GPU Price Hikes and Budget Card Shortages](https://www.tomshardware.com/tech-industry/pc-partner-warns-of-rising-gpu-prices-and-budget-card-shortages-analyst-suggests-makers-are-hiking-prices-beyond-memory-costs) ⭐️ 6.5/10

PC Partner Group, the company behind ZOTAC, Inno3D, and Manli, has warned that GPU prices will rise further in the second half of 2026 due to climbing memory costs and tightening supplies, with entry-level cards expected to face the most severe shortages. Analyst Jon Peddie suggested that manufacturers are raising prices beyond what memory cost increases alone would justify. This news directly affects PC builders and gamers, particularly those relying on affordable entry-level graphics cards, as rising prices and shortages could make budget builds significantly more expensive. It also signals broader component cost pressures across the PC hardware ecosystem, extending to monitors from brands like KTC and AOC. PC Partner's graphics card unit sales dropped 18.4% in H1 2026 due to component shortages, while revenue fell 9.2% year-over-year to HK$4.46 billion — yet average selling prices still rose 10.7%, indicating price hikes were implemented despite lower volumes. KTC and AOC have also notified distributors of upcoming monitor price increases, citing higher panel, power component, and manufacturing costs.

rss · Tom's Hardware · Aug 17, 11:00

**Background**: PC Partner Group is a Hong Kong-based manufacturer that designs and produces graphics cards sold under its own brands — ZOTAC, Inno3D, and Manli — as well as on an OEM basis for other companies. Jon Peddie is a well-known industry analyst and president of Jon Peddie Research (JPR), a firm that has tracked the GPU market for over 35 years. The current supply tightness stems from constraints in graphics memory (such as GDDR6/GDDR7) production, which is shared with the broader DRAM industry facing high demand from AI and data center applications.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/entry-level-gpus-were-gamers-last-hope-but-pc-partner-says-severe-shortages-arrive-in-second-half-of-2026/">Entry-level GPUs Were Gamers' Last Hope, But PC Partner Says...</a></li>
<li><a href="https://www.jonpeddie.com/">Jon Peddie Research – The latest statistics, trends, and reports on...</a></li>
<li><a href="https://www.eetimes.com/whats-the-story-with-gpus/">Addressing the Global GPU Supply Landscape - EE Times</a></li>

</ul>
</details>

**Tags**: `#GPU`, `#hardware`, `#pricing`, `#PC-building`, `#industry-analysis`

---

<a id="item-20"></a>
## [Japanese Shop Offers $25/GB GPU VRAM Upgrades for Budget AI](https://www.tomshardware.com/pc-components/gpus/japanese-repair-shop-sells-gddr6-vram-upgrades-for-usd25-per-gb-during-memory-crisis-rtx-2080-ti-modded-to-22gb-for-just-usd282-double-the-vram-creates-a-budget-ai-powerhouse) ⭐️ 6.5/10

A Japanese repair shop is now commercially offering GDDR6 VRAM upgrades for GPUs at $25 per gigabyte, with an RTX 2080 Ti upgraded from 11GB to 22GB costing just $282 total. This service turns an older consumer GPU into a budget-friendly AI workstation during the ongoing memory pricing crisis. This matters because the global memory price crisis has made new GPUs and AI hardware extremely expensive, and this aftermarket service offers a way to repurpose existing hardware for AI workloads at a fraction of the cost. Budget AI researchers, hobbyists, and small studios who cannot afford current-generation GPUs with large VRAM (such as RTX 3090s or datacenter cards) now have a practical path to running larger models locally. The upgrade requires advanced BGA soldering skills, proper rework equipment, and knowledge of GPU BIOS and strap configurations — it is not a beginner-friendly modification and carries risk of permanently damaging the card. The pricing of $25 per GB is set against the backdrop of skyrocketing GDDR6 prices driven by the AI-driven memory supply crunch.

rss · Tom's Hardware · Aug 17, 10:30

**Background**: VRAM (Video RAM) is the dedicated memory on a graphics card used to store textures, frame buffers, and increasingly, AI model weights and activations. Unlike desktop system RAM, which can be easily swapped, VRAM is soldered directly onto the GPU PCB using BGA (Ball Grid Array) chips, making upgrades far more difficult. The RTX 2080 Ti originally launched with 11GB of GDDR6 on a 352-bit bus; doubling it to 22GB requires replacing all memory chips and modifying the GPU's BIOS/strap settings to recognize the new capacity. Larger VRAM is crucial for AI inference and training because large language models and diffusion models often exceed the 8-12GB available on typical consumer cards.

<details><summary>References</summary>
<ul>
<li><a href="https://maketecheasier.com/what-vram-is-and-increase-vram/">What Is VRAM , How to Check It, and Can You... - Make Tech Easier</a></li>
<li><a href="https://www.youtube.com/watch?v=nJ97nUr1G-g">Can Any GPU Get a VRAM Upgrade ? | RTX 2080 Ti 11GB... - YouTube</a></li>
<li><a href="https://voltground.com/hardware/gddr6x-memory-temperature-guide/">GDDR 6 X Memory Temperature: Why 110 Degrees Is... — VoltGround</a></li>

</ul>
</details>

**Tags**: `#GPU`, `#VRAM-upgrade`, `#hardware-mod`, `#AI-hardware`, `#budget-AI`

---