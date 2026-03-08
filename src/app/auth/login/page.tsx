export default function LoginPage() {
  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="w-full max-w-md bg-slate-900/40 border border-slate-800 rounded-xl p-8 shadow-xl backdrop-blur">

        <h1 className="text-3xl font-bold mb-6 text-center">
          Iniciar sesión
        </h1>

        <form className="space-y-6">

          {/* Email */}
          <div>
            <label className="block text-sm mb-2">Correo electrónico</label>
            <input
              type="email"
              className="w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 focus:border-indigo-500 outline-none"
              placeholder="tu@email.com"
            />
          </div>

          {/* Password */}
          <div>
            <label className="block text-sm mb-2">Contraseña</label>
            <input
              type="password"
              className="w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 focus:border-indigo-500 outline-none"
              placeholder="••••••••"
            />
          </div>

          {/* Botón */}
          <button
            type="submit"
            className="w-full py-3 rounded-lg bg-indigo-600 hover:bg-indigo-700 transition text-white font-medium"
          >
            Entrar
          </button>

        </form>

        <p className="text-center text-slate-400 text-sm mt-6">
          ¿No tienes cuenta?{" "}
          <a href="/auth/register" className="text-indigo-400 hover:text-indigo-300">
            Regístrate
          </a>
        </p>

      </div>
    </div>
  );
}
