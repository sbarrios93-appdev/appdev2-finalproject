import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./auth/Login";
import Signup from "./auth/Signup";
import Welcome from "./auth/Welcome";
import GameDetails from "./GameDetails";
import Home from "./Home";

function AppRoutes({ isAuth, setIsAuth }) {
  return (
    <Routes>
      <Route
        path="/"
        element={
          isAuth ? (
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
          isAuth ? (
            <Navigate replace to="/home" />
          ) : (
            <Login setIsAuth={setIsAuth} />
          )
        }
      />
      <Route
        path="/signup"
        element={
          isAuth ? <Navigate to="/home" /> : <Signup setIsAuth={setIsAuth} />
        }
      />
      <Route
        path="/games/:id"
        element={isAuth ? <GameDetails /> : <Navigate replace to="/welcome" />}
      />
    </Routes>
  );
}

export default AppRoutes;
