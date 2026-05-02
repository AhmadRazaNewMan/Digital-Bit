import { Link } from "react-router-dom";
import type { ReactNode } from "react";

export function Layout({ children }: { children: ReactNode }) {
  return (
    <div className="shell">
      <header className="topbar">
        <Link to="/" className="brand">
          <span className="brand__glyph" aria-hidden />
          <span className="brand__text">
            <span className="brand__title">Digital Bit</span>
            <span className="brand__tag">automated lab log</span>
          </span>
        </Link>
        <nav className="nav">
          <Link to="/">Modules</Link>
          <a
            href="https://github.com/AhmadRazaNewMan/Digital-Bit"
            target="_blank"
            rel="noreferrer"
          >
            GitHub
          </a>
        </nav>
      </header>
      <main className="main">{children}</main>
    </div>
  );
}
