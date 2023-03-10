function isAuthenticated() {
  return !!localStorage.getItem("access_token");
}

export default isAuthenticated;
