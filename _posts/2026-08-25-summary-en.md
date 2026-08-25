---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 95 items, 20 important content pieces were selected

---

1. [Intel Diamond Rapids Xeon 7: 256 P-cores, 1.28 GB LLC, UCIe-S](#item-1) ⭐️ 8.5/10
2. [SK hynix Defers Hybrid Bonding to HBM5 as 775-Micron Stack Ceiling Looms](#item-2) ⭐️ 8.5/10
3. [IBM Unveils 11-Core Dual-ISA Mainframe Processor on 2nm](#item-3) ⭐️ 8.5/10
4. [Kyoto University Demonstrates 600°C SiC Transistor Using Standard Ion Implantation](#item-4) ⭐️ 8.5/10
5. [MS Paint and Photos Secretly Embed Non-Disableable GUID Watermarks](#item-5) ⭐️ 8.0/10
6. [AMD Hits Record 30.7% as Intel x86 Share Falls to 1995 Low](#item-6) ⭐️ 7.5/10
7. [Intel Details Crescent Island: 32 Xe3P Cores, up to 480 GB LPDDR5X for AI Inference](#item-7) ⭐️ 7.5/10
8. [mVolt+ v0.36 Bypasses RTX 50-Series Power Limits Without Hardware Mods](#item-8) ⭐️ 7.5/10
9. [Samsung Confirms HBM4E Memory at 16 Gbps Per Pin](#item-9) ⭐️ 7.5/10
10. [Taiwan indicts nine for smuggling Nvidia B300 GPUs to China](#item-10) ⭐️ 7.5/10
11. [AMD Unveils MI400 GPU Architecture at Hot Chips 2026](#item-11) ⭐️ 7.5/10
12. [Arm Unveils AGI, Its First Complete Data Center CPU at Hot Chips 2026](#item-12) ⭐️ 7.5/10
13. [Fujitsu’s Arm-based Monaka Data Center CPU at Hot Chips 2026](#item-13) ⭐️ 7.5/10
14. [Pew Research: Over One-Third of Post-ChatGPT English Web Pages Show AI Traces](#item-14) ⭐️ 7.3/10
15. [Entire City of San Francisco Recreated as Interactive 3D Video Game](#item-15) ⭐️ 7.0/10
16. [RISC-V at Sixteen: From Modular ISA to Standardized Platforms at Hot Chips 2026](#item-16) ⭐️ 7.0/10
17. [Hot Chips Highlights Evolving Memory Architectures for AI](#item-17) ⭐️ 7.0/10
18. [Tiangong Ultra Humanoid Robot Beats Fastest Human in 100m Sprint](#item-18) ⭐️ 7.0/10
19. [Quintessent begins sampling single-chip DWDM comb laser](#item-19) ⭐️ 7.0/10
20. [LG's native 1,000 Hz 1080p gaming monitor has a matching $1,000 price tag — preorders open for the 25-inch UltraGear 25G590B](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [Intel Diamond Rapids Xeon 7: 256 P-cores, 1.28 GB LLC, UCIe-S](https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-comes-with-up-to-256-p-cores-1-28-gb-of-last-level-cache-next-gen-18a-p-cpu-also-brings-avx-10-2-and-uses-ucie-s-instead-of-emib) ⭐️ 8.5/10

At Hot Chips 2026, Intel disclosed its next-generation Xeon 7 'Diamond Rapids' server processor, configured with up to 256 'Panther Cove' P-cores and 1.28 GB of last-level cache per socket, manufactured on the Intel 18A-P process node. The chip adopts the UCIe-S chiplet interconnect in place of Intel's legacy EMIB, and adds AVX 10.2 instructions and PCI-Express Gen 6 I/O, targeting enterprise-scale agentic AI workloads ahead of a planned 2027 launch. Diamond Rapids signals Intel's most aggressive server CPU redesign in years, directly challenging AMD EPYC and ARM-based server chips in the high-core-count data center market. The combination of 256 cores, 1.28 GB of LLC, and PCI-Express Gen 6 positions the part for AI inference and agentic AI workloads where memory bandwidth and cache capacity are critical bottlenecks. The MCM package contains 16 core chiplets organized into 4 base tiles (64 cores per tile), wired through 2 Fabric Hub Tiles and a centralized server I/O die (sIOD), closely mirroring AMD's CCD/sIOD disaggregation philosophy. Switching from Intel's proprietary EMIB silicon bridges to the open UCIe-S standard suggests Intel is aligning with industry-wide chiplet interoperability rather than maintaining a captive interconnect technology.

rss · Tom's Hardware · Aug 24, 21:07

**Background**: UCIe (Universal Chiplet Interconnect Express) is an open industry standard, first released in March 2022 and updated to version 3.0 in August 2025, that defines a standardized die-to-die interconnect allowing chiplets from different vendors to be mixed in a single package. Intel's EMIB (Embedded Multi-die Interconnect Bridge), introduced in 2018, is a proprietary 2.5D silicon-bridge technology that Intel used in products like Kaby Lake-G and earlier Xeon tiles. AVX 10.2 is the latest evolution of Intel's Advanced Vector Extensions, adding new conversion, saturating-arithmetic, and floating-point comparison instructions that accelerate AI, scientific, and cryptographic workloads. The 'P-core' designation refers to Intel's Performance cores, optimized for single-thread throughput, as opposed to the more power-efficient E-cores.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UCIe">UCIe - Wikipedia</a></li>
<li><a href="https://semiwiki.com/semiconductor-manufacturers/intel/298674-intels-emib-packaging-technology-a-deep-dive/">Intel ’s EMIB Packaging Technology – A Deep Dive - SemiWiki</a></li>
<li><a href="https://hugeonotation.github.io/pblog/2024/11/03/avx10_2_new_instructions.html">AVX-10.2's New Instructions</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#Xeon`, `#data-center`, `#HotChips2026`, `#server-CPUs`

---

<a id="item-2"></a>
## [SK hynix Defers Hybrid Bonding to HBM5 as 775-Micron Stack Ceiling Looms](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling) ⭐️ 8.5/10

At Hot Chips 2026, SK hynix disclosed that HBM cube stacks have hit a hard ceiling of 775 microns in total thickness — the standard thickness of a 300mm logic wafer — forcing the company to delay hybrid bonding from HBM4e to HBM5 while continuing to rely on its MR-MUF packaging through Nvidia's Rubin generation. This is a critical inflection point for the AI memory supply chain: the 775-micron ceiling directly limits how tall future HBM stacks can grow, meaning each generation must cram more capacity into the same vertical envelope, and the deferral of hybrid bonding keeps thermal-mechanical bottlenecks in play for another product cycle affecting every AI accelerator vendor. The 775-micron limit is not arbitrary but is dictated by the standard 300mm wafer thickness, which defines how far a thinned wafer can bow without fracture; MR-MUF (Mass Reflow-Molded Underfill) connects dies via solder reflow plus a protective molded underfill for thermal dissipation, whereas hybrid bonding creates direct metal-to-insulator bonds with higher I/O density and lower thermal resistance but remains a yield and throughput challenge for mass production.

rss · Tom's Hardware · Aug 24, 17:55

**Background**: High-Bandwidth Memory (HBM) is the stacked DRAM that powers modern AI GPUs and accelerators, providing far more bandwidth than conventional GDDR by vertically stacking multiple DRAM dies connected by through-silicon vias (TSVs). MR-MUF is SK hynix's proprietary mass-reflow and molded-underfill process, widely regarded as best-in-class for HBM stacking because it improves heat dissipation and stack rigidity compared to traditional thermo-compression bonding. Hybrid bonding is the next evolutionary step, enabling finer pitch interconnects and lower thermal resistance by bonding copper-to-copper or metal-to-dielectric directly, without solder bumps — but it requires extreme surface flatness and clean-room precision that has so far limited its use in high-volume HBM production.

<details><summary>References</summary>
<ul>
<li><a href="https://news.skhynix.com/rulebreaker-revolutions-mr-muf-unlocks-hbm-heat-control/">Rulebreakers' Revolutions: MR - MUF Unlocks HBM Heat Control</a></li>
<li><a href="https://www.mdpi.com/2079-9292/14/13/2682">Thermal Issues Related to Hybrid Bonding of 3D-Stacked High ...</a></li>
<li><a href="https://chiplet-marketplace.com/library/wiki/mr-muf-mass-reflow-molded-underfill">MR - MUF ( Mass Reflow Molded Underfill ) - Chiplet Marketplace Wiki</a></li>

</ul>
</details>

**Tags**: `#HBM`, `#SK-hynix`, `#hybrid-bonding`, `#semiconductors`, `#AI-infrastructure`

---

<a id="item-3"></a>
## [IBM Unveils 11-Core Dual-ISA Mainframe Processor on 2nm](https://www.tomshardware.com/pc-components/cpus/ibms-first-dual-isa-core-natively-executes-arm-and-z-architecture-in-the-same-core-all-cores-run-at-5-7-ghz-base-frequency-next-gen-mainframe-ai-processor-is-built-on-2nm-node-with-11-cores) ⭐️ 8.5/10

IBM announced at Hot Chips 2026 an 11-core processor whose cores natively execute both z/Architecture and AArch64 instructions at a 5.7 GHz base frequency on a 2nm process. The processor is intended for future IBM Z and LinuxONE systems and is the first processor milestone from IBM's Arm collaboration established in April 2026. The design will let Arm-native Linux environments run simultaneously with z/OS and Linux on IBM Z, bringing cloud-native and AI software to systems known for transaction processing and data-intensive workloads. This could help enterprises consolidate more workloads on one enterprise platform while retaining IBM's hardware-level fault detection and recovery, encryption, secure key management, and AI acceleration capabilities. The key implementation detail is that each physical core can natively execute both z/Architecture and AArch64, while the chip is planned for future IBM Z and LinuxONE systems. IBM describes the processor as still under development and did not announce a shipping date, measured performance, pricing, or software-migration commitments.

rss · Tom's Hardware · Aug 24, 17:42

**Background**: z/Architecture is IBM's 64-bit CISC instruction-set architecture for mainframe processors. AArch64 is the 64-bit Arm instruction-set architecture used by Linux and a broad range of cloud, edge, and AI software. IBM Z platforms serve transaction-processing and data-intensive workloads, including environments that run z/OS and Linux, while IBM and Arm established their collaboration in April 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://www.servethehome.com/ibm-z-and-linuxone-dual-isa-processor-and-ai-acceleration-at-hot-chips-2026/">IBM Z and LinuxONE Dual - ISA Processor and AI... - ServeTheHome</a></li>
<li><a href="https://www.tomshardware.com/pc-components/cpus/ibms-first-dual-isa-core-natively-executes-arm-and-z-architecture-in-the-same-core-all-cores-run-at-5-7-ghz-base-frequency-next-gen-mainframe-ai-processor-is-built-on-2nm-node-with-11-cores">IBM's first dual - ISA core natively executes ARM and z/ Architecture in...</a></li>
<li><a href="https://www.ibm.com/support/pages/sites/default/files/2021-05/SA22-7871-10.pdf">IBM z/Architecture Reference Summary</a></li>

</ul>
</details>

**Tags**: `#IBM`, `#mainframe`, `#ARM`, `#z/Architecture`, `#Hot Chips 2026`

---

<a id="item-4"></a>
## [Kyoto University Demonstrates 600°C SiC Transistor Using Standard Ion Implantation](https://www.tomshardware.com/tech-industry/kyoto-university-demonstrates-a-sic-transistor-that-runs-at-600c-using-standard-ion-implantation) ⭐️ 8.5/10

Researchers at Kyoto University have built a silicon carbide (SiC) transistor that operates reliably at 600°C (873 K), using standard ion implantation and a bottom-gate JFET design that keeps threshold voltage drift to within 0.1 V at 400°C. The approach addresses the leakage and voltage drift issues that have historically prevented SiC transistors from being manufactured with conventional semiconductor processes. This breakthrough enables high-temperature electronics — needed in aerospace, space, oil/gas downhole, and other harsh environments — to be manufactured using the same ion implantation equipment already present in commercial fabs, rather than requiring exotic dedicated processes. By making SiC high-temperature transistors fab-friendly, it dramatically lowers the barrier to mass-producing electronics that can survive where silicon devices cannot. The device is a bottom-gate junction field-effect transistor (JFET) in silicon carbide, which leverages SiC's wide bandgap for thermal stability while using ion implantation — a low-temperature, widely available doping technique — to create the active regions. The bottom-gate architecture specifically suppresses gate leakage and stabilizes threshold voltage at extreme temperatures, two failure modes that typically plague SiC transistors built with conventional approaches.

rss · Tom's Hardware · Aug 24, 10:30

**Background**: Silicon carbide is a wide-bandgap semiconductor, meaning it requires much more energy to excite electrons into the conduction band than silicon does, which gives it superior tolerance to high temperatures, high voltages, and high frequencies. Ion implantation is a standard, low-temperature doping process in which accelerated ions are driven into a semiconductor to alter its electrical properties; it is the workhorse technique used in nearly every modern CMOS fab. A bottom-gate transistor places the gate electrode beneath the semiconductor channel (rather than on top), which in this design helps control leakage current and threshold-voltage stability. Together, these elements allow the Kyoto team to combine SiC's intrinsic high-temperature capability with a manufacturing flow that mainstream fabs can execute.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/kyoto-university-demonstrates-a-sic-transistor-that-runs-at-600c-using-standard-ion-implantation">Kyoto University builds transistor that survives... | Tom's Hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ion_implantation">Ion implantation - Wikipedia</a></li>
<li><a href="https://ece.engin.umich.edu/stories/u-m-awarded-up-to-7-5m-to-bring-heat-tolerant-semiconductors-from-lab-to-fab">U-M awarded up to $7.5M to bring heat-tolerant semiconductors from...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#silicon-carbide`, `#high-temperature-electronics`, `#research-breakthrough`, `#hardware`

---

<a id="item-5"></a>
## [MS Paint and Photos Secretly Embed Non-Disableable GUID Watermarks](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

Reverse engineering reveals that Microsoft Paint and Microsoft Photos embed invisible, non-disableable watermarks containing GUIDs into images, including those generated or manipulated using on-device local AI models. The invisible watermark cannot be disabled and the user receives no notification of its presence. This raises serious privacy and anonymity concerns for hundreds of millions of Windows users, as the embedded watermarks could potentially be used to identify individuals through copyright subpoenas served on Microsoft. It also undermines the expectation of privacy when using local AI models, which users deliberately choose to avoid sending data to external servers. The visible watermark can be toggled off by the user, but the invisible watermark is embedded silently in the background with no notice and cannot be disabled through any settings. The watermark appears even when using local AI models like Stable Diffusion for image generation, implying that telemetry or network requests still occur during ostensibly offline processing.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**Background**: A GUID (Globally Unique Identifier) is a 128-bit number used to uniquely identify information in computer systems, commonly employed in Microsoft software for tagging data. Digital watermarking is a steganographic technique that embeds hidden data into digital media such as images, typically for copyright protection, authentication, or forensic tracking. Local AI image generation refers to running models like Stable Diffusion directly on a user's own hardware without sending data to cloud servers — something users typically choose specifically for privacy and to avoid content filters.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Universally_unique_identifier">Universally unique identifier - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_watermarking">Digital watermarking - Wikipedia</a></li>
<li><a href="https://techtactician.com/beginners-guide-to-local-ai-image-generation-software/">Beginner's Guide To Local AI Image Generation Software - How ...</a></li>

</ul>
</details>

**Discussion**: Community discussion is dominated by privacy and anonymity concerns. Commenters stressed that the real danger lies not in the AI aspect but in the unique identifier embedded in every image, which could be exploited via copyright subpoenas to deanonymize users, drawing parallels to age verification systems. Several users expressed surprise that MS Paint has evolved from a simple drawing tool, while others framed this as part of a broader erosion of internet anonymity and corporate surveillance.

**Tags**: `#privacy`, `#security`, `#reverse-engineering`, `#microsoft`, `#watermarking`

---

<a id="item-6"></a>
## [AMD Hits Record 30.7% as Intel x86 Share Falls to 1995 Low](https://www.techpowerup.com/351908/amd-gains-ground-as-intel-x86-market-share-goes-back-to-1995-levels) ⭐️ 7.5/10

According to Mercury Research, Intel's x86 CPU market share fell below 70% for the first time since 1995, hitting 69.3% in Q2 2026 — a 6.5-point drop year over year — while AMD climbed to a record 30.7%. When semi-custom, embedded, and IoT products are included, Intel's share drops further to 65.9% versus AMD's 34.1%, boosted by stronger-than-expected gaming console SoC shipments. This marks the most dramatic erosion of Intel's long-standing dominance in the x86 ecosystem in three decades, reflecting the cumulative impact of AMD's Zen architecture success across desktop, laptop, and server segments. The shift signals changing competitive dynamics in PCs and data centers, which will influence pricing, supply decisions, and platform investments industry-wide. Segment-by-segment, AMD's desktop share reached 34.9% (+2.7 pts YoY), server share hit 34.5% (+7.3 pts YoY), and laptop share jumped to 28.9% (+8.4 pts YoY) — the largest gain. AMD has launched 6th Gen EPYC 'Venice' server processors based on Zen 6, while Intel recently detailed its upcoming Xeon 7 'Diamond Rapids' CPUs and the 'Crescent Island' data-center GPU at Hot Chips.

rss · TechPowerUp News · Aug 24, 23:50

**Background**: x86 is a CISC instruction set architecture originally developed by Intel in 1978 with the 8086 processor, and it has since become the dominant ISA for PCs and servers. Intel and AMD are the only two major x86 CPU vendors; for most of the past two decades Intel held an overwhelming share lead, with AMD only briefly climbing above 25% during the early 2000s and again from 2017 onward. Mercury Research is the leading analyst firm tracking x86 CPU shipment shares by segment, and its quarterly reports are widely cited as the industry standard.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theregister.com/systems/2026/08/21/amd-grabs-more-cpu-share-while-pricier-pcs-punish-desktop-demand/5291053">AMD grabs more CPU share while pricier PCs punish desktop demand</a></li>
<li><a href="https://ms.codes/en-ca/blogs/computer-hardware/mercury-research-cpu-market-share">Mercury Research CPU Market Share</a></li>
<li><a href="https://en.wikipedia.org/wiki/X86">x86 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#CPU`, `#AMD`, `#Intel`, `#x86`, `#market-share`

---

<a id="item-7"></a>
## [Intel Details Crescent Island: 32 Xe3P Cores, up to 480 GB LPDDR5X for AI Inference](https://www.techpowerup.com/351901/intel-details-crescent-island-graphics-32-xe3p-cores-up-to-480-gb-lpddr5x-memory) ⭐️ 7.5/10

At Hot Chips 2026, Intel detailed its "Crescent Island" datacenter GPU based on the Xe3P architecture, featuring 32 Xe3P cores, 256 XMX engines, and up to 480 GB of LPDDR5X memory (in ODM configurations) on a 350 W air-cooled PCIe card designed purely for AI inference workloads. The card positions Intel as a competitor in the AI inference accelerator market currently dominated by NVIDIA, with its massive LPDDR5X capacity enabling frontier open-source models to run locally on a small number of cards. The deliberate removal of all graphics hardware signals Intel's strategic commitment to carving out a niche in AI infrastructure rather than competing in traditional GPU markets. The XMX engines have been redesigned from a 4-deep systolic array to a 16-deep processing pipeline, and the GPU adds FP4 data format support alongside FP8. Each Xe3P core contains 8 Vector Engines and 8 XMX Engines (256 of each total), plus 1 MB register files and 512 KB L1 cache per core, with 32 MB of unified L2 cache across the chip — and notably no graphics output hardware at all, targeting long-context and agentic AI inference.

rss · TechPowerUp News · Aug 24, 19:49

**Background**: Intel's Xe architecture is a family of GPU designs spanning from integrated graphics to datacenter accelerators, with Xe3P being a variant tuned for AI/ML workloads. XMX (Xe Matrix Extensions) engines are Intel's equivalent of NVIDIA's Tensor Cores — specialized systolic array hardware that performs the matrix multiplications central to neural network inference. LPDDR5X is a low-power variant of DDR5 memory originally designed for mobile devices; its use in datacenter GPUs is unusual, as most AI accelerators (NVIDIA H100, AMD MI300) rely on HBM (High Bandwidth Memory), though LPDDR5X can offer much higher capacity at lower cost. Hot Chips is a prestigious annual symposium where semiconductor companies reveal detailed silicon architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://videocardz.com/newz/intel-details-xe3p-gpu-architecture-crescent-island-gets-up-to-480gb-memory-and-350w-pcie-variant">Intel details Xe3P GPU architecture, Crescent Island gets up to 480GB memory and 350W PCIe variant - VideoCardz.com</a></li>
<li><a href="https://www.intel.com/content/www/us/en/docs/oneapi/optimization-guide-gpu/2024-1/xmx.html">Boost Matrix Multiplication Performance with Intel® Xe Matrix Extensions</a></li>
<li><a href="https://hardwaretimes.com/lpddr-vs-ddr5-vs-gddr7-what-is-the-difference/">DDR4 vs DDR5 vs LPDDR4 vs LPDDR5 vs GDDR6 vs GDDR7: What is the Difference? | Hardware Times</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#GPU`, `#datacenter`, `#AI infrastructure`, `#hardware`

---

<a id="item-8"></a>
## [mVolt+ v0.36 Bypasses RTX 50-Series Power Limits Without Hardware Mods](https://www.techpowerup.com/351867/nvidia-power-limit-bypass-rtx-5090-oc-hits-700-w-rtx-5080-up-to-680-w-no-shunt-mod-needed) ⭐️ 7.5/10

The mVolt+ v0.36 update reportedly enables software-based power-limit bypasses on NVIDIA RTX 50-series GPUs without requiring a shunt modification or vBIOS flash. One Reddit user achieved a 700 W power draw on an RTX 5090 (up from a 575 W stock TDP), reaching 3,127 MHz and scoring 16,523 in 3DMark Steel Nomad, while another user pushed an ASUS ROG Astral RTX 5080 OC to 680 W (up from 400 W stock TDP). This represents a significant shift in extreme GPU overclocking methodology, as achieving such power levels previously required invasive hardware modifications (shunt mods) or vBIOS flashing, both of which void warranties and carry permanent risk. If validated, this software-only approach could democratize extreme overclocking for RTX 50-series owners while raising new questions for NVIDIA about power-limit enforcement and driver-level protections. mVolt+ v0.36 exposes hidden Blackwell voltage and power controls, including separate power-channel limits for the GPU core and memory, plus voltage controls for the Core, XBAR, SYS, and Video domains—features not available in standard overclocking tools like MSI Afterburner. The reported RTX 5090 clock of 3,127 MHz is approximately 720 MHz above the reference 2,407 MHz boost clock, and the RTX 5080 result of 680 W exceeds even the 450 W limit achievable through NVIDIA's official tuning tools.

rss · TechPowerUp News · Aug 24, 12:00

**Background**: GPU power limits are enforced by the vBIOS and driver firmware to keep cards within their rated thermal and electrical design parameters. A shunt mod is a hardware modification that replaces or bypasses the current-sense resistor (shunt) on the PCB, allowing the GPU to draw more power than the monitoring circuit is designed to read. Flashing a custom vBIOS achieves a similar result by software but also bypasses factory safety limits. mVolt+ is a third-party utility that interfaces with NVIDIA's GPU voltage regulation hardware at a low level, and version v0.36 specifically targets the new Blackwell architecture used in the RTX 50-series to unlock previously inaccessible controls.

<details><summary>References</summary>
<ul>
<li><a href="https://vgtimes.com/tech-and-hardware/165162-mvolt-v0.36-lets-geforce-rtx-50-gpus-push-past-vbios-power-limits.html">mVolt+ v0.36 Lets GeForce RTX 50 GPUs Push Past VBIOS Power...</a></li>
<li><a href="https://www.pcworld.com/article/2854038/this-nvidia-rtx-laptop-mod-unlocks-amazing-performance-dont-do-it.html">This Nvidia RTX laptop mod unlocks amazing performance. | PCWorld</a></li>
<li><a href="https://www.overclock.net/threads/tutorial-power-target-limit-hardware-mod-shunt-mod-for-titan-x-and-many-other-nvidia-gpus.1608437/">overclock .net/threads/tutorial-power-target-limit- hardware - mod - shunt ...</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#GPU Overclocking`, `#mVolt+`, `#RTX 5090`, `#RTX 5080`

---

<a id="item-9"></a>
## [Samsung Confirms HBM4E Memory at 16 Gbps Per Pin](https://www.techpowerup.com/351859/samsung-confirms-hbm4e-memory-running-at-16-gbps-per-pin) ⭐️ 7.5/10

Samsung confirmed at the Hot Chips 2026 conference that it is preparing to ship HBM4E memory running at 16 Gbps per pin, upgrading from the 14 Gbps version it has been shipping since late May. At 2,048 pins per stack, this enables a maximum bandwidth of 4 TB/s per stack, up from 3.6 TB/s. HBM is a critical component for next-generation AI accelerators and GPUs, where memory bandwidth is a key bottleneck for training large models and running inference workloads. With approximately a dozen HBM stacks typically deployed per accelerator, this speed increase substantially raises the aggregate bandwidth available to AI silicon. Samsung currently offers HBM4E in a 12-high stack configuration with 48 GB density, with 8-layer 32 GB and 16-layer 64 GB variants planned to meet customer requirements. Samsung's HBM4 is currently shipping at 11.7 Gbps, making the jump to HBM4E at 16 Gbps particularly notable.

rss · TechPowerUp News · Aug 24, 05:30

**Background**: High Bandwidth Memory (HBM) is a type of stacked DRAM that uses through-silicon vias (TSVs) to connect multiple memory dies vertically, delivering significantly higher bandwidth than traditional GDDR memory used in conventional graphics cards. HBM is essential for AI accelerators from companies such as NVIDIA, AMD, and custom ASIC vendors, as AI workloads require massive data movement between compute units and memory. The HBM market is dominated by three players—Samsung, SK Hynix, and Micron—with each generation (HBM2, HBM3, HBM3E, HBM4, HBM4E) bringing improvements in per-pin speed, stack capacity, and power efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://hotchips.org/">Hot Chips</a></li>
<li><a href="https://www.advisorpedia.com/active/the-memory-shortage-wall-street-isnt-seeing/">The Memory Shortage Wall Street Isn’t Seeing | Advisorpedia</a></li>

</ul>
</details>

**Tags**: `#HBM4E`, `#Samsung`, `#high-bandwidth-memory`, `#AI-hardware`, `#semiconductors`

---

<a id="item-10"></a>
## [Taiwan indicts nine for smuggling Nvidia B300 GPUs to China](https://www.tomshardware.com/tech-industry/artificial-intelligence/nine-indicted-by-taiwan-over-illegal-export-of-nvidia-b300-gpus-to-china-details-reveal-five-point-strategy-to-exploit-and-avoid-customs-controls) ⭐️ 7.5/10

Nine individuals have been indicted in Taiwan for the illegal smuggling of Nvidia B300 AI servers to China, reportedly using a five-point strategy designed to exploit and circumvent customs controls. This case highlights the escalating enforcement efforts around AI chip export controls and demonstrates the sophisticated methods smugglers use to evade them, underscoring the geopolitical stakes of advanced AI hardware access for China. The Nvidia B300 (Blackwell Ultra) is Nvidia's most powerful single GPU, featuring 288GB of HBM3e memory, 8TB/s bandwidth, and 15 petaFLOPS of dense FP4 compute per chip, making it a prime target for export restrictions. The indictment follows related cases including a separate scheme involving a Nvidia senior manager and Supermicro.

rss · Tom's Hardware · Aug 24, 15:09

**Background**: The United States has imposed increasingly strict export controls on advanced AI chips to China, primarily administered by the Bureau of Industry and Security (BIS), aiming to limit China's access to cutting-edge semiconductor technology for military and AI applications. The Nvidia B300, part of the Blackwell Ultra generation that began shipping in January 2026, represents the latest generation of AI accelerators covered by these restrictions. Taiwan, as a major hub for AI server assembly and a key transit point for hardware, has become an important jurisdiction for enforcement actions targeting smuggling operations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.spheron.network/blog/nvidia-b300-blackwell-ultra-guide/">NVIDIA B300 (Blackwell Ultra): 288GB Specs, Pricing & Benchmarks (2026) | Spheron Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_export_controls_on_AI_chips_and_semiconductors">United States export controls on AI chips and semiconductors</a></li>
<li><a href="https://arstechnica.com/tech-policy/2026/08/nvidia-senior-manager-linked-to-supermicro-scheme-smuggling-ai-servers-to-china/">Nvidia senior manager linked to Supermicro scheme smuggling AI servers to China - Ars Technica</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#export-controls`, `#B300`, `#AI-hardware`, `#Taiwan-China`

---

<a id="item-11"></a>
## [AMD Unveils MI400 GPU Architecture at Hot Chips 2026](https://www.servethehome.com/amd-mi400-gpu-at-hot-chips-2026/) ⭐️ 7.5/10

AMD presented its MI400 GPU architecture at Hot Chips 2026, showcasing the design of its massive AI accelerator built for Helios rack-scale systems. The reveal details how the chip was engineered to power AMD's full-stack AI platform alongside EPYC Venice CPUs and Pensando Vulcano AI NICs. The MI400 is AMD's most aggressive bid yet to challenge NVIDIA's dominance in data-center AI accelerators, with the Helios rack-scale platform designed to compete head-to-head against NVIDIA's GB200/NVLink systems. A successful MI400 generation could reshape the economics of frontier AI training and inference for hyperscalers and enterprises. The MI400 is built on AMD's CDNA 5 architecture using TSMC's 2nm process node, reportedly packing 320 billion transistors, 432 GB of HBM4 memory, and delivering up to 40 PFLOPS of FP4 performance per GPU. The Helios rack integrates 72 MI400 GPUs (the MI455X variant) per rack alongside EPYC Venice CPUs, presenting the whole rack as a single coherent accelerator.

rss · ServeTheHome · Aug 25, 00:30

**Background**: Hot Chips is a prestigious annual symposium held at Stanford since 1989, where major semiconductor companies traditionally unveil deep architectural details of their high-performance chips. AMD's Instinct line is its data-center GPU family dedicated to AI and HPC workloads, competing directly with NVIDIA's H100/B100/B200 series and the upcoming Rubin generation. Rack-scale systems like Helios represent a shift from individual GPUs to integrated compute fabrics where CPUs, GPUs, and high-speed networking are co-designed to function as one large accelerator.

<details><summary>References</summary>
<ul>
<li><a href="https://www.servethehome.com/amd-helios-mi400-system-architecture-at-hot-chips-2026/">AMD Helios MI400 System Architecture at Hot Chips 2026</a></li>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi400.html">AMD Instinct™ MI400 Series GPUs</a></li>
<li><a href="https://hotchips.org/">Hot Chips</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#MI400`, `#GPU`, `#HotChips`, `#AI-Hardware`

---

<a id="item-12"></a>
## [Arm Unveils AGI, Its First Complete Data Center CPU at Hot Chips 2026](https://www.servethehome.com/arms-agi-data-center-cpu-at-hot-chips-2026/) ⭐️ 7.5/10

At Hot Chips 2026, Arm unveiled AGI, its first complete commercial CPU design, built around Neoverse V3 cores and targeting next-generation agentic AI servers. This marks a strategic shift for Arm from a pure IP licensor to offering finished chip designs for the data center market. This represents a significant strategic pivot for Arm, moving beyond licensing individual CPU cores to delivering complete data center chip designs and competing more directly in the server CPU space. The explicit focus on agentic AI workloads positions Arm to capitalize on the rapidly growing demand for autonomous AI systems, which require substantial general-purpose compute to orchestrate accelerators and execute reasoning loops. According to technical disclosures, the AGI CPU features a dual-chiplet design with approximately 100 billion transistors and 136 Neoverse V3 cores, each being a 10-wide out-of-order machine with third-generation prefetch and branch prediction alongside a fast per-core L2 cache. However, AGI is built on existing Neoverse V3 IP rather than a fundamentally new microarchitecture, meaning its differentiation lies in system-level integration, chiplet packaging, and workload-specific tuning rather than core-level innovation.

rss · ServeTheHome · Aug 24, 19:00

**Background**: Arm Neoverse is a family of 64-bit Arm processor cores specifically designed for data centers, edge computing, and high-performance computing, traditionally licensed to partners such as AWS (Graviton), Ampere, and Microsoft (Cobalt). Agentic AI refers to semi- or fully autonomous AI systems that can independently plan, use tools, and adapt to accomplish tasks—unlike traditional chatbots, they actively execute actions within an environment, often invoking multiple model calls and tool interactions per task. Hot Chips is a prestigious annual symposium held at Stanford University where leading semiconductor companies present detailed technical disclosures of their latest high-performance processors and accelerators.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/arm-dissects-agi-cpu-tailor-made-for-ai-dual-chiplets-100b-transistors-136-neoverse-v3-cores/">Arm Dissects Its AGI CPU Which Is Tailor-Made For AI: Dual Chiplets...</a></li>
<li><a href="https://en.wikipedia.org/wiki/ARM_Neoverse">ARM Neoverse - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>

</ul>
</details>

**Tags**: `#Arm`, `#data-center`, `#CPU`, `#Hot Chips 2026`, `#agentic AI`

---

<a id="item-13"></a>
## [Fujitsu’s Arm-based Monaka Data Center CPU at Hot Chips 2026](https://www.servethehome.com/fujitsus-arm-based-monaka-data-center-cpu-at-hot-chips-2026/) ⭐️ 7.5/10

Fujitsu’s Arm-based Monaka Data Center CPU at Hot Chips 2026

rss · ServeTheHome · Aug 24, 18:30

**Tags**: `#ARM`, `#Fujitsu`, `#data-center`, `#Hot-Chips-2026`, `#CPU-architecture`

---

<a id="item-14"></a>
## [Pew Research: Over One-Third of Post-ChatGPT English Web Pages Show AI Traces](https://www.solidot.org/story?sid=85172) ⭐️ 7.3/10

Pew Research Center data scientists used AI detection tools to analyze 500,000 English web pages over the past five years and found that more than one-third of pages published after ChatGPT's late-2022 launch show clear AI-generation traces. The study identified specific linguistic markers, including a doubling of em-dash usage, a 63% increase in Oxford commas, and more-than-doubled frequency of words such as "delve," "interplay," and "testament." This represents the first large-scale empirical quantification of AI's impact on the open web and raises urgent questions about information authenticity, content moderation, and trust in online sources. The uneven distribution across top-level domains—with .com pages showing roughly ten times more AI traces than .edu or .gov pages—suggests that commercial content has been far more thoroughly infiltrated by AI than educational or governmental content. In the 2026 sample, 10% of .com domains showed AI-creation traces, compared with 4.6% for .org and just 1% for .edu or .gov, even though all four domain types started with roughly equal AI-pattern frequency at ChatGPT's initial release. The contrastive rhetorical pattern "it's not just X, it's Y" nearly tripled in frequency, reinforcing that LLMs gravitate toward formulaic structured phrasing rather than purely statistical word choices.

rss · Solidot · Aug 24, 07:06

**Background**: Pew Research Center is a nonpartisan American think tank that produces empirical data on social, political, and technology trends. AI detection tools analyze text for statistical patterns characteristic of large language model output, such as unusual word frequency distributions and punctuation habits. Words like "delve," "interplay," and "testament" have become notorious "AI-tells" because they appear far more frequently in LLM-generated text than in natural human writing. The Oxford comma is the optional final comma before "and" or "or" in a list (e.g., "red, white, and blue"), while em-dashes are long dashes used to set off parenthetical or emphatic clauses—both punctuation styles have been flagged as disproportionately favored by AI writing.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/牛津逗號">牛 津 逗 号 - 维基百科，自由的百科全书</a></li>
<li><a href="https://wordvice.cn/blog/the-great-comma-debate/">英 语 标点符 号 - 牛 津 逗 号 ( oxford comma )... - Wordvice Blog</a></li>

</ul>
</details>

**Tags**: `#AI content detection`, `#Pew Research`, `#Microsoft data loss`, `#non-profit organizations`, `#web trends`

---

<a id="item-15"></a>
## [Entire City of San Francisco Recreated as Interactive 3D Video Game](https://sf.thijs.gg/) ⭐️ 7.0/10

Developer Thijs (cdngdev) launched an interactive 3D recreation of the entire city of San Francisco at sf.thijs.gg, built from mapping data that lets users drive and explore the city like a video game, complete with collectible coins. The project was shared on Twitter/X on December 9, 2025, and quickly gained traction with 326 upvotes and 115 comments. This project demonstrates a creative pipeline for converting real-world geospatial data (maps, elevation, streetview imagery) into a fully explorable game engine environment, hinting at the potential for citizen-built open-world games, urban digital twins, and new forms of location-based interactive experiences. It also illustrates how accessible tools and open data sources can enable individual developers to create projects once reserved for large studios. The recreation appears to use Apple Maps data bridged into a game engine, with driving mechanics and collectible coins for gameplay. The project is web-based and runs at sf.thijs.gg; users noted that more advanced features like DLSS upscaling, multiplayer, street name labels, and address-based teleportation would significantly enhance the experience.

hackernews · centrosphere · Aug 24, 17:05 · [Discussion](https://news.ycombinator.com/item?id=49422784)

**Background**: GIS (Geographic Information Systems) data, such as OpenStreetMap shapefiles, building footprints, digital elevation models (DEMs), and streetview imagery, can be converted into 3D environments using tools like BlenderGIS or GIS 2BLEND add-ons. These workflows typically extrude 2D building footprints into 3D meshes, apply terrain from elevation data, and texture surfaces from photographic sources. Bridging this GIS pipeline into real-time game engines like Unity or Unreal allows for interactive exploration of real-world locations, a technique increasingly used for urban planning visualization, digital twins, and game prototyping.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/domlysz/BlenderGIS">GitHub - domlysz/BlenderGIS: Blender addons to make the bridge...</a></li>
<li><a href="https://osmbuildings.org/">OSM Buildings 3 D city models and viewers</a></li>
<li><a href="https://superhivemarket.com/products/gis2blend/docs">GIS 2BLEND - Documentation - Superhive (formerly Blender Market)</a></li>

</ul>
</details>

**Discussion**: The community response was overwhelmingly enthusiastic and technical. Developers discussed the GIS-to-game-engine pipeline in detail, with jvogt describing a dream workflow combining elevation, building, maps, and streetview data with image-to-image models for texture enhancement. Former SF residents like frankhorrigan reported emotional reactions to revisiting familiar neighborhoods. Users proposed practical improvements including DLSS upscaling, multiplayer support, street name labels, and address-based teleportation, with one even requesting better underpass collision geometry in Japantown.

**Tags**: `#3d-rendering`, `#game-engine`, `#open-world`, `#creative-coding`, `#gis-movie`

---

<a id="item-16"></a>
## [RISC-V at Sixteen: From Modular ISA to Standardized Platforms at Hot Chips 2026](https://semiwiki.com/ip/sifive/372639-risc-v-at-sixteen-from-modular-isa-to-standardized-platforms-at-hot-chips-2026/) ⭐️ 7.0/10

A retrospective on RISC-V's 16-year journey from Berkeley research project to globally standardized ISA, previewing Hot Chips 2026 discussions on modularity and platform standardization.

rss · SemiWiki · Aug 24, 19:00

**Tags**: `#RISC-V`, `#ISA`, `#Hot Chips 2026`, `#SiFive`, `#hardware`

---

<a id="item-17"></a>
## [Hot Chips Highlights Evolving Memory Architectures for AI](https://semiwiki.com/semiconductor-manufacturers/372632-hot-chips-evolving-memory-architectures-for-artificial-intelligence/) ⭐️ 7.0/10

SemiWiki's coverage of Hot Chips presentations examines how next-generation memory architectures are being designed to address the memory-bandwidth bottleneck that limits AI accelerator scaling. The article frames modern AI performance as increasingly memory-bound rather than compute-bound, where scaling laws linking parameters, training data, and compute break down when processors cannot fetch operands fast enough. As AI models continue to scale toward hundreds of billions or trillions of parameters, the gap between compute throughput and memory bandwidth has become the dominant constraint on performance and efficiency. Innovations in memory architecture—such as HBM stacking, on-chip SRAM, and novel interconnect fabrics—directly determine how far AI hardware can scale, impacting chip designers, hyperscalers, and the economics of training frontier models. The publicly visible portion of the article emphasizes that contemporary accelerators are now memory-limited, meaning raw FLOPs are no longer the primary bottleneck. The full technical depth—including specific company announcements, die-stacking approaches, and benchmark results—lies behind the paywall/read-more link and cannot be evaluated here.

rss · SemiWiki · Aug 24, 17:00

**Background**: Hot Chips is a prestigious annual symposium on high-performance microprocessors and related ICs, held at Stanford since 1989. In modern AI workloads, GPUs and custom accelerators (such as TPUs) use techniques like systolic arrays and large on-chip memory to minimize costly data movement between DRAM and compute units. High Bandwidth Memory (HBM), which stacks DRAM chips vertically and uses a wide interface, is the dominant industry response to the memory bandwidth bottleneck and has become standard in AI accelerators from NVIDIA, AMD, and others.

<details><summary>References</summary>
<ul>
<li><a href="https://hotchips.org/">Hot Chips</a></li>
<li><a href="https://medium.com/b8125-fall2025/the-memory-wall-ais-silent-bottleneck-and-the-path-to-unlocking-true-intelligence-525245193c16">The Memory Wall: AI ’s Silent Bottleneck and the Path to... | Medium</a></li>
<li><a href="https://blog.kistacklab.com/en/article/hbm-memory-explained/">HBM Explained: Why High Bandwidth Memory Became... | Kistack Blog</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#memory architecture`, `#Hot Chips`, `#semiconductors`, `#accelerators`

---

<a id="item-18"></a>
## [Tiangong Ultra Humanoid Robot Beats Fastest Human in 100m Sprint](https://www.electronicsweekly.com/blogs/gadget-master/robot/picture-of-the-day-humanoid-4-0-human-2026-08/) ⭐️ 7.0/10

At the World Humanoid Robot Games in Beijing's National Stadium, the Tiangong Ultra humanoid robot surpassed the fastest human's time in the 100m sprint. The article frames the result as a symbolic "Humanoid 3 – 0 Human" milestone in the multi-sport humanoid robot competition. This represents a striking symbolic milestone in robotics, demonstrating that humanoid robots are no longer merely lab prototypes but are achieving athletic feats that surpass human capability. It signals accelerating progress in bipedal locomotion, balance, and explosive speed, with implications for future commercial deployment in logistics, manufacturing, and service roles. The article itself is extremely thin — a picture-of-the-day blurb with no performance specs, no exact sprint times, and no comparison metrics (such as Usain Bolt's 9.58s). Tiangong Ultra was developed by the Beijing Humanoid Robot Innovation Center in collaboration with UBTech, and previously completed the world's first humanoid half-marathon in 2 hours 40 minutes.

rss · Electronics Weekly · Aug 24, 15:53

**Background**: Humanoid robots are bipedal machines designed to mimic human form and movement, with applications ranging from industrial automation to scientific research. The World Humanoid Robot Games is a multi-sport competition held in Beijing where humanoid robots compete in events including sprinting, soccer, and long jump. Tiangong Ultra is one of China's flagship humanoid platforms, developed by the Beijing Humanoid Robot Innovation Center in partnership with UBTech Robotics. The robot first drew public attention when it completed a half-marathon, demonstrating sustained locomotion over long distances — a fundamentally different engineering challenge from the explosive acceleration demanded by a 100m sprint.

<details><summary>References</summary>
<ul>
<li><a href="https://humanoid.press/database/database-tiangong-ultra/">Tiangong Ultra | China’s Marathon-Running Humanoid Robot Champion</a></li>
<li><a href="https://www.aol.com/photos-beijings-world-humanoid-robot-124443007.html">Photos of Beijing 's World Humanoid Robot Games show how... - AOL</a></li>
<li><a href="https://www.roboatlas.ai/en-US/products/tiangong-ultra">X-Humanoid Tiangong Ultra Humanoid Robots Specs, Price & SDK ...</a></li>

</ul>
</details>

**Tags**: `#humanoid-robots`, `#robotics`, `#Tiangong-Ultra`, `#Beijing-Robot-Games`, `#human-vs-machine`

---

<a id="item-19"></a>
## [Quintessent begins sampling single-chip DWDM comb laser](https://www.electronicsweekly.com/news/products/quintessent-begins-sampling-single-chip-dwdm-comb-laser-2026-08/) ⭐️ 7.0/10

Quintessent begins sampling a single-chip quantum dot-based DWDM comb laser for optical interconnects, following a $40M Series A funding round.

rss · Electronics Weekly · Aug 24, 12:42

**Tags**: `#optical-interconnects`, `#photonics`, `#semiconductors`, `#DWDM`, `#data-center-infrastructure`

---

<a id="item-20"></a>
## [LG's native 1,000 Hz 1080p gaming monitor has a matching $1,000 price tag — preorders open for the 25-inch UltraGear 25G590B](https://www.tomshardware.com/monitors/gaming-monitors/lgs-native-1-000-hz-1080p-gaming-monitor-has-a-matching-usd1-000-price-tag-preorders-open-for-the-25-inch-ultragear-25g590b) ⭐️ 6.5/10

LG opens preorders for the UltraGear 25G590B, the first native 1,000 Hz 1080p gaming monitor, priced at $1,000.

rss · Tom's Hardware · Aug 24, 17:21

**Tags**: `#gaming-monitors`, `#display-technology`, `#hardware`, `#lg-ultragear`, `#product-launch`

---