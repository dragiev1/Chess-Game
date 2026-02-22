import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChessKnight } from "@fortawesome/free-solid-svg-icons";

import { useEffect, useState } from "react";

const NavBar = () => {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 80);
    };

    window.addEventListener("scroll", handleScroll, { passive: true });

    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <nav className={`navbar ${scrolled ? "scrolled" : ""}`}>
      <div className="navbar-container">
          <div className="nav-left">
            <a href="#home" className="nav-link icon nav-text">
              <FontAwesomeIcon icon={faChessKnight} />
            </a>

            <a href="#play" className="nav-links nav-text">
              PLAY
            </a>
          </div>
          <div className="nav-right">
            <a href="#login" className="nav-links nav-text">
              LOGIN
            </a>
          </div>
        </div>
    </nav>
  );
};

export default NavBar;
