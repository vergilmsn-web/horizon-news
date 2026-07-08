---
layout: default
title: "Horizon Summary: 2026-07-08 (EN)"
date: 2026-07-08
lang: en
---

> From 95 items, 20 important content pieces were selected

---

1. [GitLost: Prompt Injection Leaks Private Repos via GitHub AI Agent](#item-1) ⭐️ 8.0/10
2. [Samsung Begins Mass Production of PM1763 PCIe Gen 6 Enterprise SSD](#item-2) ⭐️ 7.5/10
3. [JEDEC Releases SPHBM4 Standard to Cut AI Memory Costs](#item-3) ⭐️ 7.5/10
4. [Nvidia touts Vera CPU's single-threaded performance as its agentic AI advantage, reveals next-gen 'Rigel' Arm CPU cores — frames chip as a 'max single-threaded CPU at scale,' not a parallel monster](#item-4) ⭐️ 7.5/10
5. [South Korea's $880B Chip and AI Plan Faces Power and Water Challenges](#item-5) ⭐️ 7.5/10
6. [Tenda firmware (multiple versions) contains hidden authentication backdoor](#item-6) ⭐️ 7.0/10
7. [Structure and Interpretation of Computer Programs Video Lectures (1986)](#item-7) ⭐️ 7.0/10
8. [Packaging PDK: The Missing Layer for Co-Packaged Optics](#item-8) ⭐️ 7.0/10
9. [SambaNova Raises $1B, Lands JPMorganChase as Customer](#item-9) ⭐️ 7.0/10
10. [Apple Commits Over $30B to Broadcom for U.S.-Made Chips](#item-10) ⭐️ 6.5/10
11. [Xbox Layoffs Decimate Id Software and Obsidian](#item-11) ⭐️ 6.5/10
12. [SiPearl's Rhea1 CPU Reaches Lab, Europe's First Sovereign HPC Processor](#item-12) ⭐️ 6.5/10
13. [Oregon approves 29.7% rate hike for data centers, cuts residential costs 1.3%](#item-13) ⭐️ 6.5/10
14. [Windows GDID telemetry used to arrest Scattered Spider hacker](#item-14) ⭐️ 6.5/10
15. [Longsys forecasts ~60,000% profit surge on AI memory demand](#item-15) ⭐️ 6.5/10
16. [Snapmaker Raises ¥1B, Largest Consumer 3D Printing Funding Round](#item-16) ⭐️ 6.3/10
17. [「德睿智药」获5200万美元B轮融资，AI设计的减肥药已进入3期临床｜36氪首发](#item-17) ⭐️ 6.3/10
18. [Cloudflare and OpenAI Launch Pilot to Improve AI Search Indexing](#item-18) ⭐️ 6.3/10
19. [Blue Origin Raises $10 Billion at $130 Billion Valuation](#item-19) ⭐️ 6.3/10
20. [Decoding the obfuscated bash script on a Uniqlo t-shirt](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [GitLost: Prompt Injection Leaks Private Repos via GitHub AI Agent](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/) ⭐️ 8.0/10

Security researchers at Noma Security disclosed the 'GitLost' vulnerability, which exploits GitHub's AI-powered Agentic Workflows via prompt injection. By embedding a malicious instruction as simple as the word 'Additionally' in a public GitHub Issue, attackers can trick the AI agent into fetching and publicly posting the contents of private repositories—no credentials or system access required. This vulnerability highlights a fundamental security challenge in agentic AI systems: once an LLM has access to private data, there is no reliable way to prevent it from leaking that data when processing untrusted input. It affects any organization using GitHub Agentic Workflows where the AI agent has cross-repository access, and underscores the broader industry-wide struggle to build effective guardrails for LLM-based automation. The attack works by a public repository's issue containing injected instructions that cause the agent to fetch README.md from both a public and a private repo, then post the private content as a public comment. The bypass is alarmingly simple—'Additionally' was enough to override the agent's safety guardrails—demonstrating that mixing system rules with untrusted user input in the same context window is inherently insecure.

hackernews · ColinEberhardt · Jul 8, 05:25 · [Discussion](https://news.ycombinator.com/item?id=48827858)

**Background**: GitHub Agentic Workflows is an AI-powered automation feature that allows AI agents to perform tasks triggered by repository events, such as responding to issues. These agents can have read access to multiple repositories within an organization. Prompt injection is a class of attack where adversarial instructions are embedded in content that an LLM processes, causing it to behave in unintended ways—such as ignoring its original instructions and following the attacker's commands instead. OWASP has ranked prompt injection as the top security risk (LLM01:2025) for LLM applications, and it remains an unsolved problem because LLMs cannot reliably distinguish between trusted system instructions and untrusted data within their context window.

<details><summary>References</summary>
<ul>
<li><a href="https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/">GitLost: How We Tricked GitHub’s AI Agent into Leaking ...</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>
<li><a href="https://www.darkreading.com/cyber-risk/gitlost-leaks-private-data-github-agentic-workflows">'GitLost' Flaw Leaks Private Data From GitHub's Agentic Workflows</a></li>

</ul>
</details>

**Discussion**: The community drew strong parallels between prompt injection and SQL injection, calling it a 'category-wide vulnerability class' requiring systematic defenses. A notable debate emerged over responsibility: some argued this is a user misconfiguration issue (analogous to exposing secrets in a public CI job) rather than a GitHub vulnerability, while others emphasized that building hard security boundaries inside an LLM context window is fundamentally impossible, as the model is designed to follow whichever instruction is most recent or persistent. There was also broader criticism of corporations hastily bolting AI onto products without adequate security considerations.

**Tags**: `#security`, `#prompt-injection`, `#github`, `#ai-agents`, `#llm-vulnerabilities`

---

<a id="item-2"></a>
## [Samsung Begins Mass Production of PM1763 PCIe Gen 6 Enterprise SSD](https://www.techpowerup.com/350600/samsung-begins-mass-production-of-pm1763-pcie-gen-6-ssd) ⭐️ 7.5/10

Samsung Electronics has announced the start of mass production for the PM1763, a PCIe 6.0-based enterprise SSD (eSSD) designed for next-generation AI and high-performance computing (HPC) server environments. The drive features high-speed data transfer capabilities and an optimized controller architecture, and has already completed validation for next-generation AI platforms. As one of the first PCIe Gen 6.0 enterprise SSDs to enter mass production, the PM1763 represents a significant milestone for storage infrastructure supporting AI training and inference workloads, where data throughput is becoming a critical bottleneck. This positions Samsung at the forefront of the storage industry's transition to PCIe 6.0, a standard designed to handle the enormous data movement demands of large AI models and distributed training clusters. The PM1763 leverages the PCIe 6.0 standard, which uses PAM4 signaling and FLIT encoding to deliver 64 GT/s per lane — double the per-lane bandwidth of PCIe 5.0. Samsung has not yet publicly disclosed specific capacity figures, form-factor details, or sequential read/write speeds, though the drive is positioned as an NVMe enterprise SSD with a controller architecture tuned for AI workloads.

rss · TechPowerUp News · Jul 8, 08:09

**Background**: PCIe (Peripheral Component Interconnect Express) is a high-speed serial computer expansion bus standard maintained by the PCI-SIG consortium, used to connect components such as SSDs, GPUs, and NICs to a system's CPU. Each new generation roughly doubles the per-lane bandwidth, and PCIe 6.0 is the latest major iteration, specifically engineered to support compute-intensive applications like AI training and inference. High-performance computing (HPC) refers to the aggregation of cutting-edge computing power to tackle problems beyond the reach of standard commercial systems, and increasingly encompasses large-scale AI model training. Enterprise SSDs (eSSDs) are storage devices designed for data center and server deployments, emphasizing high endurance, reliability, and sustained throughput rather than the cost optimizations typical of consumer drives.

<details><summary>References</summary>
<ul>
<li><a href="https://www.viavisolutions.com/en-us/resources/learning-center/what-pcie-60">The PCIe 6.0 Guide. Speed, Features and More</a></li>
<li><a href="https://www.ibm.com/think/topics/hpc">What Is High-Performance Computing (HPC)? | IBM</a></li>
<li><a href="https://www.onlogic.com/blog/your-ultimate-guide-to-understanding-pcie-6-0/">Your Ultimate Guide to Understanding PCIe 6.0 | OnLogic</a></li>

</ul>
</details>

**Tags**: `#PCIe Gen 6`, `#Samsung`, `#enterprise SSD`, `#AI infrastructure`, `#storage hardware`

---

<a id="item-3"></a>
## [JEDEC Releases SPHBM4 Standard to Cut AI Memory Costs](https://www.tomshardware.com/pc-components/dram/jedec-releases-new-sphbm4-standard-to-slash-ai-memory-costs-narrow-512-bit-interface-enables-dropping-expensive-interposers-for-organic-substrates) ⭐️ 7.5/10

JEDEC announced the SPHBM4 (Standard Package High Bandwidth Memory 4) standard on December 11, 2025, which delivers HBM4-class throughput using a narrow 512-bit interface mounted on standard organic substrates, eliminating the need for expensive silicon interposers and CoWoS-like 2.5D packaging. This standard directly addresses the AI memory bottleneck by potentially reducing HBM packaging costs and easing reliance on TSMC's CoWoS capacity, which has been a major supply constraint for AI accelerators like NVIDIA GPUs. Cheaper and more accessible HBM4-class memory could lower the total cost of AI infrastructure and broaden the market beyond premium accelerators. SPHBM4 uses the same DRAM dies as conventional HBM4 but pairs them with a redesigned interface base die that enables a 512-bit wide connection, allowing standard organic substrates to be used instead of silicon interposers. The spec is still under development according to JEDEC, meaning real-world products and adoption timelines remain to be seen.

rss · Tom's Hardware · Jul 8, 15:03

**Background**: HBM (High Bandwidth Memory) is stacked DRAM used alongside AI accelerators and GPUs to feed them data at extremely high rates. Current HBM4 implementations rely on silicon interposers—thin silicon layers containing through-silicon vias (TSVs) that route thousands of signals between the GPU die and HBM stacks. TSMC's CoWoS (Chip-on-Wafer-on-Substrate) is the dominant 2.5D packaging technology for this purpose, but its limited capacity and high cost have created a well-known bottleneck in AI chip supply. Organic substrates, made from materials like ABF (Ajinomoto Build-up Film), are far cheaper and more widely available but traditionally cannot support the dense, high-speed connections that HBM requires.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jedec.org/news/pressreleases/jedec®-prepares-sphbm4-standard-deliver-hbm4-level-throughput-reduced-pin-count">JEDEC® Prepares SPHBM4 Standard to Deliver HBM4-Level Throughput with Reduced Pin Count | JEDEC</a></li>
<li><a href="https://wccftech.com/jedec-approves-sphbm4-to-break-hbm-costs-retain-hbm4-speeds-standard-packages/">JEDEC Approves SPHBM4 to Break HBM's Costly Packaging Bottleneck, Retaining HBM4-level Speeds With Standard Packages</a></li>
<li><a href="https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm">CoWoS® - Taiwan Semiconductor Manufacturing Company Limited</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#memory standards`, `#HBM4`, `#JEDEC`, `#semiconductor manufacturing`

---

<a id="item-4"></a>
## [Nvidia touts Vera CPU's single-threaded performance as its agentic AI advantage, reveals next-gen 'Rigel' Arm CPU cores — frames chip as a 'max single-threaded CPU at scale,' not a parallel monster](https://www.tomshardware.com/pc-components/cpus/nvidia-touts-vera-cpus-single-threaded-performance-as-its-agentic-ai-advantage-frames-chip-as-a-max-single-threaded-cpu-at-scale-not-a-parallel-monster) ⭐️ 7.5/10

Nvidia reveals details of its Vera CPU featuring next-gen 'Rigel' Arm cores, claiming 1.8x single-threaded performance advantage over x86 competitors in agentic AI workloads.

rss · Tom's Hardware · Jul 8, 11:00

**Tags**: `#Nvidia`, `#Vera CPU`, `#Arm architecture`, `#agentic AI`, `#data center hardware`

---

<a id="item-5"></a>
## [South Korea's $880B Chip and AI Plan Faces Power and Water Challenges](https://www.tomshardware.com/tech-industry/power-and-water-lag-the-fabs-in-south-koreas-880-billion-chip-and-ai-plan) ⭐️ 7.5/10

South Korea's ₩1,350 trillion (approximately $880 billion) plan, which combines a $520 billion semiconductor program with AI data center and robotics investments, faces major power and water constraints, with a single AI megacluster estimated to require up to a quarter of Seoul's total power demand. This highlights that capital investment alone is insufficient for AI infrastructure dominance — physical constraints like power grids and water supply could become the true bottlenecks in the global semiconductor and AI race, potentially slowing South Korea's competitiveness against the US, China, and Taiwan. The ₩1,350 trillion total is largely composed of corporate capital expenditure rather than direct government spending, and AI megaclusters require far more electricity, cooling, and water than traditional data centers due to liquid cooling systems and energy-intensive model training.

rss · Tom's Hardware · Jul 7, 17:27

**Background**: AI megaclusters are specialized large-scale data center facilities designed for training and running AI models, requiring massive amounts of electricity, cooling, networking, and physical space. A single data center's water footprint includes on-site usage, power plant water consumption, and indirect sources. The IEA projects global data center electricity consumption to roughly double to about 945 TWh by 2030, representing nearly 3% of total global electricity use.

<details><summary>References</summary>
<ul>
<li><a href="https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai">Energy demand from AI – Energy and AI – Analysis - IEA</a></li>
<li><a href="https://www.eesi.org/articles/view/data-centers-and-water-consumption">Data Centers and Water Consumption | Article | EESI</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_data_center">AI data center - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#AI infrastructure`, `#South Korea`, `#power-grid`, `#industry-policy`

---

<a id="item-6"></a>
## [Tenda firmware (multiple versions) contains hidden authentication backdoor](https://kb.cert.org/vuls/id/213560) ⭐️ 7.0/10

CERT.org disclosure reveals a hardcoded authentication backdoor in multiple versions of Tenda router firmware, allowing access with any username and a hidden password.

hackernews · miniBill · Jul 8, 00:08 · [Discussion](https://news.ycombinator.com/item?id=48825749)

**Tags**: `#security`, `#vulnerability`, `#iot`, `#networking`, `#backdoor`

---

<a id="item-7"></a>
## [Structure and Interpretation of Computer Programs Video Lectures (1986)](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/) ⭐️ 7.0/10

MIT's classic 1986 SICP video lectures by Sussman and Abelson, a foundational computer science course covering fundamental programming concepts through Scheme/Lisp.

hackernews · gjvc · Jul 7, 23:57 · [Discussion](https://news.ycombinator.com/item?id=48825664)

**Tags**: `#SICP`, `#computer-science`, `#lisp`, `#education`, `#classic-lectures`

---

<a id="item-8"></a>
## [Packaging PDK: The Missing Layer for Co-Packaged Optics](https://semiwiki.com/3dic/370709-the-packaging-pdk-is-the-missing-layer-for-co-packaged-optics/) ⭐️ 7.0/10

A SemiWiki opinion piece argues that the co-packaged optics industry cannot scale on photonic device performance alone and urgently needs a standardized Packaging Process Design Kit (PDK) to bridge the gap between photonic device design and electro-optical realization at scale. As AI infrastructure pushes bandwidth, power, latency, and reach to new limits, optics must move closer to the compute engine. Without a shared Packaging PDK, design-to-manufacturing workflows for CPO will remain fragmented across foundries, OSATs, and photonic toolchains, slowing the deployment that hyperscalers need. A traditional fab PDK models a foundry's fabrication process so designers can verify manufacturability; by analogy, a Packaging PDK would model the assembly, interconnect, and electro-optical integration rules for advanced packages. The article frames CPO as a packaging-driven technology, not just a photonic-device problem, implying that 3DIC and advanced packaging tooling—not just silicon photonics—will determine commercial viability.

rss · SemiWiki · Jul 7, 17:00

**Background**: Co-Packaged Optics (CPO) integrates optical transceivers directly into the same package as a switch ASIC or compute chip, replacing pluggable modules to drastically cut power and boost bandwidth for AI data centers. A Process Design Kit (PDK) is the standard set of files and models a foundry provides so chip designers can ensure their layouts are manufacturable on a specific process node. Packaging PDKs and Package Assembly Design Kits extend this concept to the package level, covering die-to-die interconnects, bump patterns, and assembly rules—particularly relevant for 3DIC and 2.5D/3D heterogeneous integration. The article's argument is that the CPO ecosystem has well-developed photonic component PDKs but lacks an equivalent standardized kit that describes the electrical, thermal, and mechanical rules of the co-package itself.

<details><summary>References</summary>
<ul>
<li><a href="https://www.corning.com/oem-solutions/worldwide/en/home/products-solutions/optical-communication-components/co-packaged-optics.html">What is Co-Packaged Optics (CPO) Technology? | Corning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Process_Design_Kit">Process design kit - Wikipedia</a></li>
<li><a href="https://www.semiconductorpackagingnews.com/uploads/2/2025_SPN_White_Paper_-_Package_Assembly_Design_Kits-The_Future_of_Advanced_Package_Design.pdf">Package Assembly Design Kits: The Future of Advanced Package ...</a></li>

</ul>
</details>

**Discussion**: No community comments were provided in the source material.

**Tags**: `#co-packaged optics`, `#advanced packaging`, `#3DIC`, `#semiconductor`, `#AI infrastructure`

---

<a id="item-9"></a>
## [SambaNova Raises $1B, Lands JPMorganChase as Customer](https://www.eetimes.com/sambanova-raises-1-billion-signs-jpmorganchase-as-a-customer/) ⭐️ 7.0/10

AI chip startup SambaNova has raised $1 billion in a Series F first close led by General Atlantic, reaching an $11 billion valuation, and has signed JPMorganChase as a major enterprise customer. The funding and enterprise customer win signal that major financial institutions are beginning to adopt AI silicon alternatives to NVIDIA, validating SambaNova's position in the competitive AI hardware market and indicating that the enterprise AI chip market is maturing. The round was led by General Atlantic with additional investors expected to join; SambaNova's technology is based on its proprietary Reconfigurable Dataflow Unit (RDU) architecture, with its latest fifth-generation SN50 RDU designed specifically for large-scale agentic AI inference workloads.

rss · EE Times · Jul 8, 07:45

**Background**: SambaNova Systems is an AI hardware company that competes with NVIDIA by offering specialized chips for AI inference and training. Its core technology is the Reconfigurable Dataflow Unit (RDU), which uses a tiled array of reconfigurable processing and memory units connected through a high-speed on-chip switching fabric, differing fundamentally from NVIDIA's GPU-based approach. The company has progressed through multiple chip generations, with the SN40L and now SN50 RDU targeting large-scale, agentic AI workloads. This funding round positions SambaNova among the most well-capitalized AI chip startups challenging NVIDIA's dominance in the data center AI accelerator market.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/08/sambanova-draws-1b-at-11b-valuation-in-series-f-first-close/">AI chip maker SambaNova raises $1B at $11B valuation, 5 ...</a></li>
<li><a href="https://sambanova.ai/products/rdu-ai-chips">RDU | Next-Gen AI Chip for Inference at Scale</a></li>
<li><a href="https://www.cnbc.com/2026/07/08/sambanova-ai-chip-funding-valuation.html">SambaNova valued at $11 billion after AI chip funding - CNBC</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#funding`, `#SambaNova`, `#enterprise AI`, `#JPMorganChase`

---

<a id="item-10"></a>
## [Apple Commits Over $30B to Broadcom for U.S.-Made Chips](https://www.techpowerup.com/350606/apple-to-increase-spend-with-broadcom-to-produce-billions-more-u-s-chips) ⭐️ 6.5/10

Apple announced a new multiyear commitment with Broadcom exceeding $30 billion to design and produce custom silicon components and wireless connectivity technologies, which will result in the production of more than 15 billion U.S.-made chips and support hundreds of American jobs. This is Apple's largest commitment to date under its American Manufacturing Program (AMP) and represents a major step in onshoring semiconductor supply chains to the U.S., aligning with broader geopolitical efforts to reduce dependence on overseas chip manufacturing. Broadcom will invest $1.5 billion in capital expenditure to expand and modernize its Fort Collins, Colorado manufacturing facility, where it will produce advanced radio frequency components such as FBAR (Film Bulk Acoustic Resonator) filters and wireless connectivity technologies for Apple products.

rss · TechPowerUp News · Jul 8, 10:32

**Background**: Apple's American Manufacturing Program (AMP) was launched in 2025 as part of a broader $600 billion four-year pledge to U.S. manufacturing, with initial partners including Corning, Coherent, Texas Instruments, Samsung, and GlobalFoundries. Broadcom is a key AMP partner specializing in RF components. FBAR filters are a type of bulk acoustic wave (BAW) filter that offer superior performance compared to traditional surface acoustic wave (SAW) filters, with steeper rejection curves, lower insertion loss (0.3 to 0.5 dB less), and up to 50mA lower current consumption—making them critical for mobile device RF front-end modules.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2025/08/apple-increases-us-commitment-to-600-billion-usd-announces-ambitious-program/">Apple increases U.S. commitment to $600 billion, announces ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Thin-film_bulk_acoustic_resonator">Thin-film bulk acoustic resonator - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/03/26/apple-american-manufacturing-program-trump.html">Apple expands American manufacturing program with four new ...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#Apple`, `#Broadcom`, `#manufacturing`, `#supply-chain`

---

<a id="item-11"></a>
## [Xbox Layoffs Decimate Id Software and Obsidian](https://www.techpowerup.com/350587/xbox-layoffs-decimate-id-software-and-obsidian) ⭐️ 6.5/10

Microsoft's Xbox layoffs significantly impact id Software (~50% workforce) and Obsidian Entertainment (~25%, 60-70 workers), raising concerns about workload redistribution across their active projects.

rss · TechPowerUp News · Jul 7, 19:42

**Tags**: `#gaming-industry`, `#layoffs`, `#microsoft`, `#xbox`, `#id-software`, `#obsidian`

---

<a id="item-12"></a>
## [SiPearl's Rhea1 CPU Reaches Lab, Europe's First Sovereign HPC Processor](https://www.tomshardware.com/pc-components/cpus/sipearls-long-awaited-rhea-cpu-finally-gets-in-the-lab-opening-the-door-for-europes-first-sovereign-hpc-cpu-availability-of-rhea1-is-scheduled-for-end-of-2026-sipearl-vp-says-following-long-development-process) ⭐️ 6.5/10

SiPearl's long-awaited Rhea1 CPU, the first sovereign high-performance processor developed under the European Processor Initiative (EPI), has reached the lab stage, with availability scheduled for the end of 2026 according to a SiPearl VP. Rhea1 represents a major milestone in Europe's push for technological sovereignty in HPC, reducing the continent's dependence on US and Asian chip vendors like Intel, AMD, and Nvidia for supercomputing infrastructure. Rhea1 is designed to deliver energy-efficient computing power for HPC and AI workloads, and future iterations will increase core counts, memory bandwidth, and add custom acceleration and IP blocks targeting European exascale supercomputers.

rss · Tom's Hardware · Jul 8, 14:44

**Background**: The European Processor Initiative (EPI) is a consortium-backed effort to build a homegrown CPU architecture for European supercomputers, funded under the EuroHPC Joint Undertaking—a public-private partnership pooling EU, member-state, and private resources. SiPearl was spun out to commercialize the resulting designs, with Rhea1 being its first product. The project's strategic importance lies in Europe's desire to control its own compute supply chain rather than relying on foreign processors for sensitive scientific, defense, and research workloads. EuroHPC has also been exploring RISC-V open architectures as a parallel path toward sovereignty, which could shape future European CPU designs.

<details><summary>References</summary>
<ul>
<li><a href="https://sipearl.com/rhea1">Rhea1 first-generation CPU for HPC and AI - SiPearl</a></li>
<li><a href="https://www.techpowerup.com/338824/european-hpc-processor-rhea1-tapes-out-launch-delayed-to-2026">European HPC Processor "Rhea1" Tapes Out, Launch Delayed to ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_High-Performance_Computing_Joint_Undertaking">European High-Performance Computing Joint Undertaking</a></li>

</ul>
</details>

**Tags**: `#HPC`, `#European tech sovereignty`, `#SiPearl`, `#CPU architecture`, `#semiconductors`

---

<a id="item-13"></a>
## [Oregon approves 29.7% rate hike for data centers, cuts residential costs 1.3%](https://www.tomshardware.com/tech-industry/data-centers/power-company-hikes-data-center-bills-by-30-percent-cuts-residential-electricity-costs-by-1-3-percent-oregon-approves-change-through-power-act-pushes-developments-using-more-than-20-megawatts-of-power-to-pay-their-fair-share) ⭐️ 6.5/10

Oregon's Public Utility Commission unanimously approved Portland General Electric's (PGE) 29.7% rate hike for large electricity users consuming 20MW or more, targeting data centers under the state's POWER Act. The new rates took effect the Wednesday following the July 7, 2026 approval, while residential electricity rates will simultaneously decrease by 1.3%. This represents a significant policy shift that acknowledges data centers' outsized energy consumption and pushes them to bear a fairer share of grid infrastructure costs rather than being cross-subsidized by residential ratepayers. As AI infrastructure power demands continue to surge, this precedent could influence data center siting decisions and shape energy policy in other U.S. states grappling with similar tensions. The POWER Act, passed in 2025, requires data centers to enter 10-year contracts to offset their heavy grid usage. PGE is Oregon's largest electricity provider, serving almost two-thirds of the state's commercial and industrial activity, with its territory including Hillsboro where major operators like QTS have large facilities.

rss · Tom's Hardware · Jul 8, 13:56

**Background**: The POWER Act is an Oregon state law that establishes separate electricity rate classes for data centers and requires them to enter 10-year contracts to offset their grid impact. Portland General Electric (PGE) is a Fortune 1000 publicly traded energy company headquartered in Portland, Oregon. The 20MW threshold directly targets large-scale operations—for context, a typical hyperscale data center can consume anywhere from 50 to over 500 MW, making this threshold a direct hit on AI compute infrastructure and cloud providers operating in the region.

<details><summary>References</summary>
<ul>
<li><a href="https://www.opb.org/article/2026/07/07/oregon-data-center-general-electric-rate-hikes/">Oregon approves PGE’s 29.7% rate hike for data centers under ...</a></li>
<li><a href="https://www.centraloregondaily.com/news/regional/oregon-hikes-data-center-electric-rates-29-in-pge-territory/article_1e7127d2-4c17-5159-9cb4-02639129ca95.html">Oregon hikes data center electric rates 29% in PGE territory</a></li>
<li><a href="https://en.wikipedia.org/wiki/Portland_General_Electric">Portland General Electric - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#data-centers`, `#energy-policy`, `#infrastructure`, `#AI-economics`, `#power-consumption`

---

<a id="item-14"></a>
## [Windows GDID telemetry used to arrest Scattered Spider hacker](https://www.tomshardware.com/tech-industry/cyber-security/arrest-and-extradition-of-scattered-spider-hacker-shines-light-on-how-windows-telemetry-gdids-can-identify-users-microsoft-device-identifier-is-just-one-digital-fingerprint-in-a-software-world-rife-with-them) ⭐️ 6.5/10

Scattered Spider hacking group member Peter Stokes was arrested and extradited after investigators correlated Microsoft's Windows telemetry GDID (Global Device Identifier) with IP data, proxy usage, and service access records to identify him online. Despite Stokes cycling through IP addresses, VPNs, and remote desktop connections to mask his activity, the persistent GDID tied to his Windows installation remained constant and helped link him to the attacks. This case demonstrates that even persistent operational security measures like VPNs and rotating IPs can be undermined by seemingly innocuous telemetry built into mainstream operating systems. It raises important privacy questions about the extent of device fingerprinting inherent in modern software and how such identifiers can be leveraged by both law enforcement and potentially malicious actors. The GDID is a unique code embedded in every Windows installation, used by Microsoft for diagnostic telemetry, crash reporting, feature-usage analysis, and license verification; only reinstalling Windows assigns a new GDID. Device fingerprinting broadly collects dozens of signals—from screen resolution to timezone—to create persistent identifiers that survive cookie clearing, making GDIDs just one of many fingerprinting techniques in widespread use.

rss · Tom's Hardware · Jul 8, 10:30

**Background**: Scattered Spider (also known as UNC3944 and recently identified as ShinyHunters) is a cybercriminal group largely composed of teenagers and young adults based in the US and UK, known for targeting large companies and their IT help desks. The group's tactics often involve social engineering to gain initial access, after which they deploy ransomware and steal data. Device fingerprinting, meanwhile, is a technique that assembles dozens of subtle hardware and software clues—from screen resolution and timezone to installed fonts and browser configuration—to create a unique identifier for tracking users across the internet.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scattered_Spider">Scattered Spider - Wikipedia</a></li>
<li><a href="https://cybernews.com/security/windows-telemetry-gdid-helps-arrest-hacker/">Windows telemetry backlash: GDID tracking exposes Scattered ...</a></li>
<li><a href="https://cybersecuritynews.com/windows-device-identifier-tracking/">Windows Device Identifier Feature Leads to Arrest of ...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#privacy`, `#windows-telemetry`, `#digital-fingerprinting`, `#cybercrime`

---

<a id="item-15"></a>
## [Longsys forecasts ~60,000% profit surge on AI memory demand](https://www.tomshardware.com/tech-industry/chinese-memory-and-storage-firm-expected-to-post-more-than-60-000-percent-jump-in-profits-due-to-exploding-demand-lexar-owner-longsys-forecasts-nearly-usd1-5-billion-profit-for-1h26-compared-to-usd2-1-million-last-year) ⭐️ 6.5/10

Chinese memory and storage manufacturer Longsys forecasts a profit of nearly $1.5 billion for the first half of 2026, a jump of more than 60,000% compared to just $2.1 million in the same period last year, driven by exploding AI-related demand for memory and storage chips. The dramatic profit forecast highlights how the global AI-driven memory and storage chip shortage is reshaping the fortunes of memory manufacturers, particularly Chinese firms that have historically played a smaller role. It signals significant supply-demand tension in NAND flash and DRAM markets that affects pricing across consumer electronics, data centers, and AI infrastructure. Longsys is a global provider of NAND flash and DRAM solutions and has owned the Lexar brand since acquiring it from Micron Technology in 2017. The company supplies memory cards, SSDs, and embedded storage products to both consumer and enterprise markets worldwide.

rss · Tom's Hardware · Jul 7, 16:13

**Background**: Longsys (深圳市江波龙电子股份有限公司) is a Shenzhen-based memory and storage company that specializes in NAND flash and DRAM products. In 2017, it acquired the Lexar brand from U.S. semiconductor giant Micron Technology, gaining a well-known consumer storage brand and global distribution channels. The broader context is the ongoing AI-driven memory shortage: as AI training and inference workloads require massive amounts of high-bandwidth memory (HBM) and high-capacity storage, demand has surged while supply remains constrained, driving up prices and profitability across the memory industry.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/chinese-memory-and-storage-firm-expected-to-post-more-than-60-000-percent-jump-in-profits-due-to-exploding-demand-lexar-owner-longsys-forecasts-nearly-usd1-5-billion-profit-for-1h26-compared-to-usd2-1-million-last-year">Chinese memory and storage firm expected to post more than ...</a></li>
<li><a href="https://www.longsys.com/about-longsys/news/longsys-acquired-the-lexar-brand-from-micron.html">Longsys acquired the Lexar brand from Micron and that Lexar ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lexar">Lexar - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#memory-storage`, `#AI-demand`, `#semiconductor-industry`, `#Longsys`, `#market-forecast`

---

<a id="item-16"></a>
## [Snapmaker Raises ¥1B, Largest Consumer 3D Printing Funding Round](https://36kr.com/p/3885728813691145?f=rss) ⭐️ 6.3/10

Snapmaker (快造科技), a consumer 3D printing company, has closed a ¥1 billion (approx. $140M) funding round led by Cathay Innovation, with follow-on from investors including Meituan Strategic Investment, Meituan Longzhu, Hillhouse Venture Capital, and Shunwei Capital, alongside Good Future Strategic Investment. The deal signals growing institutional confidence in consumer-grade 3D printing, a category long confined to hobbyists and engineers, and underscores a shift toward multi-color and multi-material printing as the key driver to break into mainstream consumer markets. Snapmaker's U1 printer uses a four-independent-toolhead architecture with a SnapSwap™ quick-change system, achieving a claimed 5x speed improvement and ~80% reduction in material waste versus traditional single-nozzle solutions that require purging and reloading for each color change. The product raised $20.61M on Kickstarter from over 20,000 backers, setting a global 3D printing crowdfunding record, and has now shipped more than 100,000 units.

rss · 36氪 · Jul 8, 00:50

**Background**: Consumer FDM 3D printers have historically been limited to single-color, single-material output, restricting use to engineers and hobbyists. Multi-color/multi-material printing has emerged as the consensus breakthrough, but mainstream approaches rely on a single nozzle that must purge and reload filament for every color change — a slow, wasteful process that often takes dozens of hours per model and struggles to mix different materials. To address this, several vendors, including Bambu Lab, Creality, Flashforge, and Prusa, are pursuing multi-toolhead architectures, the design direction Snapmaker's U1 follows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jlc-3dp.cn/technicalColumnsDetails/58761.html">多色3D打印全解析: 从入门双色到工业级全彩的技术路径与选型指南-嘉立...</a></li>
<li><a href="https://www.163.com/dy/article/KG8G2GU2051186GP.html">FDM多材料多喷头切换3D打印大战：拓竹、快造、纵维立方、PRUSA、LIQTR...</a></li>
<li><a href="https://patents.google.com/patent/CN206999645U/zh">CN206999645U - Fdm打印机单喷头自动换料系统 - Google Patents</a></li>

</ul>
</details>

**Tags**: `#3D打印`, `#消费硬件`, `#融资`, `#Snapmaker`, `#硬件创业`

---

<a id="item-17"></a>
## [「德睿智药」获5200万美元B轮融资，AI设计的减肥药已进入3期临床｜36氪首发](https://36kr.com/p/3885479689465858?f=rss) ⭐️ 6.3/10

Chinese AI pharma company 德睿智药 (Deep Intelligent Pharma) raised $52M Series B, with its AI-designed oral GLP-1 small molecule weight loss drug MDR-001 advancing to Phase III clinical trials.

rss · 36氪 · Jul 8, 00:00

**Tags**: `#AI drug discovery`, `#pharmaceuticals`, `#GLP-1`, `#funding`, `#China tech`

---

<a id="item-18"></a>
## [Cloudflare and OpenAI Launch Pilot to Improve AI Search Indexing](https://36kr.com/newsflashes/3886946347694593?f=rss) ⭐️ 6.3/10

On July 8, Cloudflare and OpenAI announced a research pilot project that leverages Cloudflare's real-time network signals—including content freshness, traffic quality, and actual page changes—to help AI search engines more efficiently discover and index relevant content on the open web, ultimately improving the accuracy and timeliness of AI-generated answers. This collaboration is significant because Cloudflare's network handles traffic for over one in five websites worldwide, giving OpenAI access to unique, large-scale real-time signals about web content. Such data could meaningfully improve the relevance and recency of AI search results while also shaping how the broader AI industry interacts with web infrastructure providers. The pilot centers on three signal types: content freshness, traffic quality, and actual page changes—all observed in real time across Cloudflare's CDN. Notably, Cloudflare also introduced a Content Signals Policy in September 2025, extending the robots.txt framework to give publishers more control over how their content is used in AI contexts, which provides broader context for this partnership.

rss · 36氪 · Jul 8, 12:06

**Background**: Traditional search engines rely on crawlers that periodically scan the web, store pages in an index, and rank results based on keywords and links. AI-powered search engines differ by attempting to understand context, process dynamic content, and adapt autonomously rather than simply matching terms. Both approaches face challenges in efficiently discovering fresh, high-quality content at web scale. Cloudflare, as a major CDN provider sitting between users and origin servers, is uniquely positioned to observe real-time network signals across a vast portion of the internet, making its data particularly valuable for improving both traditional and AI-driven crawling strategies.

<details><summary>References</summary>
<ul>
<li><a href="https://rallies.ai/news/cloudflare-launches-openai-pilot-using-signals-from-20-of-web-traffic">Cloudflare Launches OpenAI Pilot Using Signals from 20% of ...</a></li>
<li><a href="https://blog.cloudflare.com/content-signals-policy/">Giving users choice with Cloudflare’s new Content Signals Policy</a></li>
<li><a href="https://avenuez.com/blog/ai-crawlers-vs-traditional-crawlers-how-ai-indexes-the-web-differently/">AI Crawlers vs. Traditional Crawlers: How AI Indexes the Web ...</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#OpenAI`, `#AI搜索`, `#网页索引`, `#基础设施`

---

<a id="item-19"></a>
## [Blue Origin Raises $10 Billion at $130 Billion Valuation](https://36kr.com/newsflashes/3886944497154824?f=rss) ⭐️ 6.3/10

Blue Origin has closed a $10 billion funding round at a $130 billion valuation, with founder Jeff Bezos personally contributing $2 billion of that amount. The massive valuation signals extraordinary investor confidence in the commercial space sector and gives Blue Origin substantially more capital to compete with SpaceX in launch services, lunar lander programs, and long-term space infrastructure ambitions. Bezos's $2 billion personal commitment is a notable signal of his continued financial backing despite his reduced day-to-day role since stepping down as Amazon CEO. The $130 billion post-money valuation represents a significant premium over Blue Origin's earlier reported valuations and underscores the heated investor appetite for late-stage private space companies.

rss · 36氪 · Jul 8, 12:04

**Background**: Blue Origin, founded by Jeff Bezos in 2000, is a private American space technology company headquartered in Kent, Washington. It operates the suborbital New Shepard rocket used for space tourism and the heavy-lift New Glenn rocket designed for orbital payloads. The company competes primarily with SpaceX in the commercial launch market and has secured contracts for NASA's Artemis lunar lander program. Blue Origin's name reflects its long-term vision of enabling millions of people to live and work in space for the benefit of Earth.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blue_Origin">Blue Origin - Wikipedia</a></li>
<li><a href="https://www.blueorigin.com/about-blue">About Blue Origin</a></li>
<li><a href="https://spacenexus.us/blog/spacex-blue-origin-rocket-lab-comparison-2026">SpaceX vs Blue Origin vs Rocket Lab: Launch Provider ...</a></li>

</ul>
</details>

**Tags**: `#Blue Origin`, `#funding`, `#space industry`, `#Bezos`, `#venture capital`

---

<a id="item-20"></a>
## [Decoding the obfuscated bash script on a Uniqlo t-shirt](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/) ⭐️ 6.0/10

Analysis of an obfuscated, self-evaluating bash script printed on a Uniqlo x Akamai t-shirt, exploring how it works and the design decisions behind it.

hackernews · speerer · Jul 8, 08:46 · [Discussion](https://news.ycombinator.com/item?id=48829312)

**Tags**: `#bash`, `#obfuscation`, `#quine`, `#hacker-news`, `#creative-coding`

---