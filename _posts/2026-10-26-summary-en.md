---
layout: default
title: "Horizon Summary: 2026-10-26 (EN)"
date: 2026-10-26
lang: en
---

> From 46 items, 11 important content pieces were selected

---

1. [Modders Unlock Firmware Limits, Boosting RTX GPU AI Compute Performance up to 2x](#item-1) ⭐️ 8.5/10
2. [Decade-Old CNN Outperforms Frontier LLMs in Skin Cancer Diagnosis](#item-2) ⭐️ 8.0/10
3. [OpenAI and Anthropic Cut LLM Prices by Up to 80%](#item-3) ⭐️ 8.0/10
4. [Nvidia considering $2,000 annual GPU fee for enterprise AI agent platform](#item-4) ⭐️ 7.5/10
5. [Nvidia Explores Converting Decommissioned German Nuclear Plants into AI Data Centers](#item-5) ⭐️ 7.5/10
6. [Samsung TVs found collecting audio and screenshots for ad targeting](#item-6) ⭐️ 7.5/10
7. [NVIDIA CEO Jensen Huang Estimates $2,000 Annual GPU Cost for AI Agents](#item-7) ⭐️ 6.5/10
8. [Playden enables running Steam games on jailbroken PS5 via Wine](#item-8) ⭐️ 6.5/10
9. [Linux tool enables Resizable BAR on Intel Arc GPUs for old motherboards](#item-9) ⭐️ 5.5/10
10. [Widening Financial Divide Between AI-Driven Big Tech and S&P 500](#item-10) ⭐️ 5.5/10
11. [Ukrainian Drones Strike Russian Finance Ministry Gorodets Data Center](#item-11) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Modders Unlock Firmware Limits, Boosting RTX GPU AI Compute Performance up to 2x](https://www.techpowerup.com/354110/geforce-unlocked-modders-boost-rtx-20-rtx-30-and-rtx-40-compute-performance-by-up-to-2x) ⭐️ 8.5/10

Modders have developed firmware patches for NVIDIA's RTX 30-series and 40-series consumer GPUs that remove artificial instruction rate limitations. These unlocks boost FP16 and BF16 tensor throughput by up to 2x, allowing consumer cards to match the performance of high-end professional RTX 6000 GPUs in AI workloads. This discovery significantly impacts AI and ML practitioners by providing a free, substantial cost-performance improvement for training and inference on existing hardware. It challenges the artificial price gap between consumer and professional NVIDIA GPUs by proving that the underlying silicon is fully capable of higher throughput. Specific tests show the RTX 4090 achieving 331.6 TeraFLOPS in FP16 tensor throughput after the unlock, compared to its standard 165.6 TeraFLOPS. Reports indicate that the output results remain bit-identical before and after the unlock, confirming that the improvement is in speed rather than computational accuracy.

rss · TechPowerUp News · Oct 25, 08:14

**Background**: NVIDIA manufactures consumer GeForce GPUs and professional RTX PRO/DAVID GPUs that are based on the same physical chip dies. However, consumer cards are sold with firmware restrictions that limit their instruction issue rates in compute-heavy tasks. These limitations are designed to protect the high-end professional product line, which is priced much higher than consumer equivalents.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Zagitta/gpu-unlock">Zagitta/gpu-unlock: Unlock FP/ BF 16 instruction issue rate on Nvidia ...</a></li>
<li><a href="https://daily.dev/posts/gpu-unlock-fp-bf16-instruction-issue-rate-on-nvidia-3000-s-cards-kbbkhu5nr">GPU-unlock: FP/ BF 16 instruction issue rate on Nvidia ...</a></li>
<li><a href="https://www.techpowerup.com/354110/geforce-unlocked-modders-boost-rtx-20-rtx-30-and-rtx-40-compute-performance-by-up-to-2x">GeForce Unlocked: Modders Boost RTX 20, RTX 30, and RTX 40 ...</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#GPU`, `#AI`, `#Hardware`, `#Performance`

---

<a id="item-2"></a>
## [Decade-Old CNN Outperforms Frontier LLMs in Skin Cancer Diagnosis](https://lynchlab.net/llm-skin-cancer) ⭐️ 8.0/10

A 10-year-old convolutional neural network (CNN) using Inception v3 outperformed two frontier large language models (LLMs) in classifying skin cancer lesions. This finding is based on a specific comparison conducted on a held-out test set. This result highlights that specialized, smaller models remain superior in high-stakes, domain-specific visual tasks like medical imaging, challenging the notion that general-purpose LLMs are universal replacements for all AI tasks. It also raises critical concerns about potential data leakage or unfair benchmarking in LLM evaluations. The CNN was fine-tuned on 68,011 images from the ISIC Archive on a single H100 GPU, while the specific test lesions were rigorously excluded from all training and validation sets to prevent contamination. Commenters note that this strict exclusion can be viewed as 'benchmaxxing', where a model is tuned specifically to beat a benchmark without genuine real-world utility.

hackernews · sungam · Oct 25, 17:15 · [Discussion](https://news.ycombinator.com/item?id=50233779)

**Background**: Convolutional Neural Networks (CNNs) like Inception v3 are specialized architectures designed to extract spatial features from images, making them highly efficient for image classification. Large Language Models (LLMs) are general-purpose transformers originally designed for text that have been adapted to vision, but they often lack the spatial specialization and efficiency of dedicated CNNs for specific diagnostic tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2505.23503v2">Can Large Language Models Challenge CNNs in Medical Image ...</a></li>

</ul>
</details>

**Discussion**: Community members strongly agreed that specialized classifiers outperform LLMs in narrow domains, drawing analogies to calculators beating LLMs at math or specialized Go-playing bots beating LLMs at Go. However, there was also critical debate about the methodology, with some arguing that the strict data exclusion was an artificial form of 'benchmaxxing' designed solely to prove the LLMs' inferiority rather than demonstrating real-world clinical value.

**Tags**: `#Machine Learning`, `#Computer Vision`, `#LLM Limitations`, `#Medical AI`, `#Model Benchmarking`

---

<a id="item-3"></a>
## [OpenAI and Anthropic Cut LLM Prices by Up to 80%](https://minimaxir.com/2026/10/cheap-llms/) ⭐️ 8.0/10

OpenAI and Anthropic have significantly reduced their LLM API prices by up to 80% over a few months. This aggressive pricing shift has intensified competition in the large language model market. This price war drastically lowers the barrier to entry for developers and businesses adopting AI. It may signal a shift in the industry toward volume-based competition driven by limited demand and GPU capacity utilization. Community analysis suggests that DeepSeek's efficient cost structures, such as high token throughput per GPU, create pressure for larger players to optimize their own inference costs. There are also concerns about whether these subsidized prices are masking data privacy risks or strategic regulatory maneuvers to ban open-source competitors.

hackernews · minimaxir · Oct 25, 21:11 · [Discussion](https://news.ycombinator.com/item?id=50236102)

**Background**: Large Language Models (LLMs) are typically accessed via APIs charged per million tokens. Inference costs are heavily dependent on GPU efficiency and optimization techniques. The market has recently seen increased competition from Chinese open-source models like Kimi and GLM, which offer lower prices and fewer content restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businessinsider.com/sam-altman-dario-amodei-anthropic-openai-rivalry-timeline-2026-2">A Timeline of Anthropic and OpenAI 's Rivalry - Business Insider</a></li>
<li><a href="https://venkyrao.medium.com/llm-the-good-and-the-bad-e9cb32fddb6d">LLMs : The Good and The Bad. A Comparative Study on the Cost of</a></li>

</ul>
</details>

**Discussion**: Users debated whether the price cuts are driven by genuine competition or strategic efforts to lobby for regulations that ban open-source models from China. Some highlighted DeepSeek's low revenue per GPU, while others raised concerns about data privacy and the use of user-generated outputs to subsidize costs. The high cost of unused GPU capacity was also cited as a factor forcing price reductions.

**Tags**: `#LLM`, `#AI-Pricing`, `#OpenAI`, `#Anthropic`, `#Tech-Industry`

---

<a id="item-4"></a>
## [Nvidia considering $2,000 annual GPU fee for enterprise AI agent platform](https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform) ⭐️ 7.5/10

Nvidia CEO Jensen Huang is reportedly considering an annual software fee of around $2,000 per GPU for a new enterprise AI agent platform. This move could generate up to $10 billion annually if five million licenses are sold, though pricing and timelines are unconfirmed. Shifting from one-time hardware sales to recurring software revenue strengthens Nvidia's lock-in within the AI infrastructure ecosystem. This strategy aligns with broader industry trends where cloud providers and enterprises are increasingly paying for optimized AI agent capabilities rather than just raw compute power. The reported fee of $2,000 per GPU is already more than twice the amount Nvidia currently charges for its existing AI enterprise software platform. The potential $10 billion revenue target assumes the sale of five million licenses, which would likely require a massive existing GPU install base.

rss · Tom's Hardware · Oct 25, 13:00

**Background**: Nvidia currently generates most of its revenue from selling GPUs and AI hardware, but it is pushing its NIM and NeMo software stacks to add value through agent tooling. NIM provides accelerated inference microservices for running AI models, while NeMo offers libraries for data preparation and agent guardrails.

<details><summary>References</summary>
<ul>
<li><a href="https://www.intelligenthq.com/nvidia-ecosystem/solutions/enterprise-ai-agents/">Enterprise AI and Agents with NVIDIA NIM , NeMo and... | IntelligentHQ</a></li>
<li><a href="https://developer.nvidia.com/nim">NIM for Developers | NVIDIA Developer</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#AI Infrastructure`, `#Business Strategy`, `#SaaS`, `#Enterprise AI`

---

<a id="item-5"></a>
## [Nvidia Explores Converting Decommissioned German Nuclear Plants into AI Data Centers](https://www.tomshardware.com/tech-industry/data-centers/nvidia-eyes-converting-old-nuclear-plants-into-massive-ai-data-centers-reusing-shut-down-german-energy-sites-could-reduce-the-cost-and-timeline-of-building-from-scratch) ⭐️ 7.5/10

Nvidia and PreussenElektra are launching a joint study to assess whether decommissioned German nuclear power plant sites can be repurposed as AI data centers. The initiative aims to leverage existing industrial infrastructure to accelerate AI deployment timelines. Repurposing former nuclear plant sites could significantly lower the cost and shorten the timeline for building massive AI facilities by bypassing years of land approvals and high-voltage grid connectivity struggles. This strategy directly addresses critical infrastructure and energy bottlenecks currently stalling global AI growth. The project does not involve using active nuclear power for computing but rather reusing the land, cooling water infrastructure, and existing grid connections left behind by the decommissioned plants. It is currently in the exploratory phase with no specific investment or site decisions made yet.

rss · Tom's Hardware · Oct 25, 10:30

**Background**: PreussenElektra is responsible for the decommissioning of eight nuclear power plants in Germany and is looking for viable reuse concepts for these sites. New AI data centers face major hurdles in securing land, cooling water, and high-voltage power grid access, which former nuclear plants are uniquely positioned to provide.

<details><summary>References</summary>
<ul>
<li><a href="https://www.preussenelektra.de/de/newsroom/pressemitteilungen/pressemitteilungen-2026/2026-pel-and-nvidia-explore-former-nuclear-power-plant-sites-for-ai-factories.html">PreussenElektra and NVIDIA explore former nuclear power plant ...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/data-centers/nvidia-eyes-converting-old-nuclear-plants-into-massive-ai-data-centers-reusing-shut-down-german-energy-sites-could-reduce-the-cost-and-timeline-of-building-from-scratch">The plan does not involve using nuclear power . | Tom's Hardware</a></li>

</ul>
</details>

**Tags**: `#AI Infrastructure`, `#Data Centers`, `#Energy`, `#Nvidia`, `#Sustainability`

---

<a id="item-6"></a>
## [Samsung TVs found collecting audio and screenshots for ad targeting](https://www.tomshardware.com/tech-industry/cyber-security/hacker-finds-own-samsung-tv-collecting-scary-amounts-of-user-information-and-gets-banned-by-openai-for-cyber-abuse-tv-runs-an-ai-model-that-collects-audio-screenshots-and-plenty-of-other-user-data-for-ad-targeting) ⭐️ 7.5/10

A cybersecurity bounty hunter reverse-engineered their Samsung TV and discovered that its AI models secretly collect audio and screenshots for ad targeting. The device also generates a cross-device tracking ID known as AID to monitor users across other platforms. This disclosure highlights severe privacy vulnerabilities in modern smart home IoT devices, where AI-powered data collection significantly erodes user trust. The findings suggest that performance issues in these devices may be caused by intensive post-processing of collected user data. The researcher theorizes that the TV's sluggishness is caused by heavy processing of computer vision models and AID tracking. Additionally, the security researcher's account was banned by OpenAI due to a policy violation during this cybersecurity research.

rss · Tom's Hardware · Oct 25, 10:00

**Background**: Smart TVs function as sophisticated computers that run AI models and process user data for personalized advertising. AID, or Android ID, is a cross-device tracking identifier that allows advertisers to build profiles of individual users across multiple smart home devices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/hacker-finds-own-samsung-tv-collecting-scary-amounts-of-user-information-and-gets-banned-by-openai-for-cyber-abuse-tv-runs-an-ai-model-that-collects-audio-screenshots-and-plenty-of-other-user-data-for-ad-targeting">Cybersecurity bounty hunter says Samsung TVs... | Tom's Hardware</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#privacy`, `#iot`, `#consumer-electronics`, `#security-bug`

---

<a id="item-7"></a>
## [NVIDIA CEO Jensen Huang Estimates $2,000 Annual GPU Cost for AI Agents](https://www.techpowerup.com/354113/nvidia-eyes-software-revenue-with-a-usd-2-000-per-gpu-yearly-figure-from-huang) ⭐️ 6.5/10

At GTC Berlin, NVIDIA CEO Jensen Huang disclosed that running the company's software stack for AI agents costs approximately $2,000 per GPU annually. This marks a clear signal that NVIDIA is shifting its business model toward a significant software licensing revenue stream. The estimate highlights a growing commercial ecosystem where enterprises pay for AI infrastructure and specialized software, rather than just hardware. It provides a critical benchmark for enterprise adoption planning, clarifying the total cost of ownership for agentic AI deployments. The $2,000 figure is notably lower than the $4,500 per GPU one-year subscription for the NVIDIA AI Enterprise suite listed in official licensing guides. It is unclear whether this price covers the full suite, a narrower agent-focused bundle, or represents a future, more affordable licensing model.

rss · TechPowerUp News · Oct 25, 15:21

**Background**: NVIDIA GTC is the company's flagship event focused on its data center and AI GPU hardware, now extending heavily into AI agents. Historically, NVIDIA has generated revenue primarily through chip sales and a premium software suite called AI Enterprise, which provides pre-optimized tools for running large language models on its GPUs. As the industry moves toward more complex, multi-agent workflows, companies are increasingly looking to monetize the software layer.

<details><summary>References</summary>
<ul>
<li><a href="https://www.buildfastwithai.com/blogs/nvidia-nemo-vs-hugging-face-vs-ollama-2026-guide">NVIDIA NeMo vs Hugging Face vs Ollama (2026 Guide)</a></li>
<li><a href="https://blogs.nvidia.com/blog/gtc-berlin-2026-keynote/">GTC Berlin 2026: Live Updates From NVIDIA CEO Jensen Huang’s ...</a></li>
<li><a href="https://aifoss.dev/blog/ollama-vs-openrouter-vs-groq-vs-nvidia-nim-llm-serving-2026/">Ollama vs OpenRouter vs Groq vs NVIDIA NIM in 2026</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#AI Business Model`, `#Software Licensing`, `#Enterprise AI`, `#Jensen Huang`

---

<a id="item-8"></a>
## [Playden enables running Steam games on jailbroken PS5 via Wine](https://www.tomshardware.com/video-games/playstation/jailbroken-ps5s-can-now-run-steam-pc-games-you-can-now-sign-in-with-your-steam-account-and-install-games-from-your-library-directly-to-the-console) ⭐️ 6.5/10

A homebrew tool called Playden now allows jailbroken PS5 consoles to sign into Steam and run PC games locally without needing a PC. Each downloaded game is packaged as a separate app with its own home screen tile. This milestone blurs the line between PC and console gaming, demonstrating that restricted hardware can run a full Windows environment through Wine. It empowers the enthusiast community to bypass platform lock-in and access their digital libraries on devices traditionally reserved for proprietary content. Playden uses prospero-win, a custom port of Wine, to create a clean Windows environment on the PS5. It ensures the runtime kit is complete and isolates each game's files and settings to prevent crashes from affecting other titles.

rss · Tom's Hardware · Oct 25, 12:40

**Background**: Jailbreaking a PS5 involves exploiting software vulnerabilities to break the console's security locks, allowing the installation of homebrew applications. Wine is a compatibility layer that allows Windows software to run on other operating systems. Historically, running complex PC games on consoles was nearly impossible due to hardware and kernel restrictions, but reverse engineering has advanced significantly in recent years.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/leolobato/playden-ps5">GitHub - leolobato/playden-ps5: Play your Steam library's ...</a></li>
<li><a href="https://www.indiekings.com/2026/10/playden-steam-games-run-directly-on.html">Playden: Steam Games Run Directly on Jailbroken PS5</a></li>

</ul>
</details>

**Tags**: `#PS5`, `#Jailbreaking`, `#Steam`, `#Gaming Hardware`, `#Reverse Engineering`

---

<a id="item-9"></a>
## [Linux tool enables Resizable BAR on Intel Arc GPUs for old motherboards](https://www.techpowerup.com/354116/new-linux-tool-brings-resizable-bar-to-intel-arc-gpus-on-old-motherboards) ⭐️ 5.5/10

Developer Rod Burlamaqui has released 'arc-rebar', a Linux tool that enables Resizable BAR on Intel Arc GPUs without requiring BIOS modifications. The tool runs from the initramfs at every boot, before the GPU driver loads, effectively unblocking performance on older systems. This provides a critical performance boost to Intel Arc users on legacy hardware, as Resizable BAR is identified by Intel and reviewers as essential for the GPU's full potential. It resolves a significant bottleneck where older motherboards lacked the necessary BIOS options to enable this PCIe feature. The tool targets the PCIe switch on Arc cards and can expand the CPU-visible VRAM window from as little as 256 MiB to the full capacity, such as 12 GiB on a B580, significantly improving bandwidth. Unlike previous workarounds that require firmware modifications, this solution does not touch the BIOS, kernel, or Intel's drivers.

rss · TechPowerUp News · Oct 25, 16:40

**Background**: Resizable BAR (ReBAR) is a PCIe feature that allows the CPU to access the entire GPU memory pool at once, improving performance. Linux uses an initramfs, a temporary filesystem loaded during boot, to execute scripts before the main operating system takes over. Intel's Alchemist and Battlemage architectures are highly dependent on this feature, to the point that Intel previously advised users without it to consider other vendors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Initial_ramdisk">Initial ramdisk - Wikipedia</a></li>
<li><a href="https://www.corsair.com/us/en/explorer/glossary/what-is-resizable-bar/">What is Resizable BAR ? | CORSAIR</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intel_Arc">Intel Arc - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Intel Arc`, `#Linux`, `#Hardware Optimization`, `#Resizable BAR`, `#GPU`

---

<a id="item-10"></a>
## [Widening Financial Divide Between AI-Driven Big Tech and S&P 500](https://www.tomshardware.com/tech-industry/artificial-intelligence/big-tech-is-cashing-in-on-ai-while-the-rest-of-corporate-america-sees-no-financial-returns-report-outlines-how-rising-token-costs-threaten-to-squeeze-corporate-profit-margins) ⭐️ 5.5/10

A new report highlights a significant growing divide in financial fortunes between America's largest technology companies and the rest of the S&P 500, where Big Tech reaps AI profits while others face no returns. The analysis emphasizes that revenue per employee for the Magnificent Seven is steadily outpacing the remaining S&P 493 due to rising AI token costs. This growing disparity is highly significant because it signals that AI profitability is highly concentrated among a few massive infrastructure builders, leaving typical enterprises vulnerable to high costs. For the broader corporate ecosystem, it highlights the need to optimize AI spending to prevent the squeeze on profit margins. Key technical factors driving this disparity include the capital expenses required to build out proprietary AI inference infrastructure and the operating expenses incurred by the ongoing consumption of AI tokens. These rising costs threaten to compress profit margins for companies that cannot replicate the massive internal revenue generation of Big Tech.

rss · Tom's Hardware · Oct 25, 15:25

**Background**: The Magnificent Seven refers to a group of heavily capitalized large-cap technology stocks that currently account for roughly 35% of the entire S&P 500 market cap. In AI terminology, a token represents a unit of data that a large language model processes or generates, making token costs a primary operational metric for enterprise AI deployment. Consequently, a company's ability to efficiently process or scale token generation determines its AI cost efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fool.com/research/magnificent-seven-sp-500/">The Magnificent Seven’s Market Cap vs. the S&P 500 | The ...</a></li>
<li><a href="https://www.nvidia.com/en-us/solutions/ai/tokenomics-guide/">Tokenomics Guide: Case Studies and More | NVIDIA AI</a></li>
<li><a href="https://www.bcg.com/publications/2026/managing-ai-token-costs">How Enterprises Can Control AI Token Costs | BCG</a></li>

</ul>
</details>

**Tags**: `#AI Economics`, `#Big Tech`, `#Corporate Finance`, `#Business Analysis`

---

<a id="item-11"></a>
## [Ukrainian Drones Strike Russian Finance Ministry Gorodets Data Center](https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drone-attacks-hammer-russias-finance-ministry-data-center-damaged-facility-reportedly-holds-tax-databases-facility-also-holds-other-important-state-registry-data) ⭐️ 5.5/10

Ukrainian drone attacks have damaged a Russian Finance Ministry data center in Gorodets, which reportedly houses Federal Tax Service tax databases and critical state registry data. The incident demonstrates how data centers have evolved into critical national infrastructure targets in modern conflict, extending risks beyond traditional IT sectors to core government administrative and tax systems. The damaged facility in Gorodets is located approximately 230 miles east of the Kremlin and more than 600 miles from the front lines, operating as one of two key processing centers in a geo-distributed setup alongside Dubna and Yerzovka.

rss · Tom's Hardware · Oct 25, 14:05

**Background**: Data centers physically host the servers and networks that store a nation's most sensitive digital records, including tax obligations, business registries, and state property databases.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/AWS/ukrainian-drones-strike-russian-finance-ministry-data-center-in-gorodets-25190443">Ukrainian Drones Strike Russian Finance Ministry Data Center ...</a></li>
<li><a href="https://mezha.net/eng/news/mezha-a48312b74195a4b00cfa1886_drones_hit_russian/">Drones hit Russian Finance Ministry data center; tax ...</a></li>

</ul>
</details>

**Tags**: `#data-center`, `#geopolitics`, `#security`, `#infrastructure`, `#physical-security`

---