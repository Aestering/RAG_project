import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

import Chat from "./pages/Chat";
import Upload from "./pages/Upload";
import Translate from "./pages/Translate";
import Combine from "./pages/Combine";
import CombineTogether from "./pages/CombineTogether";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path= "/" element={<Chat />} />
        <Route path= "/upload" element={<Upload />} />
        <Route path= "/translate" element={<Translate />} />
        <Route path='/combine' element={<Combine />} />
        <Route path='/combinetogether' element={<CombineTogether />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;