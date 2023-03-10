import API_URL from "./config";

async function fetchVenue({ queryKey }) {
  const token = localStorage.getItem("access_token");
  const id = queryKey[1];

  console.log("fetchVenue", id);

  const response = await fetch(`${API_URL}/venues/${id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error(response.statusText);
  }

  return response.json();
}

export default fetchVenue;
