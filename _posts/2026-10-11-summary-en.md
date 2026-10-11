---
layout: default
title: "Horizon Summary: 2026-10-11 (EN)"
date: 2026-10-11
lang: en
---

> From 38 items, 17 important content pieces were selected

---

1. [DuckDB 2.0 Delivers Major Performance Gains in Query Execution](#item-1) ⭐️ 8.0/10
2. [Senate Report Alleges Misleading Claims About AI Data Center Economic Benefits](#item-2) ⭐️ 7.5/10
3. [Ukrainian drones strike Yandex data center, knocking multiple modules offline](#item-3) ⭐️ 7.5/10
4. [Lightbulb Computer Prototype Uses Hand Tracking and Speech for Interaction](#item-4) ⭐️ 7.0/10
5. [Unikernels Revival Proposal in the AI Era](#item-5) ⭐️ 7.0/10
6. [Hyper-NA EUV Lithography Set as Next Major Chipmaking Frontier for 2036](#item-6) ⭐️ 7.0/10
7. [Jury Deliberation Pending in High-Profile Qualcomm vs. Arm Case](#item-7) ⭐️ 7.0/10
8. [PS2 Discs Now Load on Jailbroken PS5 Consoles Through PS5SX2 Emulator](#item-8) ⭐️ 6.5/10
9. [AMD Raises GDDR6 Prices for GPU Board Partners](#item-9) ⭐️ 6.5/10
10. [Super Micro smuggling co-conspirator pleads guilty to sending AI chips to China](#item-10) ⭐️ 6.5/10
11. [AnyPS5 project reaches critical GPU milestone in race to enable running PS5 games natively on PC](#item-11) ⭐️ 6.5/10
12. [Graduates fly 3D-printed jet RC aircraft using standard PETG](#item-12) ⭐️ 6.5/10
13. [Global PC Shipments Plunge Over 20% Amid AI-Driven Memory Price Surge](#item-13) ⭐️ 6.3/10
14. [Building Custom Decision Models and Lightweight AI Alternatives](#item-14) ⭐️ 6.0/10
15. [Receiving a Knuth Reward Check for TAoCP Error](#item-15) ⭐️ 6.0/10
16. [SoftBank Targets Middle Eastern Investors for Massive AI Fund](#item-16) ⭐️ 5.5/10
17. [SPECviewperf 15.0.1 Linux Edition Adds Official Arm Support](#item-17) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [DuckDB 2.0 Delivers Major Performance Gains in Query Execution](https://motherduck.com/blog/why-duckdb-20-is-faster/) ⭐️ 8.0/10

MotherDuck published an analysis showing that DuckDB 2.0 significantly improves performance, specifically achieving up to 90x speedups for recursive Common Table Expressions (CTEs) and 2.4x improvements in async I/O operations on S3. These improvements make DuckDB 2.0 a more efficient analytical database engine for complex data workloads, impacting developers who rely on it for scalable and fast data processing tasks. The release features a new storage format and enhanced query execution models, with notable performance boosts for the VARIANT data type compared to standard JSON text handling.

hackernews · tosh · Oct 10, 18:08 · [Discussion](https://news.ycombinator.com/item?id=50035530)

**Background**: DuckDB is an open-source, embedded analytical database engine designed for fast data processing, similar in concept to SQLite but built for analytics. Recursive CTEs are SQL constructs that allow queries to reference themselves, which are essential for traversing hierarchical data structures in relational databases.

<details><summary>References</summary>
<ul>
<li><a href="https://motherduck.com/blog/why-duckdb-20-is-faster/">Why DuckDB 2.0 is faster - MotherDuck</a></li>
<li><a href="https://duckdb.org/2026/08/17/duckdb-20-highlights">A Preview of DuckDB v2.0</a></li>
<li><a href="https://sesamedisk.com/faster-database-queries-with-duckdb/">Why is DuckDB 2.0 Faster? - Sesame Disk</a></li>

</ul>
</details>

**Discussion**: Community discussion highlights praise for the new C++ extension API, while a user noted that DuckDB's approach is somewhat of a catch-up to modern database designs like Umbra and CedarDB regarding task-based parallelism and async I/O. Another commenter pointed out DuckDB's existing powerful extensions for graph data queries using the DuckPGQ system.

**Tags**: `#duckdb`, `#databases`, `#performance`, `#sql`, `#query-optimization`

---

<a id="item-2"></a>
## [Senate Report Alleges Misleading Claims About AI Data Center Economic Benefits](https://www.tomshardware.com/tech-industry/data-centers/senate-investigation-says-that-some-ai-data-center-claims-are-misleading-senators-question-number-of-permanent-jobs-projects-bring-to-communities-but-companies-refuse-to-divulge-data) ⭐️ 7.5/10

A U.S. Senate investigation concluded that AI data center operators provide misleading information about the costs and economic benefits of their facilities when applying for local permits. The report specifically notes that companies refuse to disclose data that would allow an accurate assessment of their impact on local communities. This regulatory scrutiny will force hyperscalers to increase transparency regarding their footprint, directly impacting how local governments approve massive AI infrastructure projects. It could lead to more stringent zoning requirements and mandatory economic reporting for new data center developments. The core issue is that the cost and benefit figures presented by AI hyperscalers do not reflect the actual, localized economic impact on the communities hosting the sites. This gap has raised significant questions about the transparency of the AI infrastructure boom.

rss · Tom's Hardware · Oct 10, 14:40

**Background**: Hyperscalers are the large cloud service providers building data centers to power artificial intelligence models, which require massive amounts of power and land. Historically, these developers have often presented optimistic economic projections to secure local zoning permits, but the environmental and social costs are frequently understated.

**Tags**: `#AI Infrastructure`, `#Policy & Regulation`, `#Data Centers`, `#Economic Impact`, `#Transparency`

---

<a id="item-3"></a>
## [Ukrainian drones strike Yandex data center, knocking multiple modules offline](https://www.tomshardware.com/tech-industry/data-centers/second-russian-data-center-targeted-by-ukrainian-drones-in-just-two-days-as-yandex-reels-from-another-service-outage-russian-state-media-admits-that-multiple-modules-completely-taken-out) ⭐️ 7.5/10

Ukrainian drones struck a major Yandex data center campus in Kaluga, Russia, causing multiple modules within the 1.4 million square foot facility to go completely offline. This incident significantly disrupts Russian cloud infrastructure and highlights the vulnerabilities of critical tech sites to physical geopolitical conflicts. The attack resulted in a major service outage for Yandex, and Russian state media have admitted that multiple modules at the facility have been completely taken out of service.

rss · Tom's Hardware · Oct 10, 10:30

**Background**: Yandex is one of Russia's largest technology companies and a major provider of internet services and cloud computing infrastructure. The Kaluga campus is one of the largest data centers in Russia, with a footprint of 1.4 million square feet. This strike follows another Ukrainian drone attack on a data center in Sasovo, Russia, just two days prior.

**Tags**: `#data-center`, `#geopolitics`, `#infrastructure`, `#security`, `#cloud-outage`

---

<a id="item-4"></a>
## [Lightbulb Computer Prototype Uses Hand Tracking and Speech for Interaction](https://lightbulbcomputer.com/) ⭐️ 7.0/10

A research prototype named 'The Lightbulb Computer' was released, allowing users to interact with a computer by physically moving lightbulbs while leveraging hand tracking and speech recognition. The system runs on a Mac and uses Apple's built-in vision framework along with a 4K laser projector and a webcam. This project explores novel paradigms for human-computer interaction by combining physical objects with spatial computing, which could inspire future designs for ambient computing and home automation. It addresses the limitations of traditional screen-based interfaces by anchoring digital information to physical spaces. The prototype relies on a specific tech stack including a Mac, a custom projection mapping software, a consumer 4K laser projector, and a basic webcam. The creator emphasizes that the project is primarily a research and design prototype rather than a polished consumer product, with known issues regarding latency in the voice response loop.

hackernews · oskarth · Oct 10, 04:12 · [Discussion](https://news.ycombinator.com/item?id=50029487)

**Background**: Human-computer interaction (HCI) traditionally relies on physical interfaces like keyboards, mice, and touchscreens. Spatial computing and ambient interfaces represent a shift towards systems that understand the user's physical environment, using sensors and AI to map digital data onto real-world objects. Hand tracking refers to the use of computer vision algorithms to detect and track the position and movement of hands in real-time.

**Discussion**: Community reactions are mixed, with the creator highlighting the technical constraints and prototype nature of the device. Users expressed concerns about the constant surveillance aspect of the system, comparing it to a 'jinn' that is always listening, while others praised the concept for solving issues found in XR headsets and the Humane Pin.

**Tags**: `#Human-Computer Interaction`, `#Hardware`, `#Voice Interface`, `#Prototype`, `#Apple`

---

<a id="item-5"></a>
## [Unikernels Revival Proposal in the AI Era](https://ghuntley.com/unikernels/) ⭐️ 7.0/10

The author reflects on the historical challenges of unikernels and proposes their revival in the modern AI era, supported by community discussions on hardware acceleration and specialized cloud hosting options. As traditional isolation mechanisms become less effective against AI-related threats, unikernels offer a minimal attack surface, making them a critical architectural component for future secure AI systems. Notable technical implementations include using Zephyr as a RTOS-based unikernel, leveraging FPGAs like Zynq UltraScale+ for hardware-level isolation, and utilizing micro-VMs such as the BareMetal service for low-resource deployment.

hackernews · ghuntley · Oct 10, 14:27 · [Discussion](https://news.ycombinator.com/item?id=50033357)

**Background**: Unikernels are single-address-space machines that package an application and all its needed dependencies into a single lightweight virtual machine image. Historically, they struggled with complexity and a lack of tooling, which led to their declining popularity in favor of traditional VMs and containers.

**Discussion**: The community shares diverse, high-quality perspectives on advancing unikernel security, including adopting Zephyr for its embedded simplicity, developing AI-coded FPGA (FOGAs) to counter LLM bloat, and deploying micro-VMs via specialized services to minimize attack surfaces in AI architectures.

**Tags**: `#Unikernels`, `#Systems`, `#Security`, `#AI`, `#Hardware`

---

<a id="item-6"></a>
## [Hyper-NA EUV Lithography Set as Next Major Chipmaking Frontier for 2036](https://semiwiki.com/lithography/374764-hyper-na-euv-the-next-frontier-in-chipmaking-could-arrive-in-2036/) ⭐️ 7.0/10

SemiWiki discusses Hyper-NA EUV lithography as the next major frontier in chipmaking, with a projected deployment timeline around 2036. The article highlights that this technology represents a significant step beyond current High-NA systems discussed at recent SPIE conferences in Silicon Valley. The shift to Hyper-NA EUV is crucial for maintaining Moore's Law scaling by enabling the resolution of sub-2nm logic nodes. This evolution impacts the entire semiconductor supply chain, from ASML's tool manufacturing to foundries' process development, defining the capabilities of next-generation AI and high-performance computing chips. The key differentiator is the increased numerical aperture (NA) in the optical system, which allows the tool to collect a steeper cone of light and focus on smaller features than standard or current High-NA systems. Specific challenges include managing the increased cost and complexity of optics, as well as addressing resolution enhancement and contrast fading caused by 3D mask effects.

rss · SemiWiki · Oct 10, 12:00

**Background**: EUV lithography uses 13.5 nm extreme ultraviolet light to print patterns on wafers and is currently the standard for advanced nodes. High-NA EUV is the current next-generation step already being deployed by major foundries for leading-edge logic. Hyper-NA EUV proposes further increasing the numerical aperture beyond the limits of current High-NA tools to push resolution limits even further into the sub-2nm era.

<details><summary>References</summary>
<ul>
<li><a href="https://chipdocket.com/articles/what-is-high-na-euv-lithography-explainer-2026-06-22">High-NA EUV Lithography Explained | ChipDocket</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#lithography`, `#EUV`, `#hardware`, `#manufacturing`

---

<a id="item-7"></a>
## [Jury Deliberation Pending in High-Profile Qualcomm vs. Arm Case](https://www.electronicsweekly.com/news/business/jury-still-out-in-qualcomm-vs-arm-case-2026-10/) ⭐️ 7.0/10

The jury in the Qualcomm vs. Arm legal case returned to the court without a verdict after four hours of deliberation. The jury is scheduled to reassemble next Tuesday to continue deliberating on the case. This high-profile IP litigation in the semiconductor sector is a notable event worth tracking, though the current update is primarily a procedural development. The outcome will have significant implications for Arm's licensing model and the broader chip ecosystem. This procedural delay means that the specific verdict and its legal consequences remain unknown. The case represents a high-stakes legal dispute between major semiconductor industry players.

rss · Electronics Weekly · Oct 10, 07:20

**Background**: Qualcomm and Arm are major players in the semiconductor industry, where Arm typically provides IP licenses for CPU architectures. This ongoing dispute relates to Arm's licensing agreements and Qualcomm's rights to innovate, including its acquisition of Nuvia. Previous web search results indicate that this is part of a broader, high-stakes IP legal battle that has seen varying judicial rulings in its history.

<details><summary>References</summary>
<ul>
<li><a href="https://futurumgroup.com/insights/litigation-sitrep-ongoing-dispute-between-qualcomm-and-arm/">Litigation SITREP: Ongoing Dispute Between Qualcomm and Arm ...</a></li>
<li><a href="https://www.qualcomm.com/news/releases/2025/09/qualcomm-achieves-complete-victory-over-arm-in-litigation-challe">Qualcomm Achieves Complete Victory Over Arm in Litigation ...</a></li>

</ul>
</details>

**Tags**: `#IP Litigation`, `#Semiconductors`, `#Qualcomm`, `#Arm`, `#Legal`

---

<a id="item-8"></a>
## [PS2 Discs Now Load on Jailbroken PS5 Consoles Through PS5SX2 Emulator](https://www.techpowerup.com/353588/ps2-discs-now-load-on-jailbroken-ps5-consoles-through-ps5sx2-emulator) ⭐️ 6.5/10

Developer Sword released a beta update for the PS5SX2 emulator on jailbroken PS5 consoles, enabling physical PS2 discs to be copied to storage and played on the hardware.

rss · TechPowerUp News · Oct 10, 23:43

**Tags**: `#Emulation`, `#Jailbreak`, `#PS5`, `#PS2`, `#Homebrew`

---

<a id="item-9"></a>
## [AMD Raises GDDR6 Prices for GPU Board Partners](https://www.techpowerup.com/353584/amd-reportedly-raises-gddr6-prices-for-board-partners) ⭐️ 6.5/10

AMD has reportedly increased the cost of GDDR6 memory supplied to its board partners, effective from October 1, 2026. This price hike is directly contributing to the recent rise in retail prices for Radeon graphics cards in the Chinese market. This development reflects the broader trend of rising hardware component costs, as memory price hikes directly translate to more expensive graphics cards for consumers. It is significant because it contrasts with the relatively stable GDDR7 pricing from NVIDIA, affecting the competitive dynamics between GPU manufacturers. The timing of the GDDR6 price increase aligns with reported hikes for specific models, such as the RX 9070 and RX 9060 XT 8 GB in China. Notably, AMD is the primary supplier of GDDR6, while NVIDIA is holding its GDDR7 pricing stable after previous hikes earlier in the year.

rss · TechPowerUp News · Oct 10, 17:54

**Background**: AMD sells its GPU chips to add-in board (AIB) partners with memory bundled, meaning the cost of components directly impacts the final retail price of the cards. In contrast, the RX 9070 XT was reportedly not affected by the recent price hike in China. In 2026, AMD has implemented multiple price increases, including hikes tied to rising TSMC wafer costs.

**Tags**: `#AMD`, `#NVIDIA`, `#Hardware Pricing`, `#GDDR6`, `#GPU Market`

---

<a id="item-10"></a>
## [Super Micro smuggling co-conspirator pleads guilty to sending AI chips to China](https://www.tomshardware.com/tech-industry/artificial-intelligence/super-micro-smuggling-co-conspirator-pleads-guilty-to-sending-ai-chips-to-china-broker-admits-breaking-export-control-rules-as-company-co-founder-denies-charges) ⭐️ 6.5/10

A co-conspirator in the Super Micro server smuggling case has pleaded guilty to sending advanced Nvidia AI chips to China in violation of export control rules.

rss · Tom's Hardware · Oct 10, 15:35

**Tags**: `#AI Hardware`, `#Export Controls`, `#Legal`, `#Super Micro`, `#Nvidia`

---

<a id="item-11"></a>
## [AnyPS5 project reaches critical GPU milestone in race to enable running PS5 games natively on PC](https://www.tomshardware.com/video-games/playstation/anyps5-reaches-critical-gpu-milestone-with-100-percent-shader-instruction-coverage-ps5-games-running-natively-on-pc-still-far-off) ⭐️ 6.5/10

The open-source AnyPS5 project has achieved a critical milestone with 100% GPU shader instruction coverage, progressing the goal of running PS5 games natively on PC.

rss · Tom's Hardware · Oct 10, 11:30

**Tags**: `#Emulation`, `#Open-Source`, `#GPU`, `#PlayStation`, `#Hardware`

---

<a id="item-12"></a>
## [Graduates fly 3D-printed jet RC aircraft using standard PETG](https://www.tomshardware.com/3d-printing/worlds-first-3d-printed-remote-control-aircraft-with-a-jet-turbine-takes-flight-aims-for-mach-0-8-to-beat-world-record-for-fastest-model-aircraft-mostly-printed-using-standard-petg-materials) ⭐️ 6.5/10

A team of graduates successfully achieved flight with a 3D-printed remote-controlled aircraft powered by a jet turbine, with the goal of breaking the world record for the fastest model aircraft at Mach 0.8. The aircraft was mostly printed using standard PETG material, a notable engineering challenge given the material's typical temperature limits. This achievement demonstrates that 3D printing can produce functional components for high-performance, jet-powered model aircraft using relatively inexpensive and standard filament materials. It bridges the gap between common consumer 3D printing technologies and advanced small-scale aviation engineering. The target speed of Mach 0.8 makes this a high-stakes attempt at a Guinness World Record for jet-powered RC aircraft. Standard PETG typically remains stable up to 70-100°C, so the team's success implies they utilized clever engineering or structural design to manage the heat generated by the jet turbine during flight.

rss · Tom's Hardware · Oct 10, 10:00

**Background**: Most model aircraft rely on electric motors or propeller-driven engines, while jet turbines provide continuous thrust but operate at high exhaust temperatures. Standard PETG is a common thermoplastic filament used in FDM 3D printing known for its durability and easy extrusion, but its heat deflection temperature is generally limited to around 70-100°C, making it challenging for direct contact with high-heat jet components.

**Tags**: `#3D-Printing`, `#Aviation`, `#Materials-Science`, `#Engineering`, `#World-Record`

---

<a id="item-13"></a>
## [Global PC Shipments Plunge Over 20% Amid AI-Driven Memory Price Surge](https://www.solidot.org/story?sid=85572) ⭐️ 6.3/10

Global PC shipments dropped by 20-21% year-over-year in Q3 2026, driven by a four-fold increase in memory and SSD prices caused by AI demand. This price hike pushed memory costs to 40% of the PC BOM, leading to the market's return to DDR4 hardware. This disruption significantly impacts PC manufacturers and consumers, signaling that the AI hardware boom is creating severe supply chain constraints in the traditional PC sector. It marks a major shift where AI data center demand directly dictates consumer electronics pricing and hardware configurations. A 32GB Corsair DDR5 kit now costs $620 compared to $260 for the same DDR4 kit, prompting manufacturers like Gigabyte to release new DDR4 motherboards for Intel LGA 1700 and AMD AM4. Analysts predict shipments will fall another 24% in Q4 2026 and decline 7% in 2027.

rss · Solidot · Oct 10, 07:53

**Background**: The "AI boom" has led data center customers to aggressively buy up high-bandwidth memory chips, draining manufacturer capacity for consumer-level components. DRAM (Dynamic Random Access Memory) prices are sensitive to these shifts, and historically, when next-generation DDR5 prices are prohibitive, the market often reverts to the previous DDR4 generation to maintain competitiveness.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/10/09/tesla-renames-full-self-driving-to-tesla-assisted-driving-in-europe/">Tesla renames 'Full Self-Driving' to 'Tesla Assisted Driving ...</a></li>
<li><a href="https://hwbusters.com/news/gigabyte-builds-new-am4-motherboards-in-2026-b550-x-gets-wi-fi-7-and-a-60a-drmos-vrm/">Gigabyte Builds New AM4 Motherboards in 2026 — B550 X Gets Wi ...</a></li>
<li><a href="https://www.playground.ru/misc/news/gigabyte_podtverdila_intel_vypustit_novye_protsessory_lga1700_v_nachale_2027_goda_s_podderzhkoj_pamyati_ddr4_i_ddr5-1880402">GIGABYTE подтвердила: Intel выпустит новые процессоры...</a></li>

</ul>
</details>

**Tags**: `#PC Market`, `#Memory Prices`, `#AI Hardware`, `#Supply Chain`, `#DDR4/DDR5`

---

<a id="item-14"></a>
## [Building Custom Decision Models and Lightweight AI Alternatives](https://nishtahir.com/build-your-own-decision-model/) ⭐️ 6.0/10

The post outlines a guide for building custom decision models using lightweight techniques. Community discussion introduces a DIY tool called Jeffy for CPU-based classification and highlights Jev as a recent example of a commercial System 1 decision model. This demonstrates a trend toward minimalist AI tools that allow developers to deploy intelligent decision-making capabilities on resource-constrained environments without heavy framework dependencies. It offers an alternative to large language models for specific classification tasks. Jev is a typed AI model that returns probabilities for predefined questions to drive business rules, while Jeffy is a lightweight tool that runs entirely on CPU. A community user also shared a custom application using a SQLite-vec database and a Qwen embedding model to generate specific content.

hackernews · softwaredoug · Oct 10, 22:50 · [Discussion](https://news.ycombinator.com/item?id=50037949)

**Background**: In software engineering, decision models or classifiers are systems that analyze data to make automated choices. The 'System 1' model refers to fast, intuitive decision-making inspired by dual-process theory, whereas traditional frameworks often require significant computational resources. Lightweight or minimalist AI tools are designed to operate with fewer dependencies and lower hardware requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://aijev.org/">Jev: System One Decision Model Explained | AIJev</a></li>
<li><a href="https://aiindigo.com/blog/beyond-the-framework-lightweight-binaries-and-the-rise-of-minimalist-ai-tools">Beyond the Framework: Lightweight Binaries and the Rise of ...</a></li>

</ul>
</details>

**Discussion**: The overall sentiment is positive about the accessibility of building lightweight AI tools, with users sharing various DIY implementations and comparisons. However, there is some skepticism regarding whether Jev's recent funding valuation is justified by its algorithmic edge, and a minor concern was raised about the statistical validity of adjusting model temperatures post-hoc.

**Tags**: `#machine-learning`, `#algorithm-design`, `#lightweight-ai`, `#programming`

---

<a id="item-15"></a>
## [Receiving a Knuth Reward Check for TAoCP Error](https://www.thomas-huehn.com/knuth-reward-check/) ⭐️ 6.0/10

An author received a reward check from Donald Knuth for identifying a logical error in 'The Art of Computer Programming' where 'infinitely many' was replaced with 'a humongous number' of alphabets. This post documents the personal experience of receiving the check and explains the specifics of the mathematical correction. This story highlights the enduring legacy of Knuth's bug bounty program, which encourages rigorous peer review of one of the most influential computer science texts. It serves as a cultural touchstone for algorithm researchers and emphasizes the value of meticulous scrutiny in mathematical literature. The specific error involved the claim that infinitely many alphabets could be generated from finite parameters, which was corrected to 'a humongous number'. The author noted the irony that the error was found in the very first sentence of the book.

hackernews · Curiositry · Oct 10, 15:47 · [Discussion](https://news.ycombinator.com/item?id=50034081)

**Background**: Donald Knuth is a renowned computer scientist and Turing Award winner who established a reward system in 1968 for finding errors in his publications, starting with 'The Art of Computer Programming'. Initially paid in 2.56 cents per error, the reward later became $2.56, and has since evolved into digital or certificate-based rewards. TAoCP is considered a seminal multi-volume monograph on algorithms that forms the backbone of computer science curricula.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knuth_reward_check">Knuth reward check - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming">The Art of Computer Programming - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members shared a mix of pride and regret regarding their own reward checks, with one user humorously lamenting a lost check and another mentioning a specific past receipt. The discussion also included a detailed validation of the 'infinitely many' error and a note about Knuth personally emailing readers about published articles.

**Tags**: `#algorithms`, `#knuth`, `#taocp`, `#academic`, `#anecdote`

---

<a id="item-16"></a>
## [SoftBank Targets Middle Eastern Investors for Massive AI Fund](https://www.tomshardware.com/tech-industry/artificial-intelligence/softbank-seeks-usd100-billion-for-ai-refined-projects-from-middle-eastern-investors-fund-would-be-used-to-acquire-companies-and-improve-their-operations-using-artificial-intelligence-and-robotics) ⭐️ 5.5/10

SoftBank is actively seeking $100 billion in investment from Middle Eastern investors to establish a massive fund focused on artificial intelligence projects. The capital will be used to acquire companies that currently do not use AI or robotics, with the goal of transforming their operations to increase valuation. This massive investment effort signals a significant shift in how traditional corporations can be optimized through the integration of advanced AI and robotics, acting as a major catalyst for global AI commercialization. By transforming non-AI companies, SoftBank aims to unlock substantial value across various economic sectors. The strategy involves acquiring businesses that have not yet adopted artificial intelligence or robotics and then applying these new technologies to improve their operational efficiency. The target of $100 billion specifically earmarks the funding for projects refined by these advanced automation and machine learning tools.

rss · Tom's Hardware · Oct 10, 15:40

**Background**: SoftBank is a major Japanese conglomerate that has made history as one of the largest investors in the global tech industry, most notably through its investment in Uber. The current strategy differs from building tech companies from scratch; instead, it focuses on 'buying and improving' by infusing existing businesses with AI capabilities. This approach is a response to the growing demand for enterprise-level AI integration to stay competitive in a digital economy.

**Tags**: `#Artificial Intelligence`, `#Robotics`, `#Venture Capital`, `#SoftBank`, `#Industry`

---

<a id="item-17"></a>
## [SPECviewperf 15.0.1 Linux Edition Adds Official Arm Support](https://www.servethehome.com/specviewperf-15-0-1-linux-edition-released-linuxs-key-graphics-benchmark-adds-arm-support/) ⭐️ 5.5/10

SPEC has released version 15.0.1 of SPECviewperf for Linux, introducing official Arm architecture support and updating the benchmark suite. The release also includes a new Blender 3.6 LTS workload. This update enables standardized benchmarking for professional graphics on ARM64 Linux workstations, supporting the growing market of Arm-based server and workstation hardware. It helps bridge the gap for hardware qualification in non-x86 environments. The benchmark measures 3D graphics performance under OpenGL, DirectX, and Vulkan APIs. A commercial license fee of $2,500 was established for vendors to reduce hardware qualification costs.

rss · ServeTheHome · Oct 10, 21:00

**Background**: SPECviewperf is the worldwide standard for measuring graphics performance of professional applications. While it has been widely used on x86 architectures, Arm-based systems have lacked an official, standardized method to validate graphics performance in this benchmark suite.

<details><summary>References</summary>
<ul>
<li><a href="https://gwpg.spec.org/benchmarks/benchmark/specviewperf-15_0_1/">SPECviewperf 15.0.1 - SPEC GWPG</a></li>
<li><a href="https://briefglance.com/articles/bridging-the-gap-linux-and-arm64-secure-a-seat-at-the-graphics-table">Bridging the Gap: Linux and ARM64 Secure a Seat at the ...</a></li>

</ul>
</details>

**Tags**: `#Benchmarking`, `#Arm`, `#Linux`, `#Graphics`, `#SPECviewperf`

---