---
layout: default
title: "Horizon Summary: 2026-08-04 (EN)"
date: 2026-08-04
lang: en
---

> From 107 items, 20 important content pieces were selected

---

1. [AMD Unveils Helios: First Rackscale AI Platform with 72 MI455X GPUs](#item-1) ⭐️ 8.5/10
2. [Neural network autonomously controls satellite bus in orbit](#item-2) ⭐️ 8.0/10
3. [Sandisk and SK hynix Release First OCP Specification for High Bandwidth Flash](#item-3) ⭐️ 7.5/10
4. [TSMC Targets 100,000 N2 Wafers per Month by the End of 2026](#item-4) ⭐️ 7.5/10
5. [AI Enthusiast Uses Claude Code to Bypass BIOS RSA-2048 Signature Checks, Unlocks 55 Hidden Settings](#item-5) ⭐️ 7.5/10
6. [Co-Packaged Optics (CPO) foundry roadmaps — breaking down TSMC, Intel, Samsung, and GlobalFoundries' approach to next-generation scale-up connectivity](#item-6) ⭐️ 7.5/10
7. [AI Significantly Reduces Customer Service Jobs at Major Companies](#item-7) ⭐️ 7.3/10
8. [LLMs reward expertise](#item-8) ⭐️ 7.0/10
9. [Ten advances in mathematics and theoretical computer science](#item-9) ⭐️ 7.0/10
10. [Cloudflare's FP8 KV Cache Quantization for Serving Kimi and GLM at Scale](#item-10) ⭐️ 7.0/10
11. [MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, and 2K Video](#item-11) ⭐️ 7.0/10
12. [Andy Pavlo joins ClickHouse to establish ClickHouse Labs](#item-12) ⭐️ 7.0/10
13. [Renesas Tackles Memory Bottleneck with MRDIMM Update](#item-13) ⭐️ 7.0/10
14. [Video Interview: ChipAgents CEO on Latest Funding for Agentic AI in EDA](#item-14) ⭐️ 7.0/10
15. [TSMC Ahead of Schedule on $49B 1.4nm Fab Construction](#item-15) ⭐️ 7.0/10
16. [NVIDIA RTX 50 Series GPUs Face 20-30% Price Hike in South Korea](#item-16) ⭐️ 6.5/10
17. [Kioxia Announces GP1 Series PCIe 6.0 NVMe SSDs for AI Workloads](#item-17) ⭐️ 6.5/10
18. [CXMT Reportedly Plans Second Fab in Beijing to Boost DRAM Output](#item-18) ⭐️ 6.5/10
19. [AI companies slash token prices amid fierce competition from Chinese models](#item-19) ⭐️ 6.5/10
20. [Gaming on the 4GB Radeon RX 6500 XT and GTX 1650 Super in 2026 — upscaling makes low-end GPUs viable for esports and internet cafes](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [AMD Unveils Helios: First Rackscale AI Platform with 72 MI455X GPUs](https://www.servethehome.com/amd-helios-architecture-deep-dive-amd-broadcom-hardware-combined/) ⭐️ 8.5/10

AMD unveiled its Helios rackscale architecture at Advancing AI 2026, integrating 72 Instinct MI455X accelerators into a single unified system — marking AMD's first rackscale AI datacenter platform. The design tightly co-designs AMD's CPUs, GPUs, and networking around the data path of an AI workload. Helios represents AMD's direct challenge to NVIDIA's NVL72-class rackscale systems, signaling AMD's emergence as a serious full-stack AI infrastructure competitor. By using the open UALink standard over Ethernet instead of a proprietary fabric, AMD positions Helios as a vendor-neutral alternative that could reshape hyperscaler procurement strategies. The MI455X is equipped with HBM4 memory, and the 72 accelerators communicate via UALink over Ethernet — distinguishing AMD's approach from NVIDIA's proprietary NVLink. Helios has entered full production, with rack shipments scheduled for Q3 2026, and the platform targets 64-bit Linux environments.

rss · ServeTheHome · Aug 3, 19:00

**Background**: Rackscale architecture treats an entire server rack — compute, memory, storage, and networking — as a single coherent system rather than as independently assembled servers. NVIDIA pioneered this model with its NVL72 system, which links 72 GPUs using proprietary NVLink technology. UALink (Ultra Accelerator Link) is an industry-backed open interconnect standard designed to enable high-speed, vendor-neutral communication among accelerators from multiple vendors. The MI455X is AMD's next-generation data center GPU, positioned to compete with NVIDIA's Rubin generation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/products/rackscale-solutions/helios.html">AMD Helios Rackscale Solution – Powering Frontier AI</a></li>
<li><a href="https://www.amd.com/en/blogs/2026/amd-launches-helios-the-highest-performing-rackscale-ai-infrastructure-solution.html">AMD Launches Helios™: The Highest Performing Rackscale AI Infrastructure Solution</a></li>
<li><a href="https://www.networkworld.com/article/4204533/amd-unveils-ai-gpu-to-challenge-nvidias-rubin.html">AMD unveils AI GPU to challenge Nvidia’s Rubin | Network World</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#Helios`, `#rackscale`, `#MI455X`, `#AI-infrastructure`

---

<a id="item-2"></a>
## [Neural network autonomously controls satellite bus in orbit](https://www.electronicsweekly.com/news/neural-network-controls-satellite-bus-in-orbit-2026-08/) ⭐️ 8.0/10

The US Air Force Research Laboratory (AFRL) has demonstrated autonomous control of a satellite bus using a neural network in orbit, marking what the organisation describes as a pivotal shift toward AI-driven spacecraft operations. This demonstration represents a significant milestone for onboard AI in space, with implications for defence, autonomous space operations, and the broader deployment of edge AI in resource-constrained orbital environments where real-time ground intervention is impractical. The source article is truncated and does not disclose the neural network architecture, specific mission parameters, or failure modes, limiting deeper technical assessment. The AFRL demonstration sits alongside other orbital edge AI efforts, such as Open Cosmos's HAMMER and Φ-Sat-2 missions and EDGX's onboard edge AI compute platforms.

rss · Electronics Weekly · Aug 3, 09:08

**Background**: A satellite bus is the main structural body of a spacecraft that houses the payload and scientific instruments, typically managing power, propulsion, thermal control, and intra-spacecraft communications. Historically, satellites have functioned largely as 'bent pipes,' collecting raw data and relaying it to ground stations for processing. Orbital edge AI flips this model by running neural networks directly on the spacecraft, enabling autonomous decision-making, faster response times, and reduced dependence on ground control — capabilities increasingly critical for defence and time-sensitive applications such as disaster response.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Satellite_bus">Satellite bus - Wikipedia</a></li>
<li><a href="https://blacknightspacelabs.com/blog/orbital-edge-ai-onboard-satellite-processing-cognisat-space-ai-vpu-inference-bent-pipe-bottleneck">Orbital Edge AI & On - Board Satellite ... | BlacKnight Space Labs</a></li>

</ul>
</details>

**Tags**: `#neural-networks`, `#satellite`, `#autonomous-systems`, `#space-tech`, `#edge-AI`

---

<a id="item-3"></a>
## [Sandisk and SK hynix Release First OCP Specification for High Bandwidth Flash](https://www.techpowerup.com/351335/sandisk-and-sk-hynix-advance-global-standardization-of-high-bandwidth-flash-with-release-of-first-ocp-technical-specification) ⭐️ 7.5/10

Sandisk and SK hynix, together with Google and Tenstorrent, released the first OCP technical specification for High Bandwidth Flash (HBF) memory, just six months after the consortium began work in February 2025. The specification defines two capacity configurations (8-layer and 16-layer NAND stacking, up to 512GB) and three bandwidth grades (Grade 1–3) covering approximately 0.4 TB/s to 3.0 TB/s. HBF is positioned as a new memory tier between HBM and SSDs, offering NAND flash's high density at near-HBM bandwidth levels, which is critical for AI inference workloads that demand large memory capacity. Standardization through OCP with backing from major players like Google and Tenstorrent signals real industry momentum and could accelerate ecosystem adoption, potentially easing the cost and supply constraints of HBM in AI accelerators. HBF is built on Sandisk's low-cost, high-density CBA-based NAND core technology with 3D stack packaging, reportedly delivering performance within about 2.2% of unlimited-capacity HBM while significantly increasing capacity. The specification targets AI inference scenarios where larger, near-compute memory capacity and higher bandwidth are needed to improve power, performance, and total cost of ownership.

rss · TechPowerUp News · Aug 4, 01:46

**Background**: The Open Compute Project (OCP) is a non-profit organization that creates open-source data center hardware specifications to foster industry collaboration, reduce costs, and accelerate innovation. High Bandwidth Memory (HBM) is the current standard for high-performance AI accelerators, but it is expensive and capacity-limited due to its use of DRAM. High Bandwidth Flash (HBF) is a new class of NAND flash memory using advanced packaging and interfaces to deliver bandwidth comparable to HBM while offering much higher capacity and lower cost per gigabyte—making it particularly suited for AI inference, which typically requires large model and context storage rather than the extreme bandwidth of HBM-focused training.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sandisk.com/company/newsroom/blogs/2025/scaling-beyond-the-wall-inside-sandisks-high-bandwidth-flash-for-ai">Scaling the Memory Wall: Behind Sandisk’s High Bandwidth Flash for AI Inferencing | Sandisk</a></li>
<li><a href="https://documents.sandisk.com/content/dam/asset-library/en_us/assets/public/sandisk/collateral/company/Sandisk-HBF-Fact-Sheet.pdf">HIGH BANDWIDTH FLASH</a></li>
<li><a href="https://www.emergentmind.com/topics/high-bandwidth-flash-hbf">High Bandwidth Flash (HBF) Overview</a></li>
<li><a href="https://www.gigabyte.com/glossary/ocp">What Is OCP and How Does It Work? - GIGABYTE Global</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#memory technology`, `#OCP`, `#HBF`, `#industry standardization`

---

<a id="item-4"></a>
## [TSMC Targets 100,000 N2 Wafers per Month by the End of 2026](https://www.techpowerup.com/351326/tsmc-targets-100-000-n2-wafers-per-month-by-the-end-of-2026) ⭐️ 7.5/10

TSMC aims to scale its 2nm N2 wafer production from 20,000 to 100,000 wafers per month by end of 2026, growing the node's revenue share from 3% to over 10%.

rss · TechPowerUp News · Aug 3, 17:12

**Tags**: `#semiconductors`, `#TSMC`, `#manufacturing`, `#2nm`, `#chip-industry`

---

<a id="item-5"></a>
## [AI Enthusiast Uses Claude Code to Bypass BIOS RSA-2048 Signature Checks, Unlocks 55 Hidden Settings](https://www.tomshardware.com/laptops/ai-enthusiast-mods-bios-with-claude-code-ai-defeats-rsa-2048-signature-checks-and-unlocks-55-hidden-settings) ⭐️ 7.5/10

A Redditor used Anthropic's Claude Code to reverse-engineer their HP laptop's BIOS firmware, bypass the RSA-2048 DXE-FV signature verification check, and unlock 55 hidden setup fields along with four advanced BIOS configuration tabs on their own hardware. This case demonstrates that current AI coding agents can meaningfully assist with low-level firmware reverse engineering and binary analysis—tasks that previously demanded deep specialized expertise. It also raises broader questions about how AI tools will reshape both offensive security research and defensive firmware hardening across the industry. The work involved three layers of patches: bypassing the RSA-2048 signature check in the DXE firmware volume phase, exposing 55 hidden setup fields, and revealing additional BIOS configuration tabs. Importantly, the RSA-2048 cryptographic algorithm itself was not broken—the specific signature verification routine in the firmware was circumvented, which is a meaningful distinction.

rss · Tom's Hardware · Aug 3, 11:55

**Background**: BIOS is low-level firmware on a PC that initializes hardware before the operating system loads, and it typically contains hidden settings (such as advanced power, virtualization, or diagnostic options) that manufacturers restrict to business or enterprise users. RSA-2048 is an asymmetric cryptographic algorithm using 2048-bit keys, widely used to digitally sign firmware so that a device will only boot code approved by the manufacturer. Claude Code is Anthropic's agentic coding tool that runs in the terminal, reads codebases, and can execute commands—making it well-suited to multi-step tasks like disassembling binaries and generating patch scripts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/laptops/ai-enthusiast-mods-bios-with-claude-code-ai-defeats-rsa-2048-signature-checks-and-unlocks-55-hidden-settings">AI enthusiast unlocks and mods BIOS with Claude Code — AI defeats RSA-2048 signature checks and unlocks 55 hidden settings | Tom's Hardware</a></li>
<li><a href="https://x.com/cyber_razz/status/2079834248794493194">Abdulkadir | Cybersecurity on X: "A Reddit user gave Claude Code their HP laptop's BIOS dump. Asked it to unlock the firmware. Claude disassembled the signature-check code. Found the RSA-2048 verification function. Then wrote a Python script to bypass it. The user modified the BIOS. Flashed it back. Got https://t.co/VmpMQVbOjS" / X</a></li>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code overview - Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude Code`, `#BIOS hacking`, `#reverse engineering`, `#security`

---

<a id="item-6"></a>
## [Co-Packaged Optics (CPO) foundry roadmaps — breaking down TSMC, Intel, Samsung, and GlobalFoundries' approach to next-generation scale-up connectivity](https://www.tomshardware.com/tech-industry/artificial-intelligence/co-packaged-optics-cpo-foundry-roadmaps-breaking-down-tsmc-intel-samsung-and-globalfoundries-approach-to-next-generation-scale-up-connectivity) ⭐️ 7.5/10

Analysis of how TSMC, Intel, Samsung Foundry, and GlobalFoundries are each pursuing different co-packaged optics strategies to enable next-generation optical connectivity for AI scale-up systems.

rss · Tom's Hardware · Aug 3, 11:45

**Tags**: `#co-packaged-optics`, `#semiconductors`, `#AI-infrastructure`, `#foundry-roadmaps`, `#photonics`

---

<a id="item-7"></a>
## [AI Significantly Reduces Customer Service Jobs at Major Companies](https://www.solidot.org/story?sid=84994) ⭐️ 7.3/10

Major companies including Microsoft, Commonwealth Bank of Australia (CBA), Uber, and Hyatt are substantially cutting customer service headcount through AI-powered automation. Microsoft reduced its customer service team from approximately 50,000 to 40,000, saving about $750 million annually, while Hyatt cut 30% of its internal Americas customer service staff and Uber eliminated 10% of its customer service positions. With analysts projecting that nearly half of all customer service positions could be affected by 2030, this trend could disrupt millions of call center workers concentrated in the US, India, and the Philippines—countries that previously benefited from Western companies outsourcing customer service in English. The displacement may also reshape global labor markets and challenge the long-established business model of offshore customer support outsourcing. Microsoft's sales and service operations lead Judson Althoff noted that complex issues still require human support, but the company is continuously expanding the scope of automated resolution. CBA cut hundreds of customer service roles and expects to save tens of millions of dollars annually. The shift is driven both by improvements in generative AI capability and by executive pressure to adopt new technologies to reduce costs.

rss · Solidot · Aug 3, 14:22

**Background**: The call center industry is a major global employer, with millions of workers in countries like the Philippines and India, which became dominant outsourcing destinations because of their English-speaking workforces. Generative AI tools—including large language models and conversational AI platforms—now enable companies to automate chat and phone interactions that previously required human agents. Platforms like Zendesk and others have built AI-first customer service workflows that resolve issues across multiple channels without human intervention.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zendesk.com/">AI -Powered Service Platform | Zendesk</a></li>

</ul>
</details>

**Tags**: `#AI`, `#automation`, `#customer-service`, `#labor-market`, `#industry-trends`

---

<a id="item-8"></a>
## [LLMs reward expertise](https://www.seangoedecke.com/llms-reward-expertise/) ⭐️ 7.0/10

Article arguing that LLMs produce significantly better outputs for users with domain expertise, as experts can craft better prompts, provide better context, and critically evaluate responses, effectively making LLMs an 'amplifying mirror' of user capability.

hackernews · MaxMussio · Aug 3, 21:13 · [Discussion](https://news.ycombinator.com/item?id=49161518)

**Tags**: `#LLMs`, `#AI`, `#prompt-engineering`, `#expertise`, `#human-AI-interaction`

---

<a id="item-9"></a>
## [Ten advances in mathematics and theoretical computer science](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 7.0/10

OpenAI announces ten advances where AI models contributed to mathematics and theoretical computer science, including conjectures and proofs, with community debating implications for the future of mathematical research.

hackernews · milkshakes · Aug 3, 16:27 · [Discussion](https://news.ycombinator.com/item?id=49157930)

**Tags**: `#AI`, `#mathematics`, `#OpenAI`, `#research`, `#reasoning`

---

<a id="item-10"></a>
## [Cloudflare's FP8 KV Cache Quantization for Serving Kimi and GLM at Scale](https://blog.cloudflare.com/smaller-faster-safer-models/) ⭐️ 7.0/10

Cloudflare published a technical deep-dive detailing how it efficiently serves open-weight models Kimi (by Moonshot AI) and GLM (by Zhipu AI) at scale, with a focus on FP8 KV cache quantization and other inference optimizations to reduce memory footprint and improve throughput. As open-weight Chinese models gain global traction, the infrastructure choices made by major providers like Cloudflare directly affect latency, cost, and quality for developers building on top of these models. FP8 KV cache quantization is a critical lever for fitting large models onto limited GPU memory, and Cloudflare's public discussion offers rare transparency into a practice that many providers apply silently. FP8 KV cache quantization stores cached Key and Value tensors in 8-bit floating point instead of FP16/BF16, yielding roughly 2× memory savings on attention caches, and can be enabled independently of weight quantization (as documented in vLLM and TensorRT Edge-LLM). The post also references additional optimizations for fitting large MoE architectures like GLM-4.5/GLM-5 onto commodity GPUs.

hackernews · ascorbic · Aug 3, 17:08 · [Discussion](https://news.ycombinator.com/item?id=49158581)

**Background**: The KV cache is a per-request memory structure that stores previously computed Key and Value projections for each token in a transformer, enabling efficient autoregressive generation without re-computing attention over the full context. As context lengths grow into the hundreds of thousands of tokens, the KV cache often dominates GPU memory usage, making quantization of the cache itself a high-leverage optimization. Kimi is a long-context LLM family from Chinese startup Moonshot AI, while GLM is Zhipu AI's open-weight flagship model line, including the Mixture-of-Experts GLM-4.5 and GLM-5 (~745B parameters, 44B active).

<details><summary>References</summary>
<ul>
<li><a href="https://llm-academy.dev/kv-cache-quant/">KV Cache Quantization Explained... | LLM Academy</a></li>
<li><a href="https://docs.vllm.ai/projects/llm-compressor/en/0.9.0/examples/quantization_kv_cache/">fp 8 Weight, Activation, and KV Cache Quantization - LLM ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The discussion is mixed: several commenters praise Cloudflare's transparency about KV cache quantization, noting that many providers apply such optimizations silently while marketing unquantized weights, and ask for more thorough evaluation across model families. Others raise concerns about Cloudflare's lack of Zero Data Retention (ZDR) on its inference service as a privacy/trust issue, question the choice of int4 over nf4, complain about hidden pricing, and inquire about hiring.

**Tags**: `#LLM inference`, `#quantization`, `#model serving`, `#Cloudflare`, `#KV cache`

---

<a id="item-11"></a>
## [MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, and 2K Video](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui) ⭐️ 7.0/10

An open-weights video generation model with native audio, 2K support, and notable weight pruning optimization launches with immediate ComfyUI integration.

hackernews · vblanco · Aug 3, 13:34 · [Discussion](https://news.ycombinator.com/item?id=49155629)

**Tags**: `#video-generation`, `#open-weights`, `#comfyui`, `#multimodal-ai`, `#model-compression`

---

<a id="item-12"></a>
## [Andy Pavlo joins ClickHouse to establish ClickHouse Labs](https://clickhouse.com/blog/andy-pavlo-joins-clickhouse) ⭐️ 7.0/10

Prominent CMU database researcher Andy Pavlo joins ClickHouse to establish ClickHouse Labs, signaling the company's commitment to fundamental database systems research.

hackernews · nikolay_sivko · Aug 3, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49156011)

**Tags**: `#database-systems`, `#clickhouse`, `#industry-news`, `#research`, `#olap`

---

<a id="item-13"></a>
## [Renesas Tackles Memory Bottleneck with MRDIMM Update](https://www.eetimes.com/renesas-tackles-memory-bottleneck-with-mrdimm-update/) ⭐️ 7.0/10

Renesas announces Gen 3 DDR5 MRDIMMs delivering 16,000 MT/s bandwidth to address memory bottlenecks in AI workloads without requiring a platform redesign.

rss · EE Times · Aug 3, 19:00

**Tags**: `#MRDIMM`, `#DDR5`, `#memory-bandwidth`, `#AI-infrastructure`, `#Renesas`

---

<a id="item-14"></a>
## [Video Interview: ChipAgents CEO on Latest Funding for Agentic AI in EDA](https://www.eetimes.com/video-interview-chipagents-ceo-on-latest-funding-for-agentic-ai-in-eda/) ⭐️ 7.0/10

ChipAgents raises $60M to pursue autonomous agentic AI for chip design automation, positioning itself against traditional copilot-style EDA tools.

rss · EE Times · Aug 3, 14:07

**Tags**: `#agentic-ai`, `#eda`, `#chip-design`, `#funding`, `#ai-agents`

---

<a id="item-15"></a>
## [TSMC Ahead of Schedule on $49B 1.4nm Fab Construction](https://www.electronicsweekly.com/news/business/tsmc-ahead-of-schedule-with-1-4nm-fab-2026-08/) ⭐️ 7.0/10

TSMC is ahead of schedule in constructing its $49 billion 1.4nm fab at the Central Taiwan Science Park in Taichung, according to the Commercial Times. Construction on the facility began in November 2025. As one of the world's most advanced semiconductor fabs, an on-schedule or ahead-of-schedule 1.4nm (A14) node is critical for next-generation AI accelerators, high-performance computing, and consumer chips. The $49 billion investment scale also reflects the escalating capital requirements of leading-edge fabrication and TSMC's determination to maintain its process leadership over rivals like Samsung and Intel. The 1.4nm node is officially branded as 'A14' by TSMC and is expected to enter high-volume manufacturing around 2027–2028. It relies heavily on Extreme Ultraviolet (EUV) lithography and will succeed the N2 (2nm) node, which is scheduled for late 2025.

rss · Electronics Weekly · Aug 3, 05:15

**Background**: In semiconductor manufacturing, process 'node' names like 1.4nm no longer correspond to any physical transistor dimension—they are marketing labels representing successive generations of transistor density and performance improvements. TSMC's roadmap runs N3 (3nm) → N2 (2nm) → A14 (1.4nm), with each node offering gains in power efficiency, transistor density, and performance. The construction of cutting-edge fabs is extraordinarily capital-intensive, often costing tens of billions of dollars, partly due to the enormous expense of EUV lithography tools from ASML, which can cost over $200 million each. A14 is expected to be especially important for AI workloads, where computational density and energy efficiency are paramount.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phonearena.com/news/tsmc-says-what-follows-2nm-node_id153534">For the first time, TSMC reveals what will follow the 2 nm node</a></li>
<li><a href="https://electrazine.com/the-next-leap-in-semiconductors-the-1-4nm-process-node/">The Next Leap in Semiconductors : The 1 . 4 nm Process Node ...</a></li>

</ul>
</details>

**Tags**: `#TSMC`, `#semiconductors`, `#1.4nm`, `#fabrication`, `#industry-news`

---

<a id="item-16"></a>
## [NVIDIA RTX 50 Series GPUs Face 20-30% Price Hike in South Korea](https://www.techpowerup.com/351329/nvidia-geforce-rtx-50-series-faces-30-price-increase-in-south-korea) ⭐️ 6.5/10

NVIDIA's GeForce RTX 50 series GPUs are rumored to see a 20-30% price increase in South Korea due to rapidly rising GDDR7 memory costs from suppliers. South Korean importers and distributors have already informed the supply chain about the upcoming price hike, which could reach up to 30% depending on the model. This price increase affects the entire RTX 50 lineup, with premium models bearing the biggest impact, potentially pushing the RTX 5090 past $5,100 in South Korea. Even though South Korea hosts major DRAM producers like SK hynix and Samsung, no one is exempt from these rising costs, signaling broader GPU pricing pressure that could spread to other markets. NVIDIA bundles GDDR7 memory with the GPU die as a kit for its AIB partners, so any memory cost increase directly affects board partners and consumers. With each 2GB GDDR7 module costing in the low $20s and the RTX 5090 requiring 16 modules, NVIDIA spends at least $320 on GDDR7 alone for its flagship card, before accounting for the GPU die, R&D, and AIB margins.

rss · TechPowerUp News · Aug 3, 18:47

**Background**: GDDR7 is the latest generation of graphics double data rate memory, offering higher bandwidth than GDDR6 and GDDR6X for high-performance GPUs. Add-in Board (AIB) partners are companies like ASUS, MSI, and Gigabyte that purchase GPU dies and components from NVIDIA and manufacture retail graphics cards. The RTX 50 series is NVIDIA's latest consumer GPU lineup, with the RTX 5090 being the flagship model featuring 32GB of GDDR7 memory.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/in-a-troubling-sign-nvidia-rtx-50-series-prices-jump-up-to-30-percent-in-south-korea-tsmc-wafer-hikes-and-usd20-gddr7-modules-push-rtx-5090-past-usd5-100">In a troubling sign, Nvidia RTX 50 series prices jump... | Tom's Hardware</a></li>
<li><a href="https://grokipedia.com/page/Add-in_board">Add - in board</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#RTX-50-series`, `#GPU-pricing`, `#GDDR7-memory`, `#hardware-news`

---

<a id="item-17"></a>
## [Kioxia Announces GP1 Series PCIe 6.0 NVMe SSDs for AI Workloads](https://www.techpowerup.com/351318/kioxia-announces-gp1-series-super-high-iops-ssds-for-ai-applications) ⭐️ 6.5/10

Kioxia announced the GP1 Series, its first PCIe 6.0 NVMe SSD delivering up to 10 million random read IOPS using XL-FLASH generation 2 low-latency flash memory, designed to extend HBM as a flash-based memory tier for AI systems. Evaluation samples will be available to select customers by the end of 2026, with a public showcase at FMS 2026 in Santa Clara. The GP1 targets a critical bottleneck in AI infrastructure: GPU memory capacity. By offering a high-IOPS flash tier that sits between HBM4 and conventional NAND, it promises to expand the effective memory pool available to GPUs at a fraction of the cost of adding more HBM, directly addressing the economics of large-context and retrieval-heavy AI workloads. Key specifications include PCIe 6.0 interface, GPU direct access support, 10M random read IOPS, and use of XL-FLASH Gen 2 — Kioxia's low-latency NAND-based Storage Class Memory. The product is positioned as a HBM-extension tier rather than a general-purpose SSD, and won't reach evaluation customers until late 2026.

rss · TechPowerUp News · Aug 3, 14:47

**Background**: XL-FLASH is Kioxia's low-latency NAND-based Storage Class Memory (SCM), positioned between DRAM and conventional NAND in the memory hierarchy to deliver much faster access than typical SSDs. High Bandwidth Memory (HBM) is a 3D-stacked DRAM technology used in GPUs and AI accelerators, with HBM4 being the latest generation powering next chips such as NVIDIA Rubin. Memory tiering — combining HBM, SCM-class flash, and bulk NAND — is increasingly important for AI workloads whose working sets exceed on-package GPU memory, and PCIe 6.0 doubles per-lane bandwidth versus PCIe 5.0, which is needed to keep such flash tiers fed at the IOPS levels AI systems require.

<details><summary>References</summary>
<ul>
<li><a href="https://www.storagereview.com/news/kioxia-gp1-series-hits-10-million-random-read-iops-on-xl-flash-gen-2">KIOXIA GP1 Series Hits 10 Million Random Read IOPS on XL - FLASH ...</a></li>
<li><a href="https://blog-us.kioxia.com/post/2026/05/06/storage-class-memory-scm-explained-the-next-leap-in-memory-technology">Storage Class Memory (SCM) Explained – The Next... | KIOXIA Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#SSD`, `#PCIe 6.0`, `#AI infrastructure`, `#storage`, `#Kioxia`

---

<a id="item-18"></a>
## [CXMT Reportedly Plans Second Fab in Beijing to Boost DRAM Output](https://www.techpowerup.com/351308/cxmt-reportedly-plans-second-fab-in-beijing-to-boost-dram-output) ⭐️ 6.5/10

Chinese DRAM maker CXMT is reportedly planning a second fab in Beijing to triple its wafer production capacity to 600,000 WPM, backed by local government funding.

rss · TechPowerUp News · Aug 3, 09:45

**Tags**: `#semiconductors`, `#DRAM`, `#memory`, `#China`, `#manufacturing`

---

<a id="item-19"></a>
## [AI companies slash token prices amid fierce competition from Chinese models](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-companies-are-now-racing-to-the-bottom-crashing-token-prices-and-competitive-models-push-companies-to-cut-costs) ⭐️ 6.5/10

All major AI developers are aggressively cutting token prices to remain competitive against highly efficient new releases from Chinese AI companies, squeezing already thin profit margins. According to OpenRouter data cited by CNBC, Chinese AI models now handle 30-46% of US enterprise API tokens, up from just 4.5% a year ago, with companies like Coinbase halving their AI bills by migrating traffic to DeepSeek. This price war threatens the profit margins and investor returns that AI companies have promised to justify the massive capital being poured into the sector. As commoditization accelerates and efficiency becomes the primary differentiator, the entire economics of generative AI could shift from premium software margins toward utility-like pricing. AI services are typically priced per million tokens, with separate rates for input (prompts) and output (completions), and output tokens usually costing several times more than input tokens. The competitive pressure is largely driven by Chinese open-weight models like DeepSeek that achieve comparable or better performance at a fraction of the inference cost, forcing Western providers to match prices rather than compete purely on capability.

rss · Tom's Hardware · Aug 3, 16:26

**Background**: Tokens are the fundamental units that language models process — they are roughly word fragments, short words, or punctuation marks — and AI services charge users based on how many tokens are consumed during API calls. Major AI labs like OpenAI, Anthropic, and Google built their business models on the assumption that advanced AI capabilities would command premium pricing, attracting record-breaking investment in 2024-2025. However, the emergence of highly efficient Chinese open-source models has disrupted this assumption by demonstrating that top-tier performance can be delivered at dramatically lower costs, making price competition unavoidable.

<details><summary>References</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/quick_start/pricing/">Models & Pricing | DeepSeek API Docs</a></li>
<li><a href="https://spoonai.me/posts/2026-07-11-chinese-ai-models-30-46pct-us-enterprise-tokens-cnbc-jul2026-en">Chinese AI Ate 30-46% of US Enterprise API Traffic... | spoonai</a></li>
<li><a href="https://agenticschool.dev/fundamentals/what-are-tokens.md">agenticschool.dev/fundamentals/ what - are - tokens .md</a></li>

</ul>
</details>

**Tags**: `#ai-industry`, `#pricing`, `#market-dynamics`, `#competition`, `#china-tech`

---

<a id="item-20"></a>
## [Gaming on the 4GB Radeon RX 6500 XT and GTX 1650 Super in 2026 — upscaling makes low-end GPUs viable for esports and internet cafes](https://www.tomshardware.com/pc-components/gpus/gaming-on-the-4gb-radeon-rx-6500-xt-and-gtx-1650-super-in-2026) ⭐️ 6.5/10

Tom's Hardware tests whether 4GB VRAM graphics cards from 2020 remain viable for gaming in 2026 using modern upscaling technologies, in light of AMD's controversial RX 9050 4GB launch.

rss · Tom's Hardware · Aug 3, 12:30

**Tags**: `#gpu`, `#vram`, `#amd`, `#upscaling`, `#budget-gaming`

---