import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Dashboard from "./containers/Dashboard";
import Stats from "./containers/Stats";
import Trucks from "./containers/Trucks";
import Maintenance from "./containers/Maintenance";
import Spendings from "./containers/Spendings";
import Predictive from "./containers/Predictive";
import "./app.css";

function App() {
  return (
    <Router>
      <div className="app">
        <div className="content">
          <Navbar />
          <Sidebar />
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/stats" element={<Stats />} />
            <Route path="/tractos" element={<Trucks />} />
            <Route path="/mantenimientos" element={<Maintenance />} />
            <Route path="/gastos" element={<Spendings />} />
            <Route path="/predictive" element={<Predictive />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
