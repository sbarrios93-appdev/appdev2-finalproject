import React from "react";
import { useNavigate } from "react-router-dom";

function Welcome() {
  const navigate = useNavigate();
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-12 px-4  sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-teal-200">
            Welcome to Game Finder
          </h2>
        </div>
        <div className="flex flex-col items-center justify-center space-y-4 text-sky-400">
          <p>To continue, please log in or sign up</p>
        </div>
        <div className="flex flex-col space-y-4">
          <button
            onClick={() => navigate("/login")}
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-sky-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Login
          </button>
          <button
            onClick={() => navigate("/signup")}
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-sky-600 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Sign up
          </button>
        </div>
      </div>
    </div>
  );
}

export default Welcome;
