import { faChessKnight } from "@fortawesome/free-solid-svg-icons";
import { faChessRook } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const KnightRookAnimation = () => {
  return (
    <>
      <FontAwesomeIcon icon={faChessRook} className="rook-icon" />
      <FontAwesomeIcon icon={faChessKnight} className="knight-icon" />
    </>
  );
};

export default KnightRookAnimation;
