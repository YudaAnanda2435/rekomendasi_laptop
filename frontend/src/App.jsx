import { Route, Routes } from "react-router-dom";
import MainLayout from "./components/layouts/MainLayout";
import AboutPage from "./pages/AboutPage";
import HomePage from "./pages/HomePage";
import LaptopsPage from "./pages/LaptopsPage";
import NotFoundPage from "./pages/NotFoundPage";
import RecommendationPage from "./pages/RecommendationPage";
import AOS from "aos";
import "aos/dist/aos.css";
import { useEffect } from "react";

function App() {
  useEffect(() => {
    AOS.init({
      once: true,
      delay: 500,
      offset: 100,
    });
  });
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route index element={<HomePage />} />
        <Route path="recommendation" element={<RecommendationPage />} />
        <Route path="laptops" element={<LaptopsPage />} />
        <Route path="about" element={<AboutPage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Route>
    </Routes>
  );
}

export default App;
