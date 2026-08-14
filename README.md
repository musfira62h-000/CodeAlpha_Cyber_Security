# CodeAlpha_Cyber_Security

Cyber Security internship tasks for **CodeAlpha**.

## Intern

- **Name:** Musfira Hassan  
- **ID:** CA/DF1/201508  
- **Domain:** Cyber Security  
- **Organization:** CodeAlpha  

---

## Task 1 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Basic Network Sniffer

Build a Python program to capture and analyze network traffic packets using **Scapy**, displaying source/destination IPs, protocols, and payloads.

### Deliverables

- [`task1-network-sniffer/`](./task1-network-sniffer/) — Scapy sniffer + UPDATED report
- [`task1-network-sniffer/task1_network_sniffer.py`](./task1-network-sniffer/task1_network_sniffer.py) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Scapy network sniffer script  

### Lab roles

| Role | Machine | Details |
|------|---------|---------|
| Traffic host | Windows (`hp`) | IP `192.168.1.12` |
| Sniffer | Ubuntu (`musfira00@musfira00-virtual-machine`) | Runs Scapy sniffer |

### How to run

```bash
sudo pip install scapy
sudo python3 task1-network-sniffer/task1_network_sniffer.py
```

On Windows, generate traffic (e.g. `ping 8.8.8.8`) while the sniffer is running.

---

## Task 2 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Phishing Awareness Training

Create a presentation / awareness module on phishing attacks: recognizing phishing emails and fake websites, social engineering tactics, best practices, real-world examples, and interactive knowledge checks.

### Deliverable

- [`CodeAlpha_Task2_Phishing_Awareness_Training.pptx`](./CodeAlpha_Task2_Phishing_Awareness_Training.pptx) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â phishing awareness training presentation (20 slides)

---

## Task 4 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Network Intrusion Detection System (NIDS)

Set up and configure a network-based Intrusion Detection System using **Snort**, with custom rules and alerts for suspicious/malicious activity (ICMP, TCP, HTTP/HTTPS, UDP), traffic monitoring, and evidence of detection.

### Deliverable

- [`CodeAlpha_Task4_Network_IDS_.docx`](./CodeAlpha_Task4_Network_IDS_.docx) Ã¢â‚¬â€ full Task 4 Snort NIDS report with setup, rules, attacks, and screenshots

### Lab roles (from report)

| Role | Machine | IP |
|------|---------|-----|
| Attacker | Kali / Parrot Linux | `192.168.19.134` |
| Target | Windows | `192.168.134.173` |
| IDS / System | Ubuntu (Snort) | `192.168.19.136` |

---

Internship reference: [codealpha.tech](https://www.codealpha.tech)

