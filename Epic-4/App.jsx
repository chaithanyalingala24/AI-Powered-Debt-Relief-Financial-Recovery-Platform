import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import FinancialForm from "./pages/FinancialForm";
import LoanForm from "./pages/LoanForm";
import AIRecommendation from "./pages/AIRecommendation";
function App() {
  return (
    <BrowserRouter>
      <Navbar />


    <Routes>
  <Route path="/" element={<Login />} />
  <Route path="/register" element={<Register />} />
  <Route path="/dashboard" element={<Dashboard />} />
  <Route path="/financial-form" element={<FinancialForm />} />
  <Route path="/loan-form" element={<LoanForm />} />
  <Route path="/ai-recommendation" element={<AIRecommendation />} />
    </Routes>
    </BrowserRouter>
  );
}

export default App;