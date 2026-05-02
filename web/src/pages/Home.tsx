import type { CSSProperties } from "react";
import { useMemo } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { DigitalBackground } from "../components/DigitalBackground";
import { MODULE_CATALOG } from "../lib/moduleCatalog";
import { getAllPosts, getModules } from "../lib/posts";

export function Home() {
  const [params] = useSearchParams();
  const activeModule = params.get("m") ?? "all";

  const modules = getModules();
  const posts = getAllPosts();

  const filtered = useMemo(() => {
    if (activeModule === "all") return posts;
    return posts.filter((p) => p.moduleId === activeModule);
  }, [posts, activeModule]);

  const catalogTracks = MODULE_CATALOG.length;
  const totalNotes = posts.length;

  return (
    <div className="home">
      <DigitalBackground />
      <div className="home__inner">
        <section className="hero">
          <p className="eyebrow">Automated curriculum · Groq · GitHub Actions</p>
          <h1 className="hero__title">
            Learn in public on a
            <span className="hero__accent"> living engineering syllabus</span>
          </h1>
          <p className="hero__lede">
            Each run publishes the <strong>next track</strong> in sequence (DSA → frontend → JS/TS → backend → …).
            Pick a module below or browse everything — notes live in <code>content/modules</code>.
          </p>
          <div className="hero__stats" aria-label="Overview">
            <div className="stat">
              <span className="stat__val">{catalogTracks}</span>
              <span className="stat__lbl">tracks</span>
            </div>
            <div className="stat">
              <span className="stat__val">{totalNotes}</span>
              <span className="stat__lbl">notes indexed</span>
            </div>
            <div className="stat stat--wide">
              <span className="stat__lbl stat__lbl--solo">Round-robin automation · build-time UI</span>
            </div>
          </div>
        </section>

        <section className="learning-path" aria-label="Recommended path">
          <h2 className="learning-path__title">Track sequence</h2>
          <ol className="learning-path__steps">
            {MODULE_CATALOG.map((step, i) => (
              <li key={step.id} className="learning-path__step">
                <span className="learning-path__idx">{i + 1}</span>
                <div className="learning-path__body">
                  <span className="learning-path__name">{step.label}</span>
                  <span className="learning-path__tag">{step.tagline}</span>
                </div>
              </li>
            ))}
          </ol>
        </section>

        <section className="module-panel" aria-labelledby="module-picker-title">
          <div className="module-panel__head">
            <h2 id="module-picker-title" className="module-panel__title">
              Choose a module
            </h2>
            <p className="module-panel__hint">
              Filter the feed. Empty tracks stay visible so you know what’s coming next.
            </p>
          </div>
          <div className="module-rail__list">
            <Link
              to="/"
              className={`module-chip module-chip--link ${activeModule === "all" ? "module-chip--active" : ""}`}
            >
              <span className="module-chip__name">All tracks</span>
              <span className="module-chip__count">{totalNotes}</span>
            </Link>
            {modules.map((m) => (
              <Link
                key={m.id}
                to={`/?m=${encodeURIComponent(m.id)}`}
                className={`module-chip module-chip--link ${activeModule === m.id ? "module-chip--active" : ""}`}
                style={{ ["--chip-hue"]: String(m.hue) } as CSSProperties}
              >
                <span className="module-chip__name">{m.label}</span>
                <span className="module-chip__count">{m.count}</span>
              </Link>
            ))}
          </div>
        </section>

        <section className="post-deck" aria-label="Notes">
          <div className="post-deck__head">
            <h2 className="section-title">
              {activeModule === "all"
                ? "Latest notes"
                : `${modules.find((x) => x.id === activeModule)?.label ?? activeModule}`}
            </h2>
            {filtered.length === 0 && (
              <p className="empty">
                No notes in this track yet — they appear after the generator lands the next round-robin post here.
              </p>
            )}
          </div>
          <div className="cards">
            {filtered.map((p) => {
              const meta = modules.find((mod) => mod.id === p.moduleId);
              const hue = meta?.hue ?? (p.moduleId.length * 47) % 360;
              return (
                <Link
                  key={`${p.moduleId}/${p.postId}`}
                  to={`/post/${encodeURIComponent(p.moduleId)}/${encodeURIComponent(p.postId)}?m=${encodeURIComponent(activeModule)}`}
                  className="card"
                  style={{ ["--hue"]: String(hue) } as CSSProperties}
                >
                  <span className="card__module">{meta?.label ?? p.moduleId.replace(/-/g, " ")}</span>
                  <h3 className="card__title">{p.title}</h3>
                  <span className="card__meta">{p.postId}</span>
                </Link>
              );
            })}
          </div>
        </section>
      </div>
    </div>
  );
}
