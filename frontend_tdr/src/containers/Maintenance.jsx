import React from "react";
import Component from "../components/Carousel";
import Table from "../components/Table";

function Maintenance() {
  return (
    <div>
      <div className="p-4 sm:ml-64">
        <div className="p-4 rounded-lg dark:border-gray-700">
          <h2 className="text-customBlue text-lg font-semibold mb-4">
            Actividades de Mantenimiento
          </h2>
          <Component
            iframeSrcs={[
              "https://tdr-dashboard.onrender.com/part_number",
              "https://tdr-dashboard.onrender.com/maintenance_activities",
              "https://tdr-dashboard.onrender.com/time_to_complete",
            ]}
          />
          <Table />
        </div>
      </div>
    </div>
  );
}

export default Maintenance;
