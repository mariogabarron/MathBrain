# MathBrain

**MathBrain** is a knowledge engineering tool designed for pure mathematics and computer science students. It leverages the **Gemini 1.5/3.0 API** to transform unstructured handwritten notes into an **Interactive Semantic Graph**.

Unlike conventional digital notebooks, MathBrain identifies logical dependencies between definitions, lemmas, and theorems, allowing users to visualize the hierarchical backbone of abstract algebra.

> [!NOTE]
> Visionary is a **personal project built for experimentation**, focusing on clean architecture and scalable mobile development practices.

---

## Key Features

* **Multimodal Math OCR:** High-precision transcription of complex handwritten algebraic notes into strict $\LaTeX$ using LLMs.
* **Logical Dependency Graph:** An interactive visualization where physical proximity represents thematic relationships (e.g., Group Theory, Rings, Fields).
* **Source-Grounding:** Each node acts as a "living" document containing the formal statement and the proof retrieved directly from your uploaded sources.
* **Modern UI/UX:** A clean, scientific dashboard built with Streamlit for seamless exploration.

---

## Tech Stack

* **AI/LLM:** Google Gemini API (1.5 Flash / 3.0 models).
* **Backend:** Python 3.10+
* **Mathematical Structures:** NetworkX (Graph Theory) & SymPy.
* **Visualization:** PyVis (Force-directed graph physics) & MathJax (LaTeX rendering).
* **Frontend:** Streamlit.

---

## How it Works (Under the Hood)

1.  **Ingestion:** User uploads images or PDFs of handwritten notes.
2.  **Semantic Extraction:** Gemini analyzes the input and returns a structured JSON schema including:
    * `ID` & `Label`: The name of the mathematical entity.
    * `Classification`: (Axiom, Theorem, Lemma, Corollary).
    * `Dependencies`: An array of prerequisites required to prove the entity.
3.  **Graph Construction:** `NetworkX` computes the topology, and `PyVis` generates the interactive HTML interface with color-coded thematic clusters.

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/MathBrain.git](https://github.com/your-username/MathBrain.git)
   cd MathBrain
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure API Key: Create a .env file in the root directory:**
   ```bash
   GEMINI_API_KEY=your_google_ai_studio_key
   ```
4. **Launch the App:**
   ```
   streamlit run src/main.py
   ```

## 🧪 Visual Example

Below is a conceptual representation of how **MathBrain** maps your notes. Clicking on a node instantly renders the underlying proof using MathJax.

> [!TIP]
> **Interactive Popups:** When you click on a node like the **"First Isomorphism Theorem"**, the system triggers a popup with the full proof rendered in real-time:
>
> $$\text{Let } f: G \to H \text{ be a group homomorphism. Then: } G/\ker(f) \cong \text{im}(f)$$

*Nodes are color-coded by algebraic structure: 🔵 Groups, 🟢 Rings, 🟠 Fields.*

---

## 👥 Authorship & Motivation

This project was developed as a personal challenge to bridge the gap between **Abstract Algebra** and **AI Engineering**. As a 3rd-year Mathematics and Computer Science student, my goal was to create a tool that respects the formal rigor of math while leveraging the flexibility of LLMs.

**Developed by:** Mario Gabarrón
* **Major:** Bachelor in Mathematics & Computer Science
* **Interests:** Algebraic Structures and AI.

---

## 📄 License

This project is licensed under the **MIT License**. This means you are free to use, modify, and distribute the code for both personal and commercial purposes, as long as the original copyright notice is included. 

---

### 🌟 Show your support

If you find this project interesting or useful for your studies, please give it a **Star** on GitHub!
