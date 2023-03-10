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

  const response = await fetch(`${API_URL}/games/?=${id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error(response.statusText);
  }

  return response.json();
}
