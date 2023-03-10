import API_URL from "./config";

export async function fetchSport({ queryKey }) {
  const token = localStorage.getItem("access_token");
  const id = queryKey[1];

  const response = await fetch(`${API_URL}/sports/${id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error(response.statusText);
  }

  return response.json();
}

export default fetchSport;
