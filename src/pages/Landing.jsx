import NavBar from "../components/NavBar";
import HeroSection from "../components/HeroSection";
import Workflow from "../components/Workflow";
import Footer from "../components/Footer";

export default function Landing() {
  return (
    <div>
      <NavBar />
      <div className="max-w-7xl mx-auto pt-20 px-6">
        <HeroSection />
        <Workflow id="workflow" />
        <Footer />
      </div>
    </div>
  );
}
