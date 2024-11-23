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
            iframeSrcs={[
              "http://127.0.0.1:8050/tractos_failure_distribution",
              "http://127.0.0.1:8050/tractos_cost_distribution",
              "http://127.0.0.1:8050/tractos_performance",
              "http://127.0.0.1:8050/tractos_age",
            ]}
          />
          <Table />
        </div>
      </div>
    </div>
  );
}

export default Trucks;
