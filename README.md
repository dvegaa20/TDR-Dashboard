# **TDR-Dashboard**

TDR-Dashboard is a powerful tool for visualizing metrics related to TDR operations. It combines **Dash** for interactive graphs and **React** for an intuitive and responsive layout, making it easy to navigate across different pages.

---

## **Technologies Used**
- **Dash**: For creating interactive and customizable data visualizations.
- **React**: For building the user interface and managing the layout.

---

## **How It Works**

The TDR-Dashboard leverages the strengths of both Dash and React to deliver a seamless experience:

1. **Dash** is used to create dynamic, interactive graphs for displaying metrics and insights.
2. These graphs are embedded within **React** components using `<iframe>` elements, enabling integration between the Dash frontend and the React-based layout.
3. The React interface organizes and displays these graphs in a user-friendly way, providing smooth navigation between pages.

---

## **How to Run It**

### **Requirements**
- **Python** (for Dash server)
- **Node.js** (for React frontend)

### **Steps to Run**

#### **Dash Server**
1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment
- Windows:
```
venv\Scripts\activate
```
- Mac:
```
source venv/bin/activate
```
3. Install requirements
```
pip install -r requirements.txt
```
4. Run the Dash app:
```
python app.py
```

### React frontend
1. Install dependencies:
```
npm install
```
2. Start server
```
npm run start
```
