---
layout: default
title: "Horizon Summary: 2026-11-11 (EN)"
date: 2026-11-11
lang: en
---

> From 96 items, 20 important content pieces were selected

---

1. [AMD Unveils Zen 6 and Zen 6c CPU Architectural Details](#item-1) ⭐️ 9.3/10
2. [IBM Unveils Nighthawk r3 Processor and 1,000-Qubit Roadmap](#item-2) ⭐️ 8.5/10
3. [In Memoriam: Passing of Tim Peters, Python Core Developer and Author of the Zen of Python](#item-3) ⭐️ 8.0/10
4. [Google SWE points 48 AI agents at NASA Lidar, finds unmapped Maya pyramid in 72h](#item-4) ⭐️ 8.0/10
5. [Using voltage glitching to unleash the A100 in my mining card](#item-5) ⭐️ 8.0/10
6. [NVHBM: Can Custom HBM Change Who Builds the Memory Stack?](#item-6) ⭐️ 8.0/10
7. [STMicros’ Maria Heriz on Moving All Its MCUs to One STM32 Platform](#item-7) ⭐️ 8.0/10
8. [Credo Unveils 1.6T ZeroFlap ALC for Reliable AI Interconnects at OCP 2026](#item-8) ⭐️ 8.0/10
9. [Google Cloud integrates TPU 8i Max with Arm Neoverse Axion processors](#item-9) ⭐️ 8.0/10
10. [Imec Establishes Silicon Interposer Flows in NanoIC Pilot Line](#item-10) ⭐️ 8.0/10
11. [Linux memory management reviewer steps down over flood of AI slop patches](#item-11) ⭐️ 7.5/10
12. [AMD MEXT Achieves 95% Performance with Half DRAM on 145 Servers](#item-12) ⭐️ 7.5/10
13. [Musk's xAI faces Texas approval for $24B gas-powered AI data center](#item-13) ⭐️ 7.5/10
14. [Ukrainian drone operations squeezed by fiber optic cable shortage triggered by AI data center buildouts](#item-14) ⭐️ 7.5/10
15. [AWS Finally Built Its Own AWS Emulator](#item-15) ⭐️ 7.0/10
16. [Can a Linear Program Do Weight-Space Programming?](#item-16) ⭐️ 7.0/10
17. [Pharo in the Browser with WebAssembly](#item-17) ⭐️ 7.0/10
18. [SemiWiki Explains the Role of Silicon Substrates and SOI in Transistors](#item-18) ⭐️ 7.0/10
19. [Mobilint and Chips&Media Mass-Produce Edge AI Chips for Humanoid Robots](#item-19) ⭐️ 7.0/10
20. [Norway deploys 3,500 AI laser drones to protect salmon](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [AMD Unveils Zen 6 and Zen 6c CPU Architectural Details](https://www.solidot.org/story?sid=85852) ⭐️ 9.3/10

AMD disclosed the Zen 6 and Zen 6c CPU microarchitectures, revealing a 3-3.5ns branch misprediction penalty, dual decode clusters, and a 27% overall IPC uplift for server workloads. The new design introduces a significant architectural differentiation between the high-frequency Zen 6 core and the high-density, wider out-of-order execution Zen 6c core. This major architectural pivot restructures AMD's core designs significantly, similar to the leap from Zen 1 to Zen 2, setting a new performance baseline for next-generation CPUs. It impacts high-performance computing, cloud services, and consumer desktops by delivering substantially higher instructions per clock and expanded cache structures. Zen 6 features 12-core CCDs with 48MB of L3 cache, while the high-density Zen 6c uses 32-core CCDs with 128MB of L3 cache. Integer multiplication units were reduced from three to two to save silicon area, though the wider execution window improved 64-bit addition throughput to 5.96 per cycle.

rss · Solidot · Nov 11, 06:25

**Background**: AMD uses Core Complex Dies (CCDs) to package its CPU cores, which connect to a central I/O die via high-speed links. Zen 5 previously offered classic and dense cores that were nearly identical in architecture but differed in cache and core count. The newer TAGE-based branch predictor and larger out-of-order execution windows represent fundamental shifts in how complex integer and floating-point instructions are handled.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/review/amd-zen-6-technical-deep-dive/">AMD Zen 6 Technical Deep Dive - TechPowerUp</a></li>
<li><a href="https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast">AMD’s Zen 6 Family: Feeding the Beast - by George Cozma</a></li>
<li><a href="https://wccftech.com/amd-zen-6-architecture-ipc-cores-memory-performance-epyc-venice/">AMD Zen 6 Architecture Brings A Phenomenal 27% IPC Increase...</a></li>

</ul>
</details>

**Tags**: `#CPU Architecture`, `#AMD Zen 6`, `#Microarchitecture`, `#Branch Prediction`, `#Computer Hardware`

---

<a id="item-2"></a>
## [IBM Unveils Nighthawk r3 Processor and 1,000-Qubit Roadmap](https://www.techpowerup.com/354696/ibm-announces-quantum-nighthawk-r3-processor-plans-to-scale-beyond-1-000-qubits-in-2027) ⭐️ 8.5/10

IBM has announced its next-generation Quantum Nighthawk r3 processor, engineered to execute 10,000 quantum operations across 520 qubits. The company further plans to link two of these units into a single 1,040-qubit system by 2027. This milestone moves IBM's quantum architecture toward the complexity threshold required for industry-relevant problem solving while maintaining competitive execution speeds. Scaling beyond 1,000 qubits is a critical step for enabling applications that demand millions to billions of samples. The Nighthawk r3 design prioritizes the ability to run deep quantum circuits of 10,000 operations to ensure computations finish within practical timeframes and at reasonable costs. It maintains the high-speed performance profile of the current generation Nighthawk system while increasing qubit count and circuit depth.

rss · TechPowerUp News · Nov 11, 16:18

**Background**: Quantum computers operate by sampling the results of quantum circuits, where each run returns a single result that requires statistical aggregation over millions of trials. Unlike some trapped-ion competitors, IBM relies on superconducting qubits which offer much higher execution speeds, allowing for faster sample generation.

<details><summary>References</summary>
<ul>
<li><a href="https://thequantuminsider.com/2026/11/11/ibm-nighthawk-r3-processor-520-programmable-qubits/">IBM Plans 1,040-Qubit Quantum System with Next-Generation ...</a></li>
<li><a href="https://www.fool.com/investing/2026/10/26/ibm-continues-to-plug-along-its-quantum-computing/">IBM Continues to Plug Along, but Its Quantum ... | The Motley Fool</a></li>
<li><a href="https://www.ibm.com/think/news/ibm-goes-big-keep-quantum-computers-cold">IBM goes big to keep quantum computers cold | IBM</a></li>

</ul>
</details>

**Tags**: `#quantum-computing`, `#ibm`, `#hardware`, `#scalability`

---

<a id="item-3"></a>
## [In Memoriam: Passing of Tim Peters, Python Core Developer and Author of the Zen of Python](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028) ⭐️ 8.0/10

Tim Peters, a prominent CPython core developer and author of 'The Zen of Python,' has died. The Python community is gathering in tribute, remembering his extensive technical and community contributions. His passing marks a significant loss for the programming ecosystem, particularly because he helped shape the fundamental design philosophy of Python and created the Timsort algorithm used in many modern languages. He was a legendary figure whose mentorship and code have deeply influenced generations of developers. Besides 'The Zen of Python' (PEP 20) and the Timsort sorting algorithm, he co-developed the successful SpamBayes program and co-authored 'The Python Cookbook'. He has been a CPython core developer since the early 2000s.

hackernews · ayhanfuat · Nov 11, 07:03 · [Discussion](https://news.ycombinator.com/item?id=50450488)

**Background**: Tim Peters was a highly influential software engineer in the Python ecosystem who served as a CPython core developer. He is universally recognized for writing 'The Zen of Python' in 1999, a set of guiding aphorisms for Python's design that can be accessed by typing 'import this' in a Python interpreter. In programming, Timsort is the highly efficient hybrid sorting algorithm he created, which is the standard implementation in languages like Python and Java.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer)">Tim Peters (software engineer) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zen_of_Python">Zen of Python - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members shared deep personal reflections, recounting his generous, mentoring approach to coding and discussions that broadened their understanding. Many posted specific technical tributes, such as executing 'import this' to display his poem, and highlighted his foundational work on SpamBayes and his educational impact through the Python Cookbook.

**Tags**: `#Python`, `#Community`, `#Milestone`, `#Obituary`, `#CPython`

---

<a id="item-4"></a>
## [Google SWE points 48 AI agents at NASA Lidar, finds unmapped Maya pyramid in 72h](https://pietromiotti.com/latest/maya-site/?maya) ⭐️ 8.0/10

Google deployed 48 AI agents to analyze NASA LIDAR data, identifying an unmapped Maya pyramid within 72 hours, sparking debate on the scalability of AI-driven archaeological discoveries.

hackernews · eyvindn · Nov 11, 12:05 · [Discussion](https://news.ycombinator.com/item?id=50452455)

**Tags**: `#AI`, `#Archaeology`, `#LIDAR`, `#Computer Vision`, `#Google`

---

<a id="item-5"></a>
## [Using voltage glitching to unleash the A100 in my mining card](https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/) ⭐️ 8.0/10

A detailed post explains using voltage glitching to unlock the full 80GB of HBM memory on NVIDIA A100-based mining cards, with community discussion exploring risks, alternatives, and the economics behind the hardware binning.

hackernews · lae · Nov 11, 10:48 · [Discussion](https://news.ycombinator.com/item?id=50451903)

**Tags**: `#hardware-hacking`, `#nvidia`, `#reverse-engineering`, `#gpu`, `#hbm`

---

<a id="item-6"></a>
## [NVHBM: Can Custom HBM Change Who Builds the Memory Stack?](https://semiwiki.com/semiconductor-manufacturers/376093-nvhbm-can-custom-hbm-change-who-builds-the-memory-stack/) ⭐️ 8.0/10

NVIDIA's NVHBM initiative may reshape the semiconductor industry by altering how high-bandwidth memory is designed, manufactured, and qualified among key suppliers.

rss · SemiWiki · Nov 11, 16:00

**Tags**: `#NVIDIA`, `#HBM`, `#Semiconductor Supply Chain`, `#Memory`, `#SK Hynix`

---

<a id="item-7"></a>
## [STMicros’ Maria Heriz on Moving All Its MCUs to One STM32 Platform](https://www.eetimes.com/stmicros-maria-heriz-on-moving-all-its-mcus-to-one-stm32-platform/) ⭐️ 8.0/10

STMicroelectronics executive Maria Heriz discusses the strategic decision to unify all company MCUs under the STM32 platform, while also addressing preparation for EU cyber regulations and the integration of RISC-V, AI agents, and robotics technologies.

rss · EE Times · Nov 11, 18:28

**Tags**: `#STMicroelectronics`, `#STM32`, `#Microcontrollers`, `#Embedded Systems`, `#RISC-V`

---

<a id="item-8"></a>
## [Credo Unveils 1.6T ZeroFlap ALC for Reliable AI Interconnects at OCP 2026](https://www.eetimes.com/credo-at-ocp-2026-micro-emitter-optics-and-ai-interconnect-reliability/) ⭐️ 8.0/10

Credo’s Don Barnetson presented the 1.6T ZeroFlap Active Light Cable (ALC) at OCP 2026, which utilizes micro-emitter optics to deliver 1.6Tb/s connectivity for AI clusters. The technology provides copper-class reliability in a 10x lighter optical cable, reaching up to 50 meters to support row-scale scale-out networks. The new interconnects are vital for scaling up modern AI data centers, as they mitigate the latency and reliability risks associated with traditional pluggable optics in high-speed networks. By providing robust, cost-effective connectivity at 50m reaches, Credo is helping AI system architects build more efficient and stable cluster infrastructures. The 1.6T ZeroFlap transceivers integrate Credo’s Kfir200 SiPho PIC and PILOT diagnostics into a single device within a standard OSFP pluggable form factor. This architecture uses many small, low-power channels to spread data, building in redundancy and offering up to 10x higher bandwidth compared to traditional copper backplanes in scale-up scenarios.

rss · EE Times · Nov 11, 18:01

**Background**: Optical interconnects are becoming critical bottlenecks in modern AI data centers as the demand for high-speed, low-latency communication between compute nodes grows. The Open Compute Project (OCP) is an industry standard that focuses on designing and building open, scalable infrastructure, where Credo's 1.6T ZeroFlap ALC was showcased to address these specific hardware integration needs.

<details><summary>References</summary>
<ul>
<li><a href="https://credosemi.com/blogs/zeroflap-optics-expands-to-1-6t-why-combining-our-best-optical-technologies-changes-the-reliability-equation-for-ai/">ZeroFlap Optics Expands to 1.6T: Why Combining Our Best ...</a></li>
<li><a href="https://www.ico-optics.org/credos-zeroflap-alc-redefines-ai-data-center-reliability/">Credo’s ZeroFlap ALC Redefines AI Data Center Reliability</a></li>

</ul>
</details>

**Tags**: `#AI Infrastructure`, `#High-Speed Interconnects`, `#Optical Computing`, `#Hardware`, `#Data Centers`

---

<a id="item-9"></a>
## [Google Cloud integrates TPU 8i Max with Arm Neoverse Axion processors](https://www.electronicsweekly.com/news/business/goggle-pairs-tpu-with-arm-2026-11/) ⭐️ 8.0/10

Google Cloud is pairing its TPU 8i Max systems with Arm-based Axion processors. These processors are specifically custom Arm Neoverse-based CPUs designed for data centers. This strategic hardware integration represents a significant architectural shift toward an Arm-centric cloud data center infrastructure. It reinforces Google's commitment to custom silicon for AI workloads and enhances cloud infrastructure performance. The integration utilizes Axion, a custom Arm Neoverse-based CPU, to work alongside the TPU 8i Max system. This specific pairing is part of Google's effort to extend the use of Axion in its cloud offerings.

rss · Electronics Weekly · Nov 11, 06:32

**Background**: TPUs, or Tensor Processing Units, are custom chips designed by Google for machine learning computations, while Axion are CPUs based on the Arm Neoverse architecture. In cloud computing, combining specialized accelerator chips like TPUs with efficient general-purpose CPUs creates a balanced infrastructure for running complex AI tasks.

**Tags**: `#Hardware`, `#AI Infrastructure`, `#Cloud Computing`, `#Google`, `#Arm`

---

<a id="item-10"></a>
## [Imec Establishes Silicon Interposer Flows in NanoIC Pilot Line](https://www.electronicsweekly.com/news/business/imec-delivers-baseline-flows-for-nanoic-interposed-2026-11/) ⭐️ 8.0/10

Imec has successfully established baseline manufacturing flows for silicon interposers within its NanoIC pilot line. This provides an early technical view of a key technology for chiplet integration in advanced packaging. This milestone is significant for the semiconductor industry as it advances the development of advanced packaging, which is critical for improving chiplet scalability and integration. It provides early technical insights for hardware and systems engineering professionals. The delivery of baseline flows represents an incremental step toward developing the interposer platform, rather than a finished product or mass production. The NanoIC pilot line is specifically designed for developing beyond-2nm systems-on-chip and is supported by the EU Chips Act.

rss · Electronics Weekly · Nov 11, 06:10

**Background**: A silicon interposer is an electrical interface used in advanced packaging to provide high-density connections between processors, accelerator chiplets, and high-bandwidth memory. It is made of silicon instead of conventional laminates to support finer pitch I/O density and Through-Silicon Via (TSV) formation. The NanoIC pilot line, hosted by imec in Belgium, is a key R&D infrastructure supported by the Flemish Government and the EU Chips Joint Undertaking.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Interposer">Interposer - Wikipedia</a></li>
<li><a href="https://www.manufacturingmag.com/article/silicon-interposers-and-the-gap-in-us-advanced-packaging">What Is a Silicon Interposer? CoWoS and the US Supply Chain</a></li>
<li><a href="https://www.imec-int.com/en/what-we-offer/nanoic-pilot-line-accelerating-beyond-2nm-innovation-across-europe">NanoIC pilot line | imec</a></li>

</ul>
</details>

**Tags**: `#Silicon Interposers`, `#Advanced Packaging`, `#Imec`, `#Chiplets`, `#Semiconductors`

---

<a id="item-11"></a>
## [Linux memory management reviewer steps down over flood of AI slop patches](https://www.tomshardware.com/software/linux/linux-kernel-reviewer-steps-down-from-memory-management-duties-due-to-influx-of-ai-slop-patches-the-amount-of-time-wasted-on-ai-slop-is-already-too-much-and-were-only-at-the-start-of-this-volume-of-submissions-and-low-manpower-forces-the-step-back) ⭐️ 7.5/10

A senior Linux kernel reviewer has formally resigned from their memory management duties. The decision was driven by an unsustainable influx of low-quality AI-generated patches that overwhelm the team's limited manpower. This marks a critical breaking point where AI-generated code volume exceeds open-source maintenance capacity. It serves as a cautionary tale for the broader software industry regarding the sustainability of AI coding trends. The core issue is not a single bug, but the overwhelming ratio of low-quality submissions to available reviewer manpower. This volume of 'AI slop' makes the current maintenance model for critical kernel infrastructure like memory management structurally unsustainable.

rss · Tom's Hardware · Nov 11, 12:30

**Background**: The Linux kernel is a massive, collaborative project where code patches from the community must be manually reviewed by specialized maintainers before being integrated. Memory management is one of the most complex subsystems in the kernel, requiring rigorous review standards to prevent system crashes. As AI coding tools have become more accessible, the volume of automated and semi-automated code submissions has surged, often lacking the contextual understanding of kernel developers.

**Tags**: `#Linux`, `#AI Coding`, `#Open Source`, `#Kernel Development`

---

<a id="item-12"></a>
## [AMD MEXT Achieves 95% Performance with Half DRAM on 145 Servers](https://www.tomshardware.com/pc-components/cpus/amd-shares-how-it-can-retain-95-percent-of-server-performance-with-just-half-the-dram-sidestepping-memory-shortages-with-mext-tech-powers-over-100-servers-already-running-with-plans-to-expand-to-2-000-servers-in-2027) ⭐️ 7.5/10

AMD is deploying its acquired MEXT technology in its internal IT infrastructure, claiming that servers can run at 50% DRAM capacity while retaining 95% performance in certain workloads. The company currently has 145 servers running with MEXT and plans to expand this deployment to 2,000 servers by 2027. This innovation provides a cost-effective workaround for data center operators facing severe DRAM supply shortages and rising prices, significantly reducing hardware costs for AI and general-purpose computing. It demonstrates a shift from relying purely on silicon manufacturing advancements to AI-driven software memory optimization for solving infrastructure bottlenecks. MEXT utilizes AI to predict memory needs by offloading cold pages to flash storage and proactively moving soon-to-be-needed pages back to DRAM. In extreme scenarios, the technology could reduce physical DRAM needs by up to 75%, effectively tripling available memory capacity at a much lower cost than adding physical chips.

rss · Tom's Hardware · Nov 11, 12:00

**Background**: MEXT is an AI-driven memory optimization technology that AMD acquired to address data center bottlenecks without requiring hardware changes. DRAM currently accounts for up to 75% of total server costs, making supply chain shortages a critical issue for scaling cloud infrastructure. By using predictive software to manage memory tiering, companies can achieve near-full performance using cheaper and more abundant flash storage in the tier below DRAM.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/amd-mext-memory-solution-flash-repaces-dram-same-performance/">AMD Unveils MEXT Memory Solution: Leverages Flash ... - Wccftech</a></li>
<li><a href="https://www.trendforce.com/news/2026/11/11/news-amd-taps-flash-based-mext-amid-memory-crunch-aims-to-cut-dram-needs-by-up-to-75/">[News] AMD Taps Flash-Based MEXT amid Memory Crunch, Aims to ...</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#MEXT`, `#DRAM`, `#Server Performance`, `#Memory Optimization`

---

<a id="item-13"></a>
## [Musk's xAI faces Texas approval for $24B gas-powered AI data center](https://www.tomshardware.com/tech-industry/data-centers/elon-musk-wants-to-build-a-new-gas-powered-data-center-in-starbase-texas-usd24-billion-site-goes-up-for-approval-in-december-but-could-face-headwinds-from-new-governor) ⭐️ 7.5/10

Elon Musk is seeking approval for a $24 billion gas-powered AI data center in Starbase, Texas. The project, which could face headwinds from local officials and new state regulations, is a major step for xAI's computing infrastructure. This project highlights the massive power demands of large-scale AI training and the reliance on natural gas as a transition fuel for data centers. The regulatory uncertainty in Texas could set a precedent for future AI infrastructure approvals. xAI has already secured power capacity from five 380-megawatt natural gas turbines to support its supercomputers. Starbase is a Type C city in Texas, a designation that restricts its ability to levy certain taxes and regulate complex projects.

rss · Tom's Hardware · Nov 11, 11:30

**Background**: Starbase is a rapidly growing community in South Texas centered around SpaceX's Starship launch site. As AI workloads grow, data centers increasingly turn to natural gas turbines for quick, high-capacity power due to grid bottlenecks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c39j8rj4nmmo">Elon Musk's Starbase in Texas will officially become a city</a></li>
<li><a href="https://www.techtimes.com/articles/313840/20260107/elon-musks-xai-secures-massive-power-infrastructure-five-380-mw-natural-gas-turbines.htm">Elon Musk's xAI Secures Massive Power Infrastructure with Five 380...</a></li>

</ul>
</details>

**Tags**: `#AI Infrastructure`, `#Data Centers`, `#Energy`, `#Elon Musk`, `#Hardware`

---

<a id="item-14"></a>
## [Ukrainian drone operations squeezed by fiber optic cable shortage triggered by AI data center buildouts](https://www.tomshardware.com/tech-industry/drones/data-center-demand-for-fiber-optics-squeezes-ukrainian-drone-operations-supply-crunch-has-incurred-6x-10x-cost-increase-for-critical-cabling) ⭐️ 7.5/10

Ukrainian drone manufacturers are facing significant supply chain disruptions and cost increases for jam-proof drones due to a global fiber optic cable shortage driven by AI data center expansion.

rss · Tom's Hardware · Nov 11, 11:00

**Tags**: `#Supply Chain`, `#AI Infrastructure`, `#Defense Technology`, `#Fiber Optics`, `#Geopolitics`

---

<a id="item-15"></a>
## [AWS Finally Built Its Own AWS Emulator](https://github.com/aws/aws-emulator) ⭐️ 7.0/10

AWS has released its own open-source AWS emulator, prompting discussion about its utility compared to existing tools like Moto and LocalStack for testing and development.

hackernews · super_linear · Nov 11, 18:21 · [Discussion](https://news.ycombinator.com/item?id=50456631)

**Tags**: `#cloud-computing`, `#aws`, `#devops`, `#testing`, `#infrastructure-as-code`

---

<a id="item-16"></a>
## [Can a Linear Program Do Weight-Space Programming?](https://nathan.rs/posts/weight-space-lp/) ⭐️ 7.0/10

An analysis proposing that Linear Programming can be used to edit neural network weights by defining linear constraints in weight-space, offering a structured alternative to gradient-based optimization for specific model modification tasks.

hackernews · emschwartz · Nov 11, 12:30 · [Discussion](https://news.ycombinator.com/item?id=50452655)

**Tags**: `#Linear Programming`, `#Neural Networks`, `#Model Editing`, `#Optimization`, `#AI Research`

---

<a id="item-17"></a>
## [Pharo in the Browser with WebAssembly](https://massimo-nocentini.github.io/pharo-vm/world.html) ⭐️ 7.0/10

A demonstration of the Pharo Smalltalk virtual machine running in a web browser using WebAssembly, allowing users to interact with a live coding environment directly online.

hackernews · xkriva11 · Nov 11, 14:21 · [Discussion](https://news.ycombinator.com/item?id=50453763)

**Tags**: `#WebAssembly`, `#Smalltalk`, `#Pharo`, `#Interpreter`, `#Browser`

---

<a id="item-18"></a>
## [SemiWiki Explains the Role of Silicon Substrates and SOI in Transistors](https://semiwiki.com/semiconductor-manufacturers/soitec/376187-semiconductors-and-soi-from-bulk-wafers-to-engineered-substrates/) ⭐️ 7.0/10

An in-depth article on SemiWiki explains how silicon substrate properties, such as its 1.12 eV bandgap and high-quality native SiO2 oxide, determine the performance of modern transistors. The piece outlines the transition from standard bulk wafers to engineered Silicon-on-Insulator (SOI) substrates. This educational resource helps industry professionals and students understand the material science constraints that drive chip design evolution. It clarifies why substrate engineering is critical for reducing leakage and improving power efficiency in advanced semiconductor nodes. The article highlights that while the active transistor is located in the top few hundred nanometers of the crystal, the rest of the wafer can act as a mechanical liability. It specifically cites Silicon's moderate bandgap (1.12 eV) and excellent native oxide quality as the primary reasons for its dominance in the industry.

rss · SemiWiki · Nov 11, 18:00

**Background**: In standard semiconductor manufacturing, bulk silicon wafers are used as the base material for building chips. As transistors shrink, the electrical interference from the underlying bulk silicon becomes a major obstacle, leading to the development of Silicon-on-Insulator (SOI) technology. SOI wafers use an insulating layer (typically silicon dioxide) between the active silicon layer and the substrate, which significantly reduces parasitic effects and power consumption.

**Tags**: `#Semiconductors`, `#SOI`, `#Material Science`, `#Transistors`, `#Wafer Technology`

---

<a id="item-19"></a>
## [Mobilint and Chips&Media Mass-Produce Edge AI Chips for Humanoid Robots](https://semiwiki.com/ip/chipsmedia/375958-why-video-processing-matters-for-the-next-generation-of-robots/) ⭐️ 7.0/10

South Korean companies Mobilint and Chips&Media announced on November 4 the mass production of next-generation edge AI chips that integrate Chips&Media's video codec technology. These chips are specifically designed to handle the high-bandwidth video streams generated by multi-camera humanoid robots. As humanoid robots rely on multiple cameras to navigate complex environments, efficient on-device video processing is critical to managing bandwidth and latency. This integration of specialized codec IP into edge AI chips addresses a key bottleneck in scaling robotics applications to commercial production. The collaboration between Mobilint and Chips&Media focuses on integrating video codec IP directly into edge AI silicon to process data locally rather than offloading it. The specific target application is multi-camera humanoid robots, which generate video data exceeding the capacity of traditional system handling.

rss · SemiWiki · Nov 11, 14:00

**Background**: Edge AI refers to running artificial intelligence models on local hardware devices rather than in the cloud, which reduces latency and bandwidth usage. In robotics, particularly for humanoids, visual perception from multiple cameras generates massive amounts of data, requiring specialized hardware like video codecs to compress and process this information efficiently.

**Tags**: `#robotics`, `#edge-ai`, `#video-processing`, `#hardware`, `#chips`

---

<a id="item-20"></a>
## [Norway deploys 3,500 AI laser drones to protect salmon](https://www.tomshardware.com/tech-industry/drones/3-500-ai-laser-robots-patrol-norwegian-salmon-farms-killing-sea-lice-parasites-get-zapped-by-high-tech-alternative-to-harsh-chemical-baths) ⭐️ 6.5/10

Stingray Marine Solutions has expanded its deployment of underwater AI laser drones in Norwegian salmon farms to 3,500 units, now protecting 112 million fish. These autonomous submarines operate 24/7 to eliminate sea lice without the use of harsh chemical baths. This chemical-free approach significantly reduces environmental risk and fish mortality associated with traditional reactive treatments in the aquaculture industry. It represents a major step toward sustainable, automated pest control that minimizes ecosystem impact. The drones utilize stereo cameras and blue-light illumination to distinguish parasites from fish skin, firing precision laser pulses that coagulate lice while leaving the host unharmed. Each unit can deliver up to five laser pulses to effectively remove individual parasites.

rss · Tom's Hardware · Nov 11, 10:00

**Background**: Sea lice are parasites that feed on farmed salmon, weakening the fish and triggering the need for stressful treatments like chemical baths or mechanical removal. Optical delousing is an emerging technology that uses machine vision and targeted lasers to kill parasites on freely swimming fish, offering a continuous and less invasive alternative to traditional methods.

<details><summary>References</summary>
<ul>
<li><a href="https://thefishsite.com/articles/interest-grows-in-new-salmon-licezapping-laser">Interest Grows in New Salmon Lice -Zapping Laser | The Fish Site</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0044848625007963">Control of salmon lice through optical delousing in ...</a></li>

</ul>
</details>

**Tags**: `#Autonomous Systems`, `#AI Application`, `#Robotics`, `#Agricultural Technology`, `#Sustainability`

---