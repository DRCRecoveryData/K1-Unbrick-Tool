<img width="502" height="551" alt="{1B152BA2-6EE2-4471-8C4E-111763ADA025}" src="https://github.com/user-attachments/assets/7fad5b82-c5cf-4786-89c2-e1951bd4a7ef" />

# Creality K1 Series Partition Tool

A based utility for Creality K1, K1C, and K1 Max users to generate critical system images (`ota.img` and `sn_mac.img`) required for unbricking or partition recovery.

## 📌 Overview
When repairing the flash memory of a Creality K1 series printer, specific small partitions hold the printer's identity and boot instructions. This tool automates the creation of these files using the exact hex-offset requirements and string formats required by the bootloader.

## 🛠 Partition Layout Reference
The tool is designed based on the following partition structure:

| Hex Offset | Size | Partition Name | File/Content Description |
| :--- | :--- | :--- | :--- |
| `0x0` | 1.0 MB | uboot | u-boot-with-spl-mbr-gpt (bootloader, partitiontable) |
| `0x100000` | 1.0 MB | **ota** | `ota.img` (Boot loader instructions) |
| `0x200000` | 1.0 MB | **sn_mac** | `sn_mac.img` (Serial and MAC data) |
| `0x300000` | 4.0 MB | rtos | `zero.bin` |
| `0x700000` | 4.0 MB | rtos2 | `zero.bin` |
| `0xb00000` | 8.0 MB | kernel | `xImage` |
| `0x1300000` | 8.0 MB | kernel2 | `xImage` |
| `0x1b00000` | 300.0 MB | rootfs | `rootfs.squashfs` |
| `0x14700000`| 300.0 MB | rootfs2 | `rootfs.squashfs` |
| `0x27300000`| 100.0 MB | rootfs_data | System data storage |
| `0x2d700000`| 6.6 GB | userdata | User data storage |



## ⚙️ File Formats
### 1. ota.img
This file tells the boot loader which set of partitions to boot off of.
* **Format**: `ota:kernel` followed by two line feed characters (`0x0a 0x0a`).

### 2. sn_mac.img
Stores the unique identity of the machine.
* **Format**: `serial number [14 hex digits];mac address [12 hex digits];model code;board code;;;;;`.
* **Example**: `CB153CBA4BC8A6;EB850E76F140;K1C;CR4CU220812S12;;;;;`.

## 🚀 How to Use
1. **Clone the Repo**:
```bash

git clone https://github.com/DRCRecoveryData/K1-Unbrick-Tool.git

```

2. **Install Dependencies**:
```bash
pip install 

```

3. **Run the Tool**:
```bash
python K1-Unbrick-Tool.py

```

4. **Input Data**:
* Enter your **14-hex digit** Serial Number.
* Enter your **12-hex digit** MAC Address.
* Select your Model (K1, K1C, or K1 Max).

5. **Generate**: Click the button to save `ota.img` and `sn_mac.img` to your local folder.

## ⚖️ License

This project is provided for educational and repair purposes. Use at your own risk when flashing hardware partitions.
