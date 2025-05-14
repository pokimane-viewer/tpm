Below is a **research-backed briefing plus a starter civil complaint** you can adapt with counsel.  It’s organized so you can lift whole sections or mix-and-match language as needed.  (I’m **not** your lawyer; for legal strategy you’ll need licensed counsel.)

---

## 1  How TPM vendors land U.S. government business

| Stage                            | What happens                                                                                                                                                                                                                                                                                            | Key authority / practice                                                                                                                                                                               | Notes                                                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **Specification & lobbying**     | Chipmakers (Infineon, Nuvoton, ST, etc.) help write the *Trusted Platform Module* (TPM) specs inside the industry consortium **Trusted Computing Group (TCG)**.  Only “Promoter” and “Contributor” members vote on spec changes; *Industry Liaison* members are non-voting, and the public has no vote. | Snippet from TCG web copy (“full non-voting membership in Work Groups”) ([Trusted Computing Group][1])                                                                                                 | Vendors therefore shape the technical “rules of the game.”                                                           |
| **Federal requirements created** | DoD Instruction 8500.01 and DISA STIGs require TPMs on many devices.  NSA’s 2024 Cybersecurity Information Sheet recommends TPM 2.0 *across* DoD fleets.                                                                                                                                                | NSA CSI “Trusted Platform Module (TPM) Use Cases,” Nov 2024                                                                                                                                            | Once DoD mandates something, other civilian agencies often follow (via FIPS-140 cross-references and GSA schedules). |
| **Procurement channel**          | Vendors get **GSA Multiple Award Schedule** numbers or go direct through prime contractors; agencies then order laptops/servers that *already* embed the chips.                                                                                                                                         | GSA MAS overview page ([U.S. General Services Administration][2])                                                                                                                                      |                                                                                                                      |
| **Public-facing marketing**      | To secure civilian acceptance, vendors and platform owners (e.g., Microsoft) push messages like “TPM protects your identity” and is *non-negotiable* for Windows 11.                                                                                                                                    | Microsoft support article (“TPM 2.0 is required … for identity protection”) ([Microsoft Support][3]); Infineon OPTIGA marketing note (“highly secured, hardware-based ‘trust anchor’”) ([Infineon][4]) |                                                                                                                      |
| **Result**                       | Citizens and enterprises are effectively coerced: modern PCs won’t get OS updates—or meet agency security baselines—without a TPM.  The public never votes on, and can’t amend, the spec that drives this mandate.                                                                                      |                                                                                                                                                                                                        |                                                                                                                      |

---

## 2  Who “agrees” to the TPM protocol & can they vote?

| Actor                                             | Do they “agree”?                                                                                                                       | Voting / change rights                                                     |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Device buyers (citizens, agencies, companies)** | *Implicitly*.  Buying any modern PC means accepting TPM 2.0 + firmware you can’t inspect.                                              | **No** direct vote.  Only recourse is antitrust / consumer-protection law. |
| **OS vendors (Microsoft, Red Hat, Google)**       | Yes.  They choose to *require* a TPM for certain security features.                                                                    | They can lobby TCG and submit spec change proposals as members.            |
| **Hardware OEMs (Dell, Lenovo, HP)**              | Yes.  They integrate whichever TPM chip passes their cost/performance tests.                                                           | Most are Contributor-level TCG members → **yes** vote on spec revisions.   |
| **TPM chipmakers**                                | Absolutely—often Promoter members → super-majority voting power.                                                                       |                                                                            |
| **General public**                                | No vote, no formal comment period (except via occasional NIST drafts such as SP 800-164) ([NIST Computer Security Resource Center][5]) |                                                                            |

Bottom line: *governance is closed and vendor-centric*, yet the economic burden lands on the public.

---

## 3  Draft civil complaint (skeleton)

> **UNITED STATES DISTRICT COURT
> FOR THE \_\_\_\_\_\_\_ DISTRICT OF \_\_\_\_\_\_\_**

### 1. Parties

1. **Plaintiffs.**  U.S. residents who purchased computing devices incorporating a Trusted Platform Module (“TPM”) after January 1 2019.
2. **Defendants.**

   * Infineon Technologies AG, Nuvoton Technology Corp., and other TPM manufacturers (“Chipmaker Defendants”);
   * Microsoft Corp. and other platform vendors that market TPM-based features (“Platform Defendants”).

### 2. Jurisdiction & venue

…  (standard diversity / federal-question language—Lanham Act, FTC Act, Magnuson-Moss, etc.)

### 3. Factual allegations

