import React from "react";
import Component from "../components/Carousel";
import Table from "../components/Table";

function Trucks() {
  return (
    <div>
      <div className="p-4 sm:ml-64">
        <div className="p-4 rounded-lg dark:border-gray-700">
          <h2 className="text-customBlue text-lg font-semibold mb-4">
            Estadísticas de Mantenimiento
          </h2>
          <Component />
          <Table />
        </div>
      </div>
    </div>
  );
}

export default Trucks;
