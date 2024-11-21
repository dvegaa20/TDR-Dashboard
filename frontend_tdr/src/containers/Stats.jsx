import React from "react";
import Component from "../components/Carousel";
import Table from "../components/Table";

function Stats() {
  return (
    <div>
      <div className="p-4 sm:ml-64">
        <div className="p-4 rounded-lg dark:border-gray-700">
          <h2 className="text-customBlue text-lg font-semibold mb-4">
            Estadísticas de Mantenimiento
          </h2>
          <Component
            iframeSrc1="http://localhost:8050/failure_frequency"
            iframeSrc2="http://localhost:8050/avg_repair_frecuency"
            iframeSrc3="http://localhost:8050/monthly_repair_distribution"
            iframeSrc4="http://localhost:8050/mtbf"
          />
          <Table />
        </div>
      </div>
    </div>
  );
}

export default Stats;
