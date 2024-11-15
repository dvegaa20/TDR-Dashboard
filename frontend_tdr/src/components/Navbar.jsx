import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div>
      <nav className="text-right p-6 border-gray-200 bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
        <div className="inline-flex space-x-4 max-w-screen-xl flex flex-wrap justify-start mx-auto px-4">
          <Link
            to="/"
            className="flex items-center space-x-3 rtl:space-x-reverse"
          >
            <span className="text-2xl font-semibold whitespace-nowrap dark:text-white">
              Mantenimiento TDR
            </span>
          </Link>
        </div>
        <p className="font-thin	 antialiased text-sm pr-4">
          Proyecto - Liverpool
        </p>
      </nav>
    </div>
  );
}

export default Navbar;
