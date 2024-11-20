import React from "react";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function Dashboard() {
  return (
    <div>
      <Sidebar />
      <Navbar />
      <div className="p-4 sm:ml-64">
        <div className="p-4 rounded-lg dark:border-gray-700">
          {/* First grid with 2.5fr and 1.5fr columns */}
          <div
            className="grid"
            style={{ gridTemplateColumns: "2.5fr 1.5fr", gap: "1rem" }}
          >
            <div className="flex flex-col">
              <div className="flex justify-between items-center mb-2">
                <h2 className="text-customBlue text-lg font-semibold">
                  Estadísticas de Mantenimiento
                </h2>
                <p className="text-customBlue cursor-pointer">See all</p>
              </div>
              <div className="flex flex-col items-center justify-center h-auto p-4 bg-gray-50 dark:bg-gray-800">
                <iframe
                  src="http://localhost:8050/iris"
                  style={{ border: "none", height: "100%", width: "100%" }}
                ></iframe>
              </div>
            </div>
            <div className="flex flex-col">
              <div className="flex justify-between items-center mb-2">
                <h2 class="text-customBlue text-lg font-semibold">
                  Estado de Refacciones
                </h2>
                <p className="text-customBlue cursor-pointer">See all</p>
              </div>
              <div className="flex flex-col items-center justify-center h-auto p-4 bg-gray-50 dark:bg-gray-800">
                <iframe
                  src="http://localhost:8050/gapminder"
                  style={{ border: "none", height: "100%", width: "100%" }}
                ></iframe>
              </div>
            </div>
          </div>

          {/* Second grid with 1fr and 1fr columns */}
          <div
            className="grid mt-8"
            style={{ gridTemplateColumns: "2.5fr 1.5fr", gap: "1rem" }}
          >
            <div className="flex flex-col">
              <div className="flex justify-between items-center mb-2">
                <h2 className="text-customBlue text-lg font-semibold">
                  Actividades de Mantenimiento
                </h2>
                <p className="text-customBlue cursor-pointer">See all</p>
              </div>
              <div className="flex flex-col items-center justify-center h-auto p-4 bg-gray-50 dark:bg-gray-800">
                <iframe
                  src="http://localhost:8050/iris"
                  style={{ border: "none", height: "100%", width: "100%" }}
                ></iframe>
              </div>
            </div>
            <div className="flex flex-col">
              <div className="flex justify-between items-center mb-2">
                <h2 className="text-customBlue text-lg font-semibold">
                  Resumen de Gastos
                </h2>
                <p className="text-customBlue cursor-pointer">See all</p>
              </div>
              <div className="flex flex-col items-center justify-center h-auto p-4 bg-gray-50 dark:bg-gray-800">
                <iframe
                  src="http://localhost:8050/gapminder"
                  style={{ border: "none", height: "100%", width: "100%" }}
                ></iframe>
              </div>
            </div>
          </div>

          {/* Third grid with 1fr 1fr column */}
          <div
            className="grid mt-8"
            style={{ gridTemplateColumns: "1.5fr 2.5fr", gap: "1rem" }}
          >
            <div className="flex flex-col">
              <div className="flex justify-between items-center mb-2">
                <h2 className="text-customBlue text-lg font-semibold">
                  Actividades de Mantenimiento
                </h2>
              </div>
              <div className="flex flex-col items-center justify-center h-auto p-4 bg-gray-50 dark:bg-gray-800">
                <iframe
                  src="http://localhost:8050/iris"
                  style={{ border: "none", height: "100%", width: "100%" }}
                ></iframe>
              </div>
            </div>
            <div className="flex flex-col">
              <div className="flex justify-between items-center mb-2">
                <h2 className="text-customBlue text-lg font-semibold">
                  Resumen de Gastos
                </h2>
              </div>
              <div className="flex flex-col items-center justify-center h-auto p-4 bg-gray-50 dark:bg-gray-800">
                <iframe
                  src="http://localhost:8050/gapminder"
                  style={{ border: "none", height: "100%", width: "100%" }}
                ></iframe>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
