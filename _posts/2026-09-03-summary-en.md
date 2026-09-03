---
layout: default
title: "Horizon Summary: 2026-09-03 (EN)"
date: 2026-09-03
lang: en
---

> From 102 items, 20 important content pieces were selected

---

1. [Gemini 3.8 Flash and 3.8 Flash Cyber](#item-1) ⭐️ 9.0/10
2. [FBI Probes Leak of 153 Million Driver's Licenses on Russian Cybercrime Forum](#item-2) ⭐️ 8.5/10
3. [Researchers easily trick Fortune-500 companies' AI agents into running arbitrary code — supply-chain attack via llms.txt guidance file illustrates how data has become code](#item-3) ⭐️ 8.5/10
4. [AMD RDNA 5 GPU IP Debuts in Samsung Exynos 2700 on 2nm Node](#item-4) ⭐️ 7.5/10
5. [TSMC Delays Hybrid Bonding for HBM, Bets on 5μm Microbumps](#item-5) ⭐️ 7.5/10
6. [Micron Explores Near-GPU NAND Flash to Run Bigger LLMs](#item-6) ⭐️ 7.5/10
7. [Samsung Teases HBM5: 4 TB/s per Stack, 4,096-bit Interface](#item-7) ⭐️ 7.5/10
8. [Meta Releases Muse Spark 1.3, Approaching Frontier at Lower Cost](#item-8) ⭐️ 7.0/10
9. [Google avoids forced breakup of ad tech business in antitrust ruling](#item-9) ⭐️ 7.0/10
10. [Three sites made 215,128 “best software” pages for AI. Perplexity cites them](#item-10) ⭐️ 7.0/10
11. [World's Largest Dark Matter Detector Records Single Anomalous Event](#item-11) ⭐️ 7.0/10
12. [Meta Open-Sources 30B Agent Model, Raising Containment Concerns](#item-12) ⭐️ 7.0/10
13. [Intel 18A-P Pushes RibbonFET and Backside Power Beyond the First Generation](#item-13) ⭐️ 7.0/10
14. [WSTS Projects Memory Chip Revenue to Surge 250% to $804B in 2026](#item-14) ⭐️ 7.0/10
15. [Architect Labs Raises $24M for AI-Driven End-to-End Chip Design](#item-15) ⭐️ 7.0/10
16. [Hardware Unboxed RTX 5090 Suffers Melted Power Connector at 175°C](#item-16) ⭐️ 6.5/10
17. [RTX 5090's Single Power Connector May Bottleneck DLSS 5 Neural Rendering](#item-17) ⭐️ 6.5/10
18. [EFF Urges California Governor to Veto Online Age Verification Bill](#item-18) ⭐️ 6.5/10
19. [AI Data Center Investment Projected to Hit $32 Trillion by 2050](#item-19) ⭐️ 6.5/10
20. [China's EUV technology lags ASML by 20 years, analyst says](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [Gemini 3.8 Flash and 3.8 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 9.0/10

Google DeepMind releases Gemini 3.8 Flash and 3.8 Flash Cyber, a Flash-tier model achieving intelligence scores comparable to Opus 5 medium while maintaining low cost and high speed.

hackernews · bratao · Sep 2, 15:12 · [Discussion](https://news.ycombinator.com/item?id=49537553)

**Tags**: `#gemini`, `#google-deepmind`, `#llm`, `#ai-models`, `#model-release`

---

<a id="item-2"></a>
## [FBI Probes Leak of 153 Million Driver's Licenses on Russian Cybercrime Forum](https://www.tomshardware.com/tech-industry/cyber-security/fbi-investigating-153-million-us-and-canadian-drivers-licenses-leaked-on-russian-cybercrime-forum-including-that-of-us-secdef-pete-hegseth-data-is-suspected-to-have-come-from-an-id-authentication-service-provider) ⭐️ 8.5/10

The FBI is investigating a massive breach in which 153 million US and Canadian driver's licenses were posted on a Russian cybercrime forum, including that of US Secretary of Defense Pete Hegseth. The leaked data is suspected to have originated from a Louisiana-based ID-authentication service provider that serves clients such as Hertz, Target, and the US Coast Guard. This breach carries significant national security implications because it involves the personal data of the US Secretary of Defense and the US Coast Guard, potentially exposing them to identity theft, fraud, or targeted attacks. It also affects millions of ordinary citizens and major corporations, underscoring the systemic risk that a single compromised third-party vendor can cascade into massive cross-sector exposure. The breach is traced to a single Louisiana-based identity verification vendor, illustrating how a single point of failure in a third-party service can expose data from multiple major organizations simultaneously. The inclusion of high-ranking government officials suggests either targeted intelligence collection by threat actors or indiscriminate bulk-data trafficking on a known Russian-language cybercrime forum.

rss · Tom's Hardware · Sep 2, 13:14

**Background**: ID-authentication service providers verify users' identities for businesses by validating government-issued documents such as driver's licenses, often storing the extracted personal data in centralized systems. Russian cybercrime forums are underground online marketplaces where threat actors trade stolen data, credentials, malware, and hacking tools; they typically operate in Russian, may be accessible via the clear web or Tor browser, and often require registration or vetting for access. Supply-chain attacks targeting such identity verification vendors have become increasingly common, because compromising a single provider can yield millions of records from multiple downstream clients in one strike.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Underground_forum">Underground forum - Wikipedia</a></li>
<li><a href="https://socradar.io/blog/top-5-russian-speaking-dark-web-forums/">Top 5 Russian-Speaking Dark Web Forums</a></li>
<li><a href="https://thecyphere.com/blog/saml-authentication/">What is SAML Authentication ? Is it different from OAuth – Cyphere</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data-breach`, `#identity-theft`, `#FBI`, `#national-security`

---

<a id="item-3"></a>
## [Researchers easily trick Fortune-500 companies' AI agents into running arbitrary code — supply-chain attack via llms.txt guidance file illustrates how data has become code](https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-easily-trick-fortune-500-companies-ai-agents-into-running-arbitrary-code-supply-chain-attack-via-llms-txt-guidance-file-illustrates-how-data-has-become-code) ⭐️ 8.5/10

Researchers demonstrated a supply-chain attack on Fortune 500 AI agents by poisoning public llms.txt guidance files to trigger arbitrary code execution, highlighting critical security risks as AI systems increasingly treat ingested data as executable instructions.

rss · Tom's Hardware · Sep 2, 10:20

**Tags**: `#AI-security`, `#supply-chain-attack`, `#LLM-agents`, `#prompt-injection`, `#enterprise-AI`

---

<a id="item-4"></a>
## [AMD RDNA 5 GPU IP Debuts in Samsung Exynos 2700 on 2nm Node](https://www.techpowerup.com/352268/possible-amd-rdna-5-gpu-ip-ships-inside-a-samsung-soc-on-2-nm-node) ⭐️ 7.5/10

SemiAnalysis die annotation of Samsung's Exynos 2700 SoC reveals that AMD's next-generation RDNA 5 GPU IP is shipping inside the chip as the Xclipse 970 GPU, making it the first RDNA 5-equipped chip to reach the market. The SoC is fabricated on Samsung Foundry's SF2 2nm node and pairs the new GPU with a unique 10-core Arm CPU configuration. This is the first confirmed shipping implementation of AMD's RDNA 5 architecture, signaling that AMD's next-gen GPU technology has matured enough for mass production silicon — even if its debut comes through a mobile co-developed chip rather than a discrete Radeon card. The milestone also validates the AMD-Samsung mobile GPU partnership and positions Samsung's Exynos line as a more credible competitor to Qualcomm's Snapdragon Elite SoCs. The Xclipse 970 GPU contains 8 Work Group Processors (WGPs), yielding 16 Compute Units if the WGP/CU ratio remains unchanged from RDNA 4. On the CPU side, the chip uses Arm C2-Ultra and C2-Pro cores in a 1+1+4+4 layout, with the prime C2-Ultra core clocked at 4.24 GHz. Notably, this is a co-developed adaptation of AMD RDNA technology rather than a direct port of the discrete GPU IP.

rss · TechPowerUp News · Sep 2, 16:01

**Background**: RDNA (Radeon DNA) is AMD's GPU instruction set architecture, evolving through generations such as RDNA 2, RDNA 3, and RDNA 4 in discrete Radeon cards; RDNA 5 is expected to succeed RDNA 4. Samsung's Xclipse line is the result of a multi-year partnership with AMD, integrating customized RDNA-based GPU IP into Exynos mobile SoCs — earlier entries like the Xclipse 920 and 940/950 used RDNA 2 and RDNA 3 derivatives. Samsung Foundry's SF2 is its first-generation 2nm process using second-generation GAA (Gate-All-Around) MBCFET transistors, targeting high-volume manufacturing in 2026 and competing directly with TSMC N2 and Intel 18A.

<details><summary>References</summary>
<ul>
<li><a href="https://semiwiki.com/wikis/industry-wikis/samsung-2nm-process-technology-wiki/">Samsung 2nm Process Technology Wiki - Semiwiki</a></li>
<li><a href="https://www.gadgets360.com/mobiles/news/samsung-exynos-2700-soc-geekbench-listing-specifications-11328564">Samsung 's Exynos 2700 Chip Has Already Visited Geekbench</a></li>
<li><a href="https://www.tomshardware.com/news/amd-rdna-3-gpu-architecture-deep-dive-the-ryzen-moment-for-gpus">AMD RDNA 3 GPU Architecture Deep Dive: The... | Tom's Hardware</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#RDNA 5`, `#Samsung Exynos`, `#2nm process`, `#mobile GPU`

---

<a id="item-5"></a>
## [TSMC Delays Hybrid Bonding for HBM, Bets on 5μm Microbumps](https://www.techpowerup.com/352267/tsmc-delays-hybrid-bonding-investment-for-hbm-opts-for-microbumps) ⭐️ 7.5/10

According to supply chain sources cited by ETNews, TSMC is holding back on hybrid bonding for HBM memory packaging and instead preparing its supply chain for 5-micrometer microbumps, with mass production targeted for the second half of 2028. This decision affects the AI chip supply chain because CoWoS packaging, which underpins products like NVIDIA's H100 and B200, relies on chip-to-interposer interconnects for HBM integration. TSMC's choice to refine microbumps rather than adopt hybrid bonding signals a pragmatic path that balances yield, cost, and manufacturing maturity over the more disruptive copper-to-copper bonding approach. Hybrid bonding reduces interconnect pitch to about 1 micrometer versus roughly 20 micrometers for microbumps and 100 micrometers for traditional solder bumps, but TSMC's new 5-micrometer microbump target would still be a significant shrink from today's microbumps. Notably, AMD's 3D V-Cache uses hybrid bonding to stack SRAM on logic, showing that hybrid bonding is already in production for some applications, but TSMC views microbumps as sufficient for HBM integration.

rss · TechPowerUp News · Sep 2, 15:43

**Background**: Hybrid bonding is a permanent chip-to-chip or wafer-to-wafer connection technique that fuses embedded copper (Cu) interconnections with a dielectric (SiOx) bond, eliminating traditional solder bumps and enabling much finer pitch and shorter interconnects. TSMC's CoWoS (Chip-on-Wafer-on-Substrate) is a 2.5D advanced packaging technology that places GPU dies and memory stacks side-by-side on a silicon interposer, and it comes in variants such as CoWoS-S, CoWoS-R, and CoWoS-L. HBM (High Bandwidth Memory) is the stacked DRAM used alongside AI accelerators, and CoWoS is currently the dominant packaging method for high-end AI chips.

<details><summary>References</summary>
<ul>
<li><a href="https://www.appliedmaterials.com/us/en/semiconductor/markets-and-inflections/heterogeneous-integration/hybrid-bonding.html">Hybrid Bonding</a></li>
<li><a href="https://www.brewerscience.com/what-is-hybrid-bonding/">Hybrid Bonding Basics – What is Hybrid Bonding? - Brewer Science</a></li>
<li><a href="https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm">CoWoS ® - Taiwan Semiconductor Manufacturing Company Limited</a></li>

</ul>
</details>

**Tags**: `#semiconductor-packaging`, `#TSMC`, `#HBM`, `#hybrid-bonding`, `#AI-hardware`

---

<a id="item-6"></a>
## [Micron Explores Near-GPU NAND Flash to Run Bigger LLMs](https://www.techpowerup.com/352251/micron-explores-near-gpu-nand-flash-to-run-bigger-llms) ⭐️ 7.5/10

Micron is exploring high-endurance NAND flash modules placed closer to GPUs to expand memory capacity for larger LLM workloads, creating a new memory tier between HBM and traditional storage.

rss · TechPowerUp News · Sep 2, 11:19

**Tags**: `#AI hardware`, `#GPU memory`, `#NAND flash`, `#LLM infrastructure`, `#Micron`

---

<a id="item-7"></a>
## [Samsung Teases HBM5: 4 TB/s per Stack, 4,096-bit Interface](https://www.tomshardware.com/pc-components/dram/samsung-teases-new-hbm5-with-twice-the-performance-of-hbm4e-ambitious-data-transfer-rates-could-hint-at-4-096-bit-interface) ⭐️ 7.5/10

Samsung has teased its next-generation HBM5 memory, targeting 4 TB/s of bandwidth per stack by the late 2020s — roughly twice the performance of HBM4E. The company suggests this could be achieved through either a doubled 4,096-bit interface, a doubled per-pin transfer rate of 24 GT/s, or a combination of both. HBM5 at 4 TB/s per stack would enable AI accelerators with aggregated memory bandwidth of around 100 TB/s, a critical bottleneck for training and running large AI models. As AI models continue to grow in size, memory bandwidth — not raw compute — has become the primary constraint on AI hardware performance, making HBM roadmaps strategically vital for the entire AI infrastructure ecosystem. Samsung also claims HBM5 will deliver 20% better power efficiency and 20% lower thermal resistance compared to HBM4E, unveiled as part of Samsung's CUBE vertical integration strategy at SEMICON Taiwan 2026. Current HBM3e implementations in shipping AI accelerators offer 80–192 GB per package with per-stack bandwidth well below the HBM5 target.

rss · Tom's Hardware · Sep 2, 14:38

**Background**: High Bandwidth Memory (HBM) is a 3D-stacked DRAM interface where multiple DRAM dies are vertically bonded using Through-Silicon Vias (TSVs) and connected to a processor via a wide parallel interface. Each HBM generation increases bandwidth by widening the interface (measured in bits) and/or raising the per-pin data transfer rate (measured in GT/s). HBM has become the dominant on-package memory solution for AI accelerators (GPUs and custom ASICs) because conventional DDR memory cannot deliver the bandwidth required for large-scale AI workloads. Samsung, SK Hynix, and Micron are the three primary HBM manufacturers, competing to supply AI chip designers like NVIDIA, AMD, and Google.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/dram/samsung-teases-new-hbm5-with-twice-the-performance-of-hbm4e-ambitious-data-transfer-rates-could-hint-at-4-096-bit-interface">Samsung teases new HBM5 with twice the performance of HBM4E —ambitious data transfer rates could hint at 4,096-bit interface | Tom's Hardware</a></li>
<li><a href="https://www.techtimes.com/articles/326118/20260901/samsung-locks-hbm5-2x-hbm4e-cube-strategy-redraws-memory-roadmap.htm">Samsung Locks In HBM5 at 2x HBM4E: CUBE Strategy Redraws Memory Roadmap</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#HBM`, `#memory`, `#AI-infrastructure`, `#Samsung`, `#semiconductors`

---

<a id="item-8"></a>
## [Meta Releases Muse Spark 1.3, Approaching Frontier at Lower Cost](https://developer.meta.com/ai/models/muse-spark/) ⭐️ 7.0/10

Meta has released Muse Spark 1.3, the fourth Muse Spark model in five months, scoring 61 on the Artificial Analysis Intelligence Index (up 4 points from 1.2) and achieving a DeepSWE coding benchmark score of 75.4. The model is priced at $1.25 per million input tokens and $4.25 per million output tokens, with a 1,048,576-token context window. Muse Spark 1.3 demonstrates that Meta is closing the gap to frontier-level performance while significantly undercutting competitors on price, intensifying the downward pressure on AI API pricing. Its strong coding benchmark result (75.4 DeepSWE, briefly ahead of Gemini 3.8 Flash) suggests it could become a practical choice for agentic and multi-agent coding workflows. The model is a proprietary multimodal reasoning model from Meta Superintelligence Labs, optimized for long-running agentic, multi-agent, and coding workflows. Simon Willison's hands-on SVG test cost just 4.2 cents and ran in 38 seconds, showing notable quality improvements over Muse Spark 1.2 in visual generation tasks.

hackernews · bvaldivielso · Sep 2, 19:35 · [Discussion](https://news.ycombinator.com/item?id=49541256)

**Background**: The Muse Spark series is Meta's line of proprietary AI models developed under Meta Superintelligence Labs, positioned for complex agentic tasks rather than just simple chat. Frontier AI benchmarks like the Artificial Analysis Intelligence Index and coding-specific tests such as DeepSWE are standardized evaluations used to compare models across reasoning, coding, and multimodal capabilities. The competitive landscape in late 2025 has seen rapid iteration, with multiple vendors releasing improved models on monthly cadences and prices falling sharply.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/meta/muse-spark-1.3">Muse Spark 1 . 3 - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://llm-stats.com/models/muse-spark-1.3">Muse Spark 1 . 3 API Pricing, Context Window & Benchmarks</a></li>
<li><a href="https://artificialanalysis.ai/articles/muse-spark-1-3">Muse Spark 1 . 3 : Meta reaches the frontier | Artificial Analysis</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely positive, with users praising the cost-effectiveness and noting real productivity gains on development work. Discussion focused on the model's competitive DeepSWE score (75.4, briefly besting Gemini 3.8 Flash) and expectations that this competition will drive AI prices down. Some users raised concerns about Meta's data training policies, noting that the explicit pricing premium for opting out of training makes the value of user data transparent, though they appreciated Meta's transparency about it.

**Tags**: `#meta`, `#ai-models`, `#muse-spark`, `#llm`, `#model-release`

---

<a id="item-9"></a>
## [Google avoids forced breakup of ad tech business in antitrust ruling](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html) ⭐️ 7.0/10

A federal court ruled against the DOJ's request to force Google to divest its ad tech business, sparing the company from a structural breakup. Google's ad tech operations generated $30 billion last year, roughly 8% of Alphabet's revenue, though revenue has declined for 16 consecutive quarters and the unit now contributes less than 1% of company profit. This ruling sets a major precedent for how U.S. regulators can challenge Big Tech's vertically integrated advertising stacks, which the DOJ had argued controlled roughly 90% of the publisher ad server market and 50% of the ad exchange market. The outcome preserves Google's ability to bundle its ad exchange (AdX) and publisher ad server (Google Ad Manager), leaving advertisers and publishers with fewer competitive alternatives in programmatic advertising. The ad tech stack in question stems largely from Google's 2008 acquisition of DoubleClick, after which the DOJ says Google Ad Manager and AdX grew to dominant market shares. The court's rejection of forced divestiture marks the second major antitrust loss for the DOJ against Google this year, following a similar outcome in the search antitrust case where behavioral remedies rather than structural breakup were imposed.

hackernews · donohoe · Sep 2, 14:46 · [Discussion](https://news.ycombinator.com/item?id=49537131)

**Background**: Google's ad tech business refers to the tools that automate the buying and selling of digital advertising, including ad exchanges (marketplaces where ad inventory is auctioned), ad servers (which decide which ads to show on a webpage), and demand-side platforms used by advertisers. The DOJ argued that Google's acquisitions—most notably DoubleClick in 2008—gave it an unfair advantage across this stack, allowing it to favor its own exchange and manipulate auction dynamics. Forced divestiture, or a 'structural remedy,' means literally splitting off parts of a company; this is considered the most aggressive antitrust tool, compared to 'behavioral remedies' which only restrict how a company can act.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpolicy.press/how-three-mergers-buttressed-googles-ad-tech-monopoly-per-doj/">How Three Mergers Buttressed Google ’s Ad Tech ... | TechPolicy.Press</a></li>
<li><a href="https://markets.financialcontent.com/stocks/article/marketminute-2025-9-3-google-triumphs-in-antitrust-battle-chrome-spared-big-tech-breathes-sigh-of-relief">Google Triumphs in Antitrust Battle: Chrome Spared, Big Tech...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with the broader difficulty of unmerging companies once mergers are approved, with one user arguing legislation should make unmerging as feasible as merging. Another questioned what 'ad tech' specifically means given Google's relatively small profit contribution from this segment. Alternative policy proposals emerged, including progressive taxation of monopolies to incentivize self-breakup. Several commenters raised concerns that political donations—citing a reported $22 million ballroom contribution linked to a YouTube lawsuit settlement—may have influenced the outcome.

**Tags**: `#antitrust`, `#google`, `#ad-tech`, `#regulation`, `#monopoly`

---

<a id="item-10"></a>
## [Three sites made 215,128 “best software” pages for AI. Perplexity cites them](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 7.0/10

Investigation reveals that three sites generated over 215,000 SEO-optimized 'best software' pages specifically to be cited by AI search engines like Perplexity, exposing a new form of content manipulation targeting AI systems.

hackernews · jakobgreenfeld · Sep 2, 13:59 · [Discussion](https://news.ycombinator.com/item?id=49536375)

**Tags**: `#AI-search`, `#content-farms`, `#Perplexity`, `#SEO-manipulation`, `#LLM-reliability`

---

<a id="item-11"></a>
## [World's Largest Dark Matter Detector Records Single Anomalous Event](https://www.science.org/content/article/world-s-biggest-dark-matter-detector-spots-single-weird-particle) ⭐️ 7.0/10

The LZ (LUX-ZEPLIN) dark matter detector at the Sanford Underground Research Facility has recorded a single anomalous particle event at approximately 3 sigma significance, potentially hinting at physics beyond the Standard Model. Physicists involved in the experiment have published a preprint analyzing the signal but are urging extreme caution against overinterpretation given that it consists of just one event. This result comes from the world's largest and most sensitive dark matter detector, so any anomalous signal—even a preliminary one—draws intense scrutiny from the particle physics community. If the signal were validated with more data, it could point to new particles or interactions beyond current theory, but a single 3 sigma event falls far short of the 5 sigma threshold required to claim a discovery in particle physics. The LZ detector uses 10 tons of liquid xenon and sits 1,480 meters underground in a former South Dakota gold mine to shield against cosmic rays. The research team systematically investigated possible mis-reconstruction artifacts and background sources before publishing, but as co-founder Tom Shutt of SLAC noted, interpreting a single event remains fundamentally challenging.

hackernews · randycupertino · Sep 2, 13:40 · [Discussion](https://news.ycombinator.com/item?id=49536079)

**Background**: Dark matter is estimated to make up roughly 85% of the matter in the universe, yet it has never been directly detected. The leading theoretical candidates are WIMPs (Weakly Interacting Massive Particles), which would interact so weakly that collisions would impart less energy than a falling snowflake. LZ detects dark matter candidates by watching for tiny flashes in liquid xenon when particles interact with xenon nuclei; outer detector layers reject signals from known particles to reduce background noise.

<details><summary>References</summary>
<ul>
<li><a href="https://www.smithsonianmag.com/science-nature/new-generation-dark-matter-experiments-gear-search-elusive-particle-180974111/">New Generation of Dark Matter Experiments Gear Up to Search for...</a></li>
<li><a href="https://refractor.io/physics/lux-zeplin-world-most-sensitive-dark-matter-detector/">World's most sensitive dark matter detector joins the hunt for WIMPs</a></li>
<li><a href="https://alchetron.com/Sanford-Underground-Research-Facility">Sanford Underground Research Facility - Alchetron, the free social...</a></li>

</ul>
</details>

**Discussion**: The discussion is notably scientifically rigorous: one commenter read the full preprint and praised the team's thorough investigation of potential mis-reconstruction and background issues, while cautioning that particle physics history is littered with 3 sigma 'discoveries' that vanished with more data. Other commenters quoted the scientists directly—particularly Tom Shutt's remark about the difficulty of making sense of a single event—reflecting a collective stance of cautious interest rather than premature celebration.

**Tags**: `#dark-matter`, `#particle-physics`, `#experimental-physics`, `#LZ-detector`, `#science-news`

---

<a id="item-12"></a>
## [Meta Open-Sources 30B Agent Model, Raising Containment Concerns](https://semiwiki.com/artificial-intelligence/372426-containing-ai-agents-with-a-will-of-their-own/) ⭐️ 7.0/10

Meta has open-sourced Muse Glimmer, a 30-billion-parameter agent model under the Apache 2.0 license, designed to run locally on consumer hardware such as a MacBook Pro with M4/M5 Max chips and 32GB of memory. The model supports interleaved text and image inputs, coding, structured planning, and tool execution, enabling always-on local AI agents that do not need to send data to Meta's servers. Open-sourcing a highly capable agent model means anyone can deploy autonomous AI systems that plan and execute multi-step tasks locally, which dramatically expands the attack surface and makes traditional centralized safety guardrails harder to enforce. This raises urgent questions about how developers and enterprises can contain agents that make their own decisions, especially when containment failures can cascade faster than human response times. Unlike a standard LLM that only generates text, an AI agent perceives, reasons, plans, and takes actions toward goals, which is why containment strategies such as runtime sandboxing, behavioral monitoring, context-aware permissions, and just-in-time access control have become critical layers of defense. Running a 30B-parameter dense model on consumer hardware is itself non-trivial, requiring careful memory bandwidth and capacity optimization.

rss · SemiWiki · Sep 2, 21:00

**Background**: AI agents differ from LLMs in that they act autonomously to accomplish goals, not merely generate text, often chaining tool calls and multi-step reasoning. Agent containment refers to techniques that cap what an AI agent can reach and do when other defenses fail, including sandboxing, behavioral monitoring, JIT access, and centralized authorization. Meta's rationale for releasing such a model openly is that powerful agents belong in the hands of developers and researchers rather than being locked behind a single company's servers.

<details><summary>References</summary>
<ul>
<li><a href="https://cctest.ai/en/articles/meta-open-sources-muse-glimmer-a-30b-model-for-local-ai-agents">Meta Open - Sources Muse Glimmer, a 30 B Local Agent Model</a></li>
<li><a href="https://www.cequence.ai/blog/ai/agent-containment/">Agent Containment : Definition, Risks, and Techniques</a></li>
<li><a href="https://dev.to/alvarito1983/metas-muse-glimmer-a-real-agentic-model-that-fits-on-your-own-gpu-16oh">Meta 's Muse Glimmer: a real agentic model that fits... - DEV Community</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#open-source`, `#AI safety`, `#Meta`, `#LLM deployment`

---

<a id="item-13"></a>
## [Intel 18A-P Pushes RibbonFET and Backside Power Beyond the First Generation](https://semiwiki.com/semiconductor-manufacturers/intel/372712-intel-18a-p-pushes-ribbonfet-and-backside-power-beyond-the-first-generation/) ⭐️ 7.0/10

Intel Foundry has introduced Intel 18A-P, described as a performance-enhanced derivative of its 18A process node rather than a brand-new node. It extends RibbonFET gate-all-around (GAA) transistor technology and backside power delivery (BPD) beyond the first-generation 18A implementation, signaling a continued refinement path for Intel's leading-edge process. This matters because 18A is the cornerstone of Intel Foundry's comeback strategy, and a 'P' performance-enhanced variant demonstrates Intel's ability to offer a roadmap of incremental improvements to attract foundry customers. RibbonFET and backside power are critical differentiators as Intel competes against TSMC's N2 and A16 nodes, both of which also employ GAA transistors and backside power delivery. Intel 18A-P is positioned as an optimization rather than a full-node shrink, meaning it likely retains the same design rules and transistor architecture as 18A while improving performance, power, or area characteristics. The article's visible content is truncated and primarily serves as a teaser directing readers to Intel Foundry's official LinkedIn blog for deeper technical substance.

rss · SemiWiki · Sep 2, 17:00

**Background**: RibbonFET is Intel's brand name for its Gate-All-Around (GAA) nanosheet transistor architecture, which replaces the FinFET design used at older process nodes and offers better electrostatic control of the channel at 2nm-class geometries. Backside Power Delivery (BPD) is a relatively new chip-stacking technique that relocates the power routing network to the underside of the wafer, freeing up front-side routing resources for signals and reducing power delivery resistance. Intel initially announced RibbonFET for its 20A node in 2024, and backside power (PowerVia) was a key feature of 18A; 18A-P extends both into a refreshed variant.

<details><summary>References</summary>
<ul>
<li><a href="https://isti.studio/blog/gate-all-around-gaa-transistors-why-ribbonfets-are-replacing-finfets-at-2nm-and-">Gate - All - Around Transistors Explained: RibbonFETs at Intel ...</a></li>
<li><a href="https://avecas.in/backside-power-delivery-semiconductor-2nm-innovation/">The Vertical Revolution: Why Backside Power Delivery is... - Avecas</a></li>
<li><a href="https://www.kad8.com/hardware/tsmc-a16-node-explained-backside-power-and-angstrom-era/">TSMC A16 Node Explained: Backside Power and Angstrom Era · KAD</a></li>

</ul>
</details>

**Tags**: `#semiconductor-manufacturing`, `#intel-18A`, `#ribbonFET`, `#backside-power-delivery`, `#intel-foundry`

---

<a id="item-14"></a>
## [WSTS Projects Memory Chip Revenue to Surge 250% to $804B in 2026](https://www.electronicsweekly.com/blogs/mannerisms/markets/memory-mania-2026-09/) ⭐️ 7.0/10

According to WSTS, global memory-chip revenue is projected to surge 250% to $804 billion in 2026, with the potential to exceed $1 trillion in 2027, while memory's share of the overall semiconductor market continues to expand. This extraordinary growth forecast points to an unprecedented memory boom largely fueled by AI infrastructure demand, particularly for High Bandwidth Memory (HBM). Such a surge would reshape the semiconductor revenue landscape and disproportionately benefit leading memory manufacturers including Samsung, SK Hynix, and Micron. The report suggests memory chips are capturing a growing share of the overall semiconductor pie, with the bulk of demand coming from AI-related applications such as HBM for accelerators, DRAM for servers, and NAND flash for data-center storage. The forecast exceeds typical cyclical memory growth patterns, implying supply tightness may persist into 2027.

rss · Electronics Weekly · Sep 2, 13:07

**Background**: WSTS (World Semiconductor Trade Statistics) is the semiconductor industry's authoritative reference for market data, publishing monthly shipment figures broken down by product type, end-use, and region. Memory chips fall into several major categories: DRAM (the main volatile system memory), NAND flash (non-volatile data storage, first commercialized by Toshiba in 1991), and High Bandwidth Memory (HBM), a 3D-stacked SDRAM technology co-developed by Samsung, AMD, and SK Hynix that is now critical for AI training and inference workloads. The memory market has historically been highly cyclical, with supply gluts triggering price collapses, but AI-driven demand appears to be breaking those traditional boom-and-bust patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wsts.org/">WSTS Home</a></li>
<li><a href="https://www.semiconductors.org/data-resources/market-data/">Semiconductor Market Data | SIA | Semiconductor Industry...</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#memory chips`, `#industry forecast`, `#AI infrastructure`

---

<a id="item-15"></a>
## [Architect Labs Raises $24M for AI-Driven End-to-End Chip Design](https://www.electronicsweekly.com/news/business/the-designless-semiconductor-industry-2026-09/) ⭐️ 7.0/10

Palo Alto-based Architect Labs has raised $24 million to build an AI system that automates end-to-end chip design and verification, aiming to transform workloads into production-ready silicon and significantly accelerate development time. If successful, this system could disrupt the traditional EDA (Electronic Design Automation) industry, which has long been dominated by a handful of established players, by reducing the specialized human labor required to design and verify chips. It represents a significant step toward fully automating one of the most complex and expensive engineering workflows in technology. The company is based in Palo Alto and targets the full chip design flow, not just individual steps like synthesis or layout. The article is brief and does not specify which investors participated, the company's prior products, or the AI techniques being used (e.g., large language models, reinforcement learning, or formal methods).

rss · Electronics Weekly · Sep 2, 05:12

**Background**: Electronic Design Automation (EDA) refers to a category of software tools used by engineers to design integrated circuits (ICs) and printed circuit boards. The traditional chip design flow includes stages from RTL (Register Transfer Level) design through physical layout (GDS), followed by extensive verification to ensure the chip functions correctly before the costly fabrication process. Verification alone is highly complex, requiring simulation, formal verification, and emulation, and constitutes a major portion of chip development cost and time. AI-driven approaches to chip design have been explored by major players such as Google, which has used machine learning for chip floorplanning and other design tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electronic_design_automation">Electronic design automation - Wikipedia</a></li>
<li><a href="https://chipverify.com/tutorials/verification">Introduction to Verification</a></li>
<li><a href="https://www.mckinsey.com/industries/industrials/our-insights/semiconductor-design-and-manufacturing-achieving-leading-edge-capabilities">Semiconductor design and manufacturing: Achieving... | McKinsey</a></li>

</ul>
</details>

**Tags**: `#AI`, `#semiconductors`, `#chip-design`, `#EDA`, `#startup-funding`

---

<a id="item-16"></a>
## [Hardware Unboxed RTX 5090 Suffers Melted Power Connector at 175°C](https://www.techpowerup.com/352273/hardware-unboxed-falls-victim-to-melted-rtx-5090-power-connector-as-cable-reaches-175-c) ⭐️ 6.5/10

Hardware Unboxed's RTX 5090 test bench, pairing an ASUS ROG Astral card with a be quiet! Dark Power 13 PSU, suffered a melted 12V-2x6 power connector with thermal camera readings climbing to roughly 175°C under load. A Thermal Grizzly WireView Pro revealed the root cause: severe current imbalance where a single wire pulled around 22A while other pins carried almost no current. This adds to a growing body of evidence that the 12V-2x6 connector design—originally revised from the problematic 12VHPWR to address melting issues—continues to pose a serious reliability risk for NVIDIA's flagship RTX 5090 GPU. The incident affects prospective buyers, system integrators, and reviewers, and has even pushed some modders to solder power wires directly to the PCB to bypass the connector entirely. Notably, the connector damage was actually worse on the PSU side, where the cable fused inside the Dark Power 13 and required pliers to remove, while the GPU-side connector showed no visible marks. Hardware Unboxed confirmed the cable was fully seated and is not blaming user installation error, pointing to a fundamental design or manufacturing issue in the connector itself.

rss · TechPowerUp News · Sep 2, 17:43

**Background**: The 16-pin 12VHPWR connector was introduced as a new standard to deliver up to 600W to GPUs through a single cable, replacing multiple 8-pin PCIe power connectors. After widespread reports of melting incidents with RTX 4090 and early RTX 5090 cards, the standard was updated to the 12V-2x6 revision with improved contact design and sense pins, intended to be backward-compatible and safer. Despite this revision, melting incidents have continued across multiple PSU brands and card models, and NVIDIA initially attributed earlier failures to improper cable insertion—though this latest case where the cable was fully seated undermines that explanation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/12VHPWR">12 VHPWR - Wikipedia</a></li>
<li><a href="https://www.thermal-grizzly.com/en/wireview-gpu-pro/s-tg-wv-p-h1r">Thermal Grizzly WireView Pro GPU Monitoring Tool</a></li>
<li><a href="https://ebroky.com/16-pin-power-connector-gets-a-much-needed-revision-meet-the-new-12v-2x6-connector/">16-Pin Power Connector Gets A Much-Needed Revision... | eBroky</a></li>

</ul>
</details>

**Tags**: `#RTX 5090`, `#NVIDIA`, `#hardware reliability`, `#power connector`, `#GPU`

---

<a id="item-17"></a>
## [RTX 5090's Single Power Connector May Bottleneck DLSS 5 Neural Rendering](https://www.techpowerup.com/352262/early-dlss-5-testing-suggests-the-rtx-5090s-single-power-connector-might-be-the-bottleneck) ⭐️ 6.5/10

Early community testing of leaked DLSS 5 builds via OptiScaler injection on RTX 5090 cards shows framerate drops of 42–49% on the Founders Edition, which consistently hits its 575 W single-connector power limit, while an MSI Lightning Z with dual connectors and a 1000 W ceiling holds better performance. If confirmed, this finding shifts the bottleneck for next-generation neural rendering away from GPU compute and onto power delivery design, meaning even flagship cards like the RTX 5090 FE may be underprovisioned for DLSS 5 and could pressure NVIDIA and board partners to adopt dual-connector layouts on future flagship SKUs. In Hogwarts Legacy, the MSI card jumped from 480 W to 720 W with neural rendering active—a 50% increase—and the per-frame cost (~8 ms) closely matched NVIDIA's published figure, suggesting the OptiScaler-injected path is representative despite not using NVIDIA's official Streamline API.

rss · TechPowerUp News · Sep 2, 15:03

**Background**: DLSS 5 is NVIDIA's next-generation neural rendering technology, unveiled at GTC 2026, which uses a locally running generative model to enhance scenes rather than just reconstruct them. The 12V-2x6 (also called 12VHPWR) connector is a 16-pin PCIe Gen 5 standard designed to deliver up to 600 W to a GPU through a single cable, but it has been controversial due to reports of melting connectors on high-power cards. OptiScaler is a community tool that acts as a translation layer, allowing users to inject DLSS or other upscalers into games that support competing temporal upscaling APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/review/nvidia-dlss-5-technical-preview/2.html">NVIDIA DLSS 5 Technical Preview - Neural Rendering is Here - How ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/12VHPWR">12 VHPWR - Wikipedia</a></li>
<li><a href="https://github.com/optiscaler/OptiScaler">GitHub - optiscaler / OptiScaler : OptiScaler bridges upscaling/frame...</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#RTX 5090`, `#DLSS 5`, `#GPU hardware`, `#power delivery`

---

<a id="item-18"></a>
## [EFF Urges California Governor to Veto Online Age Verification Bill](https://www.tomshardware.com/tech-industry/eff-asks-california-governor-to-veto-bill-that-would-require-online-age-verification-electronic-frontier-foundation-argues-bill-would-result-in-privacy-invasive-checks-and-step-on-first-amendment) ⭐️ 6.5/10

The Electronic Frontier Foundation (EFF) sent an open letter to California Governor Gavin Newsom urging him to veto Assembly Bill 1709 (A.B. 1709), which would mandate online age verification checks on social media and other digital platforms. The bill functions as a sweeping restriction on social media use for users under 16 years old and will become law unless the governor issues a veto. This bill would set a significant precedent for how online services handle age verification, potentially forcing platforms to collect sensitive personal data from all users to determine age. The outcome could influence similar legislation in other states and shape the balance between child safety online and user privacy rights protected under the First Amendment. According to EFF, age verification methods in use include self-declaration age gates, document-based checks (uploading driver's licenses or passports), and biometric face scans — all of which create privacy risks by collecting sensitive personal data. California is one of at least 27 states that have moved toward ID-grade age checks following the Supreme Court's Paxton ruling, and this bill would extend that framework to social media.

rss · Tom's Hardware · Sep 2, 11:20

**Background**: The Electronic Frontier Foundation is a nonprofit organization that defends civil liberties in the digital world, particularly free speech and privacy rights online. A.B. 1709 is part of a broader wave of legislation across U.S. states aimed at protecting minors online, which intensified after the Supreme Court's decision in the Paxton case upheld age-verification requirements for adult content websites. Critics argue that mandatory age verification creates security vulnerabilities by collecting sensitive identification data, while supporters maintain it is necessary to shield children from harmful content.

<details><summary>References</summary>
<ul>
<li><a href="https://www.eff.org/deeplinks/2026/08/eff-gov-newsom-veto-californias-ab-1709">EFF to Governor Newsom: Veto California ’s AB 1709 | Electronic...</a></li>
<li><a href="https://maxintel.org/age-verification-laws-privacy-2026.html">Age Verification Laws & Your Privacy (2026)</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/eff-asks-california-governor-to-veto-bill-that-would-require-online-age-verification-electronic-frontier-foundation-argues-bill-would-result-in-privacy-invasive-checks-and-step-on-first-amendment">EFF asks California governor to veto bill that would require online age ...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#policy`, `#regulation`, `#online-safety`, `#eff`

---

<a id="item-19"></a>
## [AI Data Center Investment Projected to Hit $32 Trillion by 2050](https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-investment-projected-to-hit-usd32-trillion-by-2050-infrastructure-spending-estimated-to-exceed-capital-requirements-for-railways-electrification-or-the-internet) ⭐️ 6.5/10

A new projection estimates that AI data center infrastructure investment will reach $32 trillion by 2050, surpassing the capital requirements of historical infrastructure booms such as railways, electrification, and the internet. These costs are not one-time expenses—data center operators are expected to refresh their GPU fleets and related infrastructure every four to six years as new semiconductor technologies emerge. This projection frames AI infrastructure as the defining capital expenditure cycle of the next quarter-century, with cumulative spending dwarfing every prior industrial transformation. It has major implications for energy policy, semiconductor supply chains, and global capital allocation, as governments and investors must grapple with funding requirements that exceed even the largest historical infrastructure projects. The recurring 4–6 year GPU upgrade cycle means the $32 trillion figure reflects cumulative lifecycle costs rather than a single buildout, driven by the rapid pace of semiconductor advancement and the sustained near-100% GPU utilization typical of large-scale AI training jobs. This distinguishes AI data centers from traditional data centers, which rarely sustain maximum compute utilization for more than a few minutes.

rss · Tom's Hardware · Sep 2, 11:00

**Background**: AI data centers differ from traditional data centers in that they are purpose-built for sustained, massively parallel GPU workloads such as large-model training and inference, requiring high-performance storage, low-latency networking, and advanced cooling. Historical comparisons to railways (19th century), electrification (early 20th century), and the internet (1990s–2000s) serve as benchmarks for measuring the scale of the current AI buildout. The recurring GPU refresh cycle reflects the fact that AI performance gains are tightly coupled to advances in semiconductor manufacturing, making hardware depreciation faster than in conventional computing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.disintermediate.global/insights/ai-workloads-explained">How AI Workloads Differ from Traditional Computing | Disintermediate</a></li>
<li><a href="https://www.onesourcecloud.net/cms/ai-iaas-gpu-workloads-explained.html">What Is AI IaaS for GPU Workloads ?-OneSource Cloud</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#investment trends`, `#GPU computing`, `#tech economics`

---

<a id="item-20"></a>
## [China's EUV technology lags ASML by 20 years, analyst says](https://www.tomshardware.com/tech-industry/semiconductors/chinas-euv-technology-at-a-similar-stage-to-asml-in-2004-analyst-claims-beijings-semiconductor-industry-remains-well-behind-western-rivals) ⭐️ 6.5/10

An analyst claims that China's EUV lithography technology is roughly comparable to where ASML stood in 2004, meaning Chinese semiconductor equipment makers remain approximately two decades behind Western leaders despite recent rumors of progress. There is no evidence that Chinese lithography tool manufacturers can produce immersion lithography scanners at scale. This assessment is significant because it frames the timeline for China's semiconductor self-sufficiency ambitions and has direct implications for the ongoing US-China tech competition, export controls, and global supply chain dynamics. If accurate, China will remain dependent on foreign lithography equipment for cutting-edge chip manufacturing for many years, affecting geopolitical strategies around chip access. EUV lithography uses 13.5 nm extreme ultraviolet light from laser-pulsed tin plasma to create nanometer-scale patterns on semiconductor substrates, and ASML's scanners are so complex they require disassembly into 20 trucks or three 747s for shipment. Immersion lithography (using DUV/ArF technology with water immersion) is an intermediate step before EUV, and China's inability to mass-produce even immersion scanners highlights the fundamental equipment gap.

rss · Tom's Hardware · Sep 2, 10:15

**Background**: EUV (Extreme Ultraviolet Lithography) is a photolithography technology used to manufacture advanced integrated circuits with extremely fine features, using 13.5nm wavelength light. ASML, a Dutch company, is the sole producer of EUV scanners worldwide, with key customers including TSMC, Samsung, and Intel. EUV scanners are considered the most technically advanced machines ever made, requiring decades of R&D and a vast global supplier network. Immersion lithography using DUV (Deep Ultraviolet) wavelengths is a predecessor technology that enables somewhat finer features than dry lithography but is still significantly less advanced than EUV.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">EUV lithography - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ASML">ASML - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#EUV lithography`, `#ASML`, `#China tech`, `#semiconductor manufacturing`

---