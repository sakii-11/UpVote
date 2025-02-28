import { Menu, X } from "lucide-react";
import { useState } from "react";
import logo from "../assets/logo.svg";

const Navbar = () => {
  const [mobileDrawerOpen, setMobileDrawerOpen] = useState(false);

  const toggleNavbar = () => {
    setMobileDrawerOpen(!mobileDrawerOpen);
  };

  return (
    <nav className="sticky top-0 z-50 py-3 backdrop-blur-lg border-b border-neutral-700/80">
      <div className="container px-4 mx-auto relative lg:text-sm">
        <div className="flex justify-between items-center">
          <div className="flex items-center flex-shrink-0">
            <img className="h-10 w-10 mr-2" src={logo} alt="Logo" />
            <span className="text-xl tracking-tight font-grotesk font-bold">UpVote</span>
          </div>
          <div className="hidden lg:flex justify-center space-x-12 items-center">
            <a href="/login" className="py-2 px-3 border rounded-md">
              Sign In
            </a>
            <a
              href="/signup"
              className="bg-gradient-to-r from-purple-500 to-purple-800 py-2 px-3 rounded-md"
            >
              Create an account
            </a>
          </div>
          <div className="lg:hidden md:flex flex-col justify-end">
            <button onClick={toggleNavbar}>
              {mobileDrawerOpen ? <X /> : <Menu />}
            </button>
          </div>
        </div>
        {mobileDrawerOpen && (
          <div className="fixed right-0 z-20 bg-neutral-900 w-full p-12 flex flex-col justify-center items-center lg:hidden">
            <div className="flex space-x-6">
              <a href="/login" className="py-2 px-3 border rounded-md">
                Sign In
              </a>
              <a
                href="/signup"
                className="py-2 px-3 rounded-md bg-gradient-to-r from-purple-500 to-purple-800"
              >
                Create an account
              </a>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
