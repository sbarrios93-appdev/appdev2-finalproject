import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./auth/Login";
import Logout from "./auth/Logout";
import Signup from "./auth/Signup";
import Welcome from "./auth/Welcome";
import Home from "./Home";
import isAuthenticated from "./helpers";

function AppRoutes() {
  return (
    <Routes>
      <Route
        path="/"
        element={
          isAuthenticated() ? (
            <Navigate replace to="/home" />
          ) : (
            <Navigate replace to="/welcome" />
          )
        }
      />
      <Route path="/home" element={<Home />} />
      <Route path="/welcome" element={<Welcome />} />
      <Route
        path="/login"
        element={
          isAuthenticated() ? <Navigate replace to="/home" /> : <Login />
        }
      />
      <Route path="/logout" element={<Logout />} />
      <Route
        path="/signup"
        element={isAuthenticated() ? <Navigate to="/home" /> : <Signup />}
      />
    </Routes>
  );
}

export default AppRoutes;
