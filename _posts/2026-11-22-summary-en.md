---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 46 items, 13 important content pieces were selected

---

1. [Claude AI Assists in Formal Verification of Riemann Hypothesis in Lean](#item-1) ⭐️ 9.0/10
2. [US Administration Proposes Ban or Heavy Tax on Overseas Data Centers](#item-2) ⭐️ 8.5/10
3. [Phison Previews Enterprise SSD with Onboard NPU and 64GB Memory](#item-3) ⭐️ 7.5/10
4. [USB Hub Latency Causes 75% Drop in 2.5Gbps Ethernet Speed](#item-4) ⭐️ 7.0/10
5. [PostgreSQL Extensions in Go](#item-5) ⭐️ 7.0/10
6. [Rapidus reportedly struggles to produce working SRAM on its 2nm node, putting 2027 mass production at risk](#item-6) ⭐️ 6.5/10
7. [Defense firm’s EMP ‘Dragon’ weapon fries 51 jam-proof drones simultaneously](#item-7) ⭐️ 6.5/10
8. [Homelabber’s second-gen Optane build uses two RTX 3090s to run 2.8-trillion-parameter Kimi AI model at 3.11 tokens per second](#item-8) ⭐️ 6.5/10
9. [Intel Nova Lake-H Spec Sheet Reveals 4.8 GHz Boost and 25 W TDP](#item-9) ⭐️ 5.5/10
10. [Moore Threads Teases 'Lushan' GPU with Record-Breaking Consumer VRAM](#item-10) ⭐️ 5.5/10
11. [SilverStone HELA 1350Rz ships with three EPS cables for high-power CPUs](#item-11) ⭐️ 5.5/10
12. [Tom's Hardware Reviews HPC Hardware Announcements from SC26](#item-12) ⭐️ 5.5/10
13. [Researchers run 2.2M-parameter LLM on 35-year-old SNES with Super FX 2 acceleration](#item-13) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Claude AI Assists in Formal Verification of Riemann Hypothesis in Lean](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 9.0/10

Researchers used Claude AI to help formalize and verify a proof of the Riemann Hypothesis using the Lean theorem prover. This includes checking that every nontrivial zero of the Riemann zeta function has a real part of ½. This milestone demonstrates a paradigm shift in automated theorem proving, showing that AI can assist in formalizing complex mathematical results and modern mathematical foundations. It raises significant questions about the reliability of AI-generated proofs and the role of independent consistency checkers. The formalization of a large portion of modern mathematics by Claude is a major achievement for mathematical foundations, not just the specific hypothesis. The process involved human experts in the loop to ensure the AI did not exploit bugs in the proof checkers.

hackernews · g-b-r · Nov 21, 14:36 · [Discussion](https://news.ycombinator.com/item?id=50589618)

**Background**: The Riemann Hypothesis is one of the most famous unsolved problems in mathematics, concerning the distribution of prime numbers. Formal verification uses a computer system like Lean to mechanically check the correctness of a mathematical proof. The Lean theorem prover is a system used to express and verify mathematical statements with absolute precision.

<details><summary>References</summary>
<ul>
<li><a href="https://kingy.ai/blog/levent-alpoge-claude-riemann-hypothesis-proof/">Riemann hypothesis proof verified in Lean</a></li>
<li><a href="https://leandojo.org/">AI-Driven Formal Theorem Proving in the Lean Ecosystem</a></li>
<li><a href="https://lean-lang.org/learn/">Learn — Lean Lang</a></li>

</ul>
</details>

**Discussion**: The community debates the reliability of AI-assisted proofs, noting that while independent checkers like con-leche and con-ron have their own consistency proofs, AI could theoretically exploit bugs. There is credit given to human experts for their involvement, and the result is seen as a major step forward for formalizing mathematical foundations.

**Tags**: `#AI`, `#Formal Verification`, `#Lean`, `#Riemann Hypothesis`, `#Mathematics`

---

<a id="item-2"></a>
## [US Administration Proposes Ban or Heavy Tax on Overseas Data Centers](https://www.tomshardware.com/tech-industry/data-centers/trump-wants-to-ban-us-companies-from-building-overseas-data-centers-as-bans-slow-development-also-considers-putting-a-tremendous-tax-in-lieu-of-prohibition) ⭐️ 8.5/10

The U.S. administration has announced a proposal to restrict U.S. companies from building data centers outside of domestic borders. The plan involves either a complete prohibition on overseas construction or the imposition of a significant tax on such international expansion activities. This policy shift would fundamentally alter global cloud infrastructure strategies by forcing AI and tech companies to localize their physical assets within the United States. Such a mandate could significantly increase operational costs and reshape the competitive landscape of global data sovereignty and digital infrastructure development. The proposal explicitly links the development slowdown in the sector to these new restrictions, framing the move as a necessary measure to maintain domestic technological leadership. While a ban is mentioned, the administration is also considering a 'tremendous tax' as a viable alternative to outright prohibition.

rss · Tom's Hardware · Nov 21, 16:29

**Background**: Data sovereignty refers to the principle that data generated within a nation's borders must be governed by its own laws and regulatory frameworks. Historically, the U.S. has favored a market-driven approach to data center growth, allowing global players to build infrastructure wherever is most efficient. This proposed policy represents a sharp deviation from that traditional market-based model.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_sovereignty">Data sovereignty - Wikipedia</a></li>
<li><a href="https://michaelbommarito.com/wiki/datacenters/policy/international/">international datacenter policy comparison | mike bommarito</a></li>

</ul>
</details>

**Tags**: `#AI Infrastructure`, `#Geopolitics`, `#Data Centers`, `#Policy`, `#Tech Industry`

---

<a id="item-3"></a>
## [Phison Previews Enterprise SSD with Onboard NPU and 64GB Memory](https://www.techpowerup.com/355089/phison-previews-an-ssd-that-runs-ai-frameworks-on-its-own-npu) ⭐️ 7.5/10

Phison previewed a computational storage enterprise SSD at Supercomputing 2026 that features an onboard NPU and 64GB of memory running at 130 GB/s. This drive supports running AI frameworks like PyTorch, vLLM, OpenVINO, and llama.cpp directly on the device. This development significantly reduces data transfer overhead for data-heavy AI workloads, potentially cutting host data transfers by 10 to 100 times by processing data locally on the storage device. It represents a major shift in system architecture, allowing AI inference to be offloaded from the main CPU/GPU to the storage layer. The NPU's performance is rated in DMIPS rather than the standard TOPS metric, which is unusual for AI accelerators. Detailed specifications regarding the controller type, interface, form factor, and memory type for this NPU-equipped SSD are currently sparse as it remains a proof-of-concept preview.

rss · TechPowerUp News · Nov 22, 01:23

**Background**: Computational storage (CS) refers to storage devices that incorporate processing power to perform computations on data stored on the device, reducing the need to transfer data to the main host CPU. NPUs (Neural Processing Units) are specialized hardware designed to accelerate machine learning and AI workloads. TOPS (Trillions of Operations Per Second) is a common metric for measuring the peak performance of AI hardware, while DMIPS (Dhrystone Million Instructions Per Second) is an older metric often used for general-purpose CPU performance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.guru3d.com/story/phison-previews-a-computational-ssd-with-an-npu-and-64gb-of-memory/">Phison Previews a Computational SSD With an NPU and 64GB of ...</a></li>
<li><a href="https://www.techspot.com/news/114653-phison-shows-ssd-design-npu-64gb-memory-runs.html">Phison shows an SSD design with an NPU and 64GB of memory ...</a></li>
<li><a href="https://www.tomshardware.com/pc-components/ssds/phison-details-ssd-with-a-built-in-npu-and-64gb-of-memory-that-supports-pytorch-and-llama-cpp-running-on-the-drive-second-design-merges-fast-pslc-cache-and-qlc-capacity-behind-one-controller">Phison details SSD with a built-in NPU and 64GB of memory ...</a></li>

</ul>
</details>

**Tags**: `#Storage`, `#AI Hardware`, `#Computational Storage`, `#SSD`, `#Edge AI`

---

<a id="item-4"></a>
## [USB Hub Latency Causes 75% Drop in 2.5Gbps Ethernet Speed](https://blog.tymscar.com/posts/studiodisplayethernet/) ⭐️ 7.0/10

A user demonstrated that connecting a USB monitor via a hub reduces 2.5Gbps Ethernet download speeds by 75% due to increased network stack latency. This delay prevents the operating system from acknowledging incoming packets quickly enough, causing the network adapter's receive buffer to overflow and drop data. This issue is significant for users of high-bandwidth residential lines (1Gbps+) who use USB peripherals, as it highlights that physical USB topology, not just bandwidth limits, can severely bottleneck modern wired networking performance. It provides a specific, counter-intuitive troubleshooting angle for network engineers and enthusiasts. The performance failure was resolved by using a different network adapter that required less frequent packet acknowledgements. This confirms that the root cause was an interaction between the hub-induced latency and the specific TCP/IP stack's acknowledgement timing, rather than a raw data rate limitation of the USB cable.

hackernews · soheilpro · Nov 21, 10:36 · [Discussion](https://news.ycombinator.com/item?id=50587875)

**Background**: Ethernet connections rely on a system of acknowledgements where the receiving host confirms the arrival of data packets. In high-speed networks, if the host is too busy or delayed by hardware like a USB hub, it fails to send acknowledgements in time, causing the sender to stop and the receiver's internal buffers to fill up, resulting in dropped packets.

<details><summary>References</summary>
<ul>
<li><a href="https://kb.plugable.com/wired-network-adapters/maximizing-25gb-ethernet-performance">Maximizing 2.5Gbps Ethernet Performance - Plugable Knowledge Base</a></li>
<li><a href="https://www.xda-developers.com/usb-ethernet-adapters-are-bottlenecking-your-nas/">USB Ethernet adapters are bottlenecking your NAS - XDA Developers</a></li>
<li><a href="https://www.intel.com/content/www/us/en/support/articles/000005811/ethernet-products.html">Tuning Throughput Performance for Intel® Ethernet Adapters</a></li>

</ul>
</details>

**Discussion**: Community members noted that the bottleneck was actually in the network adapter rather than the monitor itself, and others shared similar bizarre latency-related bugs with other hardware like SFP+ modules. Some users also debated the practical utility of multi-gigabit residential speeds for typical daily tasks.

**Tags**: `#networking`, `#hardware`, `#troubleshooting`, `#usb`, `#performance`

---

<a id="item-5"></a>
## [PostgreSQL Extensions in Go](https://jespino.github.io/gopgext/) ⭐️ 7.0/10

A tool by Valentin Viallet allows developers to write PostgreSQL extensions using the Go programming language, sparking discussion on the suitability of Go for data-layer components.

hackernews · valyala · Nov 21, 17:08 · [Discussion](https://news.ycombinator.com/item?id=50591260)

**Tags**: `#Go`, `#PostgreSQL`, `#Database Extensions`, `#CGO`, `#Systems Programming`

---

<a id="item-6"></a>
## [Rapidus reportedly struggles to produce working SRAM on its 2nm node, putting 2027 mass production at risk](https://www.tomshardware.com/tech-industry/semiconductors/rapidus-reportedly-struggles-to-produce-working-sram-on-its-2nm-node-putting-2027-mass-production-at-risk-company-faces-significant-challenges-using-euv-to-develop-gaa-transistors) ⭐️ 6.5/10

Rapidus faces significant challenges in producing working SRAM on its 2nm GAA node, jeopardizing its 2027 mass production target.

rss · Tom's Hardware · Nov 21, 15:30

**Tags**: `#Semiconductors`, `#Rapidus`, `#2nm`, `#GAA Transistors`, `#Supply Chain`

---

<a id="item-7"></a>
## [Defense firm’s EMP ‘Dragon’ weapon fries 51 jam-proof drones simultaneously](https://www.tomshardware.com/tech-industry/drones/defense-firms-emp-dragon-weapon-fries-51-jam-proof-drones-simultaneously-high-power-electromagnetic-system-relies-on-120-year-old-vacuum-tube-tech-to-defeat-fiber-optic-uavs) ⭐️ 6.5/10

Aselsan's 'Dragon' weapon system utilizes high-power electromagnetic energy to simultaneously disable 51 fiber-optic, jam-proof drones.

rss · Tom's Hardware · Nov 21, 13:54

**Tags**: `#Defense Technology`, `#Counter-Drone`, `#Electromagnetic Pulse`, `#Hardware`, `#Military`

---

<a id="item-8"></a>
## [Homelabber’s second-gen Optane build uses two RTX 3090s to run 2.8-trillion-parameter Kimi AI model at 3.11 tokens per second](https://www.tomshardware.com/tech-industry/artificial-intelligence/homelabbers-second-gen-optane-build-runs-2-8-trillion-parameter-kimi-k3-at-3-11-tokens-per-second-after-adding-two-rtx-3090s-moving-nearly-half-the-model-into-a-ram-drive-boosted-performance-by-41-percent) ⭐️ 6.5/10

A homelabber utilized a second-gen Optane PMem server and two RTX 3090s to run the 2.8-trillion-parameter Kimi K3 model, achieving 3.11 tokens per second by offloading nearly half the model to a RAM drive.

rss · Tom's Hardware · Nov 21, 12:00

**Tags**: `#homelab`, `#optane`, `#LLM-inference`, `#rtx-3090`, `#kimi`

---

<a id="item-9"></a>
## [Intel Nova Lake-H Spec Sheet Reveals 4.8 GHz Boost and 25 W TDP](https://www.techpowerup.com/355088/intel-nova-lake-h-spec-sheet-shows-up-with-a-4-8-ghz-boost-and-25-w-tdp) ⭐️ 5.5/10

A preliminary datasheet from Advantech reveals that Intel's Core Ultra Series 4 "Nova Lake-H" mobile CPU will feature a 16-core design with a 4.8 GHz boost clock and a 25 W TDP. The chip is intended for mobile devices like the 4-inch ASR-A505 single-board computer built for autonomous mobile robots. This spec sheet confirms the existence and target use case for Intel's upcoming mobile processors, indicating a push toward high-performance, low-power computing for specialized applications like robotics. It provides hardware enthusiasts and system designers with early insights into the performance and power constraints of the next-generation Core Ultra mobile lineup. The Advantech datasheet lists an "8P+4E+4LE" core configuration, which likely contains a typo and contradicts previous leaks of a 4P+8E+4LE configuration. The TDP is noted as potentially configurable between 15 W and 25 W according to the document's block diagram.

rss · TechPowerUp News · Nov 21, 23:58

**Background**: Intel's "Nova Lake" is the next generation of its Core Ultra processor lineup, scheduled for release in 2026. The hybrid architecture uses two types of cores: high-performance "P-cores" for heavy tasks and power-efficient "E-cores" for background tasks, a design meant to improve battery life in laptops. TDP, or Thermal Design Power, is the maximum amount of heat a component is expected to generate, which determines how much cooling a system needs to maintain stable performance.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/intel-core-ultra-4-series-16-core-nova-lake-mobile-processor-specifications-leaked/">Intel’s 16-Core Nova Lake-H Leaked Spec Sheet Lists 4.8 GHz ...</a></li>
<li><a href="https://www.intel.com/content/www/us/en/support/articles/000055611/processors.html">Thermal Design Power (TDP) in Intel® Processors</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#CPU`, `#Hardware`, `#Mobile`, `#Leak`

---

<a id="item-10"></a>
## [Moore Threads Teases 'Lushan' GPU with Record-Breaking Consumer VRAM](https://www.techpowerup.com/355084/moore-threads-claims-its-next-gpu-will-break-the-consumer-vram-record) ⭐️ 5.5/10

Moore Threads claims that its next desktop GPU, codenamed Lushan, will hold the largest consumer VRAM capacity on record, a teaser released ahead of its December 2026 Developer Conference. This strategic move positions Moore Threads to compete more aggressively against global giants like NVIDIA in the consumer and local LLM markets. Speculation suggests the card may feature up to 64 GB of VRAM based on the company's previous promises, significantly surpassing the 32 GB on the GeForce RTX 5090.

rss · TechPowerUp News · Nov 21, 20:56

**Background**: Moore Threads is a major Chinese GPU manufacturer known for its MTT S80 card, which features 16 GB of VRAM. The 'Lushan' architecture was first introduced at the initial MUSA Developer Conference and is designed to rival high-end Western GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/gpu-specs/mtt-s80.c4259">Moore Threads MTT S 80 Specs | TechPowerUp GPU Database</a></li>
<li><a href="https://hyperpc.ae/company/news/moore-threads-introduced-lushan-chip">Moore Threads Reveals Huagang Architecture & Lushan GPU ...</a></li>

</ul>
</details>

**Tags**: `#GPU`, `#Moore Threads`, `#VRAM`, `#Hardware`, `#Computer Architecture`

---

<a id="item-11"></a>
## [SilverStone HELA 1350Rz ships with three EPS cables for high-power CPUs](https://www.techpowerup.com/355083/silverstone-equips-hela-1350rz-with-three-eps-cables-citing-nova-lake-s-high-power-demands) ⭐️ 5.5/10

SilverStone has released the HELA 1350Rz, a 1350W ATX 3.1 PSU that includes three 4+4-pin EPS cables instead of the usual two to accommodate Intel's upcoming Nova Lake-S CPUs. The company explicitly cites the high power demands of the new platform as the reason for this extra cable. This hardware update signals that Intel's next-generation desktop CPUs will likely have higher power draw, making it important for enthusiasts and system builders to ensure power delivery stability. It provides a forward-looking specification for those preparing to build systems with the new Z990 motherboard platform. Leaks suggest the flagship 52-core Nova Lake-S variant may have a PL2 power limit of 474W, while Z990 boards allow for three 8-pin EPS connectors. A leaker noted that the third connector is a 'nice to have' feature that aids overclocking but is not strictly required for maximum performance.

rss · TechPowerUp News · Nov 21, 20:27

**Background**: EPS (Enhanced Power Supply) cables are used to deliver power from the PSU to the CPU socket; the 4+4-pin design allows for high-power connections. The 12V-2x6 connector is the ATX 3.1 standard for high-power graphics cards, replacing older standards. PL2 refers to the peak power limit a CPU can briefly exceed during intensive workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/news/16-pin-power-connector-gets-a-much-needed-revision-meet-the-new-12v-2x6-connector">16-Pin Power Connector Gets A Much-Needed... | Tom's Hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Power_supply_unit_(computer)">Power supply unit (computer) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Hardware`, `#PSU`, `#Intel`, `#SilverStone`, `#Nova Lake`

---

<a id="item-12"></a>
## [Tom's Hardware Reviews HPC Hardware Announcements from SC26](https://www.tomshardware.com/tech-industry/supercomputers/this-week-on-toms-hardware-premium-21-november-2026-amd-nvidia-and-more-show-off-the-future-of-high-performance-computing-at-sc26) ⭐️ 5.5/10

Tom's Hardware published a weekly premium newsletter on November 21, 2026, summarizing the hardware announcements made by AMD, Nvidia, and Intel at the Supercomputing 2026 (SC26) conference. The digest covers new devices and developments in high-performance computing (HPC). SC26 is the premier venue for showcasing the next generation of supercomputers and AI infrastructure, making a consolidated digest from a major tech publication useful for quickly tracking the industry's technological direction. This summary helps readers understand how the major hardware vendors are competing in the datacenter space. The SC26 conference was held at McCormick Place in Chicago, with the main event running from November 15 to 20, 2026, and exhibits open from November 17 to 19. Tom's Hardware notes that the newsletter serves as an exhaustive list of everything covered at the event.

rss · Tom's Hardware · Nov 21, 16:00

**Background**: The Supercomputing (SC) conference is a major annual event in the high-performance computing industry where researchers and practitioners discuss the latest advances in hardware, networking, and storage. Vendors like AMD and Nvidia typically unveil new datacenter GPUs and CPUs at these events to compete for market share in AI and scientific computing.

**Tags**: `#HPC`, `#SC26`, `#GPU`, `#AMD`, `#Nvidia`

---

<a id="item-13"></a>
## [Researchers run 2.2M-parameter LLM on 35-year-old SNES with Super FX 2 acceleration](https://www.tomshardware.com/tech-industry/artificial-intelligence/35-year-old-snes-runs-chatgpt-accelerated-with-a-super-fx-2-chip-21-mhz-of-risc-muscle-speeds-2-2m-parameter-chatbot-replies) ⭐️ 5.5/10

Enthusiasts have successfully run a client for a 2.2-million-parameter chatbot model on a 35-year-old Nintendo SNES console. The system was accelerated using a Super FX 2 chip, which provided 21 MHz of RISC processing power for inference tasks. This project demonstrates the extreme limits of model compression and embedded inference by executing AI workloads on retro hardware with negligible memory. It serves as an interesting proof-of-concept for the efficiency of lightweight models on highly constrained embedded systems. The implementation relies on a 16-bit RISC processor designed primarily for graphics rendering to handle mathematical operations for a quantized LLM. The 2.2M parameter size indicates the use of extreme quantization and compression techniques to fit the model into the console's limited memory architecture.

rss · Tom's Hardware · Nov 21, 15:02

**Background**: The Super FX is a custom RISC processor used in the SNES as a graphics coprocessor to render 3D polygons. Large language models are typically heavy software that requires modern hardware; however, techniques like quantization reduce the precision of the model's weights, enabling smaller versions to run on resource-constrained embedded devices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Super_FX">Super FX - Wikipedia</a></li>
<li><a href="https://superfxchip.berrry.app/">Super FX - Revolutionary 16-bit Graphics Coprocessor</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/35-year-old-snes-runs-chatgpt-accelerated-with-a-super-fx-2-chip-21-mhz-of-risc-muscle-speeds-2-2m-parameter-chatbot-replies">35-year-old SNES runs ChatGPT, accelerated with a Super FX 2 chip</a></li>

</ul>
</details>

**Tags**: `#AI/ML`, `#Embedded Systems`, `#Retro Computing`, `#Model Compression`, `#Inference`

---