1. *Vendor-controlled standard.*  The TPM specification is written by TCG, where Defendants hold the only voting seats. ([Trusted Computing Group][1])
2. *Government mandate without public vote.*  DoD and civilian agencies require TPMs under DoDI 8500.01 and related STIGs, effectively forcing adoption nationwide.&#x20;
3. *Marketing to consumers.*  Defendants advertise that “TPM 2.0 protects your identity” and is “non-negotiable” for Windows 11 upgrades, implying superior security and privacy benefits. ([Microsoft Support][3], [Infineon][4])
4. *Omitted & misleading facts.*

   * No disclosure that consumers cannot audit TPM firmware or replace it.
   * No disclosure that TPM private keys may be escrowed under manufacturer root certificates, enabling third-party access.
   * No disclosure that the public has no representation in spec development.
5. *Economic harm.*  Consumers paid a price premium (hardware and forced upgrades) and lost the use of otherwise functional devices.

### 4. Causes of action

**Count I – False Advertising (15 U.S.C. § 1125(a))**
Defendants’ security claims are unsubstantiated and materially deceive purchasers.

**Count II – Unfair & Deceptive Acts (FTC Act § 5; state UDAP statutes)**
Omission of governance facts and lock-in effects is deceptive.

**Count III – Conspiracy in restraint of trade (Sherman Act § 1)**
Voting control inside TCG combined with OS-level mandates forecloses competing security architectures.

**Count IV – Violation of Administrative Procedure Act (5 U.S.C. §706)**
Agency adoption of TPM requirements without notice-and-comment exceeds statutory authority.

*(Add constitutional/due-process counts if desired.)*

### 5. Prayer for relief

1. Declaratory judgment that Defendants’ TPM marketing is false and misleading;
2. Injunctive relief prohibiting further deceptive claims and requiring disclosure of TPM source code for independent audit;
3. Restitution / damages for class members;
4. Treble damages under Clayton Act;
5. Attorneys’ fees and costs;
6. Any other relief the Court deems just.

*Respectfully submitted,*

---

Counsel for Plaintiffs

---

## 4  Practical next steps

1. **Evidence file:**  Capture PDFs of vendor whitepapers and Microsoft upgrade pop-ups (especially language like “non-negotiable” and “protects your identity”).
2. **Economic expert:**  Quantify the hardware-price delta & forced-upgrade cost.
3. **Security expert:**  Draft declaration comparing TPM claims to documented vulnerabilities (e.g., Nuvoton SA-001 firmware attack) ([Nuvoton][6]).
4. **FOIA requests:**  Seek DoD, GSA, and OMB e-mail chains showing vendor lobbying.
5. **Consider rule-making petition:**  Even if litigation stalls, a well-supported petition to FTC/NIST may pressure clearer disclosures.

---

### Quick FAQ recap

| Question                      | Short answer                                                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Who agreed to TPM?*          | Primarily vendors inside TCG; consumers did not.                                                                                                  |
| *Does the public get a vote?* | No.  Only certain membership tiers vote; gov’t adoption occurs via agency directives, not referendum.                                             |
| *Can the public amend TPM?*   | Only indirectly—through lobbying TCG or legislative/agency action. Lawsuits like the above aim to force transparency or curb deceptive marketing. |

---

**Good luck, Bo—let me know if you need deeper dives on specific counts, economic modeling, or FOIA templates.**

[1]: https://trustedcomputinggroup.org/industry-participation/?utm_source=chatgpt.com "Industry Participation | Trusted Computing Group"
[2]: https://www.gsa.gov/buy-through-us/purchasing-programs/multiple-award-schedule?utm_source=chatgpt.com "Multiple Award Schedule - GSA"
[3]: https://support.microsoft.com/en-us/windows/enable-tpm-2-0-on-your-pc-1fd5a332-360d-4f46-a1e7-ae6b0c90645c?utm_source=chatgpt.com "Enable TPM 2.0 on your PC - Microsoft Support"
[4]: https://www.infineon.com/dgdl/Infineon-ISPN-Use-Case-Easy_Incorporation_of_OPTIGA_TPMs-ABR-v09_16-EN.pdf?fileId=5546d46256fb43b3015751329f9f5e2f&utm_source=chatgpt.com "[PDF] Easy Incorporation of OPTIGA™ TPMs to Support Mission-Critical ..."
[5]: https://csrc.nist.gov/pubs/sp/800/164/ipd?utm_source=chatgpt.com "Guidelines on Hardware-Rooted Security in Mobile Devices"
[6]: https://www.nuvoton.com/support/security/security-advisories/sa-001/?utm_source=chatgpt.com "SA-001: Unauthorized Access to Non-Volatile Memory - Nuvoton"
