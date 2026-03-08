export default function Navbar() {
  return (
    <nav className="h-16 bg-slate-950 border-b border-slate-800">
      <div className="max-w-6xl mx-auto h-full px-4 flex items-center justify-between">
        
        {/* Logo */}
        <div className="text-xl font-semibold text-white">
          Secure<span className="text-indigo-500">Monitor</span>
        </div>

        {/* Enlaces */}
        <div className="hidden md:flex items-center gap-8 text-slate-300">
          <a href="#" className="hover:text-white transition">Producto</a>
          <a href="#" className="hover:text-white transition">Precios</a>
          <a href="#" className="hover:text-white transition">Documentación</a>
        </div>

        {/* Botones */}
        <div className="flex items-center gap-4">
          <a href="/auth/login" className="text-slate-300 hover:text-white transition">
            Iniciar sesión
          </a>

          <a
            href="/auth/register"
            className="px-4 py-2 rounded-md bg-indigo-600 hover:bg-indigo-700 text-white transition"
          >
            Comenzar
          </a>
        </div>

      </div>
    </nav>
  );
}
