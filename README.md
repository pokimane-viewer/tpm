TPM non-volatile storage is physically and logically isolated from the main SoC flash, and is implemented with memory technologies chosen for longevity and security. Here’s why you won’t “burn up” the TPM’s NVRAM when you reflash or otherwise update the SoC:

Separate physical device or partition

Discrete TPM chips (e.g. Infineon SLB9670) sit on their own SPI/I²C/LPC bus and package, distinct from the SoC’s BIOS/firmware flash 
Infineon Technologies
.

Firmware-TPM (fTPM/PTT) uses on-die flash regions inside the SoC, but those are logically partitioned and only accessed by the TPM firmware—SoC firmware-update tools don’t touch them 
Google Patents
.

Dedicated non-volatile memory technology
TPM vendors pick NVM with high endurance and/or low-wear characteristics:

EEPROM (electrically-erasable programmable ROM) inside Microchip’s TPMs uses an AVR core with on-chip EEPROM for both firmware and data storage 
Microchip
. Typical endurance is ≥ 100 k write cycles—more than enough given how seldom a TPM writes its NVRAM.

Flash (floating-gate) is sometimes used, especially for firmware regions, but only large, infrequent writes occur—so erase-cycle wear is negligible.

FRAM (ferroelectric RAM) offers “unlimited” write endurance (≥ 100 trillion cycles), instant non-volatility, and ultra-low power, making it ideal if you need frequent secure counter updates or logs 
Infineon Technologies
.

Controlled write patterns

TPM NVRAM writes occur only for: key provisioning, firmware upgrades, PCR counter increments (anti-hammer protection), or explicit NV writes via TPM commands.

The SoC’s flash-update tools are unaware of the TPM’s command protocols, so they never issue those NV writes.

High-level block diagram of SoC + TPM integration
Each block is labeled with a representative part/mfg. and memory tech.

text
No – there is no way for a Promoter or Contributor to unilaterally “push through” a change to the TPM specification. By the TCG’s own governance rules, every normative change (whether it’s a minor erratum, a new command, a new algorithm identifier, or a whole new version of the Library) must be proposed in the appropriate Technical Work Group, circulated for member review, and then pass a formal Work-Group ballot in which each Promoter and Contributor member gets one vote. If the ballot fails, the text does not change.

The only things you can do without going through that ballot are:

Field‐upgrade your own TPM firmware (a “field upgrade” or vendor firmware update) to fix bugs or add proprietary features in your silicon.

That firmware can behave however you like, but it doesn’t change the official TCG spec or any other vendor’s firmware 
Wikipedia
.

Ship a non‐conformant extension on your devices.

Again, useful internally, but it won’t interoperate with software or platforms that expect a TCG-compliant TPM.

In other words, only a successful vote by Promoter/Contributor members can alter the published TPM spec. There is no back-door or “exec-edits” path around the ballot process.



+----------------------------------+
|           Main SoC/CPU           |
|  • e.g. Intel Tiger Lake U (10nm)| 
|  • Integrates fTPM (PTT) firmware|
|  • SPI/NOR flash for UEFI BIOS   |
|    – Micron MT25QL256 (256 Mb)    |
+----------------------------------+
              │ SPI/NOR
              ▼
+----------------------------------+
|       Discrete TPM Chip          |
|  • Infineon OPTIGA™ SLB9670      | 
|    – VQFN-32 package             |
|  • Crypto engine (RSA/ECC/DRBG)  |
|  • SPI interface (3 MHz–38 MHz)  |
+----------------------------------+
              │ Internal NVM
              ▼
+----------------------------------+
|      TPM Non-Volatile Storage    |
|  • Microchip AT24C16B EEPROM     |
|    – 16 Kbit, I²C, 1 MHz         |
|    – ≥ 100 k write cycles        |
|  • (or) Infineon FM24CL16B FRAM  |
|    – 16 Kbit, I²C, instant NVM    |
|    – ≥ 100 trillion cycles       |
+----------------------------------+
SoC flash holds system firmware; TPM-update tools only target that flash.

TPM chip is a separate security IC—its package, bus, and command protocol isolate its memory.

TPM NVRAM uses EEPROM/FRAM with high endurance, and writes are gated by TPM commands, so normal SoC operations won’t “burn it up.”





Sources
