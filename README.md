<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FrancescoMarchiori/Ethical-Hacking">
    <img src="/imgs/cybersec_logo.png" alt="Logo" width="150" height="150">
  </a>

  <h1 align="center">Ethical Hacking</h1>

  <p align="center">
    Repository for the challenges code of the M. Sc. course in Ethical Hacking
    <br />
    <a href="https://www.unipd.it/en/educational-offer/second-cycle-degree/science?tipo=LM&scuola=SC&ordinamento=2020&key=SC2542&cg=engineering"><strong>M. Sc. Cybersecurity »</strong></a>
    <br />
    <br />
    <a>Network Security</a>
    ·
    <a>Hardware Security</a>
    ·
    <a>Reverse Engineering</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#network">Network Security</a>
      <ul>
        <li><a href="#sniffing">Sniffing and Spoofing</a></li>
      </ul>
      <ul>
        <li><a href="#tcp">TCP Spoofing</a></li>
      </ul>
      <ul>
        <li><a href="#firewall">Firewalls</a></li>
      </ul>
    </li>
    <li>
      <a href="#hardware">Hardware Security</a>
      <ul>
        <li><a href="#spectre">Spectre Attack</a></li>
      </ul>
    </li>
    <li>
      <a href="#web">Web Security</a>
    </li>
    <li>
      <a href="#reverse">Reverse Engineering</a>
    </li>
    <li>
      <a href="#pwning">Pwning</a>
    </li>
  </ol>
</details>

<div id="introduction"></div>

## 🧩 Introduction

This repository is used to organize and archive the code for the challenges of the course in Ethical Hacking. The main topics are Network Security (sniffing and spoofing, traffic analysis, attacks to transport layer protocols, firewall), Hardware Security (register execution, side channel analysis, meltdown attack, spectre attack), Web Security (cross-site scripting, cross-site request forgery, HTTP request smuggling), Reverse Engineering (static analysis, reversing in x86, reversing, patching, gdb, calling conventions, debuggers, symbolic execution, angr) and Pwning (shellcode attack, buffer overflow attack, return-to-libc attack, format string attack, Race Condition Vulnerability).

<p align="right"><a href="#top">(back to top)</a></p>
<div id="network"></div>

## 🌐 Network Security
Network security is the protection of the underlying networking infrastructure from unauthorized access, misuse, or theft. It involves creating a secure infrastructure for devices, applications, users, and applications to work in a secure manner. It can also be defined as a category of practices and technologies that keep internal networks protected from attacks and data breaches. It encompasses access control, cyber attack prevention, malware detection, and other security measures.

<p align="right"><a href="#top">(back to top)</a></p>
<div id="sniffing"></div>

### 👃🏽 Sniffing and Spoofing
Packet sniffing and spoofing are two important concepts in network security; they are two major threats in network communication. Being able to understand these two threats is essential for understanding security measures in networking. There are many packet sniffing and spoofing tools, such as Wireshark, Tcpdump, Netwox, Scapy, etc. Some of these tools are widely used by security experts, as well as by attackers. Being able to use these tools is important for students, but what is more important for students in a network security course is to understand how these tools work, i.e., how packet sniffing and spoofing are implemented in software.

For this challenge we used C and Python with Scapy, which can be installed with the following command:
```
pip install scapy
```

<p align="right"><a href="#top">(back to top)</a></p>
<div id="tcp"></div>

### 👃🏽 TCP Spoofing
The vulnerabilities in the TCP/IP protocols represent a special genre of vulnerabilities in protocol designs and implementations; they provide an invaluable lesson as to why security should be designed in from the beginning, rather than being added as an afterthought. Moreover, studying these vulnerabilities might help us understand the challenges of network security and why many network security measures are needed.

<p align="right"><a href="#top">(back to top)</a></p>
<div id="firewall"></div>

### 🧱 Firewalls
A firewall inspects each incoming and outgoing packets and enforces the firewall policies set by the administrator. Since the packet processing is done within the kernel, the filtering must also be done within the kernel. Therefore, it seems that implementing such a firewall requires us to modify the Linux kernel. In the past, this had to be done by modifying and rebuilding the kernel. The modern Linux operating systems provide several new mechanisms to facilitate the manipulation of packets without rebuilding the kernel image. These two mechanisms are Loadable Kernel Module (LKM) and netfilter.

<p align="right"><a href="#top">(back to top)</a></p>
<div id="hardware"></div>

## 🖥️ Hardware Security
Hardware security is vulnerability protection that comes in the form of a physical device rather than software that is installed on the hardware of a computer system. The term "hardware security" also refers to the protection of physical systems from harm. equipment destruction attacks, for example, focus on computing devices and networked non-computing devices such as the ever-increasing number of connected devices in M2M or IoT (Internet of Things) environments.

<p align="right"><a href="#top">(back to top)</a></p>
<div id="spectre"></div>

### 👻 Spectre Attack

Discovered in 2017 and publicly disclosed in January 2018, the Spectre attack exploits critical vulnerabilities existing in many modern processors, including those from Intel, AMD, and ARM. The vulnerabilities allow a program to break inter-process and intra-process isolation, so a malicious program can read the data from the area that is not accessible to it. However, I don't own any device that comes with a CPU older than 2018, and therefore I couldn't be able to perform this attack on my own machines.

![MEME](/images/ive_won_meme.png?raw=true "MEME")

<p align="right"><a href="#top">(back to top)</a></p>
<div id="web"></div>

## 🧭 Web Security

<p align="right"><a href="#top">(back to top)</a></p>
<div id="reverse"></div>

## 🔎 Reverse Engineering

<p align="right"><a href="#top">(back to top)</a></p>
<div id="pwning"></div>

## ⚔️ Pwning

<p align="right"><a href="#top">(back to top)</a></p>