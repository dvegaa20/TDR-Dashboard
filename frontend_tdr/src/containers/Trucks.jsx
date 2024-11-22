import React from "react";
import Component from "../components/Carousel";
import Table from "../components/Table";

function Trucks() {
  return (
    <div>
      <div className="p-4 sm:ml-64">
        <div className="p-4 rounded-lg dark:border-gray-700">
          <h2 className="text-customBlue text-lg font-semibold mb-4">
            Estado de Tractos
          </h2>
          <Component
            iframeSrc1="https://tdr-dashboard.onrender.com/tractos_failure_distribution"
            iframeSrc2="https://tdr-dashboard.onrender.com/tractos_cost_distribution"
            iframeSrc3="https://tdr-dashboard.onrender.com/tractos_age"
            iframeSrc4="https://tdr-dashboard.onrender.com/mtbf"
          />
          <Table />
        </div>
      </div>
    </div>
  );
}

export default Trucks;
