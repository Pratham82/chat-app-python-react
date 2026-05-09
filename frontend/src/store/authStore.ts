// DAY 5 — EXERCISE 1: Zustand Auth Store
//
// TASK: Zustand is a lightweight state manager (like Redux but without boilerplate).
// Build the auth store that tracks whether the user is logged in.
// Every component can subscribe to this store — no prop drilling needed.
//
// STEPS:
//   1. Define the AuthState interface:
//      - token: string | null       (the JWT from the API)
//      - user: { id: number; username: string; email: string } | null
//      - isAuthenticated: boolean   (derived: token !== null)
//
//   2. Implement the actions:
//      - login(token, user): save to state AND localStorage ("token", "user")
//      - logout():           clear state AND localStorage
//
//   3. Initialise from localStorage so the user stays logged in across page reloads:
//      read "token" and "user" from localStorage in the initial state
//
//   4. Export useAuthStore — the hook used by all components
//
// USAGE (once done):
//   const { token, user, login, logout, isAuthenticated } = useAuthStore();

import { create } from "zustand";

interface User {
  id: number;
  username: string;
  email: string;
}

interface AuthState {
  token: string | null;
  user: User | null;
  isAuthenticated: boolean;
  login: (token: string, user: User) => void;
  logout: () => void;
}

// TODO: implement useAuthStore with create<AuthState>()(...)
// Hint: read initial token/user from localStorage:
//   const savedToken = localStorage.getItem("token");
//   const savedUser = localStorage.getItem("user");
export const useAuthStore = create<AuthState>()(() => ({
  token: null,
  user: null,
  isAuthenticated: false,
  login: (_token, _user) => {
    // TODO: set state and persist to localStorage
  },
  logout: () => {
    // TODO: clear state and remove from localStorage
  },
}));
