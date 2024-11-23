import React from "react";
import Component from "../components/Carousel";
import Table from "../components/Table";

function Maintenance() {
  return (
    <div>
      <div className="p-4 sm:ml-64">
        <div className="p-4 rounded-lg dark:border-gray-700">
          <h2 className="text-customBlue text-lg font-semibold mb-4">
            Estadísticas de Mantenimiento
          </h2>
          <Component
            iframeSrcs={[
              "http://127.0.0.1:8050/part_number",
              "http://127.0.0.1:8050/maintenance_activities",
              "http://127.0.0.1:8050/time_to_complete",
            ]}
          />
          <Table />
        </div>
      </div>
    </div>
  );
}

export default Maintenance;
