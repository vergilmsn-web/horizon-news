---
layout: default
title: "Horizon Summary: 2026-08-18 (EN)"
date: 2026-08-18
lang: en
---

> From 75 items, 20 important content pieces were selected

---

1. [A Preview of DuckDB v2.0](#item-1) ⭐️ 8.0/10
2. [HBM Shipments to Malaysia Surge, Pointing to Intel's Project Pelican](#item-2) ⭐️ 7.5/10
3. [Geekom Pulls Driver Download Pages After Trojan Found in Legacy Mini PC Drivers](#item-3) ⭐️ 7.5/10
4. [China's Domestic AI Chips to Capture 90% of Local Market by 2026](#item-4) ⭐️ 7.5/10
5. [AirTag Exposes Amazon Facility Destroying Books for AI Training](#item-5) ⭐️ 7.5/10
6. [Nvidia crypto mining GPUs hacked to restore locked-away VRAM — software mod unlocks 64GB of VRAM on $250 CMP 170HX](#item-6) ⭐️ 7.5/10
7. [Memory prices climb 500% in 12 months, up to 10x the lowest ever tracked prices — 128GB of DDR5 now $3,399](#item-7) ⭐️ 7.5/10
8. [Intel Xeon 658X Review: Granite Rapids Enters Workstations](#item-8) ⭐️ 7.5/10
9. [Alibaba's Qwen Surpasses 3 Billion Downloads, Leading Global Open-Weight AI](#item-9) ⭐️ 7.3/10
10. [Linux 7.3 improves performance when running out of vRAM](#item-10) ⭐️ 7.0/10
11. [Google buys Spirit Airlines' bankruptcy data for $10M for AI training](#item-11) ⭐️ 7.0/10
12. [Israel accused of creating fake think tank to manipulate AI chatbots](#item-12) ⭐️ 7.0/10
13. [Top Five NAND Flash Brands' Revenue Soars 77% QoQ in Q2 2026; Micron Climbs to Third](#item-13) ⭐️ 7.0/10
14. [Roblox In Hot Water Again for "Priotitizing Revenue" Over Child Safety](#item-14) ⭐️ 6.5/10
15. [ASUS GPU Tweak III Adds Auto-Shutdown to Prevent 12V-2×6 Meltdowns](#item-15) ⭐️ 6.5/10
16. [Federal Court Upholds Judicial Immunity Despite Alleged AI Reliance](#item-16) ⭐️ 6.5/10
17. [China Orders State Agencies to Uninstall Government-Customized Windows 10](#item-17) ⭐️ 6.5/10
18. [Indian Startup Othisis Test-Fires 3D-Printed Cryogenic Reusable Rocket Engine](#item-18) ⭐️ 6.5/10
19. [Alibaba Sells Lingxi Games for $2B+ to Fund AI Infrastructure](#item-19) ⭐️ 6.5/10
20. [Quake Shareware CD-ROM: A Technical Deep-Dive into 90s Game Distribution](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [A Preview of DuckDB v2.0](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 8.0/10

Preview of DuckDB v2.0 highlighting major new features and improvements for the popular in-process analytical database.

hackernews · ibotty · Aug 17, 13:46 · [Discussion](https://news.ycombinator.com/item?id=49330781)

**Tags**: `#duckdb`, `#database`, `#analytics`, `#data-engineering`, `#major-release`

---

<a id="item-2"></a>
## [HBM Shipments to Malaysia Surge, Pointing to Intel's Project Pelican](https://www.techpowerup.com/351658/hbm-shipments-to-malaysia-surge-pointing-to-intels-project-pelican-facility) ⭐️ 7.5/10

South Korean export data analyzed by SemiAnalysis shows that approximately $1.3 billion worth of high-bandwidth memory (HBM) is now being shipped to Malaysia, while shipments to Taiwan have dropped from over $5 billion to under $3 billion in just a few months. Since TSMC operates no advanced packaging facility in Malaysia, this shipment surge strongly suggests that Intel's $7 billion Project Pelican advanced packaging complex is operational and capturing HBM integration work traditionally dominated by TSMC's CoWoS technology. This development signals Intel's emergence as a credible third-party advanced packaging provider for AI and high-performance computing chips, directly challenging TSMC's near-monopoly on CoWoS services amid a severe global capacity crunch. It represents a major strategic milestone for Intel's foundry ambitions and could reshape supply chain dynamics for hyperscalers and AI chip designers seeking alternatives to TSMC. Project Pelican supports both EMIB (Embedded Multi-die Interconnect Bridge) and Foveros packaging flows, enabling die sort and die prep operations for heterogeneous chip integration. Interest in Intel's packaging services has reportedly attracted companies such as MediaTek, Google, and Qualcomm, though the article notes that other Malaysian packaging players remain too small to account for the observed shipment volumes.

rss · TechPowerUp News · Aug 17, 17:19

**Background**: High-bandwidth memory (HBM) is a type of 3D-stacked DRAM that delivers very high data throughput with better energy efficiency than conventional memory, making it essential for AI accelerators and GPUs used in training and inference workloads. Advanced packaging technologies such as TSMC's CoWoS (Chip-on-Wafer-on-Substrate) and Intel's EMIB and Foveros are needed to integrate HBM stacks with logic dies into a single package. The current global demand for CoWoS capacity has far outstripped supply due to the AI chip boom, creating an opening for alternative providers like Intel, whose Foveros technology stacks chiplets face-to-face on a silicon interposer, while EMIB uses small silicon bridges embedded in the package substrate for high-density chip-to-chip connections.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/343545/intel-completes-project-pelican-malaysia-packaging-fab-for-emib-and-foveros">Intel Completes "Project Pelican" Malaysia Packaging Fab for ...</a></li>
<li><a href="https://www.lovechip.com/blog/foveros-vs-emib">Foveros vs EMIB: Key Differences, Performance Trade-offs, and ...</a></li>
<li><a href="https://www.aminext.blog/en/post/tsmc-cowos-s-r-l-differences">CoWoS - S , R , L Explained – TSMC ’s Advanced Packaging Strategies...</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#semiconductors`, `#advanced-packaging`, `#HBM`, `#TSMC-competition`

---

<a id="item-3"></a>
## [Geekom Pulls Driver Download Pages After Trojan Found in Legacy Mini PC Drivers](https://www.techpowerup.com/351651/geekom-pulls-download-pages-after-malware-found-in-legacy-mini-pc-drivers) ⭐️ 7.5/10

Geekom has removed the legacy LAN driver download page for its A7, A8, AE7, AX7 Pro, and AX8 Pro mini PCs after multiple malware scanning services confirmed the package contained a trojan capable of executing attacker commands. The company issued an official apology, stating the issue stemmed from an outdated resource that was not linked from the main product page but remained publicly accessible and indexed by search engines. This is a notable supply chain security incident involving a mainstream consumer hardware vendor distributing trojan-laced drivers through its official download infrastructure, affecting users who purchased affected AMD-based mini PCs. The case underscores how legacy pages left unmaintained on vendor sites can become persistent malware distribution vectors, and highlights the value of independent community-driven malware verification. The trojan was first flagged by Windows Security and subsequently verified by VirusTotal, FileScan, and MetaDefender, lending strong credibility to community reports on the r/MiniPCs subreddit. Geekom confirmed the malicious code was confined to the now-removed legacy drivers and stated the affected page was an outdated resource that failed to be cleaned up in time, though users who previously downloaded the package may still have infected files locally.

rss · TechPowerUp News · Aug 17, 16:09

**Background**: A supply chain attack in cybersecurity refers to a compromise in which malicious code or tampered components are introduced through a trusted vendor's legitimate distribution channels, making the malware harder to detect because users trust the source. Multi-engine malware scanning services like VirusTotal and OPSWAT's MetaDefender aggregate dozens of antivirus engines to verify suspicious files, significantly increasing detection reliability compared to a single scanner. Mini PCs are compact desktop computers that have surged in popularity as affordable alternatives to traditional desktops, and vendors like Geekom ship downloadable driver packages from their websites to support varied hardware configurations across product generations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack - Wikipedia</a></li>
<li><a href="https://www.opswat.com/blog/metadefender-more-private-alternative-virustotal">Metadefender : A More Private Alternative to VirusTotal - OPSWAT</a></li>

</ul>
</details>

**Discussion**: Community discussion on Reddit's r/MiniPCs subreddit confirmed the malware warning, with multiple users reporting that the trojan-flagged driver was also detected by independent antivirus tools, validating the initial report. The discussion emphasized concerns about legacy vendor pages remaining online and indexed long after products are superseded, and praised Geekom's relatively swift and transparent response in pulling the page and issuing an apology.

**Tags**: `#security`, `#malware`, `#supply-chain`, `#hardware`, `#mini-pc`

---

<a id="item-4"></a>
## [China's Domestic AI Chips to Capture 90% of Local Market by 2026](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd) ⭐️ 7.5/10

Analysts forecast that Chinese AI accelerator vendors, led by Huawei and Cambricon, will supply roughly 90% of the AI processors used within China by 2026, marking near self-sufficiency in high-end AI hardware and a major shift away from Nvidia and AMD. This shift would significantly erode Nvidia and AMD's footprint in one of the world's largest AI chip markets, accelerating the US-China tech decoupling and reshaping the global AI supply chain. It also signals that export controls on advanced GPUs may be pushing China toward an indigenous AI hardware stack that rivals Western offerings. Cambricon, a partially state-owned Beijing-listed chip designer specializing in neural processing units (NPUs) and GPGPUs, and Huawei with its Ascend AI accelerator line (including variants like the Ascend 950PR for inference workloads) are expected to be the primary beneficiaries. Despite HBM memory and fab capacity remaining bottlenecks, analysts see domestic supply reaching the 90% threshold within roughly a year.

rss · Tom's Hardware · Aug 18, 11:20

**Background**: AI accelerators are specialized processors (GPUs, NPUs, or custom ASICs) designed to train and run large AI models efficiently. Nvidia currently dominates this market with its H100 and B-series GPUs, while AMD offers competing accelerators. Huawei's Ascend and Cambricon's MLU chips are China's leading domestic alternatives. US export controls have restricted China's access to cutting-edge Nvidia chips, pushing Chinese cloud providers and AI firms to adopt local alternatives. The claim that 90% domestic supply is achievable reflects both rapid progress in Chinese chip design and the effectiveness of US sanctions in redirecting demand toward homegrown silicon.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cambricon_Technologies">Cambricon Technologies - Wikipedia</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-chip-champions-ramp-up-production-of-ai-accelerators-at-domestic-fabs-but-hbm-and-fab-production-capacity-are-towering-bottlenecks">China's chip champions ramp up production of AI accelerators at...</a></li>
<li><a href="https://www.supercomputing.news/entity/huawei-ascend-950pr">Huawei Ascend 950PR — Supercomputing News</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#China tech`, `#Huawei`, `#Cambricon`, `#semiconductors`

---

<a id="item-5"></a>
## [AirTag Exposes Amazon Facility Destroying Books for AI Training](https://www.tomshardware.com/tech-industry/artificial-intelligence/secret-tracking-device-placed-in-rare-book-ends-up-in-amazon-processing-facility-destroying-books-to-train-ai-models-is-all-the-vegas-warehouse-does) ⭐️ 7.5/10

404 Media placed an Apple AirTag inside a shipment of 1,000 books and tracked it to an Amazon processing facility in Las Vegas, where the books were systematically destroyed by having their spines cut off and pages scanned, allegedly solely to generate training data for AI models. This investigation reveals the industrial-scale destruction of physical books to feed AI training pipelines, raising serious ethical, copyright, and environmental concerns about how AI companies source their data. It exposes practices that affect publishers, authors, and the broader ecosystem of knowledge production. The Las Vegas facility reportedly spends all day cutting spines and scanning pages, destroying the books in the process. The AirTag, a small Apple IoT tracker that uses the crowdsourced Find My network, allowed reporters to follow the shipment's chain of custody and uncover the facility's sole purpose.

rss · Tom's Hardware · Aug 18, 10:30

**Background**: An Apple AirTag is a quarter-sized tracking device that uses Apple's crowdsourced Find My network to locate lost or stolen items. Many AI companies have turned to digitizing physical books — including rare and out-of-print titles — to create training datasets, as much of the world's knowledge still resides in printed volumes. Anthropic's 'Project Panama' is a notable example of large-scale physical-to-digital book scanning for AI training. The practice of destroying books by cutting spines to scan individual pages raises questions about copyright law (first-sale doctrine, fair use), data provenance, and environmental waste.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AirTag">AirTag - Wikipedia</a></li>
<li><a href="https://www.e-arc.com/ai-data-capture/">AI Training Document Digitization | AI Document Scanning | ARC</a></li>
<li><a href="https://www.wisdomai.com/insights/The+Vergecast/project-panama-anthropic-books-ai-training-data-d99975cc">Millions of Books, One Copy Each: H... (2026) | The Vergecast ...</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#training data`, `#copyright`, `#investigative journalism`, `#Amazon`

---

<a id="item-6"></a>
## [Nvidia crypto mining GPUs hacked to restore locked-away VRAM — software mod unlocks 64GB of VRAM on $250 CMP 170HX](https://www.tomshardware.com/pc-components/gpus/nvidia-crypto-mining-gpus-hacked-to-restore-locked-away-vram-in-order-to-feed-ai-boom-software-mod-unlocks-64gb-of-vram-on-usd250-cmp-170hx) ⭐️ 7.5/10

Software mod unlocks disabled VRAM on Nvidia's CMP 170HX crypto mining GPU, exposing 64GB of usable memory on a $250 card for AI workloads.

rss · Tom's Hardware · Aug 18, 09:30

**Tags**: `#gpu`, `#nvidia`, `#ai-infrastructure`, `#hardware-hacking`, `#cryptocurrency-mining`

---

<a id="item-7"></a>
## [Memory prices climb 500% in 12 months, up to 10x the lowest ever tracked prices — 128GB of DDR5 now $3,399](https://www.tomshardware.com/pc-components/ram/memory-prices-climb-500-percent-in-12-months-up-to-10x-the-lowest-ever-tracked-prices-128gb-of-ddr5-now-usd3-399) ⭐️ 7.5/10

DRAM prices have surged up to 500% in 12 months due to the ongoing memory crisis, with 128GB DDR5 kits now reaching $3,399.

rss · Tom's Hardware · Aug 17, 13:52

**Tags**: `#hardware`, `#memory`, `#DDR5`, `#market-trends`, `#PC-components`

---

<a id="item-8"></a>
## [Intel Xeon 658X Review: Granite Rapids Enters Workstations](https://www.servethehome.com/intel-xeon-658x-review-granite-rapids-for-workstations/) ⭐️ 7.5/10

ServeTheHome has published a hands-on review of Intel's Xeon 658X, a 24-core member of the new Xeon 600 workstation family, which brings the Granite Rapids server architecture to professional workstation platforms. The review highlights the chip's strong memory bandwidth as a key factor driving its performance for workstation workloads. This marks Intel's first Granite Rapids–based offering targeted at the workstation segment, giving professionals in 3D rendering, simulation, and complex data analysis access to the same P-core architecture that has powered Intel's top-end server chips. The Xeon 600 line competes directly with AMD's Ryzen Threadripper and EPYC workstation platforms, where memory bandwidth and core count are decisive for many professional workflows. The reviewed Xeon 658X is a 24-core part within the wider Xeon 600 family, which scales up to 86 P-cores and offers 128 lanes of PCIe 5.0 connectivity paired with the W890 chipset on the GNR-W platform. Granite Rapids is built on the Intel 3 process node and uses the Redwood Cove architecture, originally designed for high-performance computing and latency-sensitive workloads.

rss · ServeTheHome · Aug 17, 18:00

**Background**: Granite Rapids is the codename for Intel's 6th-generation Xeon Scalable server processors, originally launched on September 24, 2024, with configurations scaling up to 128 P-cores for data center use. The Xeon 600 workstation family, announced in February 2026, adapts this same core architecture to single-socket and multi-socket workstation boards, bringing enterprise-class memory bandwidth and PCIe 5.0 I/O to professional desktops. Workstation buyers typically care about a balance of core count, memory channels, and platform stability for sustained professional workloads such as CAD, rendering, and simulation.

<details><summary>References</summary>
<ul>
<li><a href="https://newsroom.intel.com/intel-products/intel-launches-new-intel-xeon-600-processors-for-workstation">Intel Launches new Intel® Xeon® 600 Processors for Workstation</a></li>
<li><a href="https://www.intel.com/content/www/us/en/products/details/processors/xeon/workstations.html">Intel Xeon 600 Processors for Workstations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Granite_Rapids">Granite Rapids - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Intel Xeon`, `#Granite Rapids`, `#Workstations`, `#CPU Review`, `#Memory Bandwidth`

---

<a id="item-9"></a>
## [Alibaba's Qwen Surpasses 3 Billion Downloads, Leading Global Open-Weight AI](https://www.solidot.org/story?sid=85118) ⭐️ 7.3/10

According to a Hugging Face report, Alibaba's Qwen open-weight models surpassed 3 billion global downloads in the past six months, making it the largest community foundation model with 151,448 derivative models. Google and Meta's open-weight models trailed significantly at 418 million and 227 million downloads respectively. This data highlights the growing dominance of Chinese AI labs in the open-weight ecosystem, with Chinese labs consistently releasing models with parameters ranging from 754 billion to 2.78 trillion—far exceeding US counterparts that typically stay below 130 billion. The shift signals a significant redistribution of influence in global AI development, with downstream applications, derivatives, and commercial ecosystems increasingly anchored to Chinese-origin models. Among 178 Chinese models with over 20 billion parameters, 55% use the Apache 2.0 license and 22% use MIT, though most carry non-commercial use restrictions. The recently released Kimi K3 and Qwen3.8 large models add revenue-sharing requirements on top of non-commercial clauses. Notably, Thinking Machines' 952B-parameter Inkling model is built upon a Chinese base model, illustrating how the Chinese open-weight ecosystem underpins even Western AI efforts.

rss · Solidot · Aug 17, 15:44

**Background**: Open-weight models release trained model parameters for public download and use, but differ from fully open-source AI by not necessarily disclosing training code, data, or architecture. Hugging Face is the leading platform for hosting and distributing these models, making its ecosystem data a key indicator of AI development trends. The parameter count of a model roughly indicates its capacity to handle complex tasks, with larger models generally capable of more sophisticated reasoning but requiring more computational resources.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fierce-network.com/content/open-weight-ai-vs-open-source-ai-whats-difference">Open weight AI vs open - source AI : what’s the difference?</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://thinkingmachines.ai/inkling/">Inkling - Thinking Machines Lab</a></li>

</ul>
</details>

**Tags**: `#open-source-ai`, `#qwen`, `#alibaba`, `#hugging-face`, `#ai-ecosystem`

---

<a id="item-10"></a>
## [Linux 7.3 improves performance when running out of vRAM](https://pixelcluster.dev/VRAM-Overcommit/) ⭐️ 7.0/10

Analysis of Linux kernel 7.3 improvements for VRAM overcommit handling, addressing GPU memory management when applications exceed available VRAM.

hackernews · flaburgan · Aug 18, 07:51 · [Discussion](https://news.ycombinator.com/item?id=49342719)

**Tags**: `#linux-kernel`, `#gpu-computing`, `#memory-management`, `#vram`, `#performance-optimization`

---

<a id="item-11"></a>
## [Google buys Spirit Airlines' bankruptcy data for $10M for AI training](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962) ⭐️ 7.0/10

Google won a U.S. bankruptcy court auction for Spirit Airlines' corporate data, paying $10 million for a trove that includes 100 million emails, 500 million Microsoft Teams messages, 17 million OneDrive files, 20.5 million SharePoint items, over 30 million recorded customer service calls, and more than 15 million customer service chat records. This sets a potential precedent for how corporate data accumulated by bankrupt companies is valued, turning previously discarded information into a monetizable asset that AI labs are willing to pay premium prices for. It raises significant data privacy questions about whether customer information is being adequately de-identified before transfer, and may prompt future bankruptcy trustees to specifically market corporate data assets to AI companies. The dataset also includes 600,000 ServiceNow tickets, 13.7 million active email addresses from Oracle's Responsys marketing application, and details of 11 million in-flight Wi-Fi service sales, with community members expressing strong skepticism that all of this information was properly de-identified. The sale was conducted as a standard Section 363 asset sale in bankruptcy proceedings.

hackernews · pseudolus · Aug 18, 10:13 · [Discussion](https://news.ycombinator.com/item?id=49343559)

**Background**: When companies file for bankruptcy, their assets—including data—are typically liquidated through court-supervised auctions under Section 363 of the U.S. Bankruptcy Code to repay creditors. AI labs have increasingly sought high-quality, real-world human interaction data for training large language models, having largely exhausted publicly available internet data. Bobby Samuels, CEO of data company Protege, noted that AI labs have 'scraped the entire Internet' and now need authentic human-to-human conversations, making corporate communication archives from bankruptcies particularly valuable.

<details><summary>References</summary>
<ul>
<li><a href="https://www.troutman.com/insights/bankruptcy-asset-sales-a-primer/">Bankruptcy Asset Sales: A Primer - Troutman Pepper Locke</a></li>
<li><a href="https://eu.36kr.com/en/p/3943281519983746">AI Begins "Feeding On" Chat Records of Bankrupt Companies : What...</a></li>

</ul>
</details>

**Discussion**: Community members were divided between those fascinated by the precedent-setting nature of the sale and those concerned about privacy implications. Commenter 'dgrin91' questioned whether this was the first major case of corporate data being sold at bankruptcy and speculated that bankruptcy managers everywhere might now see this as a new revenue stream. 'ronbenton' raised concerns about whether the data, including 13.7 million marketing email addresses and detailed service records, was properly de-identified, while 'estetlinus' noted the broader trend of accumulated corporate data being auctioned like any other asset.

**Tags**: `#AI-training-data`, `#data-privacy`, `#bankruptcy`, `#Google`, `#corporate-data`

---

<a id="item-12"></a>
## [Israel accused of creating fake think tank to manipulate AI chatbots](https://responsiblestatecraft.org/israel-influence-chatgpt/) ⭐️ 7.0/10

A report from Responsible Statecraft reveals that Israel allegedly created a fake think tank website specifically designed to influence AI chatbot responses, representing a new and concerning vector for AI manipulation through strategically crafted web content. The site was engineered to be ingested by AI training pipelines or retrieved during chatbot queries, shaping model outputs on geopolitical topics. This incident exposes a real vulnerability in how AI chatbots consume and trust web content, showing that state actors can exploit training data ingestion and retrieval-augmented generation (RAG) systems to shape AI outputs at scale. It raises urgent questions about content provenance, source verification, and the integrity of AI-mediated information ecosystems. The tactic exploits both the training data collection phase (where crawlers index web content) and the live retrieval phase used by RAG-based chatbots, making it effective against both static model knowledge and real-time search-augmented responses. Unlike direct prompt injection, this approach is indirect and difficult to detect because the malicious content appears as a legitimate, well-structured source.

hackernews · DeepLogin · Aug 17, 20:46 · [Discussion](https://news.ycombinator.com/item?id=49337392)

**Background**: Data poisoning is a type of cyberattack where threat actors manipulate or corrupt the training data used to develop AI and machine learning models, potentially embedding biases, backdoors, or false narratives into the model's outputs. Retrieval-augmented generation (RAG) is a technique that enables large language models to retrieve and incorporate new information from external data sources at query time, meaning that any content published on the web can potentially influence a chatbot's response. Together, these two mechanisms mean that creating convincing-looking web content — such as a fake think tank with polished articles — can manipulate AI systems either at training time or at inference time.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/data-poisoning">What is data poisoning? - IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The top comment by 2001zhaozhao raises a prescient technical concern that fake organizations and AI-generated narratives will flood the internet within a year, making it nearly impossible to distinguish genuine sources from manufactured ones without external verification mechanisms. Other commenters, including karim79 and watutalkinbout, focus on Israel's broader geopolitical conduct, arguing that influence operations are redundant given public statements and visible military actions, while techteach00 identifies the Foundation for Defense of Democracies as another allegedly foreign-aligned think tank posing as American. The discussion splits between forward-looking AI security concerns and direct political critique.

**Tags**: `#ai-security`, `#disinformation`, `#llm-vulnerabilities`, `#information-warfare`, `#ai-ethics`

---

<a id="item-13"></a>
## [Top Five NAND Flash Brands' Revenue Soars 77% QoQ in Q2 2026; Micron Climbs to Third](https://www.dramexchange.com/WeeklyResearch/Post/2/12803.html) ⭐️ 7.0/10

TrendForce reports that the combined revenue of the top five publicly listed NAND Flash brands rose 77% QoQ to US$68.87 billion in Q2 2026, driven by steady AI server demand for enterprise SSDs that created a supply shortage and enabled suppliers to significantly raise ASPs through contract negotiations. Micron also moved up to third place in the market share ranking. This 77% QoQ revenue surge underscores how AI infrastructure spending is reshaping the memory market, with NAND Flash suppliers benefiting from sustained enterprise SSD demand even as consumer device markets such as smartphones and PCs weaken. Micron's rise to third place signals intensifying competition in a supply-constrained environment increasingly driven by AI workloads. Looking ahead to Q3 2026, TrendForce expects smartphone and PC demand to remain weak as higher BOM costs push up device prices, while AI server enterprise SSD demand stays strong. Suppliers are generally prioritizing capital expenditure on DRAM and HBM, limiting new NAND Flash capacity expansion and supporting continued ASP-driven revenue growth.

rss · DRAMeXchange (TrendForce) · Aug 18, 15:19

**Background**: NAND Flash is a type of non-volatile storage memory widely used in SSDs, smartphones, and other devices, with cell types ranging from SLC (1 bit/cell) to QLC (4 bits/cell), with TLC being the most prevalent in server and consumer SSDs. Enterprise SSDs built on high-capacity NAND are critical for AI workloads that require fast access to massive training datasets. HBM (High Bandwidth Memory) is a 3D-stacked DRAM technology used primarily in AI accelerators such as GPUs, and competes with NAND Flash for limited semiconductor manufacturing capacity and supplier capex budgets.

<details><summary>References</summary>
<ul>
<li><a href="https://intuitionlabs.ai/articles/hbm-vs-ddr-memory-comparison">HBM vs. DDR: Key Differences in Memory Technology Explained</a></li>

</ul>
</details>

**Tags**: `#NAND-flash`, `#semiconductor-industry`, `#memory-market`, `#AI-servers`, `#TrendForce`

---

<a id="item-14"></a>
## [Roblox In Hot Water Again for "Priotitizing Revenue" Over Child Safety](https://www.techpowerup.com/351669/roblox-in-hot-water-again-for-priotitizing-revenue-over-child-safety) ⭐️ 6.5/10

Roblox faces a new US Senate investigation over prioritizing revenue over child safety, following previous concerns about predatory behavior on the platform.

rss · TechPowerUp News · Aug 17, 22:23

**Tags**: `#Roblox`, `#child-safety`, `#tech-regulation`, `#US-Senate`, `#platform-policy`

---

<a id="item-15"></a>
## [ASUS GPU Tweak III Adds Auto-Shutdown to Prevent 12V-2×6 Meltdowns](https://www.techpowerup.com/351662/asus-gpu-tweak-iii-adds-auto-shutdown-to-prevent-12v-2x6-meltdowns) ⭐️ 6.5/10

ASUS has updated its GPU Tweak III software to version V2.1.8.0, adding an auto-shutdown feature for GPUs equipped with Power Detector+ that will power off the system when persistently high current is detected on the 12V-2×6 power connector. The feature is currently limited to four ASUS graphics cards: the ROG Astral GeForce RTX 5090, ROG Astral LC GeForce RTX 5090, ROG Astral GeForce RTX 5080, and ROG Matrix GeForce RTX 4090. The 12V-2×6 connector melting issue has destroyed numerous high-end NVIDIA GPUs, causing both financial loss and potential safety hazards. This software-based safeguard represents a meaningful mitigation layer, complementing hardware-side efforts by PSU and cable manufacturers, and could prevent catastrophic failures for users of compatible ASUS cards. ASUS has not disclosed the specific current thresholds or duration required to trigger the shutdown, and the feature requires both Power Detector+ hardware on the GPU and the latest GPU Tweak III software to function. This is an incremental industry response, following similar protective measures previously introduced by ASRock with its L-shaped 12V-2×6 cable design.

rss · TechPowerUp News · Aug 17, 18:48

**Background**: The 16-pin 12V-2×6 connector is a power standard introduced by NVIDIA in 2022 to replace older 6-pin and 8-pin GPU power connectors, capable of delivering up to 600W (or 660W in its updated form) to high-end graphics cards. It evolved from the earlier 12VHPWR connector, which was notorious for melting incidents, especially on GeForce RTX 4090 and RTX 5090 cards. Power Detector+ is an ASUS-specific hardware feature that monitors current flowing through individual pins on compatible ROG Astral graphics cards, originally designed to alert users to abnormal current draw before the latest update added the auto-shutdown capability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/12VHPWR">12 VHPWR - Wikipedia</a></li>
<li><a href="https://rog.asus.com/articles/guides/how-gpu-tweaks-power-detector-alerts-you-to-abnormal-current-on-your-rog-astral-graphics-card/">How GPU Tweak's Power Detector+ alerts you to abnormal ... - ROG</a></li>
<li><a href="https://overclock3d.net/news/gpu-displays/asus-adds-automatic-shutdown-support-to-power-detector-gpus-with-gpu-tweak-iii/">ASUS adds automatic shutdown support to Power Detector+ GPUs ...</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#GPU`, `#NVIDIA`, `#safety`, `#ASUS`

---

<a id="item-16"></a>
## [Federal Court Upholds Judicial Immunity Despite Alleged AI Reliance](https://www.tomshardware.com/tech-industry/artificial-intelligence/judges-who-use-ai-to-make-decisions-still-protected-by-judicial-immunity-court-ruling-protects-outcomes-regardless-of-ai-usage) ⭐️ 6.5/10

A U.S. federal court ruled that a judge accused of relying entirely on AI for a judicial decision can retain immunity from civil lawsuits. The decision did not determine whether using AI that way was legally or ethically permissible. 该裁定可能限制当事人通过民事诉讼质疑由人工智能深度影响的司法决定，同时没有解决人工智能治理中的关键问题。它凸显了区分司法豁免与透明度、准确性及独立人类判断等实质义务的必要性。 The court did not establish that AI actually produced the ruling; complete AI reliance was alleged in the dispute. The decision addressed civil-suit immunity rather than validating AI-generated judicial decisions or creating new standards for judicial AI use.

rss · Tom's Hardware · Aug 18, 11:00

**Background**: Judicial immunity limits certain civil claims against judges for conduct connected to their judicial role. That protection is separate from substantive questions about whether the conduct is lawful or ethical. Generative AI in judicial decision-making raises distinct concerns about transparency, accuracy, and preserving human judgment.

<details><summary>References</summary>
<ul>
<li><a href="https://151farmers.org/wp-content/uploads/2018/07/Immunity-of-Federal-and-State-Judges-from-Civil-Suit-Time-for-a.pdf">Immunity of Federal and State Judges from Civil Suit - Time for...</a></li>
<li><a href="https://www.ncsc.org/resources-courts/ai-courts-judicial-and-legal-ethics-issues">AI & the courts: Judicial and legal ethics issues</a></li>
<li><a href="https://www.cambridge.org/core/journals/data-and-policy/article/artificial-intelligence-at-the-bench-legal-and-ethical-challenges-of-informingor-misinformingjudicial-decisionmaking-through-generative-ai/D1989AC5C81FB67A5FABB552D3831E46">Artificial intelligence at the bench: Legal and ethical ...</a></li>

</ul>
</details>

**Tags**: `#ai-governance`, `#judicial-ai`, `#legal-tech`, `#ai-ethics`, `#ai-policy`

---

<a id="item-17"></a>
## [China Orders State Agencies to Uninstall Government-Customized Windows 10](https://www.tomshardware.com/software/operating-systems/china-reportedly-orders-state-agencies-to-uninstall-its-government-only-edition-of-windows-10) ⭐️ 6.5/10

China's Ministry of State Security has ordered some state-linked organizations to uninstall a customized version of Windows 10 from their machines, citing data security concerns. The directive, reported by Bloomberg, accelerates the planned retirement of the government-only edition. This move signals China's accelerating push for technological sovereignty and reducing reliance on foreign operating systems in government infrastructure. It reflects broader geopolitical tensions around supply chain security and could accelerate the adoption of domestic operating systems like Kylin or openKylin in China's public sector. The customized edition was originally created by Microsoft in partnership with Chinese authorities and included government-approved anti-virus solutions. With Windows 10 mainstream support having ended on October 14, 2025, organizations can only continue receiving critical security patches through Microsoft's paid Extended Security Updates (ESU) program.

rss · Tom's Hardware · Aug 18, 10:11

**Background**: Windows 10 has multiple editions tailored for different use cases, including a special Chinese government edition developed by Microsoft to comply with local regulations and address piracy concerns. This version included pre-installed government-approved security software. As Windows 10 approaches its end-of-support date, organizations worldwide must either migrate to Windows 11 or enroll in the ESU program for continued security updates. China's push to remove foreign operating systems aligns with its longstanding 'Secure and Controllable' (安全可控) technology policy, which aims to replace Western software and hardware in sensitive government environments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/software/operating-systems/china-reportedly-orders-state-agencies-to-uninstall-its-government-only-edition-of-windows-10">China reportedly orders state agencies to uninstall... | Tom's Hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Windows_10_editions">Windows 10 editions - Wikipedia</a></li>
<li><a href="https://hothardware.com/news/microsoft-cuts-through-piracy-fog-by-offering-chinese-government-customized-version-of-windows-10">Microsoft Cuts Through Piracy Fog By Offering Chinese Government ...</a></li>

</ul>
</details>

**Tags**: `#operating-systems`, `#china`, `#cybersecurity`, `#windows`, `#geopolitics`

---

<a id="item-18"></a>
## [Indian Startup Othisis Test-Fires 3D-Printed Cryogenic Reusable Rocket Engine](https://www.tomshardware.com/3d-printing/othisis-test-fires-3d-printed-fully-cryogenic-reusable-rocket-engine-indian-startup-leverages-slm-printing-to-create-its-first-working-prototype) ⭐️ 6.5/10

Othisis, an Indian aerospace startup founded just two years ago, has successfully test-fired a fully 3D-printed, reusable rocket engine operating on cryogenic propellants, marking the company's first working prototype. This milestone demonstrates that additive manufacturing can be applied not just to conventional rocket components but to entire cryogenic engines, potentially lowering production costs, shortening lead times, and enabling faster iteration for reusable launch vehicles in the growing commercial space sector. The engine was produced using Selective Laser Melting (SLM), a metal additive manufacturing process that uses a high-power fiber laser to fully melt fine metal powder layer by layer into dense solid parts from digital CAD models. Because SLM can produce near-net-shape geometries, it is well suited to the complex internal channels—such as regenerative cooling passages—required in cryogenic engines.

rss · Tom's Hardware · Aug 18, 10:00

**Background**: Selective Laser Melting (SLM), also called Direct Metal Laser Melting (DMLM), is a form of metal additive manufacturing that uses a high-power fiber laser to fully melt metal powder into 100% dense solid parts layer by layer. Cryogenic rocket engines are propulsion systems powered by ultra-cold liquefied gases—most commonly liquid hydrogen as fuel and liquid oxygen as oxidizer—stored at very low temperatures. They typically include a combustion chamber, fuel injector, turbopumps, cryogenic valves, fuel tanks, and a nozzle, and often use regenerative cooling, where cryogenic fuel is circulated around the nozzle before being pumped into the combustion chamber. Cryogenic engines offer high efficiency and thrust-to-weight ratios, which is why they are favored for modern space missions, but their extreme operating temperatures make them difficult and expensive to manufacture traditionally.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cryogenic_rocket_engine">Cryogenic rocket engine - Wikipedia Cryogenic fuel - Wikipedia Understanding Cryogenic Rocket Engine Propulsion in Modern ... What Makes a Cryogenic Rocket Engine Work? - Students for ... Cryogenic rocket engine explained Foundations of Cryogenic Rocket Propulsion: Unlocking the ... Get to know everything about the highly efficient cryogenic ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cryogenic_fuel">Cryogenic fuel - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#3D printing`, `#additive manufacturing`, `#rocket propulsion`, `#cryogenic engines`, `#space technology`

---

<a id="item-19"></a>
## [Alibaba Sells Lingxi Games for $2B+ to Fund AI Infrastructure](https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-sells-its-gaming-studio-for-at-least-1-5-billion-to-help-fund-ai-buildout) ⭐️ 6.5/10

Alibaba has agreed to sell its game development unit Lingxi Games — the studio behind the mobile hit 'Three Kingdoms: Strategy Edition' — to Asian private equity firm Trustar Capital for more than $2 billion, according to reports from Bloomberg and Reuters. This deal represents a massive capital reallocation by one of China's largest tech companies away from gaming and toward AI infrastructure, signaling the enormous financial demands of the AI buildout race and reflecting a broader trend of major tech firms divesting non-core businesses to fund AI ambitions. Lingxi Games, formerly known as Alibaba Games, will operate independently under Trustar Capital while retaining its existing teams and product lineup. Trustar Capital is a Hong Kong-based private equity affiliate of CITIC Capital Holdings, with offices in Beijing, Shanghai, Tokyo, and New York.

rss · Tom's Hardware · Aug 17, 15:39

**Background**: Lingxi Games is a major Chinese mobile game developer best known for 'Three Kingdoms: Strategy Edition,' a strategy game based on the classic historical period. The gaming industry in China is highly competitive and heavily regulated, with periodic licensing freezes historically impacting publishers. Meanwhile, the AI industry — particularly large language models and generative AI — requires enormous capital expenditure on data centers, GPUs, and cloud infrastructure, which has driven many tech giants to liquidate or divest non-core assets. Trustar Capital's acquisition of Lingxi Games mirrors similar strategic pivots, such as Micron's exit from its consumer memory business, as companies refocus on AI-adjacent opportunities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/legal/transactional/alibaba-sell-lingxi-games-more-than-2-billion-deal-source-says-2026-08-17/">Alibaba to sell Lingxi Games in more than $2 billion deal ...</a></li>
<li><a href="https://fortune.com/2026/08/18/alibaba-lingxi-china-ai-us/">Alibaba's $2 billion gaming exit signals where Beijing wants ...</a></li>
<li><a href="https://beijingtimes.com/business/companies/2026/08/18/alibaba-sells-lingxi-games-trustar-capital-ai-focus/">Alibaba Sells Lingxi Games to Trustar Capital in $2B Deal</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Alibaba`, `#industry-news`, `#investment`, `#cloud-infrastructure`

---

<a id="item-20"></a>
## [Quake Shareware CD-ROM: A Technical Deep-Dive into 90s Game Distribution](https://fabiensanglard.net/quake_shareware_cd/index.html) ⭐️ 6.0/10

Fabien Sanglard published a detailed technical analysis examining how id Software packed Quake's game assets onto its shareware CD-ROM and navigated the economics of shareware distribution in the mid-1990s. The article traces the engineering decisions behind squeezing the shareware episode onto a medium whose capacity far exceeded what the game alone required. This piece offers a rare, technically grounded look at how pioneering 90s studios solved the unusual problem of CD-ROM overkill in an era of floppy-based distribution. It also illuminates the shareware business model's role in bootstrapping iconic studios like id Software, Apogee, and Epic MegaGames into industry giants. The Quake shareware CD was announced on July 3, 1996, and released on August 30, 1996, with hacker group GNOMON cracking it just 39 days later. The disc notably included the Nine Inch Nails (NIN) soundtrack—making it the only CD release of that music—though listeners are advised to skip track 1.

hackernews · shdon · Aug 17, 22:06 · [Discussion](https://news.ycombinator.com/item?id=49338328)

**Background**: Shareware was a dominant distribution model in the early 1990s, particularly for DOS games, where developers released a portion of the game for free and charged for the full version. Studios like id Software, Apogee Software (later 3D Realms), and Epic MegaGames (now Epic Games) built their early businesses on this approach. CD-ROMs of that era offered roughly 650 MB of capacity—far more than the typical game's assets—leading to either 'shovelware' compilations or, in id Software's case, bundling high-quality bonus content like full soundtracks to fill the disc.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shareware">Shareware - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quake_(video_game)">Quake (video game) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shovelware">Shovelware - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The comments are overwhelmingly nostalgic, with users reminiscing about copying files from the shareware disc as teenagers and still carrying Quake's ID1 directory across computers decades later. Several commenters highlight the NIN soundtrack as the disc's main draw, while others recall how cracks appeared on newsgroups like a.b.m.a almost as fast as software was posted—one user speculates that id Software intentionally made the shareware easily crackable as a grassroots marketing strategy.

**Tags**: `#game-development`, `#retro-computing`, `#reverse-engineering`, `#cd-rom`, `#quake`

---