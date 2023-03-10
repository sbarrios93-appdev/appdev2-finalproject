import React from "react";

function GameCard({ game }) {
  return (
    <div className="GameCard">
      <img src={game.venue.image_url} alt={game.venue.name} />
      <div className="GameCardContent">
        <h2>{game.venue.name}</h2>
        <h3>{game.sport.name}</h3>
        <p>
          {game.venue.city}, {game.venue.country_code}
        </p>
        <p>Duration: {game.duration}</p>
        <div className="GameCardFooter">
          <span>
            {game.joined} / {game.capacity}
          </span>
          <button>Book</button>
        </div>
      </div>
    </div>
  );
}

export default GameCard;
