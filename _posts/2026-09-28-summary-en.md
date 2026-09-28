---
layout: default
title: "Horizon Summary: 2026-09-28 (EN)"
date: 2026-09-28
lang: en
---

> From 39 items, 8 important content pieces were selected

---

1. [SharpEmu PS5 Emulator Achieves Playable 60 FPS on Six Titles](#item-1) ⭐️ 8.5/10
2. [Fireworks AI announces Ember-1, its first in-house open-weight model](#item-2) ⭐️ 8.0/10
3. [ProsperoEden Ports Nintendo Switch Emulator to Jailbroken PS5](#item-3) ⭐️ 7.5/10
4. [Linux Kernel Compilation Approaches 10-Second Mark](#item-4) ⭐️ 7.5/10
5. [Go Developers Debate Decoupling Code from GitHub](#item-5) ⭐️ 7.0/10
6. [Flock seeks to have security researchers' map of Flock cameras taken down](#item-6) ⭐️ 6.5/10
7. [Developer says AI decision model Jev beat Pokémon Red in under a week](#item-7) ⭐️ 6.5/10
8. [UK Drone Submarine Successfully Launches Heavy Torpedo in Joint Test](#item-8) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [SharpEmu PS5 Emulator Achieves Playable 60 FPS on Six Titles](https://www.tomshardware.com/desktops/gaming-pcs/ps5-emulator-successfully-runs-six-titles-at-a-playable-60-fps-ps5-emulation-continues-to-gather-momentum-as-developers-improve-shader-translation-and-vulkan-support) ⭐️ 8.5/10

The SharpEmu PS5 emulator has released an update that enables it to run six specific tested titles at a stable 60 FPS. Additionally, the emulator now successfully reaches gameplay state on 12 out of 55 tested games. Achieving stable 60 FPS on modern console hardware is a significant technical milestone for emulation enthusiasts and systems researchers. It demonstrates the viability of translating complex next-generation graphics APIs to open-source backends. The performance gains were primarily driven by improvements to the shader translation pipeline and the integration of Vulkan backend support. Reaching 12 out of 55 titles at a playable state indicates a strong upward trajectory for the project's compatibility.

rss · Tom's Hardware · Sep 27, 12:40

**Background**: PS5 emulation requires translating the PlayStation 5's proprietary graphics and compute APIs into standard formats like Vulkan that run on general-purpose PC hardware. Shader translation is a critical bottleneck in this process, as it involves converting high-level graphics code into efficient GPU instructions compatible with consumer graphics cards.

**Tags**: `#Game Emulation`, `#Vulkan`, `#PS5`, `#Graphics Programming`, `#Hardware`

---

<a id="item-2"></a>
## [Fireworks AI announces Ember-1, its first in-house open-weight model](https://fireworks.ai/blog/ember-1) ⭐️ 8.0/10

Fireworks AI, a major AI infrastructure provider, has released Ember-1, its first in-house developed model, signaling a strategic shift from purely hosting third-party models to conducting foundational model research. This move blurs the line between inference infrastructure providers and model developers, potentially accelerating the convergence of these sectors and driving competition on both cost-efficiency and open-source innovation. The release is characterized by a focus on efficiency and the development of open-weight models, which contrasts with the proprietary approaches of major tech companies. Community interest centers on how this in-house development impacts Fireworks' neutrality as an API provider for other open models.

hackernews · gmays · Sep 27, 17:31 · [Discussion](https://news.ycombinator.com/item?id=49868830)

**Background**: Fireworks AI is a company that primarily provides optimized inference infrastructure for running AI models on GPUs. In the current AI landscape, 'open-weight' models are those whose parameters are publicly available for download, but distinct from 'open-source' AI which includes full access to training data and code. Most infrastructure providers traditionally host models developed by external research labs or large tech corporations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fireworks_AI">Fireworks AI - Wikipedia</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed, with some celebrating the accessibility of model training and fine-tuning workflows, while others express concern about Fireworks' potential conflicts of interest now that it is competing with the open-source models it previously hosted. Some users also engaged in comparative pricing discussions, noting the value proposition of other models like Sol and Kimi K3 against the backdrop of new releases.

**Tags**: `#LLM`, `#Model-Release`, `#Fireworks-AI`, `#Open-Source-AI`, `#Fine-Tuning`

---

<a id="item-3"></a>
## [ProsperoEden Ports Nintendo Switch Emulator to Jailbroken PS5](https://www.techpowerup.com/353135/experimental-emulator-brings-nintendo-switch-games-to-jailbroken-ps5-consoles) ⭐️ 7.5/10

Developer BlackBearReloaded released ProsperoEden, an experimental homebrew port of the Eden Nintendo Switch emulator that runs natively on jailbroken PS5 consoles. The v1.000.010 build achieves playable frame rates, reaching 60 FPS for titles like Cuphead and allowing actual gameplay for Mario Kart 8 Deluxe. This project demonstrates the advanced capabilities of jailbroken PS5 hardware, showing its potential for cross-emulation and systems research. It highlights how quickly the homebrew community can leverage new firmware vulnerabilities to expand the console's functionality beyond official support. The port currently supports only the OpenGL backend, with no Vulkan renderer built for the PS5 side. The build is still in alpha and requires manual user-supplied keys, firmware, and game files, and some games like Pokemon Legends Z-A remain very slow with crashes.

rss · TechPowerUp News · Sep 27, 19:03

**Background**: The Nintendo Switch emulator Yuzu was famously shut down by Nintendo in 2024, leading to the rise of new forks like Eden. The PS5 jailbreak scene has been rapidly expanding since 2024, with new tools and homebrew applications allowing the console to run non-licensed software and operating systems like Linux.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yuzu_(emulator)">Yuzu (emulator) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#PS5 Jailbreak`, `#Emulation`, `#Nintendo Switch`, `#Homebrew`, `#Reverse Engineering`

---

<a id="item-4"></a>
## [Linux Kernel Compilation Approaches 10-Second Mark](https://www.tomshardware.com/software/linux/linux-enthusiasts-see-10-second-kernel-compilation-times-on-the-horizon-ai-assisted-patches-cut-build-times-by-nearly-a-third-without-a-ramdisk) ⭐️ 7.5/10

Phoronix reported that clean Linux kernel build times are approaching 10 seconds, with AI-assisted compiler patches cutting build times by nearly a third. This milestone is achieved through modern multi-core hardware, such as the AMD EPYC 9575F 2P system ranking fastest in benchmarking. Reduction of kernel compilation to under 10 seconds significantly accelerates developer workflows and CI/CD pipelines. This milestone allows Linux developers to iterate on complex system-level changes with near-instantaneous feedback. The AMD EPYC 9575F 2P setup is currently benchmarked at around 20 seconds for an x86_64 defconfig build. This speed was achieved without the use of a ramdisk, highlighting the impact of hardware advancements and optimized compiler heuristics.

rss · Tom's Hardware · Sep 27, 12:20

**Background**: Compiling the Linux kernel is a resource-intensive process that traditionally takes minutes to hours on consumer hardware. Multi-core processors from AMD and Intel have dramatically reduced these times, making the 10-second mark a highly sought-after milestone in the community.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/review/near-10-sec-kernel-build">Approaching A 10 Second Linux Kernel Build - Phoronix</a></li>
<li><a href="https://www.tomshardware.com/software/linux/linux-enthusiasts-see-10-second-kernel-compilation-times-on-the-horizon-ai-assisted-patches-cut-build-times-by-nearly-a-third-without-a-ramdisk">Linux enthusiasts see 10-second kernel compilation times on ...</a></li>

</ul>
</details>

**Tags**: `#Linux`, `#Compiler Optimization`, `#AI`, `#Build Systems`, `#Performance`

---

<a id="item-5"></a>
## [Go Developers Debate Decoupling Code from GitHub](https://iain.rocks/blog/dont-couple-your-go-code-to-github) ⭐️ 7.0/10

A technical article and subsequent Hacker News discussion advocate for using custom domains instead of GitHub URLs to namespace Go packages. The authors argue that decoupling code from a specific git host simplifies future migrations and improves long-term portability. Go's module system uses import paths as its namespace, making the choice of domain critical for enterprise stability and cloud-vendor neutrality. This issue directly impacts how large teams manage dependency risks and plan infrastructure transitions over the long term. Critics point out that using a custom domain introduces new operational overhead, such as the need to maintain a Git server or configure a custom Git host. Additionally, the 'replace' directive in go.mod offers a standard, native workaround for migrating dependencies without altering the codebase itself.

hackernews · birdculture · Sep 27, 16:50 · [Discussion](https://news.ycombinator.com/item?id=49868404)

**Background**: In Go modules, the import path serves as the source of truth for where a package is fetched from and is embedded into the code. While this ensures unique naming, it rigidly ties the code to a specific Git hosting provider like GitHub. The go.mod file and 'vendor' directory are the primary mechanisms for managing and overriding these external dependencies.

<details><summary>References</summary>
<ul>
<li><a href="https://go.dev/ref/mod">Go Modules Reference - The Go Programming Language</a></li>
<li><a href="https://arslan.io/2019/08/02/why-you-should-use-a-go-module-proxy/">Why you should use a Go module proxy - Fatih Arslan</a></li>

</ul>
</details>

**Discussion**: The discussion is highly divided, with some developers arguing that a custom domain offers long-term safety but others counter that GitHub's dominance makes this a premature optimization. Furthermore, the conversation shifts to the reliability of owning a custom domain, with some noting that domain registrars can unilaterally delete accounts and that the go.mod 'replace' directive makes manual code refactoring unnecessary.

**Tags**: `#Go`, `#Software Engineering`, `#Dependency Management`, `#Best Practices`, `#Cloud Infrastructure`

---

<a id="item-6"></a>
## [Flock seeks to have security researchers' map of Flock cameras taken down](https://www.tomshardware.com/tech-industry/cyber-security/flock-seeks-to-have-security-researchers-map-of-flock-cameras-taken-down-unauthenticated-flaw-exposed-335-701-camera-locations-nationwide) ⭐️ 6.5/10

Flock is attempting to have security researchers' maps of its 335,701 camera locations removed after an unauthenticated vulnerability exposed data enabling tracking of personnel at sensitive government sites.

rss · Tom's Hardware · Sep 27, 12:00

**Tags**: `#Cybersecurity`, `#Surveillance`, `#Vulnerability`, `#Data Privacy`, `#IoT`

---

<a id="item-7"></a>
## [Developer says AI decision model Jev beat Pokémon Red in under a week](https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-says-jev-decision-model-beat-pokemon-red-in-under-a-week-non-llm-engine-succeeds-where-traditional-chatbots-stalled-for-months-but-claude-opus-5-coached-the-model-through-its-dead-ends) ⭐️ 6.5/10

TypeSafe AI's non-LLM model Jev successfully beat Pokémon Red in under a week, demonstrating that specialized decision models can outperform general-purpose LLMs in specific gaming environments.

rss · Tom's Hardware · Sep 27, 11:30

**Tags**: `#Artificial Intelligence`, `#Reinforcement Learning`, `#Gaming`, `#LLM vs Non-LLM`, `#Automation`

---

<a id="item-8"></a>
## [UK Drone Submarine Successfully Launches Heavy Torpedo in Joint Test](https://www.tomshardware.com/tech-industry/u-s-and-uk-navies-successfully-launch-3-700-pound-submarine-sinking-torpedo-from-robotic-drone-submarine-in-historic-first-project-broadsword-proves-weapon-interchangeability-in-just-seven-months) ⭐️ 6.5/10

The U.S. and UK navies successfully launched a 3,700-pound Mk 48 torpedo from Britain's uncrewed XV Excalibur submarine. This marked the first time such a heavy weapon was fired from an autonomous underwater vehicle. The milestone proves cross-platform weapon compatibility and interoperability, demonstrating the practical value of autonomous systems in high-stakes defense. It significantly shortens the development cycle for integrating heavy armaments into drone platforms. The weapon used was the Mk 48 heavyweight torpedo, and the autonomous vehicle was the UK's XV Excalibur submarine. This achievement was accomplished under Project Broadsword, a program that proved weapon interchangeability in just seven months.

rss · Tom's Hardware · Sep 27, 10:30

**Background**: The Mk 48 torpedo is one of the most widely used anti-submarine weapons in the world, typically launched from manned nuclear or conventional submarines. Unmanned Underwater Vehicles (UUVs) are increasingly being used to extend naval reach, but adapting them to carry and launch heavy torpedos has historically been a significant technical hurdle. Interoperability allows weapons designed for one ship class to be used on another.

**Tags**: `#Autonomous Systems`, `#Defense Technology`, `#Robotics`, `#Interoperability`, `#Maritime`

---