import type { CSSProperties } from "react";
import { Link } from "react-router-dom";
import { DigitalBackground } from "../components/DigitalBackground";
import { getAllPosts, getModules } from "../lib/posts";

export function Home() {
  const modules = getModules();
  const posts = getAllPosts();

  return (
    <div className="home">
      <DigitalBackground />
      <div className="home__inner">
        <section className="hero">
          <p className="eyebrow">Three.js · Markdown · CI</p>
          <h1 className="hero__title">
            A digital surface for
            <span className="hero__accent"> everything you ship daily</span>
          </h1>
          <p className="hero__lede">
            Notes land in <code>content/modules</code> from the generator; this UI
            reads them at build time and lays them out like a control room.
          </p>
        </section>

        <section className="module-rail" aria-label="Modules">
          {modules.length === 0 ? (
            <p className="empty">No posts yet — run the daily script or wait for Actions.</p>
          ) : (
            <ul className="module-rail__list">
              {modules.map((m) => (
                <li key={m.id} className="module-chip" id={`mod-${m.id}`}>
                  <span className="module-chip__name">{m.label}</span>
                  <span className="module-chip__count">{m.count}</span>
                </li>
              ))}
            </ul>
          )}
        </section>

        <section className="post-deck" aria-label="Latest notes">
          <h2 className="section-title">Signal stream</h2>
          <div className="cards">
            {posts.map((p) => (
              <Link
                key={`${p.moduleId}/${p.postId}`}
                to={`/post/${encodeURIComponent(p.moduleId)}/${encodeURIComponent(p.postId)}`}
                className="card"
                style={
                  {
                    ["--hue"]: String((p.moduleId.length * 47) % 360),
                  } as CSSProperties
                }
              >
                <span className="card__module">{p.moduleId.replace(/-/g, " ")}</span>
                <h3 className="card__title">{p.title}</h3>
                <span className="card__meta">{p.postId}</span>
              </Link>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}
