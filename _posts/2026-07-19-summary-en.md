---
layout: default
title: "Horizon Summary: 2026-07-19 (EN)"
date: 2026-07-19
lang: en
---

> From 51 items, 13 important content pieces were selected

---

1. [Hacker Fits 537K Domains into $5 ESP32 Ad-Blocker Using Clever Hashing](#item-1) ⭐️ 7.5/10
2. [世界人工智能合作组织未来将重点开展三方面工作](#item-2) ⭐️ 7.3/10
3. [Alibaba's Qwen 3.8 LLM Set for Upcoming Open-Source Release](#item-3) ⭐️ 7.3/10
4. [The Kimi K3 Moment](#item-4) ⭐️ 7.0/10
5. [Zilog Z80 Turns 50 as Open-Source Replacement Heads to DIP40 Silicon](#item-5) ⭐️ 6.5/10
6. [Memory chip boss admits RAM prices are 'abnormally high' — SK Group chairman considering building a semiconductor plant in the US to expand supply, calm ‘chipflation’](#item-6) ⭐️ 6.5/10
7. [DDR5-8000 RDIMMs and MRDIMM Gen2 DDR5-12800 Demoed at Computex 2026](#item-7) ⭐️ 6.5/10
8. [商汤科技旗舰级SenseNova U1 Pro正式发布](#item-8) ⭐️ 6.3/10
9. [What I learned selling 2,500 MIDI recorders: Hardware is not so hard](#item-9) ⭐️ 6.0/10
10. [Transcribe.cpp: Open-Source C++ Speech-to-Text Library Gains Hacker News Traction](#item-10) ⭐️ 6.0/10
11. [Valve Reportedly Sells 12-15K Steam Machine Units Per Week](#item-11) ⭐️ 5.5/10
12. [‘Phantom Twist’ drone spins so fast that it is nearly invisible — flying device adds motion blur to the real world](#item-12) ⭐️ 5.5/10
13. [Russian Drones Use Magnetic Compasses as Backup Navigation](#item-13) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Hacker Fits 537K Domains into $5 ESP32 Ad-Blocker Using Clever Hashing](https://www.tomshardware.com/networking/clever-hacker-fits-537-000-domains-in-a-tiny-usd5-esp32-ad-blocking-dongle-firmware-uses-only-around-50kb-of-ram-and-can-answer-blocked-lookups-in-10-milliseconds) ⭐️ 7.5/10

A hacker has demonstrated a DNS-based ad-blocking implementation on a $5 ESP32 dongle, fitting 537,000 blocked domains into just 4MB of flash memory using only around 50KB of RAM, with blocked-lookup responses answered in approximately 10 milliseconds. This demonstrates how extremely resource-constrained hardware can deliver network-wide ad-blocking at a tiny fraction of the cost and power of commercial solutions like Pi-hole, making privacy-focused networking accessible to hobbyists with basic electronics skills. The implementation almost certainly relies on a Bloom filter, a probabilistic data structure that trades a tunable false-positive rate for dramatic memory savings; the ESP32 typically ships with 520KB SRAM and 4MB flash, so consuming only 50KB leaves substantial headroom for Wi-Fi, TCP/IP, and DNS protocol handling.

rss · Tom's Hardware · Jul 19, 10:00

**Background**: The ESP32 is a low-cost, low-power microcontroller from Espressif Systems widely used in IoT projects. DNS-based ad-blocking intercepts name-resolution queries and refuses to resolve any domain found on a blocklist, the same approach used by Pi-hole and AdGuard Home. A Bloom filter is a space-efficient probabilistic data structure, conceived by Burton Howard Bloom in 1970, that tests set membership with very small memory footprint but allows occasional false positives—meaning it might rarely block a legitimate domain but will never miss a blocked one.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bloom_filter">Bloom filter - Wikipedia</a></li>
<li><a href="https://dev.to/ashokan/bloom-filters-a-deep-dive-into-probabilistic-data-structures-5gii">Bloom Filters: A Deep Dive into Probabilistic Data Structures - DEV Community</a></li>

</ul>
</details>

**Tags**: `#embedded-systems`, `#ESP32`, `#ad-blocking`, `#DNS`, `#IoT`

---

<a id="item-2"></a>
## [世界人工智能合作组织未来将重点开展三方面工作](https://36kr.com/newsflashes/3902324507281026?f=rss) ⭐️ 7.3/10

29 countries signed an agreement in Shanghai to establish the World Artificial Intelligence Cooperation Organization, with China announcing three priority work areas focused on international AI capacity building, resource collaboration, and global AI governance.

rss · 36氪 · Jul 19, 08:58

**Tags**: `#AI governance`, `#international cooperation`, `#China AI policy`, `#global AI regulation`, `#geopolitics`

---

<a id="item-3"></a>
## [Alibaba's Qwen 3.8 LLM Set for Upcoming Open-Source Release](https://36kr.com/newsflashes/3902296634050437?f=rss) ⭐️ 7.3/10

On July 19, Alibaba announced that its latest large language model, Qwen 3.8, will soon be released and open-sourced. A preview version, Qwen3.8-Max-Preview, is already available on Alibaba Cloud's Token Plan, Qoder, and QoderWork platforms for early access. The Qwen series has been one of the most impactful open-source model families globally, and a new 2.4T-parameter release would intensify the open-weight LLM competition, particularly with Moonshot AI's Kimi K3. Open-sourcing such a large model benefits researchers, developers, and enterprises seeking alternatives to closed proprietary models. According to community discussion, Qwen 3.8 is reported to have approximately 2.4 trillion parameters, positioning it among the largest open-weight LLMs. The preview is already accessible for free via Qwen Chat and through Alibaba Cloud's Token Plan subscription, while the final open-source release is expected in the near term.

rss · 36氪 · Jul 19, 08:43

**Background**: Alibaba's Qwen (Tongyi Qianwen) model family has established itself as a leading open-source LLM lineup, with previous versions like Qwen2.5 and Qwen3 widely adopted in both research and production settings. Alibaba Cloud's Token Plan is a subscription-based service that provides bundled model usage quotas for AI coding tools such as Claude Code, Cursor, and Cline. Qoder and QoderWork are Alibaba's AI-powered development tools, with QoderWork being a desktop-level agentic assistant launched by Alibaba's Qoder team.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aliyunbaike.com/bailian/10051/">阿 里 云 百炼 Token Plan 支持哪些 AI 大 模 型 ？这张表一目了然！</a></li>
<li><a href="https://qoder.com/qoderwork">QoderWork | A desktop agentic assistant for everyone</a></li>
<li><a href="https://qoder.com.cn/">研 发 编程助手 | Qoder CN</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely positive and enthusiastic, with users welcoming the open-source release and hoping for smaller model variants suitable for local deployment (e.g., 35B MoE or 27B dense sizes). Several commenters frame the announcement as a competitive response to Moonshot AI's Kimi K3 (2.8T parameters), while also noting DeepSeek 4's imminent release. Overall, the discussion highlights growing open-source momentum and user demand for both frontier-scale and locally-runnable models.

**Tags**: `#AI`, `#LLM`, `#Open Source`, `#Alibaba`, `#Qwen`

---

<a id="item-4"></a>
## [The Kimi K3 Moment](https://stephen.bochinski.dev/blog/2026/07/18/the-kimi-k3-moment/) ⭐️ 7.0/10

Analysis of how the Kimi K3 model represents a potential inflection point where Chinese open-weight models achieve frontier-level capability, disrupting the competitive landscape dominated by Western AI labs.

hackernews · sbochins · Jul 18, 17:32 · [Discussion](https://news.ycombinator.com/item?id=48960218)

**Tags**: `#AI`, `#Kimi K3`, `#open-weight models`, `#distillation`, `#AI competition`

---

<a id="item-5"></a>
## [Zilog Z80 Turns 50 as Open-Source Replacement Heads to DIP40 Silicon](https://www.tomshardware.com/tech-industry/zilog-z80-turns-50-as-open-source-replacement-heads-for-drop-in-dip40-silicon) ⭐️ 6.5/10

The Zilog Z80, one of the most iconic 8-bit CPUs, celebrates its 50th anniversary, having been launched in July 1976 and officially discontinued in 2024. Simultaneously, an open-source drop-in replacement targeting the classic DIP40 package is preparing to move into silicon production. This milestone highlights both the enduring legacy of the Z80 in retro computing history and a growing movement to preserve classic CPU architectures through open-source silicon. Hobbyists, educators, and embedded systems developers will benefit from continued availability of a pin-compatible, modern open-source implementation. The original Z80 packed 8,500 transistors on a 4μm process node and typically ran at 2.5 MHz. The DIP40 (40-pin Dual In-line Package) is a through-hole IC package that was once an industry standard for complex logic and memory chips, offering a robust and serviceable solution before surface-mount technology became dominant.

rss · Tom's Hardware · Jul 19, 14:12

**Background**: The Zilog Z80 was designed by Federico Faggin and became one of the most popular CPUs for home computers up until the mid-1980s, typically running the CP/M operating system. It powered notable machines such as the Heathkit H89, Osborne 1, Kaypro series, TRS-80, and some Timex/Sinclair computers. The 4μm process node used in the original Z80 is generations behind modern semiconductor fabrication — today's cutting-edge nodes are measured in single-digit nanometers, meaning the open-source replacement will likely use vastly more advanced manufacturing while remaining electrically and physically compatible with legacy systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dual_in-line_package">Dual in-line package - Wikipedia</a></li>
<li><a href="https://hackaday.com/2018/06/19/federico-faggin-the-real-silicon-man/">Federico Faggin: The Real Silicon Man | Hackaday</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_semiconductor_scale_examples">List of semiconductor scale examples - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Z80`, `#retro-computing`, `#open-source-hardware`, `#CPU-architecture`, `#embedded-systems`

---

<a id="item-6"></a>
## [Memory chip boss admits RAM prices are 'abnormally high' — SK Group chairman considering building a semiconductor plant in the US to expand supply, calm ‘chipflation’](https://www.tomshardware.com/tech-industry/policy/memory-chip-boss-admits-ram-prices-are-abnormally-high-sk-group-chairman-considering-building-a-semiconductor-plant-in-the-us-to-expand-supply-calm-chipflation) ⭐️ 6.5/10

SK Group Chairman admits memory chip prices are 'abnormally high' and is considering building a semiconductor plant in the US to expand supply amid concerns about 'chipflation' and potential new market entrants.

rss · Tom's Hardware · Jul 19, 13:55

**Tags**: `#semiconductors`, `#memory`, `#SK-Hynix`, `#supply-chain`, `#hardware-pricing`

---

<a id="item-7"></a>
## [DDR5-8000 RDIMMs and MRDIMM Gen2 DDR5-12800 Demoed at Computex 2026](https://www.servethehome.com/next-gen-server-memory-on-display-ddr5-8000-rdimms-and-mrdimm-gen2-hits-ddr5-12800/) ⭐️ 6.5/10

At Computex 2026, Micron showcased DDR5-8000 RDIMMs while Samsung demonstrated second-generation MRDIMMs reaching 12,800 MT/s, highlighting the next leap in server memory speeds. Faster server memory is critical for AI/ML workloads and data center applications where memory bandwidth bottlenecks can limit performance, and these speeds represent a significant step forward in addressing that challenge. MRDIMM Gen2 uses multiplexing techniques that allow DRAM chips to operate at their native data rate while effectively doubling the memory channel frequency. The JEDEC MRDIMM Gen 2 standard is nearing completion, with a new Multiplexed Rank Registering Clock Driver designed to improve signal integrity and timing control.

rss · ServeTheHome · Jul 18, 17:00

**Background**: RDIMMs (Registered DIMMs) are the standard server memory modules featuring a register buffer chip for improved signal stability and reliability. MRDIMMs (Multiplexed Rank DIMMs) are a newer type that use multiplexing between the host memory channel and the DRAM chips, enabling much higher effective data rates than conventional RDIMMs while keeping the underlying DRAM operating at native speeds. Both module types target AI, HPC, and data center workloads where memory bandwidth is a key performance constraint.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tweaktown.com/news/111452/jedec-pushes-ddr5-server-memory-to-12800-mt-s-with-new-mrdimm-gen2-standard-for-ai-and-data-center-workloads/index.html">JEDEC pushes DDR5 server memory to 12,800 MT/s with new...</a></li>
<li><a href="https://www.industrysourcing.com/article/476129">JEDEC pushes DDR5 memory performance to new heights with...</a></li>
<li><a href="https://arxiv.org/html/2605.02371">Performance and Energy Benefits of MRDIMMs</a></li>

</ul>
</details>

**Tags**: `#DDR5`, `#server memory`, `#MRDIMM`, `#RDIMM`, `#Computex 2026`

---

<a id="item-8"></a>
## [商汤科技旗舰级SenseNova U1 Pro正式发布](https://36kr.com/newsflashes/3902187700766593?f=rss) ⭐️ 6.3/10

SenseTime officially released its flagship multimodal large model SenseNova U1 Pro, featuring unified understanding, generation, and action capabilities with delivery-grade image creation.

rss · 36氪 · Jul 19, 06:30

**Tags**: `#multimodal-ai`, `#sense-time`, `#large-language-models`, `#chinese-ai`, `#product-launch`

---

<a id="item-9"></a>
## [What I learned selling 2,500 MIDI recorders: Hardware is not so hard](https://chipweinberger.com/articles/20260719-hardware-is-not-so-hard) ⭐️ 6.0/10

A hardware entrepreneur shares lessons learned from selling 2,500 MIDI recorder devices, arguing that hardware development is more accessible than commonly believed.

hackernews · chipweinberger · Jul 19, 10:34 · [Discussion](https://news.ycombinator.com/item?id=48966713)

**Tags**: `#hardware`, `#entrepreneurship`, `#manufacturing`, `#product-development`, `#midi`

---

<a id="item-10"></a>
## [Transcribe.cpp: Open-Source C++ Speech-to-Text Library Gains Hacker News Traction](https://workshop.cjpais.com/projects/transcribe-cpp) ⭐️ 6.0/10

Transcribe.cpp, an open-source C/C++ speech-to-text inference library developed through Mozilla.ai's Builders in Residence program, has been gaining significant traction on Hacker News with 611 upvotes and 130 comments. The tool provides portable, GPU-accelerated support for multiple STT models and is designed to make adding fast, local transcription to applications easier. This release matters because local, open-source STT infrastructure reduces dependence on cloud APIs and gives developers fine-grained control over model selection and deployment. The community discussion highlights gaps that proprietary solutions fail to address, including phonetic transcription for endangered languages and seamless continuous dictation workflows. The library uses GGUF format models and includes a transcribe-quantize tool for producing smaller model variants. It supports multiple STT model architectures and offers cross-platform portability, making it suitable for embedding into desktop applications like the macOS virtual camera app Emyn.

hackernews · sebjones · Jul 19, 00:38 · [Discussion](https://news.ycombinator.com/item?id=48963879)

**Background**: Speech-to-text (STT) technology converts spoken language into written text and is commonly used for transcription, voice assistants, and accessibility. Most STT systems rely on large neural network models that traditionally required cloud processing, though recent advances have made local inference feasible on consumer hardware. The ggml ecosystem, which includes projects like llama.cpp, has been instrumental in enabling efficient on-device AI inference across platforms. Mozilla.ai's Builders in Residence program supports independent developers working on open-source AI tooling.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/handy-computer/transcribe.cpp/">GitHub - handy-computer/ transcribe . cpp : ggml speech - to - text ...</a></li>
<li><a href="https://blog.mozilla.ai/announcing-transcribe-cpp/">Announcing transcribe . cpp</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion surfaced several substantive themes: rmunn noted the absence of IPA-based phonetic transcription needed for documenting minority languages with fewer than 10,000 speakers; abdullahkhalids highlighted the lack of continuous dictation workflows that type into documents at the cursor in real time; ghm2199 raised concerns about the sustainability and funding of open-source STT projects; and terhechte praised the library's easy integration into their macOS virtual camera app Emyn.

**Tags**: `#speech-to-text`, `#transcription`, `#cpp`, `#open-source`, `#linguistics`

---

<a id="item-11"></a>
## [Valve Reportedly Sells 12-15K Steam Machine Units Per Week](https://www.techpowerup.com/350872/valve-reportedly-sells-12-15k-steam-machine-units-per-week) ⭐️ 5.5/10

Valve reportedly sells 12,000-15,000 Steam Machine units per week based on estimated revenue derived from Steam's Global Top Sellers rankings.

rss · TechPowerUp News · Jul 18, 21:38

**Tags**: `#Steam Machine`, `#Valve`, `#gaming hardware`, `#PC gaming`, `#sales data`

---

<a id="item-12"></a>
## [‘Phantom Twist’ drone spins so fast that it is nearly invisible — flying device adds motion blur to the real world](https://www.tomshardware.com/tech-industry/drones/phantom-twist-drone-spins-so-fast-that-it-is-nearly-invisible-flying-device-adds-motion-blur-to-the-real-world) ⭐️ 5.5/10

Northwestern University researchers built a drone that spins so rapidly it appears nearly invisible due to motion blur, creating a rudimentary form of visual cloaking.

rss · Tom's Hardware · Jul 19, 13:27

**Tags**: `#drones`, `#robotics`, `#motion-blur`, `#cloaking`, `#research`

---

<a id="item-13"></a>
## [Russian Drones Use Magnetic Compasses as Backup Navigation](https://www.tomshardware.com/tech-industry/drones/russian-drones-spotted-using-screwed-on-magnetic-compasses-as-navigation-aids-the-on-board-camera-can-occasionally-tilt-down-to-check-bearings-if-satellite-comms-are-lost) ⭐️ 5.5/10

Russian drone operators have been observed screwing cheap magnetic compasses onto their drones as improvised backup navigation aids. When satellite communications are lost, the drone's onboard camera can occasionally tilt downward to visually verify bearings, allowing the operator to maintain directional awareness without GPS. This crude workaround highlights how electronic warfare and GPS jamming on the modern battlefield force militaries to develop low-cost, redundant navigation methods. It also illustrates the gap between sophisticated commercial GPS-denied solutions (which use AI-based visual-inertial odometry) and what can be rapidly field-deployed in a conflict zone. The compass is a cheap, off-the-shelf component physically screwed onto the airframe rather than integrated into the flight controller, meaning its readings must be manually cross-checked via the camera's downward view. This approach is far less accurate than proper sensor fusion or visual-inertial odometry systems, and magnetic interference from the drone's own motors and electronics can degrade readings significantly.

rss · Tom's Hardware · Jul 19, 12:05

**Background**: Modern military drones typically rely on GPS or GLONASS satellite navigation for waypoint following and targeting, but both sides in the Russia-Ukraine conflict have extensively deployed GPS jamming and spoofing systems. GPS-denied navigation is therefore a critical capability, and commercial solutions such as visual-inertial odometry (VIO) modules and AI-based terrain matching are increasingly available. The magnetic compass approach is a much cruder alternative that trades precision for simplicity and cost.

<details><summary>References</summary>
<ul>
<li><a href="https://www.spleenlab.ai/solutions-for-gps-denied-navigation">GPS - Denied Navigation Solutions for Drones | Spleenlab</a></li>
<li><a href="https://oksi.ai/omninav-gps-denied-navigation/">OMNInav: A Breakthrough in GPS - Denied Navigation for UAS - OKSI</a></li>
<li><a href="https://pilotinstitute.com/heavy-interference-drones/">Flying Your Drone in Urban Areas with Heavy Signal Interference</a></li>

</ul>
</details>

**Tags**: `#drones`, `#navigation`, `#military-tech`, `#GPS-denied`, `#hardware-quirks`

---