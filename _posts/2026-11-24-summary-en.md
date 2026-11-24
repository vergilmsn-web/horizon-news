---
layout: default
title: "Horizon Summary: 2026-11-24 (EN)"
date: 2026-11-24
lang: en
---

> From 108 items, 20 important content pieces were selected

---

1. [Why Peak FLOPS is the Wrong Yardstick for Inference Hardware](#item-1) ⭐️ 9.0/10
2. [Windows Server 2028 Removes 32-bit WoW64 Compatibility by Default](#item-2) ⭐️ 8.3/10
3. [Ternary Bonsai 2.5 27B brings agentic coding to consumer Macs](#item-3) ⭐️ 8.0/10
4. [GreyNoise Reports Active Intrusion Campaign Targeting Check Point Security Servers](#item-4) ⭐️ 8.0/10
5. [Hacker News Debates AI Coding Agents Enabling 2035-Tech Now](#item-5) ⭐️ 8.0/10
6. [Cloudflare hides shortcomings of the underlying infrastructure](#item-6) ⭐️ 8.0/10
7. [Moores Lab AI’s Benchmark Push: Measuring Whether AI Can Actually Verify Chips](#item-7) ⭐️ 8.0/10
8. [Why Siemens’ Breker Deal Matters for the Next Generation of AI Chips](#item-8) ⭐️ 8.0/10
9. [JEDEC Publishes JESD209-6: LPDDR6 Standard Updated for AI and Mobile](#item-9) ⭐️ 8.0/10
10. [OpenAI employee found with covert device recording confidential meetings](#item-10) ⭐️ 7.5/10
11. [Songe: Open-source engine for local LLM dreaming and fine-tuning](#item-11) ⭐️ 7.0/10
12. [Quad9 Pulls DNS Service in France Over Legal Blockade Mandate](#item-12) ⭐️ 7.0/10
13. [Acorn and UCLouvain advance buried stressor technology for FDSOI and RF-SOI](#item-13) ⭐️ 7.0/10
14. [US DOJ Seizes $17 Billion and 14,000 Devices in Global Anti-Scam Operation](#item-14) ⭐️ 6.5/10
15. [Frontier AI employees alarmed that unseen Open AI and Anthropic models are too powerful to release, report claims](#item-15) ⭐️ 6.5/10
16. [Reinstated Nvidia CEO Jensen Huang must still face China congressional and Senate Banking committees](#item-16) ⭐️ 6.5/10
17. [Trump pressured Nvidia to bring Jensen back, called into board meeting to push reinstatement, reports claim](#item-17) ⭐️ 6.5/10
18. [Vehicle-to-Grid Faces Significant Practical and Technical Barriers](#item-18) ⭐️ 6.0/10
19. [Vehicle-to-Grid: Great Idea or Unrealistic Dream?](#item-19) ⭐️ 6.0/10
20. [AMD AGESA 1.3.0.1f Patch Limits Ryzen 8000 Max Core Voltage to 1.4V](#item-20) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Why Peak FLOPS is the Wrong Yardstick for Inference Hardware](https://semiwiki.com/semiconductor-manufacturers/vsora/376702-why-peak-flops-is-the-wrong-yardstick-for-inference-hardware/) ⭐️ 9.0/10

The article argues that peak FLOPS is an inadequate metric for evaluating AI inference hardware because inference workloads differ fundamentally from training, requiring a shift in how hardware is benchmarked.

rss · SemiWiki · Nov 24, 14:00

**Tags**: `#AI Hardware`, `#Inference Optimization`, `#Performance Metrics`, `#Semiconductor Industry`

---

<a id="item-2"></a>
## [Windows Server 2028 Removes 32-bit WoW64 Compatibility by Default](https://www.solidot.org/story?sid=85978) ⭐️ 8.3/10

Microsoft has announced that the WoW64 compatibility layer will no longer be installed by default in Windows Server 2028, requiring users to manually enable the optional component to run 32-bit applications. This change is designed to reduce the operating system's footprint and enhance security by blocking 32-bit malicious code. This decision forces developers and IT administrators to migrate legacy 32-bit software to 64-bit environments, addressing a critical gap in enterprise security and maintaining system compatibility. It aligns with the broader industry trend of eliminating outdated software components to reduce vulnerability to modern threats. The WoW64 subsystem has existed in all 64-bit versions of Windows since 2008 to bridge the gap between 32-bit user-mode code and the 64-bit kernel. Microsoft notes that this change will specifically prevent the execution of 32-bit malware, which cannot run on the new operating system without the manually installed optional component.

rss · Solidot · Nov 24, 14:04

**Background**: WoW64 (Windows 32-bit on Windows 64-bit) is a translation and redirection layer that allows 32-bit applications to coexist with the 64-bit kernel. It uses a set of DLLs like Wow64.dll to intercept kernel calls and create a virtual environment for older software. Windows Server's last native 32-bit version was released in 2008, meaning 32-bit support has relied on this compatibility layer for over 15 years.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WoW64">WoW64 - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/win32/winprog64/wow64-implementation-details">WOW64 Implementation Details - Win32 apps | Microsoft Learn WOW64 and cross-architecture compatibility | Windows Internals Windows on Windows - Wikipedia Running 32-bit Applications - Win32 apps | Microsoft Learn WOW64 and cross-architecture compatibility: Windows internals ... WoW64: Running 32-bit Processes on 64-bit Windows</a></li>
<li><a href="https://en.wikipedia.org/wiki/Windows_on_Windows">Windows on Windows - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Windows Server`, `#System Administration`, `#Security`, `#Bioengineering`, `#Pharmacology`

---

<a id="item-3"></a>
## [Ternary Bonsai 2.5 27B brings agentic coding to consumer Macs](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 8.0/10

PrismML released Ternary Bonsai 2.5 27B, a ternary quantized LLM that executes agentic coding tasks on consumer hardware like the Mac M5 Pro. It achieves 22-25 tokens/s speed and supports up to 128k context in memory. This release significantly lowers the hardware barrier for local AI coding assistants by enabling complex agentic tasks on mainstream laptops without expensive GPU clusters. It marks a shift toward highly accessible, low-bit AI models that prioritize real-world utility over raw benchmark scaling. Ternary quantization restricts model weights to three values (-1, 0, +1), resulting in a 1.58-bit precision footprint that drastically reduces memory usage. While it scores equivalently to frontier models on SWE-bench, practical performance depends on context limits and prefill speed rather than just raw generation speed.

hackernews · b0m · Nov 24, 20:08 · [Discussion](https://news.ycombinator.com/item?id=50633922)

**Background**: Standard LLMs typically use 16-bit floating point weights, which makes them memory-intensive and hard to run on consumer hardware. Ternary LLMs (1.58-bit) represent a form of extreme quantization that compresses the model size to fit within tight memory budgets. Agentic coding refers to AI systems that can independently perform multi-step tasks such as writing code, running tests, and fixing errors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/1.58-bit_large_language_model">1.58-bit large language model - Wikipedia</a></li>
<li><a href="https://prismml.com/">PrismML — Concentrating intelligence</a></li>
<li><a href="https://arxiv.org/abs/2406.07177">[2406.07177] TernaryLLM: Ternarized Large Language Model</a></li>

</ul>
</details>

**Discussion**: Community members are impressed by the 128k context window and prefill speeds, confirming its usefulness for agentic coding. However, there is debate about the validity of SWE-bench scores for small models and a need for direct hardware comparisons against other popular 1B-10B quantized models. Some users also inquired about specific hardware acceleration methods beyond FPGAs.

**Tags**: `#LLM`, `#LocalAI`, `#Quantization`, `#AgenticCoding`, `#PrismML`

---

<a id="item-4"></a>
## [GreyNoise Reports Active Intrusion Campaign Targeting Check Point Security Servers](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) ⭐️ 8.0/10

GreyNoise has identified an active intrusion campaign targeting Check Point Security Management Servers across multiple organizations. The attack involves exploiting vulnerabilities to reverse-engineer a weak Pseudo-Random Number Generator and forge administrative session cookies. Compromising the security tooling of a major enterprise vendor like Check Point allows attackers to pivot into sensitive network environments. This significantly lowers the barrier for attackers to access critical infrastructure and customer data. While the summary details Check Point exploitation, web search results associate this PRNG state-reconstruction and session forgery technique with a critical flaw in Rejetto HFS (CVE-2026-61500). Attacker IP infrastructure spans 99 addresses, and the campaign is reportedly assisted by LLMs.

hackernews · louiereederson · Nov 24, 16:32 · [Discussion](https://news.ycombinator.com/item?id=50630594)

**Background**: Security Management Servers are highly sensitive targets because they often hold the keys to managing entire network environments. PRNGs are computer algorithms that generate sequences of numbers mimicking randomness, and their internal state can sometimes be predicted if outputs are observed. Forging session cookies allows attackers to impersonate legitimate users without needing to discover or exploit actual authentication flaws.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/hackers-compromise-check-point-servers-in-22-organizations/">Hackers compromise Check Point Servers in 22 organizations</a></li>
<li><a href="https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html">Attackers Target Rejetto HFS Flaw That Enables Admin Session ...</a></li>

</ul>
</details>

**Discussion**: Commenters express concern about the growing threat of AI-driven swarms of cybercriminals. There is also technical debate over how attackers initially bypassed security, and frustration that JavaScript's Math.random() remains insecure for security-critical session management.

**Tags**: `#cybersecurity`, `#check-point`, `#intrusion-campaign`, `#prng`, `#session-cookie-forgery`

---

<a id="item-5"></a>
## [Hacker News Debates AI Coding Agents Enabling 2035-Tech Now](https://fzakaria.com/2026/11/23/2035-came-early) ⭐️ 8.0/10

A high-engagement Hacker News discussion analyzed by F. Zakaria confirms that AI coding agents have allowed solo developers to build complex systems like OS kernels, effectively bringing forward capabilities previously predicted for 2035. The community validated this shift through examples of individuals successfully using LLM orchestration to create previously unattainable software milestones. This represents a significant paradigm shift in software engineering where LLM orchestration removes the historical barrier of team size, enabling individuals to execute high-complexity projects. It impacts the broader industry by forcing a re-evaluation of technical career trajectories and traditional software development methodologies. The capability to build complex systems now relies heavily on LLM orchestration—coordinating multiple AI models—rather than purely manual coding, as seen in a community member's 100-hour, two-month project to create a bare-metal OS. While some developers are rushing to release their agent-built work, the approach is not without skepticism regarding the fundamental utility and limits of web-based languages.

hackernews · setheron · Nov 24, 06:30 · [Discussion](https://news.ycombinator.com/item?id=50624497)

**Background**: The term '2035' refers to a technological singularity concept popularized by Ray Kurzweil, predicting a future where machine intelligence matches or surpasses human cognitive limits. Currently, software development still predominantly relies on human engineers writing code manually. LLM orchestration is the technical process of managing and coordinating Large Language Models to act as autonomous agents that can plan and execute complex multi-step coding tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technological_singularity">Technological singularity - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/llm-orchestration">What is LLM orchestration? - IBM</a></li>
<li><a href="https://theaiagentindex.com/resources/guides/ai-coding-agents-vs-traditional-ides">AI Coding Agents vs Traditional IDEs: When to Use Each (2026)</a></li>

</ul>
</details>

**Discussion**: The discussion reveals a mix of excitement and skepticism, with developers sharing personal experiences of building OS kernels and other complex software by prompting AI rather than writing code by hand. While some highly praise the 'software heros' who pioneered these methods, others remain unconvinced, drawing parallels to early Mozilla claims that JavaScript would replace native operating systems. There is also a notable emotional sentiment among engineers who had to adapt to the new, agent-driven development landscape.

**Tags**: `#AI Coding Agents`, `#Hacker News`, `#Software Engineering`, `#LLM Orchestration`, `#Operating Systems`

---

<a id="item-6"></a>
## [Cloudflare hides shortcomings of the underlying infrastructure](https://charlie.fish/posts/2026/11/what-cloudflare-doesnt-tell-you/) ⭐️ 8.0/10

A technical analysis exposing the hidden infrastructure shortcomings and configuration complexities of Cloudflare's CDN service, supplemented by a high-quality community debate on security and reliability trade-offs.

hackernews · fishcharlie · Nov 24, 19:03 · [Discussion](https://news.ycombinator.com/item?id=50632883)

**Tags**: `#Cloudflare`, `#Network Security`, `#CDN`, `#DevOps`, `#TLS`

---

<a id="item-7"></a>
## [Moores Lab AI’s Benchmark Push: Measuring Whether AI Can Actually Verify Chips](https://semiwiki.com/eda/moores-lab-ai/375754-moores-lab-ais-benchmark-push-measuring-whether-ai-can-actually-verify-chips/) ⭐️ 8.0/10

Moores Lab AI launches a benchmark initiative focused on evaluating the ability of AI systems to verify the correctness of chip designs, shifting the focus from code generation speed to functional accuracy.

rss · SemiWiki · Nov 24, 18:00

**Tags**: `#AI`, `#Semiconductors`, `#EDA`, `#Verification`, `#Hardware`

---

<a id="item-8"></a>
## [Why Siemens’ Breker Deal Matters for the Next Generation of AI Chips](https://semiwiki.com/eda/376542-why-siemens-breker-deal-matters-for-the-next-generation-of-ai-chips/) ⭐️ 8.0/10

Siemens' acquisition of Breker aims to solve critical system-level integration and power-state bugs that prevent next-generation AI chips from performing reliably, even when individual components pass standard tests.

rss · SemiWiki · Nov 24, 16:00

**Tags**: `#Semiconductors`, `#AI Hardware`, `#Chip Verification`, `#Siemens`, `#EDA`

---

<a id="item-9"></a>
## [JEDEC Publishes JESD209-6: LPDDR6 Standard Updated for AI and Mobile](https://www.electronicsweekly.com/news/products/memory/jedec-updates-lpddr6-to-address-mobile-and-ai-memory-performance-2026-11/) ⭐️ 8.0/10

The Solid State Technology Association, JEDEC, has released the JESD209-6 standard, which is the latest revision of the Low Power Double Data Rate 6 (LPDDR6) specification. This update is specifically designed to address and enhance memory performance for both mobile devices and AI workloads. This standard defines the next generation of memory performance envelopes, which is critical for engineers and architects designing mobile and edge AI hardware. It enables future devices to handle demanding AI tasks while maintaining the power efficiency required for battery-powered platforms. The new standard is designated as JESD209-6, representing a significant update to the LPDDR6 specification. The content does not provide specific numerical figures for bandwidth or latency improvements, but emphasizes the focus on AI-specific performance metrics.

rss · Electronics Weekly · Nov 24, 15:56

**Background**: JEDEC is the global standards body that defines specifications for various types of memory, including DRAM and NAND. LPDDR, or Low Power DDR, is a class of memory designed to reduce power consumption in mobile and portable electronics. As AI workloads move to mobile devices, new memory standards are required to support higher data throughput without excessive power draw.

**Tags**: `#LPDDR6`, `#JEDEC`, `#Memory Standards`, `#AI Hardware`, `#Mobile Technology`

---

<a id="item-10"></a>
## [OpenAI employee found with covert device recording confidential meetings](https://www.tomshardware.com/tech-industry/artificial-intelligence/saudi-openai-eavesdropper-who-bugged-company-office-had-hundreds-of-private-recordings-was-in-frequent-communication-with-saudi-government-perp-had-dozens-of-recordings-of-discussions-of-trade-secrets) ⭐️ 7.5/10

Prosecutors discovered a covert listening device installed by a Saudi employee inside an OpenAI conference room. This device recorded hundreds of private conversations involving corporate trade secrets, which were shared with the Saudi government. This incident represents a severe state-sponsored espionage breach that puts critical AI intellectual property at risk. It underscores the growing vulnerability of high-value tech companies to targeted corporate espionage by foreign entities. The employee maintained frequent communication with the Saudi government while possessing dozens of recordings of sensitive discussions. The covert device was specifically placed in a conference room to monitor internal company communications.

rss · Tom's Hardware · Nov 24, 16:30

**Background**: In the high-stakes AI industry, corporate espionage is a major concern as competitors seek to steal proprietary algorithms and strategic plans. While most corporate security focuses on digital firewalls, physical access to office spaces and meeting rooms remains a critical vulnerability for sensitive information. OpenAI, as a leading developer of artificial intelligence, is a primary target for state actors seeking to advance their own national AI capabilities.

**Tags**: `#AI Security`, `#Espionage`, `#OpenAI`, `#Data Breach`

---

<a id="item-11"></a>
## [Songe: Open-source engine for local LLM dreaming and fine-tuning](https://github.com/sous-labs/songe) ⭐️ 7.0/10

Songe is an open-source tool released by Sous Labs that uses a machine's idle cycles to iteratively train local Large Language Models. It operates by replaying corrected user interactions in a 'dreaming' process to improve model performance. This project lowers the barrier to continuous model improvement for individual developers by leveraging existing hardware without requiring dedicated data centers. It aligns with industry trends toward on-device AI and sustainable resource utilization. Before training, Songe measures the device's available learning capacity to ensure the model fits in memory. The system only applies new model versions if they successfully pass verification checks.

hackernews · bluepeter · Nov 24, 15:03 · [Discussion](https://news.ycombinator.com/item?id=50629231)

**Background**: Local Large Language Models are often run on consumer hardware with limited resources, making traditional fine-tuning difficult without powerful GPUs. Concepts like 'sleep' or 'dreaming' phases in AI research propose that models can consolidate new data and correct errors during periods of inactivity, similar to how biological brains process memory.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sous-labs/songe">GitHub - sous-labs/ songe : A training engine for your local model...</a></li>
<li><a href="https://souslabs.ai/songe">About Songe · Sous Labs</a></li>

</ul>
</details>

**Discussion**: The community is highly interested in the practical implications, with users asking about the quantitative improvement per epoch and specific hardware requirements for modest machines. There is also significant discussion regarding the potential for creating distributed computing networks, similar to SETI@home, to leverage collective idle resources.

**Tags**: `#local-llm`, `#fine-tuning`, `#open-source`, `#distributed-computing`, `#python`

---

<a id="item-12"></a>
## [Quad9 Pulls DNS Service in France Over Legal Blockade Mandate](https://quad9.net/news/blog/quad9-service-deactivation-in-france/) ⭐️ 7.0/10

The non-profit DNS provider Quad9 deactivated its public resolvers for French users on November 24, 2026, to avoid complying with a legal order to block specific domains. This event highlights the conflict between legal censorship mandates and the integrity of public DNS infrastructure, serving as a significant warning for digital sovereignty and user privacy in the EU. Users can verify the service refusal via DiG, which returns a 'REFUSED' status containing an Extended DNS Error (EDE) code indicating prohibited service due to French legal constraints.

hackernews · farrokhi · Nov 24, 08:33 · [Discussion](https://news.ycombinator.com/item?id=50625384)

**Background**: Quad9 is a global non-profit DNS resolver that provides free, trusted DNS services to individuals, businesses, and governments. The legal order that triggered the withdrawal was issued by a French court to combat unauthorized sports broadcasts and piracy.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/quad9-withdrawal-from-france/">Quad9’s withdrawal from France: A canary in the coal mine</a></li>
<li><a href="https://cyberinsider.com/quad9-to-leave-france/">Quad9 to leave France after court orders piracy-related DNS ...</a></li>
<li><a href="https://techstackups.com/articles/quad9-leaves-france-dns-blocking/">Quad9 Is Leaving France: Why DNS Resolvers Are the Wrong ...</a></li>

</ul>
</details>

**Discussion**: The community immediately began sharing open DNS proxy configurations that cache and forward requests to bypass the localized block, supporting DoH, DoT, and IPv4/IPv6. Additionally, users shared technical DiG outputs to confirm the refusal code and noted that the restriction also affects certain German servers.

**Tags**: `#DNS`, `#Privacy`, `#Infrastructure`, `#Legal`, `#Networking`

---

<a id="item-13"></a>
## [Acorn and UCLouvain advance buried stressor technology for FDSOI and RF-SOI](https://www.electronicsweekly.com/news/business/research-boost-for-fdsoi-and-rf-soi-2026-11/) ⭐️ 7.0/10

Researchers at Acorn Technologies and UCLouvain have demonstrated advancements in buried stressor technology for FDSOI and RF-SOI semiconductor platforms. The collaboration has successfully applied this specific technology to improve these silicon-on-insulator processes. Advancing buried stressor technology in these platforms allows for the integration of complex devices with improved performance and reduced power consumption. This is particularly significant for RF front-end integration where RF-SOI is widely used in consumer electronics and telecommunications. The work involves Acorn Technologies, a semiconductor IP company based in La Jolla near San Diego, and Prof Jean-Pierre Raskin from UCLouvain. The specific technology developed is referred to as the Acorn Buried Stressor.

rss · Electronics Weekly · Nov 24, 06:12

**Background**: FDSOI (Fully Depleted Silicon on Insulator) and RF-SOI (Radio Frequency Silicon on Insulator) are advanced semiconductor fabrication technologies where a thin silicon layer sits on an insulating layer, unlike standard bulk CMOS. Buried stressor technology involves engineering subsurface layers to manage strain, which can optimize device properties and enable better integration of specialized components.

<details><summary>References</summary>
<ul>
<li><a href="https://gf.com/technologies/cmos/fdx-fd-soi/">FDX™ FD-SOI technology | GlobalFoundries</a></li>
<li><a href="https://www.everythingrf.com/community/what-is-rf-soi">What is RF SOI? - everything RF RF-SOI technology | GlobalFoundries RF-SOI - STMicroelectronics The Ultimate Guide to RF-SOI - AnySilicon SOI in Integrated Circuits — CMOS, RF, MEMS & Photonics SOI Wafers Explained: Pros, Cons, and Applications</a></li>

</ul>
</details>

**Tags**: `#Semiconductor`, `#FDSOI`, `#RF-SOI`, `#Research`, `#IP`

---

<a id="item-14"></a>
## [US DOJ Seizes $17 Billion and 14,000 Devices in Global Anti-Scam Operation](https://www.tomshardware.com/tech-industry/cyber-security/us-doj-touts-largest-ever-crackdown-on-scammers-across-the-globe-as-it-seizes-14-000-devices-and-usd17-billion-in-illicit-funds-operation-results-in-800-defendants-and-frees-2-200-forced-laborers) ⭐️ 6.5/10

The US Department of Justice announced that its largest-ever anti-scam operation has resulted in the seizure of 14,000 devices and $17 billion in illicit funds, with over 800 defendants charged and 2,200 forced laborers freed. The action has specifically recovered $8 billion in intended victim losses. This operation demonstrates the US government's intensified effort to combat the transnational financial fraud that plagues the global digital economy. The massive scale of assets seized highlights the significant threat posed by cyber-enabled scams to international victims and financial systems. Notable outcomes of the crackdown include the recovery of $8 billion in intended victim losses and the liberation of 2,200 forced laborers who were likely exploited by the illicit networks.

rss · Tom's Hardware · Nov 24, 22:30

**Background**: The surge in global cyber scams has become a major concern, often involving sophisticated financial crimes and human trafficking networks that span multiple jurisdictions. The US DOJ coordinates such operations to disrupt these cross-border criminal activities and recover stolen assets to mitigate harm to global victims.

**Tags**: `#Cybersecurity`, `#Law-Enforcement`, `#Anti-Fraud`, `#Policy`

---

<a id="item-15"></a>
## [Frontier AI employees alarmed that unseen Open AI and Anthropic models are too powerful to release, report claims](https://www.tomshardware.com/tech-industry/artificial-intelligence/frontier-ai-employees-alarmed-that-unseen-open-ai-and-anthropic-models-are-too-powerful-to-release-report-claims-worry-spreads-that-executives-are-out-of-touch-with-severity-of-risks-will-choose-profit-over-safety) ⭐️ 6.5/10

Reports suggest that employees at OpenAI and Anthropic are concerned that unreleased frontier models are too powerful and pose significant risks if released without adequate safety controls, with executives prioritizing profit.

rss · Tom's Hardware · Nov 24, 21:00

**Tags**: `#AI Safety`, `#OpenAI`, `#Anthropic`, `#Tech Industry`, `#Model Risks`

---

<a id="item-16"></a>
## [Reinstated Nvidia CEO Jensen Huang must still face China congressional and Senate Banking committees](https://www.tomshardware.com/tech-industry/policy/reinstated-nvidia-ceo-jensen-huang-must-still-face-china-congressional-and-senate-banking-committees-senators-and-representatives-demand-answers-from-nvidia-ceo-on-national-security-threats-and-export-controls) ⭐️ 6.5/10

Nvidia CEO Jensen Huang is scheduled to testify before US congressional committees on December 1 and 3 regarding national security concerns and export control enforcement in China.

rss · Tom's Hardware · Nov 24, 16:00

**Tags**: `#Nvidia`, `#Geopolitics`, `#Export Controls`, `#AI Industry`, `#Semiconductors`

---

<a id="item-17"></a>
## [Trump pressured Nvidia to bring Jensen back, called into board meeting to push reinstatement, reports claim](https://www.tomshardware.com/tech-industry/policy/trump-pressured-nvidia-to-bring-jensen-back-called-into-board-meeting-to-push-reinstatement-reports-claim-president-concerned-over-falling-stock-prices-with-huangs-return-reversing-slide) ⭐️ 6.5/10

Reports indicate that President Donald Trump allegedly intervened in Nvidia's corporate governance by pressuring the board to reinstate Jensen Huang to stabilize the company's falling stock prices.

rss · Tom's Hardware · Nov 24, 13:45

**Tags**: `#Nvidia`, `#Jensen Huang`, `#US Politics`, `#Market Regulation`, `#Tech Industry`

---

<a id="item-18"></a>
## [Vehicle-to-Grid Faces Significant Practical and Technical Barriers](https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream-part-2/) ⭐️ 6.0/10

This article explores the technical and practical challenges hindering the widespread adoption of Vehicle-to-Grid systems. It highlights concerns related to battery degradation, grid infrastructure, charging access, and user convenience. Addressing these critical barriers is essential for the future of smart grid integration and renewable energy management. The analysis is significant for automakers and energy providers evaluating the commercial viability of two-way charging technologies. The analysis specifically points out that battery health degradation and the lack of robust grid infrastructure are the primary technical bottlenecks. Furthermore, the economic costs involved in the required equipment and the practical inconvenience for EV drivers are major adoption hurdles.

rss · EE Times · Nov 24, 11:53

**Background**: Vehicle-to-Grid (V2G) technology allows electric vehicles to send excess power back to the electrical grid, acting as mobile energy storage. While it can help stabilize the grid and integrate renewable energy, it requires specialized bidirectional charging infrastructure that is currently rare.

**Tags**: `#Vehicle-to-Grid`, `#Energy Systems`, `#Battery Technology`, `#Smart Grid`, `#Automotive Electronics`

---

<a id="item-19"></a>
## [Vehicle-to-Grid: Great Idea or Unrealistic Dream?](https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream/) ⭐️ 6.0/10

This article critically examines the potential of Vehicle-to-Grid technology, arguing that user behavior and the 'human factor' may limit its effectiveness despite its technical promise.

rss · EE Times · Nov 24, 08:40

**Tags**: `#Vehicle-to-Grid`, `#Energy Systems`, `#Infrastructure`, `#Sustainability`, `#Power Electronics`

---

<a id="item-20"></a>
## [AMD AGESA 1.3.0.1f Patch Limits Ryzen 8000 Max Core Voltage to 1.4V](https://www.techpowerup.com/355153/amd-agesa-1-3-0-1f-patch-arrives-to-limit-max-vcore-on-ryzen-8000-series) ⭐️ 5.5/10

AMD has released AGESA 1.3.0.1f Patch A, introducing a 1.4V maximum core voltage limit for specific Ryzen 8000-series desktop APUs. Motherboard manufacturers like ASUS and MSI are distributing BIOS updates to implement this restriction and improve memory training visibility. This update is significant for the stability of systems using Ryzen 8000-series APUs, as capping the voltage at 1.4V helps prevent hardware degradation and system instability caused by excessive power draw. It ensures long-term reliability for users of these specific processors on the AM5 platform. The patch also adds additional POST codes to enhance visibility into memory training, allowing users to better differentiate between normal initialization and unresponsive states. The voltage limit applies specifically to select Ryzen 8000-series desktop APUs, and manual overclocking beyond this ceiling may be affected or restricted.

rss · TechPowerUp News · Nov 24, 13:31

**Background**: AGESA, or AMD Generic Encapsulated Software Architecture, is a procedure library used by motherboard manufacturers to perform Platform Initialization for AMD processors. It acts as a bridge between the CPU's firmware and the mainboard's BIOS, governing how hardware components are initialized and managed during the boot process. The Ryzen 8000 series refers to AMD's recent generation of APUs that integrate CPU and GPU on a single package.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AGESA">AGESA - Wikipedia</a></li>
<li><a href="https://www.techpowerup.com/355153/amd-agesa-1-3-0-1f-patch-arrives-to-limit-max-vcore-on-ryzen-8000-series">AMD AGESA 1.3.0.1f Patch Arrives to Limit Max vCore on Ryzen ...</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#Ryzen 8000`, `#BIOS`, `#AGESA`, `#Hardware`

---