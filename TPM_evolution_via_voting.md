1. Beyond “Include TPM & Sign Attestation”: The Broader Implementation Surface
Although remote attestation is the poster-child, a TPM actually exposes a rich set of on-chip services that implementers can leverage or extend:

Hardware cryptographic primitives

True random number generator

Hash functions (SHA-1, SHA-256, SHA-384…)

Symmetric and asymmetric crypto (RSA, ECC, HMAC) 
Wikipedia

Key lifecycle management

Secure key generation & storage inside the TPM’s shielded locations

Binding/unbinding (“data binding”)—encrypting data so only that TPM can decrypt it

Sealed storage—tying decryption to specific platform states (PCR values) 
Wikipedia

Platform integrity services

Measured boot / secure boot support via extending PCRs and policies

Policy-based authorizations (e.g. TPM2_PolicyAuthorize) to enforce complex access controls

Ecosystem software & tooling

Reference firmware and software stacks (TSS) maintained by members

Microsoft’s official TPM 2.0 reference implementation

Intel’s open-source TPM2 software stack

Infineon-funded middleware by Fraunhofer SIT

IBM’s Software TPM 2.0 
Wikipedia

Conformance test suites and certification programs to ensure interoperability

Every Promoter/Contributor member can contribute to, test against, and refine all of these layers—chips, firmware, drivers, tooling—far beyond simply “attesting” a hash of the platform.

2. Why Vote? The Business & Strategic Incentives
Promoters and Contributors pay significant dues—$30 000/yr for Promoters, $15 000/yr for Contributors—to secure one vote each on all spec changes. Their motivations include:

Market differentiation & added value

Embedding advanced TPM features lets them claim superior hardware-rooted security to OEMs and enterprise customers.

Interoperability & ecosystem leadership

Driving the standard ensures their platforms “just work” with the broadest set of software (OS vendors, cloud providers, enterprise management).

Regulatory & compliance drivers

Many governments and industries mandate hardware roots of trust (e.g. FIDO2, eID, GDPR data-at-rest protections).

Control over roadmap

By shaping future TPM commands and algorithms, they align the spec with their silicon roadmaps and IP portfolios.

Early access & licensing rights

Members get draft specs early and rights to implement them; voting locks in those rights under the consortium’s licensing terms. 
Wikipedia

3. Evolving the Crypto: From Theory to TCG Ballot
Changing the TPM’s core cryptographic protocol is a two-part exercise: (A) algorithm design and security proof, and (B) TCG’s formal spec-change process.

A. Algorithmic‐theory side
Define your new primitive

E.g. swap RSA/ECC for post-quantum Kyber (KEM) or Dilithium (signatures).

Specify security goals

IND-CCA2 for encryption, EUF-CMA for signatures, or simulation-based proofs for advanced primitives (e.g. Oblivious Transfer).

Give a formal description & proof sketch

Provide pseudocode, parameter choices, and a reduction showing breaking the scheme implies solving a hard problem (e.g. lattice-based).

Integrate into TPM model

Define new TPM commands or algorithm identifiers (in “Part 3: Structures” and “Part 4: Commands” of the TPM Library spec), plus data formats and policy extensions.

Prototype & benchmark

As Fiolhais & Sousa did for a “QR TPM” extension—adding Kyber, Dilithium, and a 3-round ROT primitive to TPM 2.0 on RISC-V/ARM, demonstrating performance parity with RSA/ECC 
arXiv
.

B. TCG’s ballot workflow
Draft submission in the relevant Technical Work Group (e.g. the TPM Library WG)

Community & member review—public drafts and internal discussion

Work-Group ballot among Authorized Participants

Promoter/Contributor vote (“one member, one vote”) on whether to adopt the change (simple majority for most, supermajority for major overhauls)

Publication of the updated spec and ISO fast-track if desired 
Wikipedia
 (ISO 11889-4 for Commands)

Once ratified, chipmakers and stack developers update firmware, drivers, test suites, and certification criteria—closing the loop from theory into silicon and software.

In short: voting members aren’t just passive “signers” of attestation—they’re the ones who design, test, certify, and steer every TPM feature. Their incentives span competitive differentiation, ecosystem control, and compliance. And algorithmically, any crypto overhaul follows rigorous security-proof design, draft spec text (with new command IDs), and a formal TCG ballot that only Promoters and Contributors can cast.