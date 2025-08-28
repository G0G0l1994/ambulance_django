// import axios from "axios";
import React from "react";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ChakraProvider } from "@chakra-ui/react";

import Login from "./routes/login";
import CardsHistory from "./routes/history";
import CardPage from "./routes/card-create";
import CardDetail from "./routes/card-detail";
import CardUpdate from "./routes/card-update";
import MainPage from "./routes/main-page";
import MainLayout from "./components/MainLayout";
import DispatcherMain from "./routes/dispatcher-main";
import { AuthProvider } from "./contexts/useAuth";
import PrivateRoute from "./components/private_route";
import Register from "./routes/register";
import DocumentTitle from "./components/DocumentTitle";
import { CrewList } from "./routes/crew-list";

function App() {
  return (
    <ChakraProvider>
      <Router>
        <AuthProvider>
          <DocumentTitle />
          <Routes>
            <Route
              path="/"
              element={
                <PrivateRoute>
                  <MainLayout />
                </PrivateRoute>
              }
            >
              <Route path="/history/:user_id" element={<CardsHistory />} />
              <Route path="/cards/create" element={<CardPage />} />
              <Route path="/dispatcher-main" element={<DispatcherMain />} />
              <Route path="/cards/:card_id" element={<CardDetail />} />
              <Route path="/cards/:card_id/update" element={<CardUpdate />} />
              <Route path="/crew/list/" element={<CrewList />} />
            </Route>

            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
          </Routes>
        </AuthProvider>
      </Router>
    </ChakraProvider>
  );
}

export default App;
