# HACKUPC26 - AntiPollen: The Barcelona Shield

> **Real-time, hyper-local pollen detection for a sneeze-free Sant Jordi.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hardware: Arduino](https://img.shields.io/badge/Hardware-Arduino-00979D.svg)](https://www.arduino.cc/)
[![AI: Edge Computing](https://img.shields.io/badge/AI-Edge%20Computing-orange.svg)]()

## 🌸 Inspiration
This year’s Sant Jordi was supposed to be about books and roses, but for many of us, it was a near-death experience. Pollen was the absolute protagonist, turning a beautiful tradition into a blurred haze of itchy eyes and antihistamines. 

We decided the citizens of Barcelona deserved a shield. We built **AntiPollen** to protect our respiratory systems (and our sanity) by making the invisible threat visible.

## 🛰️ What it Does
AntiPollen is a distributed mesh network of sensors that maps pollen concentrations street by street.
* **Real-Time Heatmaps:** An intuitive dashboard showing current pollen "hot zones" across Barcelona.
* **Edge AI Detection:** Unlike standard air quality monitors, our nodes distinguish between common dust and specific allergenic pollen.
* **Navigation Integration:** Provides the data necessary for allergy-friendly routing to help users avoid high-pollen corridors.

---

## 🛠️ Technical Architecture

### Hardware Stack
* **Microcontrollers:** Arduino-based mesh nodes.
* **Sensors:** Particulate Matter (PM) sensors calibrated for organic particulates.
* **Network:** Low-power mesh communication between nodes for urban deployment.

### Software & AI
* **The Brain:** A custom **Edge AI model** trained to analyze particulate signatures. By processing data on the device (Edge Computing), we reduce latency and bandwidth usage.
* **Data Fusion:** Integrates public Meteorological APIs to factor in wind speed and direction (compensating for hardware limitations).
* **Frontend:** A real-time intelligent dashboard aggregating distributed data into a visual heatmap.

---

## 🚧 Challenges & Solutions
**The Wind Sensor Pivot:** We originally attempted to use vibro-sensors to measure local wind speed. However, the sensitivity wasn't sufficient for subtle urban breezes. 
* **Solution:** We pivoted to a hybrid data model, pulling real-time wind vectors from public APIs to calculate pollen drift accurately.

## 🏆 Accomplishments
* **Bespoke ML Model:** Successfully trained a model capable of running on low-power Arduino hardware to differentiate particulate types.
* **Mesh Stability:** Achieved a reliable communication sync between multiple distributed nodes in a noisy urban environment.

## 🧠 Lessons Learned
* **Arduino Power:** We discovered that the Arduino ecosystem is significantly more capable of handling AI workloads than we initially anticipated.
* **Sensor Calibration:** We learned the intricacies of environmental noise and how to filter out non-organic particulates from our dataset.

---

## 🚀 Roadmap
- [ ] **Scale the Mesh:** Expand node deployment to high-density areas like Gràcia and Eixample.
- [ ] **Mobile App:** Develop a cross-platform app for push notifications when entering high-pollen zones.
- [ ] **API for Maps:** Integrate with Google Maps/Apple Maps to offer "Least-Pollen" walking routes.

## 👥 Contributors
* **Your Name/Team Name** - *Initial Work & ML Development*

---
*Built with ❤️ (and a lot of tissues) in Barcelona.*
