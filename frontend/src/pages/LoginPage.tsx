// DAY 5 — EXERCISE 2: Login Page
//
// TASK: Build the login form. On submit it calls POST /api/login, gets a JWT,
// then calls login() from the auth store and navigates to /chat.
//
// STEPS:
//   1. Add controlled inputs for username and password using useState
//   2. Implement handleSubmit():
//      - POST to /api/login with { username, password }
//      - on success: call useAuthStore().login(token, user), navigate("/chat")
//      - on failure: show the error message from the API response
//   3. Make sure the backend (day4/04_protected_routes.py) is running on port 8000
//      so the Vite proxy (/api → localhost:8000) can forward requests
//   4. Run frontend: npm run dev  (from frontend/)
//   5. Go to http://localhost:5173/login and test the form
//
// EXPECTED BEHAVIOUR:
//   - Valid credentials → redirect to /chat
//   - Invalid credentials → display "Invalid credentials" below the form
//   - Empty submit → browser validation prevents it (use required on inputs)

import { FormEvent, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuthStore } from "../store/authStore";

export function LoginPage() {
  const navigate = useNavigate();
  const login = useAuthStore((s) => s.login);

  // TODO: useState for username, password, error, isLoading

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    // TODO:
    //   1. set isLoading true, clear error
    //   2. POST /api/login with { username, password }
    //   3. if ok: call login(data.access_token, data.user), navigate("/chat")
    //   4. if error: set error message
    //   5. set isLoading false in finally
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-50">
      <div className="w-full max-w-sm rounded-2xl bg-white p-8 shadow-md">
        <h1 className="mb-6 text-2xl font-bold text-gray-800">Sign in</h1>

        {/* TODO: render error message here if error state is set */}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">
              Username
            </label>
            <input
              type="text"
              required
              // TODO: wire value and onChange
              className="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="alice"
            />
          </div>

          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">
              Password
            </label>
            <input
              type="password"
              required
              // TODO: wire value and onChange
              className="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <button
            type="submit"
            // TODO: disable while isLoading
            className="w-full rounded-lg bg-blue-600 py-2 text-sm font-semibold text-white hover:bg-blue-700 disabled:opacity-50"
          >
            {/* TODO: show "Signing in…" when isLoading */}
            Sign in
          </button>
        </form>

        <p className="mt-4 text-center text-sm text-gray-500">
          No account?{" "}
          <Link to="/signup" className="text-blue-600 hover:underline">
            Sign up
          </Link>
        </p>
      </div>
    </div>
  );
}
