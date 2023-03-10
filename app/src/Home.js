import React from "react";
import { useQuery } from "react-query";
import { fetchAllGames } from "./fetchGames";
import GameCard from "./GameCard";

function Home() {
  const { data: games, isLoading, error } = useQuery("allGames", fetchAllGames);
  if (isLoading) {
    return <div>Loading...</div>;
  }
  if (error) {
    return <div>Error: {error.message}</div>;
  }
  return (
    <div>
      <header className="App-header">
        <div className="pb-3">
          <h2 className="mt-6 text-left text-3xl font-extrabold text-sky-200">
            Available Games
          </h2>
        </div>
      </header>
      <main>
        <div className="space-y-8">
          {games.map((game) => (
            <GameCard key={game.id} game={game} />
          ))}
        </div>
      </main>
    </div>
  );
}

export default Home;
