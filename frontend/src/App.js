// import axios from "axios";
import React from "react";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ChakraProvider } from "@chakra-ui/react";

import Login from "./routes/login";
import CardsPage from "./routes/cards-page";
import MainPage from "./routes/main-page";

function App() {
  return (
    <ChakraProvider>
      <Router>
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/history" element={<CardsPage />} />
        </Routes>
      </Router>
    </ChakraProvider>
  );
}

export default App;
