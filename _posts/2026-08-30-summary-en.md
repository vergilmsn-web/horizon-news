---
layout: default
title: "Horizon Summary: 2026-08-30 (EN)"
date: 2026-08-30
lang: en
---

> From 39 items, 16 important content pieces were selected

---

1. [Arbitrary Code Execution in QubesOS via qvm-copy-to-vm Error Reporting](#item-1) ⭐️ 8.0/10
2. [China's top DRAM maker CXMT sues Pentagon over its blacklisting — argues chips are standard civilian JEDEC spec, not defense hardware](#item-2) ⭐️ 7.5/10
3. [Pixel 11 Drops Hardware MTE Support; Sony & Warner Sue Anthropic](#item-3) ⭐️ 7.3/10
4. [Omarchy Linux: Any User Process Can Escalate to Root via Docker Group](#item-4) ⭐️ 7.0/10
5. [Creepy Crawlies](#item-5) ⭐️ 7.0/10
6. [European Commission Revives Push for Encryption Backdoors in ProtectEU Strategy](#item-6) ⭐️ 7.0/10
7. [Bug Blindness](#item-7) ⭐️ 7.0/10
8. [SpaceX brings turbine blade manufacturing in-house to speed up AI data center power](#item-8) ⭐️ 6.5/10
9. [DIY Archivists Use Budget Nikons and Neural Networks to Digitize 1,800 Rare Books](#item-9) ⭐️ 6.5/10
10. [Corsair RM1000e (2026) Review: Temperature-Sensing Cable Prevents GPU Connector Melting](#item-10) ⭐️ 6.5/10
11. [Leaked DLSS 5 Runs on RTX 30-Series GPUs but Performance Collapses](#item-11) ⭐️ 5.5/10
12. [SteamOS 3.9.0 Preview Released with KDE 6.7.3 and Linux Kernel 7.2](#item-12) ⭐️ 5.5/10
13. [Intel Officially Confirms LGA1954 Socket for Nova Lake-S Processors](#item-13) ⭐️ 5.5/10
14. [Donkey Kong 64 finally gets a fully native PC port written in C — DK64 ReKONGpiled brings ultrawide support, uncapped framerates, and zero AI code](#item-14) ⭐️ 5.5/10
15. [Modders Solder Cables Directly to RTX 5090 PCB to Bypass Melting Connector](#item-15) ⭐️ 5.5/10
16. [US military uses high-energy lasers to shoot down three Mexican cartel drones over the southern border — narcos suspected of using UAVs for surveillance and reconnaissance to support illegal activities](#item-16) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Arbitrary Code Execution in QubesOS via qvm-copy-to-vm Error Reporting](https://www.qubes-os.org/news/2026/08/29/qsb-118/) ⭐️ 8.0/10

A critical arbitrary code execution vulnerability (QSB-118) was disclosed in QubesOS, found in the `qvm-copy-to-vm` tool's error reporting mechanism, which calls `system()` and can be abused as a backchannel from the privileged Dom0 domain. Notably, the VM-side variant of the tool is not affected because its error reporting function does not use `system()`. This vulnerability is significant because QubesOS is a security-focused operating system used by high-value targets such as journalists, activists, and security professionals who rely on its compartmentalization architecture to protect sensitive workflows. Even though QubesOS is designed around minimizing the trusted computing base, a relatively mundane error-handling path using `system()` created a bridge for code execution back into Dom0, undermining core security assumptions. The flaw specifically affects the Dom0-side implementation of `qvm-copy-to-vm`, where error messages are constructed via `system()`, allowing attacker-controlled content to influence command execution. Because Dom0 has full control over all VMs, any code execution within it is catastrophic; QubesOS best practice already recommends not performing routine tasks in Dom0, which significantly limits the practical attack surface.

hackernews · vntok · Aug 30, 08:51 · [Discussion](https://news.ycombinator.com/item?id=49496918)

**Background**: QubesOS is a security-oriented operating system that uses Xen-based virtualization to compartmentalize different activities into isolated virtual machines (qubes). Dom0 is the privileged administrative domain that manages all other VMs and has full access to them, making it the most security-sensitive component of the system. The `qvm-copy-to-vm` tool is commonly used to securely transfer files between qubes, with design features that sanitize content to prevent data leakage between compartments. The use of `system()` to format error messages—a pattern long discouraged by security-conscious projects like OpenBSD—created an unexpected vector for code execution.

<details><summary>References</summary>
<ul>
<li><a href="https://doc.qubes-os.org/en/latest/user/how-to-guides/how-to-copy-from-dom0.html">How to copy from dom0 — Qubes OS Documentation</a></li>

</ul>
</details>

**Discussion**: Commenters expressed surprise that even QubesOS, with its minimal attack surface, could harbor such a bug, while also noting that the vulnerability only affects Dom0 usage, which should be rare in normal operation. Several users referenced OpenBSD's Theo DeRaadt as a philosophical parallel on avoiding risky APIs, and others discussed founder Joanna Rutkowska's legacy and practical limitations like the lack of GPU acceleration. Overall sentiment remained positive about QubesOS despite the disclosure, with users reaffirming trust in its design philosophy.

**Tags**: `#security`, `#qubesos`, `#vulnerability`, `#operating-systems`, `#exploit`

---

<a id="item-2"></a>
## [China's top DRAM maker CXMT sues Pentagon over its blacklisting — argues chips are standard civilian JEDEC spec, not defense hardware](https://www.tomshardware.com/pc-components/dram/chinas-top-dram-maker-cxmt-sues-pentagon-over-its-blacklisting-argues-chips-are-standard-civilian-jedec-spec-not-defense-hardware) ⭐️ 7.5/10

CXMT, China's leading DRAM manufacturer, is suing the Pentagon to remove itself from the Chinese military companies blacklist, arguing its chips are standard JEDEC-spec civilian hardware.

rss · Tom's Hardware · Aug 30, 11:30

**Tags**: `#semiconductors`, `#US-China-tech-war`, `#DRAM`, `#export-controls`, `#geopolitics`

---

<a id="item-3"></a>
## [Pixel 11 Drops Hardware MTE Support; Sony & Warner Sue Anthropic](https://www.solidot.org/story?sid=85233) ⭐️ 7.3/10

GrapheneOS has discovered that Google's Pixel 11 removes hardware MTE (Memory Tagging Extension) support, making it unable to support the device and prompting a recommendation against purchase. Separately, Sony and Warner have sued Anthropic for allegedly using tens of thousands of copyrighted songs to train its Claude models, seeking up to $150,000 per infringed work in a case that could result in billions of dollars in damages. The Pixel 11's removal of MTE is a notable security regression, especially given that Apple's iPhone 17 enables memory integrity protection by default, marking a divergence in security philosophy between the two flagship platforms. The Anthropic lawsuit represents a landmark legal challenge that could reshape how AI companies handle copyrighted training data, with potential ripple effects across the entire generative AI industry. Google first supported hardware MTE starting with the Pixel 8 in 2023, but Android and Pixel OS never enabled it by default—GrapheneOS offered per-app toggles to enable MTE for compatible applications. Meanwhile, the Anthropic lawsuit alleges co-founder Benjamin Mann used BitTorrent to download over 5 million pirated books, and Anthropic employees downloaded over 2 million books from the Pirate Library Mirror, as well as scraped lyrics from licensed services like MusixMatch and LyricFind.

rss · Solidot · Aug 29, 23:44

**Background**: ARM Memory Tagging Extension (MTE) is a hardware security feature introduced in ARMv8.5-A that assigns tags to memory allocations, enabling the detection of buffer overflows, use-after-free bugs, and other memory safety violations. Apple's equivalent implementation, called Memory Integrity Enforcement (MIE) on iPhone 17, covers the kernel and over 70 userland processes by default. GrapheneOS is an open-source, privacy-focused mobile operating system built on AOSP, originally available only on Google Pixel devices but now expanding to Motorola hardware using Qualcomm's Snapdragon 8 Elite Gen 5 SoC, which supports hardware MTE. The Anthropic lawsuit joins a growing wave of copyright litigation against AI companies, similar to cases brought by authors and the New York Times against OpenAI and Microsoft.

<details><summary>References</summary>
<ul>
<li><a href="https://source.android.com/docs/security/test/memory-safety/arm-mte">Arm Memory Tagging Extension | Android Open Source Project</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS - Wikipedia</a></li>
<li><a href="https://redact.dev/blog/iphone-17-memory-integrity-enforcement-explained">Memory Integrity Enforcement : iPhone 17 ’s Counter-Spyware System</a></li>

</ul>
</details>

**Tags**: `#android-security`, `#mte`, `#grapheneos`, `#anthropic`, `#copyright-lawsuit`

---

<a id="item-4"></a>
## [Omarchy Linux: Any User Process Can Escalate to Root via Docker Group](https://0xcc.io/posts/omarchy-root-creds/) ⭐️ 7.0/10

A security analysis published on 0xcc.io reveals that Omarchy's default configuration grants users membership in the Docker group, allowing any user process to trivially escalate privileges to root by mounting the host filesystem inside a container. The post also references a previously disclosed flaw (commit 9285b19d) in which Omarchy flowed raw USB descriptors directly into the shell, reinforcing concerns about systemic security weaknesses in the distribution. This matters because Omarchy is a high-profile, opinionated Arch-based distribution promoted by DHH (David Heinemeier Hansson) and has attracted significant hype from YouTube creators and developers. The default inclusion of users in the Docker group normalizes a configuration that effectively disables the user/root privilege boundary, undermining the security model that most users expect from a desktop operating system. The Docker group privilege escalation is a long-documented attack vector: a user in the docker group can run `docker run -v /:/mnt` to gain read/write access to the host's `/etc/passwd` and `/etc/shadow`, effectively becoming root. Omarchy's previous USB shell-injection flaw (where untrusted device descriptors were passed straight to shell evaluation) suggests a broader pattern of insufficient input sanitization rather than an isolated misconfiguration.

hackernews · trap0xcc · Aug 30, 15:59 · [Discussion](https://news.ycombinator.com/item?id=49499854)

**Background**: Omarchy is an opinionated Linux distribution built on top of Arch Linux and the Hyprland Wayland compositor, released by DHH on June 26, 2025, and positioned primarily as a developer environment. The broader concept of 'vibe coding' refers to AI-assisted development where code is generated largely through iterative LLM prompts with minimal manual review, and critics apply the term to entire distributions when such practices appear to shape system-level configuration. Membership in the Docker group has been a recognized privilege escalation vector for over a decade, because Docker's architecture inherently requires the daemon to operate with root-level control over the host — alternatives such as rootless Podman exist precisely to mitigate this risk.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Omarchy">Omarchy - Wikipedia</a></li>
<li><a href="https://github.com/omacom/omarchy">GitHub - omacom/omarchy: Beautiful, Modern & Opinionated Linux · GitHub</a></li>
<li><a href="https://www.securitum.com/privilege_escalation_through_docker_group_membership_and_sudo_backdoor.html">privilege escalation through Docker group membership</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agreed that adding users to the docker group is a well-known footgun, but one user (exitb) pushed back against framing it as Omarchy-specific since the misconfiguration is common elsewhere. mike_hearn argued this is largely 'security theatre' because Linux lacks proper desktop sandboxing, meaning a malicious process can still compromise the user regardless of root containment. Others recommended rootless Podman as a modern alternative and warned against adopting hyped, vibecoded distributions, noting that CachyOS faced similar scrutiny earlier. Multiple commenters suggested using vanilla Arch with archinstall rather than relying on opinionated wrapper layers.

**Tags**: `#security`, `#linux`, `#privilege-escalation`, `#omarchy`, `#docker`

---

<a id="item-5"></a>
## [Creepy Crawlies](https://people.kernel.org/monsieuricon/creepy-crawlies) ⭐️ 7.0/10

Article on the escalating battle against AI scrapers through proof-of-work systems like Anubis, with expert community critique arguing that high-powered scrapers are better equipped to handle PoW challenges than legitimate users.

hackernews · zdw · Aug 29, 17:49 · [Discussion](https://news.ycombinator.com/item?id=49491791)

**Tags**: `#bot-detection`, `#proof-of-work`, `#ai-scraping`, `#web-security`, `#anubis`

---

<a id="item-6"></a>
## [European Commission Revives Push for Encryption Backdoors in ProtectEU Strategy](https://reclaimthenet.org/eu-protecteu-strategy-encryption-backdoor-law-enforcement) ⭐️ 7.0/10

The European Commission's ProtectEU strategy revives efforts to mandate encryption backdoors for law enforcement access, raising concerns about privacy, security, and EU democratic accountability.

hackernews · nickslaughter02 · Aug 30, 15:12 · [Discussion](https://news.ycombinator.com/item?id=49499394)

**Tags**: `#encryption`, `#privacy`, `#EU-policy`, `#law-enforcement`, `#cybersecurity`

---

<a id="item-7"></a>
## [Bug Blindness](https://danluu.com/bug-blind/) ⭐️ 7.0/10

Dan Luu's analytical essay explores how developers and users can be 'blind' to bugs due to misaligned mental models with the system, illustrated through search, productivity tools, and other software examples.

hackernews · davidmckenna · Aug 30, 00:21 · [Discussion](https://news.ycombinator.com/item?id=49494520)

**Tags**: `#software-engineering`, `#ux`, `#debugging`, `#dan-luu`, `#cognitive-bias`

---

<a id="item-8"></a>
## [SpaceX brings turbine blade manufacturing in-house to speed up AI data center power](https://www.tomshardware.com/tech-industry/data-centers/spacex-starts-in-house-turbine-blade-manufacturing-to-boost-gas-powered-generator-output-for-elons-ai-data-centers-new-manufacturing-strategy-cuts-generator-delays-by-18-months) ⭐️ 6.5/10

SpaceX has begun manufacturing turbine blades and vanes in-house to address critical supply bottlenecks, a move the company says will cut generator delivery delays by up to 18 months for Elon Musk's AI data center power needs. This vertical integration move highlights the severe power supply bottleneck constraining AI infrastructure expansion and illustrates how companies are resorting to unconventional manufacturing strategies to secure energy capacity amid surging demand from AI workloads. A single set of roughly 40 advanced turbine blades can cost over $600,000 and require 60 to 90 weeks to manufacture due to precision machining and advanced materials requirements, which has kept the global gas turbine industry highly concentrated among a few players such as GE Vernova and Siemens Energy.

rss · Tom's Hardware · Aug 30, 14:49

**Background**: Gas turbines are increasingly being deployed as backup or primary power sources for AI data centers because they can be installed quickly and deliver large-scale, reliable electricity. The AI boom has driven unprecedented power demand, creating a multi-billion-dollar windfall for industrial gas turbine manufacturers while simultaneously exposing deep supply chain bottlenecks. Turbine blades and vanes are among the most complex components in a turbine engine, requiring precision casting or additive manufacturing, superalloy materials, and extensive quality assurance. Vertical integration, the practice of bringing previously outsourced production in-house, is a strategy companies use to reduce dependency on external suppliers, shorten lead times, and improve quality control.

<details><summary>References</summary>
<ul>
<li><a href="https://www.filtercoffee.co/stories/why-is-the-world-suddenly-short-on-gas-turbines">Why is the world suddenly short on gas turbines ? - Filter Coffee</a></li>
<li><a href="https://www.squaredtech.co/ai-data-centers-are-driving-a-major-gas-turbine-boom">AI Data Centers Powering The Biggest Gas Turbine Boom In Yea</a></li>
<li><a href="https://www.linkedin.com/pulse/ai-cybersecurity-from-ground-up-part-6-gas-turbines-brendan-cronin-vzvse">AI cybersecurity from the ground up - Part 6 ' Gas Turbines '</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#manufacturing`, `#SpaceX`, `#power generation`

---

<a id="item-9"></a>
## [DIY Archivists Use Budget Nikons and Neural Networks to Digitize 1,800 Rare Books](https://www.tomshardware.com/tech-industry/artificial-intelligence/diy-archivists-push-budget-nikons-to-902-000-clicks-to-save-1-800-rare-books-team-trains-neural-net-on-photoshop-edits-to-process-526-000-scans) ⭐️ 6.5/10

A team of DIY archivists pushed budget Nikon cameras to 902,000 shutter actuations to scan 1,800 rare books, producing 526,000 scans that were then processed using a neural network trained on human Photoshop edits. This project demonstrates how resourceful DIY approaches combined with custom machine learning can enable cultural heritage preservation at scale, offering a low-cost alternative to expensive institutional digitization efforts. The cameras were pushed to an extreme 902,000 shutter actuations — far beyond typical consumer camera lifespans — while the neural network was specifically trained on Photoshop edits to automate the labor-intensive post-processing of 526,000 scanned pages.

rss · Tom's Hardware · Aug 30, 12:00

**Background**: Shutter actuation count refers to the total number of times a camera's mechanical shutter has fired; consumer-grade cameras are typically rated for 100,000–300,000 actuations before the mechanism may fail, making 902,000 clicks exceptional stress testing. Neural networks are machine learning models that learn patterns from training data — in this case, the team fed the network pairs of raw scans and their human-edited Photoshop counterparts so it could learn to apply corrections automatically. Digitizing rare books is critical for preservation, as physical copies are vulnerable to deterioration, fire, and loss of access.

<details><summary>References</summary>
<ul>
<li><a href="https://countmyshutter.com/?ref">Camera Shutter Counter | Check Your DSLR Shutter Count</a></li>
<li><a href="https://petapixel.com/camera-shutter-count/">How to Check Your Camera ’s Shutter Count | PetaPixel</a></li>

</ul>
</details>

**Tags**: `#digital-preservation`, `#machine-learning`, `#computer-vision`, `#DIY-tech`, `#cultural-heritage`

---

<a id="item-10"></a>
## [Corsair RM1000e (2026) Review: Temperature-Sensing Cable Prevents GPU Connector Melting](https://www.tomshardware.com/pc-components/power-supplies/corsair-rm1000e-2026-thermalprotect-power-supply-review) ⭐️ 6.5/10

Corsair's 2026 RM1000e power supply delivers Platinum-class efficiency, a 500W fanless operation window, and a ThermalProtect 12V-2x6 cable that can shut down the GPU before the connector overheats. The ThermalProtect cable embeds Over Temperature Protection (OTP) sensing directly into its integrated cable comb as a last-line-of-defense safety mechanism. This addresses the persistent and well-documented problem of melting 12VHPWR/12V-2x6 connectors on high-wattage GPUs, which have caused fires and destroyed thousands of dollars in hardware. By adding an active thermal shutdown to the cable itself rather than relying solely on connector design improvements, Corsair is raising the bar for GPU power safety and may pressure other PSU makers to follow. The ThermalProtect cable has strict orientation requirements—the temperature sensor must face the GPU side of the connection in order to function correctly, which is a notable installation caveat. The cable is also sold separately as a standalone accessory and is compatible with any PSU that provides a native 12V-2x6 connector.

rss · Tom's Hardware · Aug 30, 11:05

**Background**: The 12VHPWR (12-Volt High Power) connector is a 16-pin standard designed to deliver up to 600W to graphics cards, replacing older 8-pin PCIe power connectors for high-end GPUs. After widespread reports of connectors melting due to poor contact, uneven insertion, and manufacturing defects, the industry revised the standard to 12V-2x6, which is mechanically more durable and less prone to melting. However, melting incidents have continued to occur, prompting hardware vendors to add active safeguards such as thermal sensors and automatic shutdown circuits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/power-supplies/corsair-rm1000e-2026-thermalprotect-power-supply-review">Corsair RM1000e (2026) ThermalProtect power... | Tom's Hardware</a></li>
<li><a href="https://www.corsair.com/us/en/explorer/diy-builder/power-supply-units/corsair-thermalprotect-technical-overview/">Technical overview of the CORSAIR ThermalProtect 12V-2x6 cable</a></li>
<li><a href="https://en.wikipedia.org/wiki/12VHPWR">12 VHPWR - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#power-supply`, `#corsair`, `#gpu-safety`, `#pc-components`

---

<a id="item-11"></a>
## [Leaked DLSS 5 Runs on RTX 30-Series GPUs but Performance Collapses](https://www.techpowerup.com/352147/leaked-dlss-5-reaches-rtx-30-series-ampere-gpus-but-performance-falls-apart) ⭐️ 5.5/10

Modders on the RenoDX Discord have ported a leaked build of DLSS 5's Neural Rendering technology onto unsupported RTX 30-series 'Ampere' GPUs, but the results are essentially unusable — an RTX 3070 laptop saw render latency skyrocket from ~29 ms to over 3,300 ms in Kingdom Come: Deliverance II, while an RTX 3080 dropped from ~130 FPS to just 4 FPS in Deep Rock Galactic, and RTX 3050/3060 Ti cards hovered near 1 FPS. This confirms that DLSS 5's Neural Rendering relies heavily on hardware features absent in Ampere, making any official backport to RTX 30-series extremely unlikely, and signaling NVIDIA's intent to lock the technology to newer architectures — it also shows the gap between Blackwell's capable RTX 40-series results and the catastrophic Ampere experience. The root cause is that Ampere lacks native FP8 (8-bit floating point) support, which the leaked DLSS 5 model relies on for its Tensor Core operations, forcing the GPU to emulate or fail at the precision DLSS 5 expects. Official DLSS 5 only supports RTX 50-series 'Blackwell' GPUs, and NVIDIA has not announced plans to add RTX 40-series support, let alone older generations.

rss · TechPowerUp News · Aug 30, 16:43

**Background**: NVIDIA DLSS (Deep Learning Super Sampling) is a suite of neural rendering technologies powered by dedicated Tensor Cores on RTX GPUs, designed to boost frame rates by using AI to reconstruct higher-resolution images from lower-resolution renders. DLSS 5 is NVIDIA's latest generation, unveiled at GTC 2026, which uses a 'Neural Rendering' model to add photorealistic lighting and material effects in real time — a much heavier workload than previous DLSS upscaling. The RTX 30-series 'Ampere' architecture, launched in 2020, features 3rd-generation Tensor Cores that lack native FP8 throughput, unlike the newer RTX 40-series 'Ada Lovelace' and RTX 50-series 'Blackwell' architectures, which is why DLSS 5's compute demands cannot be met on these older cards.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ampere_(microarchitecture)">Ampere (microarchitecture) - Wikipedia</a></li>
<li><a href="https://wccftech.com/nvidia-dlss-5-neural-rendering-in-10-modern-games-the-best-unofficial-dlss-5-on-vs-off-comparisons-so-far/">NVIDIA DLSS 5 Neural Rendering In 10 Modern Games – The Best...</a></li>

</ul>
</details>

**Tags**: `#nvidia`, `#dlss-5`, `#rtx-30-series`, `#gpu`, `#modding`

---

<a id="item-12"></a>
## [SteamOS 3.9.0 Preview Released with KDE 6.7.3 and Linux Kernel 7.2](https://www.techpowerup.com/352133/steamos-3-9-0-preview-launches-with-kde-6-7-3-and-linux-kernel-7-2) ⭐️ 5.5/10

Valve has released the SteamOS 3.9.0 Preview, upgrading Desktop Mode to KDE Plasma 6.7.3 (from 6.4.3) and updating the Linux kernel to version 7.2. The release follows a recent 3.8.26 beta patch that fixed numerous desktop and gaming mode bugs. This update brings meaningful component upgrades to Steam Deck and SteamOS users, particularly benefiting Intel Arc B390 iGPU performance and introducing USB4 device-to-device file sharing capabilities. It signals Valve's continued investment in refining the SteamOS desktop experience for both handheld and living-room use cases. The KDE 6.7.3 upgrade brings improved KRunner search functionality, clipboard pinning, and better drawing tablet support. Linux Kernel 7.2 reportedly adds a new Intel USB4Stream driver for low-latency device-to-device file sharing over USB4 and delivers notable Intel Arc B390 iGPU performance gains, while Valve has also made configuration changes to improve everyday usability.

rss · TechPowerUp News · Aug 30, 05:14

**Background**: SteamOS is a Linux-based operating system developed by Valve, designed to combine the stability of Linux with a gaming experience optimized for the big screen and handheld devices like the Steam Deck. KDE Plasma is a feature-rich desktop environment built around widgets that allows extensive customization of the user interface. KRunner is a built-in launcher tool in KDE Plasma (accessible via Alt+Space) that enables quick application launching, searching, and command execution, with extensible functionality through plugins called 'runners'.

<details><summary>References</summary>
<ul>
<li><a href="https://itsfoss.com/steamos/">What is SteamOS ? Everything You Need to Know</a></li>
<li><a href="https://kde.org/plasma-desktop/">Plasma is KDE 's desktop environment . Simple by default, powerful...</a></li>

</ul>
</details>

**Tags**: `#SteamOS`, `#Linux`, `#KDE`, `#Valve`, `#Gaming`

---

<a id="item-13"></a>
## [Intel Officially Confirms LGA1954 Socket for Nova Lake-S Processors](https://www.techpowerup.com/352121/intel-confirms-lga1954-as-the-socket-for-nova-lake-s-processors-through-internal-tools) ⭐️ 5.5/10

Intel has officially confirmed the LGA1954 socket for its upcoming Nova Lake-S Core Ultra 400 series desktop processors by publishing an internal validation test tool on its website that links LGA1954 to Nova Lake-S. This marks the first time Intel itself has officially associated the Nova Lake-S name with the new socket, replacing the current LGA1851. This confirmation gives PC builders and hardware enthusiasts certainty that Nova Lake-S will require new Intel 900-series motherboards, meaning current LGA1851 motherboards will not be compatible with the next-generation platform. It also signals another socket transition, which impacts upgrade costs and cooler compatibility planning. The LGA1954 socket will feature a 2L-ILM (two-lever independent loading mechanism) design that uses levers on each side of the CPU to ensure better contact flatness and reduce CPU bending. According to leaks, Nova Lake-S flagship SKUs could include up to 52 cores with bLLC cache up to 288 MB, and the platform is expected to use DMI Gen 5 x4 with the Z990 chipset.

rss · TechPowerUp News · Aug 29, 20:46

**Background**: Intel desktop CPUs use LGA (Land Grid Array) sockets, where the pins are located on the motherboard rather than the CPU itself. Each new generation of Intel desktop processors typically requires a new socket, which in turn requires a new motherboard. LGA1851 was introduced with the Arrow Lake / Core Ultra 200S series, and Nova Lake-S represents the next major architectural leap, expected to launch in Q1 2027. The 2L-ILM socket design is a response to past issues with CPU bending and uneven contact pressure seen on LGA1700 platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/roundup/intel-nova-lake-s/">Intel Nova Lake: Full Specs , Release Date & Lineup (Up to 52 Cores...)</a></li>
<li><a href="https://www.hwcooling.net/en/nova-lake-to-feature-new-2l-ilm-socket-to-prevent-cpu-bending/">Nova Lake to feature new 2 L - ILM socket to prevent CPU bending</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#Nova Lake-S`, `#LGA1954`, `#CPU`, `#hardware`

---

<a id="item-14"></a>
## [Donkey Kong 64 finally gets a fully native PC port written in C — DK64 ReKONGpiled brings ultrawide support, uncapped framerates, and zero AI code](https://www.tomshardware.com/video-games/retro-gaming/donkey-kong-64-finally-gets-a-fully-native-pc-port-written-in-c-dk64-rekongpiled-brings-ultrawide-support-uncapped-framerates-and-zero-ai-code) ⭐️ 5.5/10

Veteran developers have created a native C-based PC port of Donkey Kong 64 with ultrawide support and uncapped framerates, notably without using generative AI.

rss · Tom's Hardware · Aug 30, 14:26

**Tags**: `#retro-gaming`, `#reverse-engineering`, `#pc-port`, `#donkey-kong-64`, `#cross-platform`

---

<a id="item-15"></a>
## [Modders Solder Cables Directly to RTX 5090 PCB to Bypass Melting Connector](https://www.tomshardware.com/pc-components/gpus/modders-solder-power-cables-directly-to-rtx-5090-pcb-to-eliminate-notorious-melting-16-pin-connector-bare-board-galax-hof-card-pulls-600w-under-chiller-cooling) ⭐️ 5.5/10

Brazilian YouTuber TecLab soldered power cables directly to an RTX 5090 PCB on a bare-board Galax HOF (Hall of Fame) card, bypassing the notorious 16-pin 12VHPWR connector entirely, with the card reportedly pulling 600W under chiller cooling. This extreme workaround underscores how severe and persistent NVIDIA's 16-pin connector melting issue remains two generations later, and highlights the community's frustration that the problem still has not been fully resolved even on the new RTX 5090 flagship. The mod creates what may be an even greater fire hazard than the melting connector itself, since hand-soldered wire connections on a high-current 600W load bypass all of the connector's safety and contact-design features. Galax HOF cards are specifically designed for overclocking enthusiasts and record-breaking challenges.

rss · Tom's Hardware · Aug 30, 10:30

**Background**: The 16-pin 12VHPWR connector was introduced with the RTX 4090 to deliver higher power to GPUs through a single cable, but it quickly became infamous for melting incidents often linked to improper insertion or contact issues. RTX 5090 cards continue to use this connector standard, and reports of melting have persisted into the new generation. Galax's Hall of Fame (HOF) line is a premium series built for extreme overclocking, which is why TecLab paired the soldering mod with a chiller cooling setup to sustain the card's 600W power draw.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/news/rtx-4090-16-pin-connector-melted-after-one-year-of-usage">RTX 4090's 16 - Pin Connector Melted After One... | Tom's Hardware</a></li>
<li><a href="https://galax.com/en/category/graphics-cards/hall-of-fame-series/">Hall of Fame ( HOF ) - GALAX</a></li>
<li><a href="https://ww-article-cache-1.s3.amazonaws.com/en/16-pin_12VHPWR_connector">ww-article-cache-1.s3.amazonaws.com/en/ 16 - pin _ 12 VHPWR ...</a></li>

</ul>
</details>

**Tags**: `#RTX 5090`, `#GPU modding`, `#hardware issues`, `#16-pin connector`, `#PC hardware`

---

<a id="item-16"></a>
## [US military uses high-energy lasers to shoot down three Mexican cartel drones over the southern border — narcos suspected of using UAVs for surveillance and reconnaissance to support illegal activities](https://www.tomshardware.com/tech-industry/drones/us-military-uses-high-energy-lasers-to-shoot-down-three-mexican-cartel-drones-over-the-southern-border-narcos-suspected-of-using-uavs-for-surveillance-and-reconnaissance-to-support-illegal-activities) ⭐️ 5.5/10

The US military used high-energy laser systems to shoot down three Mexican cartel drones conducting surveillance over the southern border.

rss · Tom's Hardware · Aug 30, 10:00

**Tags**: `#directed-energy-weapons`, `#counter-UAS`, `#defense-technology`, `#drones`, `#military`

---