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
        <h1>Airbnb-style Listings</h1>
      </header>
      <main>
        {games.map((game) => (
          <GameCard key={game.id} game={game} />
        ))}
      </main>
    </div>
  );
}

export default Home;
