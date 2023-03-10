import { BrowserRouter } from "react-router-dom";
import "./App.css";
import { QueryClient, QueryClientProvider } from "react-query";
import AppRoutes from "./AppRoutes";
import Navigation from "./Navigation";
import isAuthenticated from "./helpers";
import { useState } from "react";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: Infinity,
      cacheTime: Infinity,
    },
  },
});

function App() {
  const [isAuth, setIsAuth] = useState(isAuthenticated()); // [1
  return (
    <BrowserRouter>
      <QueryClientProvider client={queryClient}>
        <AppRoutes isAuth={isAuth} setIsAuth={setIsAuth} />
      </QueryClientProvider>
      <Navigation isAuth={isAuth} setIsAuth={setIsAuth} />
    </BrowserRouter>
  );
}

export default App;
