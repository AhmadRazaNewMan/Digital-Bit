/** Canonical track order — keep aligned with `MODULES` in `scripts/daily_post.py`. */
export type ModuleMeta = {
  id: string;
  label: string;
  tagline: string;
  /** CSS hue for accents */
  hue: number;
};

export const MODULE_CATALOG: ModuleMeta[] = [
  {
    id: "dsa-algorithms",
    label: "DSA & algorithms",
    tagline: "Complexity, patterns, interview readiness",
    hue: 301,
  },
  {
    id: "frontend-basics",
    label: "Frontend foundations",
    tagline: "Readable interfaces with resilient UX",
    hue: 29,
  },
  {
    id: "javascript-typescript",
    label: "JavaScript & TypeScript",
    tagline: "Runtime safety with practical TypeScript patterns",
    hue: 138,
  },
  {
    id: "backend",
    label: "Backend",
    tagline: "APIs, auth, reliability, and service boundaries",
    hue: 157,
  },
  {
    id: "system-design",
    label: "System design",
    tagline: "Design choices for growth, latency, and reliability",
    hue: 186,
  },
  {
    id: "devops",
    label: "DevOps",
    tagline: "CI/CD discipline and operational excellence",
    hue: 253,
  },
  {
    id: "dbms",
    label: "Databases",
    tagline: "Storage design and performance tuning fundamentals",
    hue: 205,
  },
];

export const MODULE_IDS = MODULE_CATALOG.map((m) => m.id);

export function moduleMeta(id: string): ModuleMeta | undefined {
  return MODULE_CATALOG.find((m) => m.id === id);
}
