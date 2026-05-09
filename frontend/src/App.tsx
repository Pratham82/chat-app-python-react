// DAY 5 — EXERCISE 4 (wiring): App shell with React Router
//
// This file wires together all the pieces you built in exercises 1–3:
//   - the Zustand auth store (exercise 1)
//   - Login / Signup pages (exercises 2 & 3)
//   - ProtectedRoute (exercise 4)
//
// STEPS:
//   1. Complete the routes below — import the real components once you build them
//   2. Run: npm run dev  (from frontend/)
//   3. Navigate to http://localhost:5173
//      - / should redirect to /login if not authenticated
//      - /login and /signup should be accessible
//      - /chat should be accessible only when logged in
//
// Nothing to implement here until exercises 1–3 are done.

import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { ProtectedRoute } from "./router/ProtectedRoute";
import { LoginPage } from "./pages/LoginPage";
import { SignupPage } from "./pages/SignupPage";

function ChatPage() {
  return (
    <div className="flex h-screen items-center justify-center">
      <p className="text-2xl font-semibold">Chat — coming soon (Day 6+)</p>
    </div>
  );
}

export function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
        <Route
          path="/chat"
          element={
            <ProtectedRoute>
              <ChatPage />
            </ProtectedRoute>
          }
        />
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
