// DAY 5 — EXERCISE 4: Protected Route
//
// TASK: A ProtectedRoute wraps any page that requires auth.
// If the user is not authenticated, redirect them to /login.
// This is the React Router equivalent of Day 4's get_current_user dependency.
//
// STEPS:
//   1. Read isAuthenticated from the auth store
//   2. If false → return <Navigate to="/login" replace />
//   3. If true  → return children (the wrapped page)
//   4. Verify in App.tsx that /chat is wrapped with <ProtectedRoute>
//   5. Test:
//      - visit http://localhost:5173/chat without being logged in → redirected to /login
//      - log in → /chat is accessible
//      - refresh the page while logged in → still on /chat (Zustand reads localStorage)
//
// CONCEPTS:
//   - This is called a "wrapper component" pattern
//   - `children` is typed as ReactNode — it accepts any valid JSX
//   - `replace` on Navigate replaces the history entry so Back doesn't loop

import { ReactNode } from "react";
import { Navigate } from "react-router-dom";
import { useAuthStore } from "../store/authStore";

interface Props {
  children: ReactNode;
}

export function ProtectedRoute({ children }: Props) {
  // TODO: read isAuthenticated from useAuthStore
  // TODO: if not authenticated, return <Navigate to="/login" replace />
  // TODO: otherwise return <>{children}</>
  return <>{children}</>;
}
