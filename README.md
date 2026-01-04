# 📡 WiFi-Based Human Activity Detection with Visual Overlay

<p align="center">
  <img src="assets/banner.gif" width="85%" />
</p>

<p align="center">
  <b>A phone/laptop-based demo that detects human-associated activity using Wi-Fi signal disturbance and visualizes it in real time.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Phone%20%7C%20Laptop-blue" />
  <img src="https://img.shields.io/badge/WiFi-Required-green" />
  <img src="https://img.shields.io/badge/OpenCV-Laptop%20Version-orange" />
  <img src="https://img.shields.io/badge/Status-Working%20Demo-success" />
</p>

---

## 🚀 Overview

This project demonstrates how **Wi-Fi signal disturbances** caused by a human carrying a device can be **detected in real time** and **symbolically visualized** using a live camera feed.

Unlike viral “see-through-walls” videos, this project is:
- ✔ Technically honest  
- ✔ Reproducible  
- ✔ Built step-by-step from real signals  

The visualization is **symbolic**, while the **detection is real**.

---

## 🎥 Demo Preview

<p align="center">
  <img src="assets/demo.gif" width="75%" />
</p>

> Green scan overlays and a human-like structure appear when Wi-Fi signal variance crosses a threshold.

---

## 🧠 How It Works

<p align="center">
  <img src="assets/workflow.gif" width="80%" />
</p>

### Step-by-step logic:
1. Two devices connect to the same Wi-Fi network
2. One device moves with a human (behind a wall or obstacle)
3. Wi-Fi signal timing and variance change
4. The system detects activity from signal disturbance
5. A **relative distance range** is estimated
6. A **visual overlay** represents detection events

---

## 📐 What This Project Does (and Does NOT)

### ✅ What it does
- Detects **human-associated movement**
- Estimates **relative distance ranges**
- Works on **phones and laptops**
- Visualizes detection on live camera feed
- Uses **real Wi-Fi behavior**

### ❌ What it does NOT claim
- No wall penetration
- No imaging through walls
- No exact distance measurement
- No human reconstruction

---

## 📱 Phone Version (No Laptop)

<p align="center">
  <img src="assets/phone_demo.gif" width="70%" />
</p>

- Detection runs in **Termux**
- Visualization runs in **browser (JavaScript + Canvas)**
- Events are **visually synchronized**
- Fully phone-only, no IDE required

---

## 💻 Laptop Version (OpenCV)

<p align="center">
  <img src="assets/opencv_demo.gif" width="70%" />
</p>

- Python + OpenCV
- Live camera feed
- Animated scan + human-like overlay
- Automatic detection → visualization pipeline

---

## 📂 Repository Structure

```text
wifi-human-detection-demo/
│
├── motion_detect.py        # Wi-Fi activity & distance estimation
├── wifi_vision.html       # Browser-based camera visualization
├── camera_overlay.py      # OpenCV live overlay (laptop)
├── requirements.txt
├── assets/
│   ├── banner.gif
│   ├── demo.gif
│   ├── workflow.gif
│   ├── phone_demo.gif
│   └── opencv_demo.gif
└── README.md
