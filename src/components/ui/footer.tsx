export default function Footer() {
  return (
    <footer className="border-t border-slate-800 mt-24 py-10">
      <div className="max-w-6xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-6">

        {/* Logo */}
        <div className="text-xl font-semibold text-white">
          Secure<span className="text-indigo-500">Monitor</span>
        </div>

        {/* Enlaces */}
        <div className="flex gap-6 text-slate-400 text-sm">
          <a href="#" className="hover:text-white transition">Producto</a>
          <a href="#" className="hover:text-white transition">Precios</a>
          <a href="#" className="hover:text-white transition">Documentación</a>
          <a href="#" className="hover:text-white transition">Contacto</a>
        </div>

        {/* Derechos */}
        <p className="text-slate-500 text-xs">
          © {new Date().getFullYear()} SecureMonitor. Todos los derechos reservados.
        </p>

      </div>
    </footer>
  );
}

