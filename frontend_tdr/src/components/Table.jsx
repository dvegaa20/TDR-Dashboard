import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { Pagination } from "flowbite-react";

function Table() {
  const [data, setData] = useState([]);
  const [columns, setColumns] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage] = useState(10);
  const location = useLocation();

  useEffect(() => {
    const fetchData = async () => {
      let endpoint = "";

      switch (location.pathname) {
        case "/stats":
          endpoint = "https://tdr-dashboard.onrender.com/api/data/stats";
          break;
        case "/tractos":
          endpoint = "https://tdr-dashboard.onrender.com/api/data/tractos";
          break;
        case "/gastos":
          endpoint = "https://tdr-dashboard.onrender.com/api/data/spendings";
          break;
        case "/mantenimientos":
          endpoint = "https://tdr-dashboard.onrender.com/api/data/maintenance";
          break;
      }

      try {
        const response = await fetch(endpoint);
        const result = await response.json();

        setData(result);

        if (result.length > 0) {
          setColumns(Object.keys(result[0]));
        }
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    };

    fetchData();
  }, [location.pathname]);

  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentData = data.slice(indexOfFirstItem, indexOfLastItem);

  const onPageChange = (page) => setCurrentPage(page);

  return (
    <div>
      <div className="relative overflow-x-auto shadow-md sm:rounded-lg mt-4">
        {data.length > 0 ? (
          <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
              <tr>
                {columns.map((column, index) => (
                  <th scope="col" className="px-6 py-3" key={index}>
                    {column}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {currentData.map((item, index) => (
                <tr
                  className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
                  key={index}
                >
                  {columns.map((column, idx) => (
                    <td className="px-6 py-4" key={idx}>
                      {item[column]}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p className="text-sm text-customBlue cursor-pointer hover:text-blue-900 hover:underline hover:decoration-dashed">
            Cargando datos...
          </p>
        )}
      </div>
      <div className="flex justify-center mt-4">
        <Pagination
          currentPage={currentPage}
          totalPages={Math.ceil(data.length / itemsPerPage)}
          onPageChange={onPageChange}
        />
      </div>
    </div>
  );
}

export default Table;
