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
    tagline: "Problem-solving drills and performance tradeoffs",
    hue: 118,
  },
  {
    id: "frontend-basics",
    label: "Frontend foundations",
    tagline: "Readable interfaces with resilient UX",
    hue: 227,
  },
  {
    id: "javascript-typescript",
    label: "JavaScript & TypeScript",
    tagline: "Runtime safety with practical TypeScript patterns",
    hue: 275,
  },
  {
    id: "backend",
    label: "Backend",
    tagline: "Production-grade endpoints and failure handling",
    hue: 294,
  },
  {
    id: "system-design",
    label: "System design",
    tagline: "Design choices for growth, latency, and reliability",
    hue: 323,
  },
  {
    id: "devops",
    label: "DevOps",
    tagline: "Build, release, observe, and recover confidently",
    hue: 70,
  },
  {
    id: "dbms",
    label: "Databases",
    tagline: "Queries, indexes, transactions, data correctness",
    hue: 22,
  },
];

export const MODULE_IDS = MODULE_CATALOG.map((m) => m.id);

export function moduleMeta(id: string): ModuleMeta | undefined {
  return MODULE_CATALOG.find((m) => m.id === id);
}
