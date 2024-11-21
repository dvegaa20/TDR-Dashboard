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
            iframeSrc1="http://localhost:8050/tractos_age"
            iframeSrc2="http://localhost:8050/tractos_age2"
            iframeSrc3="http://localhost:8050/tractos_age3"
            iframeSrc4="http://localhost:8050/tractos_age4"
          />
          <Table />
        </div>
      </div>
    </div>
  );
}

export default Maintenance;
