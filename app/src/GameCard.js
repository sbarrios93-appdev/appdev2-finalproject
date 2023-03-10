import { Button } from "flowbite-react";
import React from "react";
import { useNavigate } from "react-router-dom";
function GameCard({ game }) {
  const navigate = useNavigate();
  return (
    <div className="GameCard bg-slate-900 block rounded-lg p-4 shadow-sm shadow-indigo-100">
      <img
        src={game.venue.image_url}
        alt={game.venue.name}
        className="h-56 w-full rounded-md object-cover"
      />
      <div className="flex flex-row justify-between">
        <div className="GameCardContent mt-2">
          <dl>
            <div>
              <dt className="sr-only">Sport</dt>

              <dd className="text-sm text-zinc-200">{game.sport.name}</dd>
            </div>
            <div>
              <dt className="sr-only">Name</dt>

              <dd className="font-medium text-zinc-200">{game.venue.name}</dd>
            </div>
          </dl>
          <div className="GameCardFooter text-zinc-200">
            <span className="text-zinc-200">
              {game.joined} / {game.capacity}
            </span>
          </div>
        </div>
        <div className="mt-2">
          <dl>
            <div>
              <dt className="sr-only">Address</dt>

              <dd className="font-light text-zinc-200">
                {game.venue.city}, {game.venue.country_code}
              </dd>
            </div>
            <div>
              <dt className="sr-only">Duration</dt>

              <dd className="font-light text-zinc-200">
                Duration: {game.duration}
              </dd>
            </div>
          </dl>
          <Button
            className="mt-5 w-full"
            text="Join"
            onClick={() => {
              navigate(`/games/${game.id}`);
            }}
          >
            Join
          </Button>
        </div>
      </div>
    </div>
  );
}

export default GameCard;
