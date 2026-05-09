// DAY 5 — EXERCISE 3: Signup Page
//
// TASK: Build the signup form. On success, auto-login the user and navigate to /chat.
//
// STEPS:
//   1. Add controlled inputs for username, email, password, confirmPassword
//   2. Implement handleSubmit():
//      - validate that password === confirmPassword client-side → show error if not
//      - POST to /api/signup with { username, email, password }
//      - on success: POST to /api/login to get a token, then login() + navigate("/chat")
//      - on failure: show the error detail from the API
//   3. Test:
//      - happy path: fill valid data → ends up on /chat
//      - mismatched passwords → inline error before any network call
//      - duplicate username → API returns 409, show the error
//
// EXPECTED BEHAVIOUR:
//   - Passwords don't match → "Passwords do not match" shown immediately
//   - Successful signup → auto-logged in, redirected to /chat
//   - Duplicate username → "username already exists" (or similar API message)

import { FormEvent, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuthStore } from "../store/authStore";

export function SignupPage() {
  const navigate = useNavigate();
  const login = useAuthStore((s) => s.login);

  // TODO: useState for username, email, password, confirmPassword, error, isLoading

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    // TODO:
    //   1. validate passwords match → set error and return early if not
    //   2. set isLoading, clear error
    //   3. POST /api/signup
    //   4. on success: POST /api/login to get token, call login(), navigate("/chat")
    //   5. on error: set error from response
    //   6. set isLoading false in finally
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-50">
      <div className="w-full max-w-sm rounded-2xl bg-white p-8 shadow-md">
        <h1 className="mb-6 text-2xl font-bold text-gray-800">Create account</h1>

        {/* TODO: render error message */}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">
              Username
            </label>
            <input
              type="text"
              required
              // TODO: wire value + onChange
              className="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="alice"
            />
          </div>

          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">
              Email
            </label>
            <input
              type="email"
              required
              // TODO: wire value + onChange
              className="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="alice@example.com"
            />
          </div>

          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">
              Password
            </label>
            <input
              type="password"
              required
              // TODO: wire value + onChange
              className="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">
              Confirm password
            </label>
            <input
              type="password"
              required
              // TODO: wire value + onChange
              className="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <button
            type="submit"
            // TODO: disable while isLoading
            className="w-full rounded-lg bg-blue-600 py-2 text-sm font-semibold text-white hover:bg-blue-700 disabled:opacity-50"
          >
            {/* TODO: show "Creating account…" while isLoading */}
            Create account
          </button>
        </form>

        <p className="mt-4 text-center text-sm text-gray-500">
          Have an account?{" "}
          <Link to="/login" className="text-blue-600 hover:underline">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
}
