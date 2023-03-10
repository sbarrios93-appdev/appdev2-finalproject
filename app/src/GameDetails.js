import React from "react";
import { useQuery } from "react-query";
import { fetchGame } from "./fetchGames";
import { useParams } from "react-router-dom";
import Team from "./Team";

function GameDetails() {
  const { id } = useParams();
  const {
    data: response,
    isLoading,
    error,
  } = useQuery(["game", id], () => fetchGame(id));
  if (isLoading) {
    return <div>Loading...</div>;
  }
  if (error) {
    return <div>Error: {error.message}</div>;
  }
  const game = response[0];
  return (
    <div className="max-w-md w-full space-y-8">
      <div>
        <h2 className="mt-6 text-center text-3xl font-extrabold text-teal-200">
          {game.venue.name}
        </h2>
      </div>
      <div className="GameCard bg-slate-900 block rounded-lg p-4 ">
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
          </div>
        </div>
        <div className="mt-2 teams">
          <dl>
            <div>
              <dt className="sr-only">Teams</dt>'
              <dt className="font-extrabold text-4xl text-zinc-200">Teams</dt>
              <dd className="font-light text-zinc-200">
                {game.teams.map((team) => (
                  <Team team={team} game={game} />
                ))}
              </dd>
            </div>
          </dl>
        </div>
      </div>
    </div>
  );
}

export default GameDetails;
