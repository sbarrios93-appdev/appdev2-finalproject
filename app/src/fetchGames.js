import API_URL from "./config";

export async function fetchAllGames() {
  const token = localStorage.getItem("access_token");

  const response = await fetch(`${API_URL}/games/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error(response.statusText);
  }

  return response.json();
}

export async function fetchGame(id) {
  const token = localStorage.getItem("access_token");

  const response = await fetch(`${API_URL}/games/?id=${id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error(response.statusText);
  }

  return response.json();
}

export async function lookUpPlayerInGame({ queryKey }) {
  const token = localStorage.getItem("access_token");
  const { playerId, gameId, side } = queryKey[1];

  const response = await fetch(
    `${API_URL}/games/teams/?game_id=${gameId}&side=${side}`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  if (!response.ok) {
    throw new Error(response.statusText);
  }

  for (const team of response) {
    for (const player of team.players) {
      if (player.id === playerId) {
        return true;
      } else {
        return false;
      }
    }
  }
}
