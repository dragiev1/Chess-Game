import "/src/css/ContentCard.css";
import checkmate from "/src/assets/checkmate.svg";
import learnlink from "/src/assets/learn-link.svg";
import analyze from "/src/assets/analyze.svg";

const ContentCard = () => {
  return (
    <section className="content-section">
      <div className="content-container">
        <h2 className="content-title">~ Relive Chess Again ~</h2>
        
        <div className="grid md:grid-cols-3 gap-8 mt-16">
          {/* Learn Card */}
          <div className="card-glass">
            <h3 className="content-subtitle">Learn</h3>
            <p className="content-text">
              Improve your chess strategy with popular tutorials!
            </p>
            <img src={learnlink} alt="chess background" className="img" />
          </div>

          {/* Play Card */}
          <div className="card-glass">
            <h3 className="content-subtitle">Play</h3>
            <p className="content-text">Match against players in real time!</p>
            <img src={checkmate} alt="chess background" className="img" />
          </div>

          {/* Analyze Card */}
          <div className="card-glass">
            <h3 className="content-subtitle">Analyze</h3>
            <p className="content-text">
              Review games and improve using battle history!
            </p>
            <img src={analyze} alt="chess background" className="img" />
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContentCard;
