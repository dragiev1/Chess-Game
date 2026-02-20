import { useEffect, useRef } from 'react';
import '../css/HomePage.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChessKnight } from '@fortawesome/free-solid-svg-icons';

const HomePage = () => {
  const parallaxRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleScroll = () => {
      if (parallaxRef.current) {
        const scrollPosition = window.pageYOffset;
        parallaxRef.current.style.transform = `translateY(${scrollPosition * 0.5}px)`;
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div className="homepage">
      {/* Navbar */}
      <nav className="navbar">
        <div className="navbar-container">
          <div className="nav-links">
            <a href="#home" className="nav-link icon nav-text">
              <FontAwesomeIcon icon={faChessKnight}/>
            </a>
            <a href="#login" className="nav-link nav-text">LOGIN</a>
            <a href="#play" className="nav-link nav-text">PLAY</a>
          </div>
        </div>
      </nav>

      {/* Parallax Hero Section */}
      <div className="parallax-container">
        <div 
          ref={parallaxRef}
          className="parallax-background"
          style={{
            backgroundImage: 'url("/parallax-background.jpg")'
          }}
        />
        
        <div className="hero-content">
          <h1 className="hero-title">
            <span className="hero-ch">Ch
              
            </span>
            <span className="hero-yes fancy-italic">yes</span>
            <span className="hero-s">s</span>
          </h1>
          <p className="hero-subtitle">
            Where Strategy Meets Elegance
          </p>
          <button className="btn-primary hero-btn">
            <FontAwesomeIcon className='btn-icon' icon={faChessKnight}/>
            <span className="btn-text">PLAY!</span>
          </button>
        </div>

        <div className="scroll-indicator">
          <div className="mouse">
            <div className="wheel"></div>
          </div>
          <div className="arrow">
            <span></span>
          </div>
        </div>
      </div>

      {/* Content Section */}
      <section className="content-section">
        <div className="content-container">
          <h2 className="content-title">Relive Chess Again</h2>
          <p className="content-text">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Esse, iusto modi mollitia ea pariatur facilis laborum explicabo suscipit, quis porro eveniet excepturi id dolor ullam eligendi dolores distinctio quidem est.
          </p>
        </div>
      </section>
    </div>
    
  );
};

export default HomePage;