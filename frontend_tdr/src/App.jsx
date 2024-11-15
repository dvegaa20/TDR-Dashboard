// App.jsx
import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Dashboard from "./containers/Dashboard";
import Stats from "./containers/Stats";
import Trucks from "./containers/Trucks";
import Maintenance from "./containers/Maintenance";
import Spendings from "./containers/Spendings";

import "./app.css";

function App() {
  return (
    <Router>
      <div className="app">
        <div className="content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/stats" element={<Stats />} />
            <Route path="/tractos" element={<Trucks />} />
            <Route path="/mantenimientos" element={<Maintenance />} />
            <Route path="/gastos" element={<Spendings />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
