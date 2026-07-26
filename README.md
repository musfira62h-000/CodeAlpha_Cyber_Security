# CodeAlpha_Cyber_Security

Cyber Security internship tasks for **CodeAlpha**.

## Intern

- **Name:** Musfira Hassan  
- **ID:** CA/DF1/201508  
- **Domain:** Cyber Security  
- **Organization:** CodeAlpha  

---

## Task 1 â€” Basic Network Sniffer

Build a Python program to capture and analyze network traffic packets using **Scapy**, displaying source/destination IPs, protocols, and payloads.

### Deliverables

- `task1_network_sniffer.py` / Task 1 report (local) â€” Task 1 report with setup, screenshots, and analysis  
- [`task1_network_sniffer.py`](./task1_network_sniffer.py) â€” Scapy network sniffer script  

### Lab roles

| Role | Machine | Details |
|------|---------|---------|
| Traffic host | Windows (`hp`) | IP `192.168.1.12` |
| Sniffer | Ubuntu (`musfira00@musfira00-virtual-machine`) | Runs Scapy sniffer |

### How to run

```bash
sudo pip install scapy
sudo python3 task1_network_sniffer.py
```

On Windows, generate traffic (e.g. `ping 8.8.8.8`) while the sniffer is running.

---

## Task 2 â€” Phishing Awareness Training

Create a presentation / awareness module on phishing attacks: recognizing phishing emails and fake websites, social engineering tactics, best practices, real-world examples, and interactive knowledge checks.

### Deliverable

- [`CodeAlpha_Task2_Phishing_Awareness_Training.pptx`](./CodeAlpha_Task2_Phishing_Awareness_Training.pptx) â€” phishing awareness training presentation (20 slides)

---

## Task 4 â€” Network Intrusion Detection System (NIDS)

Set up and configure a network-based Intrusion Detection System using **Snort**, with custom rules and alerts for suspicious/malicious activity (ICMP, TCP, HTTP/HTTPS, UDP), traffic monitoring, and evidence of detection.

### Deliverable

- Task 4 report (see local docs) â€” full Task 4 report with setup, rules, attacks, and screenshots

### Lab roles (from report)

| Role | Machine | IP |
|------|---------|-----|
| Attacker | Kali / Parrot Linux | `192.168.19.134` |
| Target | Windows | `192.168.134.173` |
| IDS / System | Ubuntu (Snort) | `192.168.19.136` |

---

Internship reference: [codealpha.tech](https://www.codealpha.tech)

